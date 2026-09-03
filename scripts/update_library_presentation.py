from pathlib import Path
import base64

# Materialise the two user-provided images from the temporary base64 staging files.
def materialise(staged_path: str, asset_path: str) -> None:
    staged = Path(staged_path)
    asset = Path(asset_path)
    if asset.exists():
        return
    if not staged.exists():
        raise SystemExit(f'Missing staged image data: {staged_path}')
    asset.parent.mkdir(parents=True, exist_ok=True)
    asset.write_bytes(base64.b64decode(staged.read_text(encoding='utf-8').strip()))

materialise('scripts/ioannis-benetatos.b64', 'assets/ioannis-benetatos.webp')
materialise('scripts/governance-frame.b64', 'assets/governance-frame.webp')

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# Use the exact uploaded portrait rather than the previously linked external photo.
s = s.replace(
    'src="https://nglgreece.org/wp-content/uploads/2026/04/benetatos-683x1024.jpeg"',
    'src="assets/ioannis-benetatos.webp" width="300" height="450"',
    1,
)
s = s.replace(
    'alt="Επίσημη φωτογραφία Μεγάλου Διδασκάλου"',
    'alt="Σεβτ. Αδ. Ιωάννης Μπενετάτος, Μέγας Διδάσκαλος"',
    1,
)

# Show the full uploaded portrait and softly merge its dark background into the page.
s = s.replace(
    '''  .grand-master-photo-wrap{\n    position:relative;\n    width:100%;\n    height:265px;\n    overflow:hidden;\n    border-radius:12px;\n    background:\n      radial-gradient(ellipse at 50% 38%, rgba(201,162,75,0.11), transparent 58%),\n      var(--bg-deep);\n    box-shadow:0 18px 36px -22px rgba(0,0,0,.92);\n  }''',
    '''  .grand-master-photo-wrap{\n    position:relative;\n    width:100%;\n    height:280px;\n    overflow:hidden;\n    border-radius:12px;\n    background:\n      radial-gradient(ellipse at 50% 42%, rgba(201,162,75,0.08), transparent 62%),\n      var(--bg-deep);\n    box-shadow:0 18px 36px -22px rgba(0,0,0,.92);\n  }''',
    1,
)
s = s.replace(
    '''  .grand-master-photo{\n    display:block;\n    width:100%;\n    height:100%;\n    object-fit:cover;\n    object-position:center 16%;\n    -webkit-mask-image:radial-gradient(ellipse 92% 96% at 50% 43%, #000 68%, transparent 100%);\n    mask-image:radial-gradient(ellipse 92% 96% at 50% 43%, #000 68%, transparent 100%);\n  }''',
    '''  .grand-master-photo{\n    display:block;\n    width:100%;\n    height:100%;\n    object-fit:contain;\n    object-position:center center;\n    -webkit-mask-image:radial-gradient(ellipse 86% 94% at 50% 46%, #000 58%, rgba(0,0,0,.92) 72%, transparent 100%);\n    mask-image:radial-gradient(ellipse 86% 94% at 50% 46%, #000 58%, rgba(0,0,0,.92) 72%, transparent 100%);\n    filter:drop-shadow(0 10px 16px rgba(0,0,0,.38));\n  }''',
    1,
)

# Replace the missing governance JPG with the tightly cropped frame-only image.
s = s.replace(
    'src="assets/governance-frame.jpg" width="520" height="633"',
    'src="assets/governance-frame.webp" width="300" height="365"',
    1,
)

p.write_text(s, encoding='utf-8')
