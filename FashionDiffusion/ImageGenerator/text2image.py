import torch
import firebase_admin
from firebase_admin import credentials, storage
from diffusers import DiffusionPipeline
from diffusers import EulerAncestralDiscreteScheduler
import sys, datetime
from uuid import uuid4

# set up firebase credentials, put the firebase admin sdk in the same directory as this python file
cred = credentials.Certificate("greenieverse-firebase-adminsdk-e3b5a-f38879b828.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'greenieverse.appspot.com'
})

# Install pre-trained pipeline from hugging face
pipeline = DiffusionPipeline.from_pretrained("22h/vintedois-diffusion-v0-1")
pipe = pipeline.to("cuda") # Use cuda only if the GPU is nvidia

# Generate image 


# Adjustment parameters
# pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config) # scheduler algorithms
height = 512
width = 512
cfg_scale = 10 # guidance_scale
seed = torch.Generator("cuda").manual_seed(44) # generator
step = 50 # num_inference_steps
negative = "out of frame, duplicate, watermark, signature, text, ugly, morbid, mutated, deformed, blurry, bad anatomy, bad proportions, cloned face, disfigured, fused fingers, fused limbs, too many fingers, long neck, twisted face, three legs"
prompt = sys.argv[1]

# image generation
image = pipe(prompt, num_inference_steps=step, guidance_scale=cfg_scale, generator=seed, negative_prompt=negative).images[0]
image.save(f"test.png")



# Save to firebase storage and get image url
bucket = storage.bucket()
token = uuid4()
metadata = {"firebaseStorageDownloadTokens": token}
blob = bucket.blob("/test.png")
blob.metadata = metadata
with open("/test.png", "rb") as image_file:
    blob.upload_from_file(image_file, content_type="image/png")
api = blob.generate_signed_url(expiration=datetime.datetime(2024, 1, 20), method='GET', access_token=token)

print(api) # return url