from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0004_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_store',
            name='image',
            field=models.FileField(blank=True, upload_to='Book_images'),
        ),
    ]