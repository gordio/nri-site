# encoding: utf8
from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):
    
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(verbose_name='Title', max_length=22)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(verbose_name='Image file', upload_to='portfolio/')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
            },
            bases=(models.Model,),
        ),
    ]
