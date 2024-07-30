# Generated by Django 5.0.7 on 2024-07-29 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generatedimage',
            name='image_url',
        ),
        migrations.AddField(
            model_name='generatedimage',
            name='file_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='generatedimage',
            name='image',
            field=models.ImageField(default=0, upload_to='generated_images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='generatedimage',
            name='prompt',
            field=models.TextField(),
        ),
    ]
