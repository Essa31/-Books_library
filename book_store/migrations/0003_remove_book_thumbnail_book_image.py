from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0002_remove_book_image_book_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_store',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='book_store',
            name='image',
            field=models.FileField(blank=True, upload_to='Book_images'),
        ),
    ]