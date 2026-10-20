"""Generate AI substitute images for the Shangwan village Manichaean reliefs.

The only photographs of the reliefs are non-free, so they are kept as
references in the gitignored nonfree/shangwan/ folder and never published.
This script runs SDXL img2img locally (GPU) on each reference and writes
several candidates per relief to nonfree/shangwan/ai/ for the user to review.
Nothing is published until the user picks images.

Usage: scratch/genv/Scripts/python scripts/generate_shangwan_substitutes.py [--strength 0.55] [--seeds 3]
"""
import argparse
from pathlib import Path

import torch
from diffusers import StableDiffusionXLImg2ImgPipeline
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "nonfree" / "shangwan"
OUT = SRC / "ai"
MODEL = "stabilityai/stable-diffusion-xl-base-1.0"

STYLE = ("weathered grey granite stone relief carving, low relief, Song dynasty "
         "Chinese Manichaean temple sculpture, Fujian, photographed in soft "
         "daylight, highly detailed chisel marks, museum documentation photo")
PANELS = {
    "A1_and_A2": "two carved stone slabs side by side, each with a haloed seated "
                 "deity, the right figure seated cross-legged on a lotus throne on a "
                 "pedestal, cloud scroll background",
    "B": "three small standing and seated haloed figures in a row on lotus "
         "pedestals, the centre figure seated in meditation, cloud ornament above",
    "C": "a small standing figure in long robes holding an object at the chest, "
         "beside a tall staff on the left edge of the slab",
    "C2": "a small standing figure in long robes holding a staff diagonally, "
          "beside a carved pillar",
    "d1": "a standing monk-like figure in flowing robes holding a tall staff "
          "topped with a flower finial, standing on a lotus, flames or clouds "
          "around the robe",
    "d2": "a standing haloed monk-like figure with hands joined at the chest, "
          "in long robes, standing on a lotus with cloud scrolls",
    "e": "a long horizontal frieze with a central dancing figure holding two "
         "round objects, flanked by intertwined scrolling vine and knot "
         "ornament in a rounded frame",
}
NEGATIVE = "photo of people, color painting, text, watermark, blurry, modern, cartoon"


def prepare(img, long_side=1024):
    w, h = img.size
    s = long_side / max(w, h)
    w, h = int(w * s) // 8 * 8, int(h * s) // 8 * 8
    return img.convert("RGB").resize((w, h), Image.LANCZOS)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strength", type=float, default=0.55)
    ap.add_argument("--seeds", type=int, default=3)
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    pipe = StableDiffusionXLImg2ImgPipeline.from_pretrained(
        MODEL, torch_dtype=torch.float16, variant="fp16", use_safetensors=True)
    pipe.enable_model_cpu_offload()
    for key, desc in PANELS.items():
        src = SRC / f"Manichaean_stone_reliefs_of_Shangwan_village_{key}.gif"
        init = prepare(Image.open(src))
        for seed in range(a.seeds):
            g = torch.Generator("cpu").manual_seed(seed)
            img = pipe(prompt=f"{desc}, {STYLE}", negative_prompt=NEGATIVE,
                       image=init, strength=a.strength, guidance_scale=6.0,
                       num_inference_steps=30, generator=g).images[0]
            path = OUT / f"shangwan_{key}_s{seed}.png"
            img.save(path)
            print("wrote", path.name, flush=True)


if __name__ == "__main__":
    main()
