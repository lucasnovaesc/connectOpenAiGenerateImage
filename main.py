import openai
from dotenv import load_dotenv
import os

openai.api_key = ""

response = openai.Image.create(
  prompt="a realist photo of unicorn",
  n=1,
  size="256x256"
)
image_url = response["data"][0]["url"]

print (image_url)
