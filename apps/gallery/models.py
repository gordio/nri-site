from datetime import datetime
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer


class Photo(models.Model):
    title = models.CharField(_("Title"), max_length=22)
    image = ThumbnailerImageField(_("Image file"), upload_to="portfolio/",
        resize_source=dict(
            size=(1280, 1024), crop=False, quality=92, sharpen=True
        )
    )

    def image_thumb(self):
        thumbnailer = get_thumbnailer(self.image)
        img = thumbnailer.get_thumbnail({
            'crop': "smart",
            'size': (210, 210),
        })
        return u'<img width="70px" height="70px" src="%s">' % img.url

    image_thumb.short_description = 'Thumbnail'
    image_thumb.allow_tags = True

    def get_absolute_url(self):
        return "%s%s" % (settings.MEDIA_URL, self.image)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")


def slide_pre_delete(sender, instance, signal, *args, **kwargs):
    deleted = instance.image.delete_thumbnails()
    instance.image.delete()


models.signals.pre_delete.connect(slide_pre_delete, sender=Photo)
