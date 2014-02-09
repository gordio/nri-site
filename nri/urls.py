from django.conf.urls import patterns, include, url
from django.contrib import admin
from gallery.views import GalleryListView
from feedback.views import ContactsView


urlpatterns = patterns('',
    url(r'^$', GalleryListView.as_view(), name="gallery"),

    url(r'^contacts/$', ContactsView.as_view(), name="contacts"),
    url(r'^captcha/', include('captcha.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
