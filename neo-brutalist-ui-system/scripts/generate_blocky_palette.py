#!/usr/bin/env python3
"""Generate adaptive blocky design tokens from two input colors."""

from __future__ import annotations

import argparse
import json
import re
from typing import Dict, Tuple

RGB = Tuple[int, int, int]


def parse_hex_color(value: str) -> RGB:
    match = re.fullmatch(r"#?([0-9a-fA-F]{6})", value.strip())
    if not match:
        raise ValueError(f"Invalid hex color: {value}")
    hex_value = match.group(1)
    return tuple(int(hex_value[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def to_hex(rgb: RGB) -> str:
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def clamp_channel(value: float) -> int:
    return max(0, min(255, round(value)))


def mix(left: RGB, right: RGB, t: float) -> RGB:
    return (
        clamp_channel(left[0] * (1 - t) + right[0] * t),
        clamp_channel(left[1] * (1 - t) + right[1] * t),
        clamp_channel(left[2] * (1 - t) + right[2] * t),
    )


def srgb_to_linear(channel: int) -> float:
    c = channel / 255.0
    if c <= 0.04045:
        return c / 12.92
    return ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb: RGB) -> float:
    r = srgb_to_linear(rgb[0])
    g = srgb_to_linear(rgb[1])
    b = srgb_to_linear(rgb[2])
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(a: RGB, b: RGB) -> float:
    l1 = relative_luminance(a)
    l2 = relative_luminance(b)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def pick_foreground(bg: RGB) -> RGB:
    dark = (26, 26, 26)
    light = (240, 240, 232)
    return dark if contrast_ratio(dark, bg) >= contrast_ratio(light, bg) else light


def adapt_for_background(color: RGB, bg: RGB, minimum: float = 3.0) -> RGB:
    if contrast_ratio(color, bg) >= minimum:
        return color
    target = pick_foreground(bg)
    for step in range(1, 21):
        candidate = mix(color, target, step / 20.0)
        if contrast_ratio(candidate, bg) >= minimum:
            return candidate
    return target


def to_css_vars(vars_map: Dict[str, str]) -> str:
    return "\n".join(f"  --{key}: {value};" for key, value in vars_map.items())


def build_palette(base: RGB, accent: RGB) -> Dict[str, Dict[str, str]]:
    white = (255, 255, 255)
    black = (0, 0, 0)

    light_background = mix(base, white, 0.84)
    light_surface = mix(base, white, 0.92)
    light_surface_alt = mix(base, white, 0.78)
    light_surface_muted = mix(base, white, 0.68)
    light_foreground = pick_foreground(light_background)
    light_border = mix(light_foreground, light_background, 0.15)
    light_border_subtle = mix(light_foreground, light_background, 0.72)
    light_accent = adapt_for_background(accent, light_background, 3.0)
    light_accent_hover = mix(light_accent, black, 0.12)
    light_accent_light = mix(light_accent, light_background, 0.58)

    dark_background = mix(base, black, 0.78)
    dark_surface = mix(base, black, 0.65)
    dark_surface_alt = mix(base, black, 0.58)
    dark_surface_muted = mix(base, black, 0.52)
    dark_foreground = pick_foreground(dark_background)
    dark_border = mix(dark_foreground, dark_background, 0.22)
    dark_border_subtle = mix(dark_foreground, dark_background, 0.68)
    dark_accent = adapt_for_background(accent, dark_background, 3.0)
    dark_accent_hover = mix(dark_accent, dark_foreground, 0.18)
    dark_accent_light = mix(dark_accent, dark_foreground, 0.45)

    return {
        "light": {
            "background": to_hex(light_background),
            "background-alt": to_hex(light_foreground),
            "surface": to_hex(light_surface),
            "surface-alt": to_hex(light_surface_alt),
            "surface-strong": to_hex(light_foreground),
            "surface-muted": to_hex(light_surface_muted),
            "foreground": to_hex(light_foreground),
            "foreground-muted": to_hex(mix(light_foreground, light_background, 0.50)),
            "foreground-subtle": to_hex(mix(light_foreground, light_background, 0.62)),
            "foreground-inverse": to_hex(light_background),
            "border": to_hex(light_border),
            "border-subtle": to_hex(light_border_subtle),
            "accent": to_hex(light_accent),
            "accent-hover": to_hex(light_accent_hover),
            "accent-light": to_hex(light_accent_light),
            "shadow-color": to_hex(light_foreground),
            "shadow-accent": to_hex(light_accent),
        },
        "dark": {
            "background": to_hex(dark_background),
            "background-alt": to_hex(dark_foreground),
            "surface": to_hex(dark_surface),
            "surface-alt": to_hex(dark_surface_alt),
            "surface-strong": to_hex(dark_border),
            "surface-muted": to_hex(dark_surface_muted),
            "foreground": to_hex(dark_foreground),
            "foreground-muted": to_hex(mix(dark_foreground, dark_background, 0.42)),
            "foreground-subtle": to_hex(mix(dark_foreground, dark_background, 0.58)),
            "foreground-inverse": to_hex(dark_background),
            "border": to_hex(dark_border),
            "border-subtle": to_hex(dark_border_subtle),
            "accent": to_hex(dark_accent),
            "accent-hover": to_hex(dark_accent_hover),
            "accent-light": to_hex(dark_accent_light),
            "shadow-color": to_hex(dark_accent_light),
            "shadow-accent": to_hex(dark_accent),
        },
    }


def print_css(palette: Dict[str, Dict[str, str]]) -> None:
    print(":root {")
    print(to_css_vars(palette["light"]))
    print("}")
    print()
    print(':root[data-theme="dark"] {')
    print(to_css_vars(palette["dark"]))
    print("}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate adaptive blocky design tokens from base + accent colors."
    )
    parser.add_argument("--base", required=True, help="Base color hex, e.g. #f0f0e8")
    parser.add_argument("--accent", required=True, help="Accent color hex, e.g. #2d5a2d")
    parser.add_argument(
        "--format",
        choices=("css", "json", "both"),
        default="both",
        help="Output format.",
    )
    args = parser.parse_args()

    base = parse_hex_color(args.base)
    accent = parse_hex_color(args.accent)
    palette = build_palette(base, accent)

    if args.format in ("css", "both"):
        print_css(palette)
    if args.format in ("json", "both"):
        if args.format == "both":
            print()
        print(json.dumps(palette, indent=2))


if __name__ == "__main__":
    main()
