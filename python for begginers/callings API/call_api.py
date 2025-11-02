import requests
import json
import os

# Replace with your actual subscription key
SUBSCRIPTION_KEY = "your_actual_subscription_key"

# Replace with your actual endpoint (e.g., from Azure portal)
vision_service_address = "https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/analyze"

# Parameters for the API call
parameters = {
    'visualFeatures': 'Description,Color',
    'language': 'en'
}

# Path to the image file
image_path = r"D:\PYTHON\python for begginers\callings API\pictures\PolarBear.jpg"

# Check if the image file exists
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image not found at path: {image_path}")

# Read the image data
with open(image_path, "rb") as image_file:
    image_data = image_file.read()

# Headers for the API call
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY
}

# Make the POST request
response = requests.post(vision_service_address, headers=headers, params=parameters, data=image_data)

# Raise an error if the request failed
response.raise_for_status()

# Parse and print the JSON response
results = response.json()
print(json.dumps(results, indent=2))
