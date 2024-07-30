from django.urls import path
from .views import GenerateImagesView, CheckTaskStatusView

urlpatterns = [
    path('generate/', GenerateImagesView.as_view(), name='generate_images'),
    path('status/<task_id>/', CheckTaskStatusView.as_view(), name='check_task_status'),
]
