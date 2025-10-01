# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True, use_fast=True, device=0)