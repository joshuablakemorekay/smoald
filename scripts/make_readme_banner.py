"""
Build a README banner: the SMOALD bolt + wordmark on a clean white rounded
card, so the logo always sits on the brand's white background on GitHub
(GitHub strips CSS backgrounds, and transparent PNGs otherwise follow the
viewer's light/dark theme). Run from repo root: python scripts/make_readme_banner.py
"""
from PIL import Image, ImageDraw
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"


def resize_h(img: Image.Image, h: int) -> Image.Image:
    w = round(img.width * h / img.height)
    return img.resize((w, h), Image.LANCZOS)


def main():
    # wide banner: bolt + wordmark side by side, centred on a full-width white field
    bolt = resize_h(Image.open(ASSETS / "smoald-bolt.png").convert("RGBA"), 150)
    word = resize_h(Image.open(ASSETS / "smoald-wordmark.png").convert("RGBA"), 78)

    W, H, radius, gap = 1280, 300, 26, 40

    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(canvas)
    # white card with a faint edge so it still reads on a white (light-mode) page
    d.rounded_rectangle([0, 0, W - 1, H - 1], radius=radius, fill=(255, 255, 255, 255))
    d.rounded_rectangle([0, 0, W - 1, H - 1], radius=radius, outline=(26, 18, 11, 28), width=2)

    group_w = bolt.width + gap + word.width
    x0 = (W - group_w) // 2
    canvas.alpha_composite(bolt, (x0, (H - bolt.height) // 2))
    canvas.alpha_composite(word, (x0 + bolt.width + gap, (H - word.height) // 2))

    out = ASSETS / "smoald-readme-banner.png"
    canvas.save(out)
    print(f"banner -> {canvas.size} at {out}")


if __name__ == "__main__":
    main()
