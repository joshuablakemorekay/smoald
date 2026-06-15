"""Make the dark background of the SMOALD logo screenshots transparent.

The logos are bright artwork on a near-black background. We key transparency
off each pixel's brightness (max RGB channel): very dark -> transparent,
bright -> opaque, with a soft ramp in between to feather the edges and avoid
a hard halo. Bright art (white SM, orange ALD, glowing cloud, grey circuit
lines) is preserved; the dark box dissolves.
"""
import sys
from PIL import Image

def knockout(src, dst, lo, hi):
    im = Image.open(src).convert("RGBA")
    px = im.load()
    w, h = im.size
    span = float(hi - lo)
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            v = max(r, g, b)            # HSV "value" — keeps coloured art bright
            if v <= lo:
                na = 0
            elif v >= hi:
                na = a
            else:
                na = int(a * (v - lo) / span)
            if na != a:
                px[x, y] = (r, g, b, na)
    im.save(dst)
    # report how much became see-through
    clear = sum(1 for y in range(h) for x in range(w) if px[x, y][3] == 0)
    print(f"{dst}: {w}x{h}, {100*clear//(w*h)}% transparent")

if __name__ == "__main__":
    base = sys.argv[1]
    knockout(f"{base}/smoald-logo-hero.png", f"{base}/smoald-logo-hero.png", 26, 64)
    knockout(f"{base}/smoald-logo-nav.png",  f"{base}/smoald-logo-nav.png",  26, 60)
    print("done")
