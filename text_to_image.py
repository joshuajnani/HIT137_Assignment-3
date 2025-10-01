from diffusers import StableDiffusionPipeline
import torch

class TextToImageGenerator:
    def __init__(self, model_name="runwayml/stable-diffusion-v1-5"):
        # Detect device
        device = "cuda" if torch.cuda.is_available() else "cpu"

        # Only use float16 if GPU is available
        if device == "cuda":
            self.pipe = StableDiffusionPipeline.from_pretrained(
                model_name,
                torch_dtype=torch.float16,
            ).to(device)
        else:
            self.pipe = StableDiffusionPipeline.from_pretrained(
                model_name,
            ).to(device)

    def generate_image(self, prompt, output_path="output.png"):
        image = self.pipe(prompt).images[0]
        image.save(output_path)
        return output_path