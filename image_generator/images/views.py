from celery.result import AsyncResult
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .models import GeneratedImage
from .tasks import generate_image


class GenerateImagesView(View):
    def get(self, request):
        return render(request, 'generate_images.html')

    def post(self, request):
        try:
            prompt1 = request.POST.get('prompt1')
            prompt2 = request.POST.get('prompt2')
            prompt3 = request.POST.get('prompt3')
            api_key = settings.STABILITY_API_KEY
            task_ids = [
                generate_image.delay(prompt1, api_key).id,
                generate_image.delay(prompt2, api_key).id,
                generate_image.delay(prompt3, api_key).id
            ]

            return JsonResponse({'task_ids': task_ids})
        except Exception as e:
            raise (e)


class CheckTaskStatusView(View):
    def get(self, request, task_id):
        result = AsyncResult(task_id)

        if result.state == 'SUCCESS':
            data = result.get()
            GeneratedImage.objects.create(prompt=data['prompt'], image_url=data['image_url'])
            return JsonResponse({'status': 'SUCCESS', 'data': data})
        else:
            return JsonResponse({'status': result.state})
