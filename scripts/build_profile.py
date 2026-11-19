"""Gera os SVGs do perfil (botões e cartões da stack).

Uso (na raiz do repositório):
    python scripts/build_profile.py

O que ele faz:
  1. Botões (idioma, movimento e ações dos projetos) em assets/buttons/
  2. Cartões da stack em assets/stack/, a partir dos ícones em assets/icons/

Rode o script de novo sempre que mudar um rótulo de botão ou a lista da stack.

Paleta (GitHub dark): fundo #0d1117 · superfície #161b22 · borda #30363d
texto #e6edf3 / #c9d1d9 / #8b949e · acento #ab7df8 (uso pontual)
"""

from __future__ import annotations

import re
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

SURFACE = "#161b22"
BORDER = "#30363d"
TEXT = "#e6edf3"
MUTED = "#8b949e"
ACCENT = "#ab7df8"
INK = "#0d1117"
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

# Largura aproximada de cada caractere a 13px, peso 600 (métrica parecida com Segoe/Helvetica).
_NARROW = set("iljtfrI.,:;·!' ")
_WIDE = set("mwMWOQGDCH")


def text_width(s: str, size: float = 13) -> float:
    units = 0.0
    for ch in s:
        if ch in _NARROW:
            units += 0.34
        elif ch in _WIDE:
            units += 0.86
        elif ch.isupper():
            units += 0.70
        else:
            units += 0.58
    return units * size


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


# ---------------------------------------------------------------- botões

ARROW = "M{x} {y} h12 M{x2} {y1} l5 5 l-5 5"
EXTERNAL = "M{x} {y2} l9 -9 M{x1} {y1} h6 v6"


def button(label: str, *, active: bool = False, icon: str = "arrow") -> str:
    h = 34
    pad = 16
    w = round(pad + text_width(label) + 14 + 18 + pad - 6)
    bg = ACCENT if active else SURFACE
    stroke = ACCENT if active else BORDER
    fg = INK if active else TEXT
    ax = w - pad - 14
    if icon == "external":
        d = EXTERNAL.format(x=ax + 2, y2=h / 2 + 5, x1=ax + 5, y1=h / 2 - 4)
    else:
        d = ARROW.format(x=ax, y=h / 2, x2=ax + 7, y1=h / 2 - 5)
    label_x = escape(label)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label_x}">
  <title>{label_x}</title>
  <rect x="0.75" y="0.75" width="{w - 1.5}" height="{h - 1.5}" rx="8" fill="{bg}" stroke="{stroke}" stroke-width="1.5"/>
  <text x="{pad}" y="21.5" fill="{fg}" font-family="{FONT}" font-size="13" font-weight="600">{label_x}</text>
  <path d="{d}" fill="none" stroke="{fg}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
"""


BUTTONS = {
    # idioma
    "lang-pt-active": ("PT · Português", True, "arrow"),
    "lang-pt": ("PT · Português", False, "arrow"),
    "lang-en-active": ("EN · English", True, "arrow"),
    "lang-en": ("EN · English", False, "arrow"),
    # ações dos projetos
    "screens-pt": ("Ver as telas", False, "external"),
    "site-pt": ("Ver o site", False, "external"),
    "code-pt": ("Ver o código", False, "external"),
    "screens-en": ("See the screens", False, "external"),
    "site-en": ("Visit the site", False, "external"),
    "code-en": ("See the code", False, "external"),
}


# ---------------------------------------------------------------- stack

# nome exibido, arquivo do ícone, monocromático (para logos escuros no fundo escuro)
STACK = [
    ("Python", "python", False),
    ("SQL", None, False),
    ("JavaScript", "javascript", False),
    ("FastAPI", "fastapi", False),
    ("SQLite", "sqlite", False),
    ("Linux", "linux", True),
    ("Git", "git", False),
    ("Astro", "astro", True),
    ("Tailwind CSS", "tailwindcss", False),
    ("Figma", "figma", False),
    ("Claude", "claude", False),
]


def icon_inner(name: str) -> tuple[str, str]:
    raw = (ASSETS / "icons" / f"{name}.svg").read_text(encoding="utf-8")
    view_box = re.search(r'viewBox="([^"]+)"', raw).group(1)
    inner = re.sub(r"^.*?<svg[^>]*>", "", raw, count=1, flags=re.S)
    inner = re.sub(r"</svg>\s*$", "", inner, flags=re.S)
    return view_box, inner


def stack_tile(label: str, icon: str | None, mono: bool) -> str:
    h = 40
    w = 140
    label_x = escape(label)
    if icon:
        vb, inner = icon_inner(icon)
        fill = f' fill="{TEXT}"' if mono else ""
        glyph = f'<svg x="12" y="10" width="20" height="20" viewBox="{vb}"{fill}>{inner}</svg>'
    else:
        # sem logotipo oficial: um monograma neutro, em vez de inventar uma marca
        glyph = (
            f'<rect x="12" y="10" width="20" height="20" rx="5" fill="none" stroke="{MUTED}" stroke-width="1.4"/>'
            f'<text x="22" y="24" text-anchor="middle" fill="{MUTED}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace" font-size="9" font-weight="700">&lt;/&gt;</text>'
        )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label_x}">
  <title>{label_x}</title>
  <rect x="0.75" y="0.75" width="{w - 1.5}" height="{h - 1.5}" rx="8" fill="{SURFACE}" stroke="{BORDER}" stroke-width="1.5"/>
  {glyph}
  <text x="42" y="25" fill="{TEXT}" font-family="{FONT}" font-size="13" font-weight="600">{label_x}</text>
</svg>
"""


def slug(label: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")


def main() -> None:
    for name, (label, active, icon) in BUTTONS.items():
        write(ASSETS / "buttons" / f"{name}.svg", button(label, active=active, icon=icon))
    for label, icon, mono in STACK:
        write(ASSETS / "stack" / f"{slug(label)}.svg", stack_tile(label, icon, mono))
    print("ok: botões e stack gerados")


if __name__ == "__main__":
    main()
