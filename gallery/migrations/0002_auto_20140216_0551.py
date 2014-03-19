# encoding: utf8
from django.db import models, migrations
import gallery.models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(verbose_name='Image file', upload_to=gallery.models.gallery_image_upload_to),
        ),
    ]
