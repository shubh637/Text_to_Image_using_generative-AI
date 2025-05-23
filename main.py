
# Commented out IPython magic to ensure Python compatibility.
#diffusers is a hugging face page for using diffusion models from huggingface hub
# %pip install diffusers transformers accelerate

from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt
import torch
device="cuda" if torch.cuda.is_available() else "cpu"
print(device)

# Commented out IPython magic to ensure Python compatibility.
# %pip show torch

model_id1 = "dreamlike-art/dreamlike-diffusion-1.0"
model_id2 = "stabilityai/stable-diffusion-xl-base-1.0"

pipe = StableDiffusionPipeline.from_pretrained(model_id1, torch_dtype=torch.float16, use_safetensors=True)
pipe = pipe.to("cuda")

prompt = """text to image use interface inmages
"""

image = pipe(prompt).images[0]

image

print("[PROMPT]: ",prompt)
plt.imshow(image);
plt.axis('off');

prompt2 = """A girl is sittig on a chair & She is accompanied by her tiger. Make sure to keep it cinematic and color to be golden iris
"""

image = pipe(prompt2).images[0]

print('[PROMPT]: ',prompt2)
plt.imshow(image);
plt.axis('off');

pipe.save_pretrained('saved_model1')

"""https://huggingface.co/docs/diffusers/using-diffusers/loading

### Working with Stable Diffusion parameters

* Negative prompting
* num_inference_steps
* height
* weight
* num_images_per_prompt
"""

def generate_image(pipe, prompt, params):
  img = pipe(prompt, **params).images

  num_images = len(img)
  if num_images>1:
    fig, ax = plt.subplots(nrows=1, ncols=num_images)
    for i in range(num_images):
      ax[i].imshow(img[i]);
      ax[i].axis('off');

  else:
    fig = plt.figure()
    plt.imshow(img[0]);
    plt.axis('off');
  plt.tight_layout()

prompt = "dreamlike, beautiful girl playing the festival of colors, draped in traditional Indian attire, throwing colors"

params = {}

generate_image(pipe, prompt, params)

#num inference steps
params = {'num_inference_steps': 100}

generate_image(pipe, prompt, params)

#height width
params = {'num_inference_steps': 100, 'width': 512, 'height': int(1.5*640)}

generate_image(pipe, prompt, params)

#num_images_per_prompt
params = {'num_inference_steps': 100, 'num_images_per_prompt': 2}

generate_image(pipe, prompt, params)

# negative_prompt
params = {'num_inference_steps': 100, 'num_images_per_prompt': 2, 'negative_prompt': 'ugly, distorted, low quality'}

generate_image(pipe, prompt, params)

