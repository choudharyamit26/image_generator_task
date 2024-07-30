from django.db import models


class GeneratedImage(models.Model):
    prompt = models.TextField()
    image = models.ImageField(upload_to='generated_images/')
    file_path = models.CharField(max_length=255, blank=True, null=True)  # Path field to store the image file path
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prompt
