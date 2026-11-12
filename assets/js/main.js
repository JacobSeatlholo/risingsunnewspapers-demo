/* Rising Sun Newspapers demo — progressive enhancement only.
   The site is fully readable with JavaScript disabled. */
(function () {
  "use strict";

  /* Sticky header shadow */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 4);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* Mobile navigation */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  /* Topbar date — localised for South Africa */
  var el = document.getElementById("topbar-date");
  if (el) {
    try {
      var now = new Date();
      var text = now.toLocaleDateString("en-ZA", {
        weekday: "long", day: "numeric", month: "long", year: "numeric"
      });
      el.textContent = text;
    } catch (err) {
      /* keep the build-time fallback text */
    }
  }

  /* Newsletter form (demo) — no data leaves the page in this demo build */
  var form = document.getElementById("newsletter-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var email = form.querySelector("input[type=email]");
      var ok = document.getElementById("newsletter-ok");
      if (!email.value || email.value.indexOf("@") < 1) {
        email.focus();
        return;
      }
      form.style.display = "none";
      if (ok) { ok.style.display = "block"; ok.focus(); }
    });
  }

  /* Reading progress on article pages */
  var bar = document.getElementById("read-progress");
  if (bar) {
    var update = function () {
      var doc = document.documentElement;
      var max = doc.scrollHeight - window.innerHeight;
      var pct = max > 0 ? Math.min(100, Math.round((window.scrollY / max) * 100)) : 0;
      bar.style.width = pct + "%";
    };
    window.addEventListener("scroll", update, { passive: true });
    update();
  }
})();
