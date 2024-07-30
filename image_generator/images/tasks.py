import random
import string

import requests
from celery import shared_task
from django.core.files.base import ContentFile

from .models import GeneratedImage


def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


@shared_task
def generate_image(prompt, api_key):
    response = requests.post(
        "https://api.stability.ai/v2beta/stable-image/generate/core",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "image/*"
        },
        files={"none": ''},
        data={
            "prompt": prompt,
            "output_format": "webp",
        },
    )

    if response.status_code == 200:
        file_name = generate_random_string() + '.webp'

        image_file = ContentFile(response.content, file_name)

        image_instance = GeneratedImage(prompt=prompt, image=image_file)

        image_instance.save()

        # protocol = 'http' if settings.DEBUG else 'https'
        # host = request.get_host()
        # image_url = urljoin(f'{protocol}://{127.0.0.1:8000}', image_instance.image.url)
        return {
            'prompt': prompt,
            'image_url': image_instance.image_url,
        }
    else:
        raise Exception(str(response.json()))
