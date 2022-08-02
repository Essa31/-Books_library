
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0003_remove_book_thumbnail_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_store',
            name='image',
            field=models.FileField(upload_to='Book_images'),
        ),
    ]