# encoding: utf8
from django.db import models, migrations
import easy_thumbnails.fields
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20140216_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, verbose_name='Image file', upload_to=gallery.models.gallery_image_upload_to),
        ),
    ]
