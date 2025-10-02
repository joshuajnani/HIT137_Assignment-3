# Import stable diffusion pipelinne
from diffusers import StableDiffusionPipeline
import torch
# Define class that generates images from text prompts using the Stable Diffusion ai model
class TextToImageGenerator:
    def __init__(self, model_name="runwayml/stable-diffusion-v1-5"):
        # Detects if a compatible gpu is available
        device = "cuda" if torch.cuda.is_available() else "cpu"
        # Load the stable diffusion model using gpu if avalable
        if device == "cuda":
            self.pipe = StableDiffusionPipeline.from_pretrained(
                model_name,
                torch_dtype=torch.float16,
            ).to(device)
        # Load the stable diffusion model using the cpu, if an appropriate gpu is unavailable
        else:
            self.pipe = StableDiffusionPipeline.from_pretrained(
                model_name,
            ).to(device)
    # Generate an image from a text prompt and save it to disk using the stable diffusion model
    def generate_image(self, prompt, output_path="generated_image.png"):
        image = self.pipe(prompt).images[0] # Creates the image
        image.save(output_path)             # Saves the image to the chosen path
        return output_path