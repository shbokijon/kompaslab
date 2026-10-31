// Inglizcha soʻzlar yangi alifbo konvertorida buzilmasligini tekshiradi (PhD M0–M8, 2026-10-31).
//   node tools/modules/phd/en_check.cjs tools/modules/src/phd-lab-m1.src.html ...
// js/alifbo.js ni yuklaydi, koʻrinadigan matnni (script/style va lang="en"/translate="no" dan tashqari)
// oʻgiradi va oʻzgargan soʻzlardan inglizchaga oʻxshaganlarini chiqaradi. Topilsa: [[...]] bilan oʻrang yoki EX ga qoʻshing.
const fs = require("node:fs"), path = require("node:path"), vm = require("node:vm");
const src = fs.readFileSync(path.resolve(__dirname, "../../../js/alifbo.js"), "utf8");
const window = {}, store = new Map();
vm.runInNewContext(src, { window, document: { documentElement: { setAttribute() {} }, readyState: "loading", addEventListener() {} },
  location: { search: "" }, localStorage: { getItem: (k) => store.get(k) ?? null, setItem: (k, v) => store.set(k, v) } });
const conv = window.KAlifbo.conv;
const EN = /(w|c(?!h)|th|ph|tion|ship|ee|oo|ck|ea|ch(?=[ae]r|ing|e?d\b))/i;
const OK = new Set(["oching", "qoching", "beruvchingiz", "charchoq"]); // oʻzbekcha soʻzlar (soxta signal)
let bad = 0;
for (const f of process.argv.slice(2)) {
  let s = fs.readFileSync(f, "utf8");
  s = s.replace(/<script[\s\S]*?<\/script>|<style[\s\S]*?<\/style>/g, " ");
  // lang="en" va translate="no" ichidagi matnni olib tashlash (ichma-ich span yoʻq deb faraz)
  s = s.replace(/<([a-z0-9]+)[^>]*(lang="en"|translate="no"|data-alifbo="off")[^>]*>[\s\S]*?<\/\1>/g, " ");
  s = s.replace(/<[^>]+>/g, " ").replace(/&[a-z#0-9]+;/g, " ");
  const words = new Set(s.match(/[A-Za-zʻʼ‘'’-]+/g) || []);
  const hits = [...words].filter((w) => !OK.has(w.toLowerCase()) && conv(w) !== w && EN.test(w.replace(/[ʻʼ]/g, "")));
  if (hits.length) { bad += hits.length; console.log(path.basename(f) + ": " + hits.sort().join(", ")); }
  else console.log(path.basename(f) + ": OK");
}
process.exit(bad ? 1 : 0);
