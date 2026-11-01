/* Kompas Lab — production Supabase monitoring.
 * Additive to admin.html; no other Admin features and no browser secrets.
 * Data source: existing Supabase RPC kompas_admin_usage() (Admin-only).
 */
async function loadSystemStats() {
  const box = document.getElementById('sysMetrics');
  const freshness = document.getElementById('sysFresh');
  const quota = document.getElementById('sysQuota');
  if (!box) return;

  box.setAttribute('aria-busy', 'true');
  box.textContent = 'Supabase statistikasi yuklanmoqda…';
  if (freshness) freshness.textContent = '';
  if (quota) quota.replaceChildren();

  try {
    // Authorization is not only client-side: the RPC itself checks fn_is_admin().
    const { data, error } = await supabase.rpc('kompas_admin_usage');
    if (error) throw error;
    if (!data || typeof data !== 'object') throw new Error('Statistika javobi notoʻgʻri.');

    const bytes = Number(data.database_bytes);
    const isBytes = Number.isFinite(bytes) && bytes >= 0;
    const cells = [
      ['Database hajmi', isBytes ? (bytes / 1048576).toFixed(2) + ' MB' : '—'],
      ['Roʻyxatdan oʻtganlar', safeCount(data.profiles_count)],
      ['Lablar', safeCount(data.course_count)],
      ['Modullar', safeCount(data.module_count)],
      ['Darslar', safeCount(data.lesson_count)]
    ];
    function safeCount(v) {
      const n = Number(v);
      return Number.isSafeInteger(n) && n >= 0 ? n.toLocaleString('en-GB') : '—';
    }

    const fragment = document.createDocumentFragment();
    cells.forEach(([label, value]) => {
      const item = document.createElement('div');
      item.className = 'sys-metric';
      const number = document.createElement('div');
      number.className = 'sys-metric-value';
      number.textContent = value;
      const name = document.createElement('div');
      name.className = 'sys-metric-label';
      name.textContent = label;
      item.append(number, name);
      fragment.appendChild(item);
    });
    box.replaceChildren(fragment);

    const date = data.sampled_at ? new Date(data.sampled_at) : null;
    if (freshness) {
      freshness.textContent = date && Number.isFinite(date.getTime())
        ? 'Yangilandi: ' + date.toLocaleString('uz-UZ', {dateStyle:'short', timeStyle:'medium'})
        : 'Yangilanish vaqti mavjud emas';
    }

    if (quota && isBytes) {
      const reference = 500 * 1024 * 1024;
      const percent = bytes / reference * 100;
      const displayPercent = Math.max(0, Math.min(100, percent));

      const header = document.createElement('div');
      header.className = 'sys-reference-heading';
      const text = document.createElement('span');
      text.textContent = 'Database / Free plan reference (500 MB)';
      const strong = document.createElement('strong');
      strong.textContent = percent.toFixed(1) + '%';
      header.append(text, strong);

      const track = document.createElement('div');
      track.className = 'sys-reference-track';
      track.setAttribute('role','progressbar');
      track.setAttribute('aria-label','Database hajmi 500 MB maʼlumotnoma bilan solishtirilgan');
      track.setAttribute('aria-valuemin','0');
      track.setAttribute('aria-valuemax','100');
      track.setAttribute('aria-valuenow',String(Math.round(displayPercent)));
      const fill = document.createElement('div');
      fill.className = 'sys-reference-fill';
      fill.style.width = displayPercent + '%';
      track.appendChild(fill);

      const note = document.createElement('p');
      note.className = 'sys-reference-note';
      note.textContent = 'Database hajmi Supabase PostgreSQL orqali oʻlchandi. 500 MB — solishtirish uchun maʼlumotnoma; tarifingizning joriy limiti yoki billing hisoboti emas.';
      quota.append(header, track, note);
    }
  } catch (error) {
    box.textContent = 'Statistikani olishda xatolik: ' + (error?.message || 'Nomaʼlum xatolik');
    if (freshness) freshness.textContent = 'Supabase RPC: kompas_admin_usage';
  } finally {
    box.removeAttribute('aria-busy');
  }
}
