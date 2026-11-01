// Server-only Vercel billing usage proxy. No provider token ever reaches the browser.
// GET /api/admin/vercel-usage — Supabase authenticated Super Admin only.
// Vercel FOCUS v1.3 /v1/billing/charges: team-wide billed costs, not project quota usage.
export default async function handler(req, res) {
  res.setHeader('Cache-Control','private, no-store, max-age=0');
  res.setHeader('Vary','Authorization');
  res.setHeader('X-Content-Type-Options','nosniff');
  if (req.method !== 'GET') {
    res.setHeader('Allow','GET');
    return res.status(405).json({error:'METHOD_NOT_ALLOWED'});
  }
  const auth = String(req.headers.authorization || '');
  const jwt = auth.match(/^Bearer ([A-Za-z0-9._-]+)$/)?.[1];
  if (!jwt) return res.status(401).json({error:'LOGIN_REQUIRED'});
  const supabaseUrl = process.env.SUPABASE_URL || 'https://usxpkmbjrdllnitlzdpq.supabase.co';
  const anonKey = process.env.SUPABASE_ANON_KEY;
  if (!anonKey) return res.status(503).json({error:'AUTH_SERVER_NOT_CONFIGURED'});
  const common = { apikey: anonKey, Authorization: 'Bearer ' + jwt };
  try {
    // Verify the user on Supabase Auth; never trust a locally decoded JWT or email allowlist.
    const who = await fetch(supabaseUrl + '/auth/v1/user', {
      headers: common, signal: AbortSignal.timeout(9000)
    });
    if (!who.ok) return res.status(401).json({error:'INVALID_SESSION'});
    const user = await who.json();
    if (!user || !user.id) return res.status(401).json({error:'INVALID_SESSION'});
    const [isAdmin, accountActive] = await Promise.all([
      fetch(supabaseUrl + '/rest/v1/rpc/fn_is_admin', {
        method: 'POST', headers: {...common,'Content-Type':'application/json'},
        body:'{}', signal:AbortSignal.timeout(9000)
      }),
      fetch(supabaseUrl + '/rest/v1/rpc/kompas_account_active', {
        method: 'POST', headers: {...common,'Content-Type':'application/json'},
        body:'{}', signal:AbortSignal.timeout(9000)
      })
    ]);
    if (!isAdmin.ok || !accountActive.ok)
      return res.status(503).json({error:'AUTH_CHECK_UNAVAILABLE'});
    if (await isAdmin.json() !== true || await accountActive.json() !== true)
      return res.status(403).json({error:'ADMIN_ONLY'});

    const token = process.env.VERCEL_API_TOKEN;
    const teamId = process.env.VERCEL_TEAM_ID || 'team_8uGplJ2cOUVP74ZZ4DDHMsQ2';
    if (!token) return res.status(503).json({error:'VERCEL_TOKEN_NOT_CONFIGURED'});

    // Completed UTC days only; FOCUS response supports one-day granularity.
    const end = new Date(); end.setUTCHours(0,0,0,0);
    const start = new Date(end.getTime() - 30 * 86400000);
    const url = new URL('https://api.vercel.com/v1/billing/charges');
    url.searchParams.set('teamId',teamId);
    url.searchParams.set('from',start.toISOString());
    url.searchParams.set('to',end.toISOString());
    const response = await fetch(url, {
      headers:{Authorization:'Bearer '+token,Accept:'application/x-ndjson'},
      signal:AbortSignal.timeout(13000)
    });
    if (response.status === 403) return res.status(503).json({error:'VERCEL_PERMISSION_DENIED'});
    if (response.status === 401) return res.status(503).json({error:'VERCEL_TOKEN_INVALID'});
    if (response.status === 404) return res.status(503).json({error:'VERCEL_BILLING_NOT_AVAILABLE'});
    if (!response.ok) return res.status(502).json({error:'VERCEL_API_ERROR',status:response.status});

    const limit = 5 * 1024 * 1024;
    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    const byService = new Map();
    let partial = '', totalBytes = 0, count = 0, currency = null, total = 0;
    function record(line) {
      if (!line.trim()) return;
      let obj;
      try { obj = JSON.parse(line); } catch { throw Error('INVALID_JSONL'); }
      if (Array.isArray(obj)) { obj.forEach(item => record(JSON.stringify(item))); return; }
      if (typeof obj?.BilledCost !== 'number' && typeof obj?.BilledCost !== 'string') return;
      const amount = Number(obj.BilledCost);
      if (!Number.isFinite(amount)) return;
      const curr = String(obj.BillingCurrency || 'USD');
      if (currency && curr !== currency) throw Error('MULTIPLE_CURRENCIES');
      currency = curr;
      const service = String(obj.ServiceName || obj.ServiceCategory || 'Other').slice(0,100);
      const prev = byService.get(service) || {service,billed:0,items:0};
      prev.billed += amount; prev.items++; byService.set(service,prev);
      total += amount; count++;
    }
    try {
      while (true) {
        const {done,value} = await reader.read();
        if (done) break;
        totalBytes += value.byteLength;
        if (totalBytes > limit) {await reader.cancel();return res.status(413).json({error:'USAGE_TOO_LARGE'});}
        partial += decoder.decode(value,{stream:true});
        let index;
        while ((index=partial.indexOf('\n'))>=0) {
          record(partial.slice(0,index));partial=partial.slice(index+1);
        }
      }
      partial += decoder.decode();
      if (partial.trim()) record(partial);
    } catch (err) {
      return res.status(502).json({error:'USAGE_PARSE_FAILED'});
    }
    return res.status(200).json({
      source:'vercel-focus-v1.3',scope:'team',granularity:'completed-utc-days',
      from:start.toISOString(),to:end.toISOString(),currency:currency||'USD',
      totalBilled:Number(total.toFixed(4)),chargeCount:count,
      services:[...byService.values()].sort((a,b)=>b.billed-a.billed).slice(0,30)
        .map(s=>({...s,billed:Number(s.billed.toFixed(4))})),
      note:'Billing costs are not usage limits or remaining quota.'
    });
  } catch (error) {
    if (error?.name === 'TimeoutError' || error?.name === 'AbortError')
      return res.status(504).json({error:'UPSTREAM_TIMEOUT'});
    return res.status(502).json({error:'UPSTREAM_UNAVAILABLE'});
  }
}
