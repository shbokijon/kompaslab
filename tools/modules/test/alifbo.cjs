// Regression: new Uzbek Latin alphabet converter must handle o‘/g‘ at word end.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const src = fs.readFileSync(path.resolve(__dirname, "../../../js/alifbo.js"), "utf8");
function load(query = "") {
  const store = new Map();
  const window = {};
  const document = {
    documentElement: { setAttribute() {} },
    readyState: "loading",
    addEventListener() {}
  };
  const sandbox = {
    window, document, location: { search: query },
    localStorage: {
      getItem(k) { return store.get(k) ?? null; },
      setItem(k, v) { store.set(k, v); }
    }
  };
  vm.runInNewContext(src, sandbox, { filename: "alifbo.js" });
  return window.KAlifbo;
}
const { mode, conv } = load();
assert.equal(mode, "yangi");
const cases = [
  ["Akademik obroʻ 30%", "Akademik obrö 30%"],
  ["Ish beruvchi obroʻsi", "Iş beruvçi obrösi"],
  ["obro‘", "obrö"],
  ["togʻ", "toğ"],
  ["Koʻp", "Köp"],
  ["Oʻzbekiston", "Özbekiston"],
  ["Gʻarb", "Ğarb"],
  ["Shahar", "Şahar"],
  ["Chin", "Çin"],
  ["maʼlumot", "maʼlumot"],
  ["Research", "Research"],
  ["University of Manchester", "University of Manchester"],
  ["https://example.com/shop", "https://example.com/shop"]
];
for (const [input, expected] of cases) {
  assert.equal(conv(input), expected, `failed: ${input}`);
}
const oldMode = load("?alifbo=eski");
assert.equal(oldMode.mode, "eski");
assert.equal(oldMode.conv, undefined);
console.log(`alifbo: ${cases.length} regression cases passed`);
