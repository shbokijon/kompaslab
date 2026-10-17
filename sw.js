// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — sw.js (service worker)
//  · Sahifalar: avval internet, boʻlmasa oxirgi saqlangan nusxa, u ham
//    boʻlmasa offline.html. Ochilgan M0 darslar internetsiz ham ochiladi.
//  · Rasm, shrift, CSS: keshdan tez, orqada yangilanadi.
//  · js/ va boshqa domenlar (Supabase API): har doim internetdan.
//  Yangilanganda V ni oshiring.
// ═══════════════════════════════════════════════════════════════
var V = "kl-v2", PAGES = V + "-pages", ASSETS = V + "-assets";
var PRECACHE = ["/offline.html", "/css/brand.css", "/favicon.ico", "/img/brand/logo-base.webp", "/img/brand/logo-arrow.webp", "/img/brand/icon-192.png"];

self.addEventListener("install", function (e) {
  e.waitUntil(caches.open(ASSETS).then(function (c) { return c.addAll(PRECACHE); }).then(function () { return self.skipWaiting(); }));
});
self.addEventListener("activate", function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (k) { return k.indexOf(V) !== 0; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});

function trim(name, max) {
  caches.open(name).then(function (c) { c.keys().then(function (k) { if (k.length > max) c.delete(k[0]).then(function () { trim(name, max); }); }); });
}

self.addEventListener("fetch", function (e) {
  var req = e.request, url = new URL(req.url);
  if (req.method !== "GET" || url.origin !== self.location.origin) return;
  if (url.pathname.indexOf("/js/") === 0 || url.pathname === "/sw.js") return;   // har doim yangi

  if (req.mode === "navigate") {
    e.respondWith(fetch(req).then(function (res) {
      if (res.ok) { var copy = res.clone(); caches.open(PAGES).then(function (c) { c.put(url.pathname, copy); trim(PAGES, 40); }); }
      return res;
    }).catch(function () {
      return caches.match(url.pathname).then(function (r) { return r || caches.match("/offline.html"); });
    }));
    return;
  }

  if (/\.(webp|png|jpg|jpeg|svg|ico|css|woff2?)$/.test(url.pathname)) {
    e.respondWith(caches.open(ASSETS).then(function (c) {
      return c.match(req).then(function (hit) {
        var net = fetch(req).then(function (res) { if (res.ok) { c.put(req, res.clone()); trim(ASSETS, 120); } return res; }).catch(function () { return hit; });
        return hit || net;
      });
    }));
  }
});
