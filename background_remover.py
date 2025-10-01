# background_remover.py

from transformers import pipeline

def load_background_remover():
    # Load the model for background removal
    return pipeline(
        "image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)