from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# ---------- Special front-facing book: The Four Cardinal Virtues ----------
css_anchor = "  /* ---------- Αγγλικό τμήμα ---------- */"
cardinal_css = r'''
  /* ---------- The Four Cardinal Virtues: front-facing antique book ---------- */
  .slot--cardinal{
    width:244px;
    align-items:flex-end;
    perspective:1100px;
  }
  .book-cardinal{
    position:relative;
    display:block;
    width:244px;
    height:288px;
    flex:0 0 auto;
    overflow:hidden;
    border-radius:5px 7px 5px 4px;
    text-decoration:none;
    cursor:pointer;
    transform-origin:bottom left;
    transform:rotateY(-4deg) rotateZ(-.35deg);
    box-shadow:
      -7px 2px 0 #2a160c,
      -10px 4px 12px rgba(0,0,0,.45),
      11px 18px 24px rgba(0,0,0,.55),
      inset 0 0 0 1px rgba(233,205,134,.24);
    transition:transform .35s cubic-bezier(.2,.8,.2,1), box-shadow .35s, filter .35s;
    filter:saturate(.92) brightness(.94) sepia(.06);
  }
  .book-cardinal::before{
    content:"";
    position:absolute;
    inset:5px;
    z-index:2;
    pointer-events:none;
    border:1px solid rgba(220,183,92,.30);
    border-radius:3px;
    box-shadow:
      inset 0 0 15px rgba(25,12,5,.34),
      0 0 0 1px rgba(40,19,7,.38);
  }
  .book-cardinal::after{
    content:"";
    position:absolute;
    z-index:2;
    inset:0;
    pointer-events:none;
    background:
      linear-gradient(90deg, rgba(0,0,0,.28), transparent 12%, transparent 86%, rgba(0,0,0,.18)),
      linear-gradient(180deg, rgba(255,223,146,.07), transparent 24%, transparent 80%, rgba(0,0,0,.22));
  }
  .book-cardinal img{
    display:block;
    width:100%;
    height:100%;
    object-fit:cover;
    object-position:left center;
  }
  .cardinal-number{
    position:absolute;
    z-index:3;
    right:10px;
    bottom:9px;
    padding:3px 7px 2px;
    border:1px solid rgba(218,183,97,.52);
    border-radius:2px;
    background:rgba(40,21,10,.78);
    color:#ead18c;
    font-family:'Cormorant Garamond', serif;
    font-size:11px;
    font-style:italic;
    letter-spacing:.06em;
    text-shadow:0 1px 2px #000;
    box-shadow:0 2px 6px rgba(0,0,0,.45);
  }
  .slot--cardinal:hover .book-cardinal,
  .slot--cardinal:focus-within .book-cardinal{
    transform:translateY(-13px) rotateY(-1deg) rotateZ(-.15deg) scale(1.045);
    box-shadow:
      -5px 2px 0 #2a160c,
      -9px 5px 14px rgba(0,0,0,.44),
      16px 24px 32px rgba(0,0,0,.62),
      0 0 0 1px rgba(233,205,134,.24);
    filter:saturate(1) brightness(1.02) sepia(.03);
  }
  .book-cardinal:focus-visible{outline:2px solid var(--gold-bright); outline-offset:4px;}
  @media (max-width:640px){
    .slot--cardinal{width:205px;}
    .book-cardinal{width:205px; height:242px;}
  }

'''
if '.book-cardinal{' not in s:
    if css_anchor not in s:
        raise SystemExit('Could not find CSS anchor for Cardinal Virtues book')
    s = s.replace(css_anchor, cardinal_css + css_anchor, 1)

# Update the visible Philosophy & Principles count from 6 to 7.
old_count = '''      <span class="wing-title" id="w1">Φιλοσοφία &amp; Αρχές</span>\n      <span class="wing-thread"></span>\n      <span class="wing-count">6 τόμοι</span>'''
new_count = '''      <span class="wing-title" id="w1">Φιλοσοφία &amp; Αρχές</span>\n      <span class="wing-thread"></span>\n      <span class="wing-count">7 τόμοι</span>'''
if old_count in s:
    s = s.replace(old_count, new_count, 1)

# Place the new cover book immediately before the Philosophy shelf label.
book_marker = '        <div class="shelf-label"><span class="lead">Philosophy</span><span>and Principles</span></div>'
book_html = '''        <!-- 0020 · Οι Τέσσερις Θεμελιώδεις Αρετές -->\n        <div class="slot slot--cardinal">\n          <a class="book-cardinal" target="_blank" rel="noopener"\n             href="library/0020-tesseris-themeliodeis-aretes.pdf"\n             aria-label="Άνοιγμα: Οι Τέσσερις Θεμελιώδεις Αρετές">\n            <img src="assets/cardinal-virtues-book.webp" width="340" height="402"\n                 alt="Οι Τέσσερις Θεμελιώδεις Αρετές — παλαιό δερματόδετο βιβλίο" loading="lazy" decoding="async">\n            <span class="cardinal-number">Αρ. 0020</span>\n          </a>\n          <div class="flyout">\n            <h4>Οι Τέσσερις Θεμελιώδεις Αρετές</h4>\n            <p class="flyout-note">Φρόνηση · Εγκράτεια · Ανδρεία · Δικαιοσύνη · Σεβτ. Αδ. Ιωάννης Μπενετάτος, Μέγας Διδάσκαλος</p>\n            <a href="library/0020-tesseris-themeliodeis-aretes.pdf" target="_blank" rel="noopener">Ανάγνωση →</a>\n          </div>\n        </div>\n'''
if 'href="library/0020-tesseris-themeliodeis-aretes.pdf"' not in s:
    if book_marker not in s:
        raise SystemExit('Could not find Philosophy shelf label')
    s = s.replace(book_marker, book_html + book_marker, 1)

p.write_text(s, encoding='utf-8')
