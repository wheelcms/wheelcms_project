from django.contrib import admin
from django.conf.urls.defaults import patterns, include

from django.conf import settings
from django.views.defaults import page_not_found


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from wheelcms_axle.urls import handler500, handler404

admin.autodiscover()


urlpatterns = staticfiles_urlpatterns()

## or import static_urls; urlpatterns = static_urls.urlpatterns

if not settings.ALLOW_SIGNUP:
    urlpatterns += patterns('',
        ('^accounts/signup', page_not_found),
    )

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^favicon.ico$', 'django.views.generic.simple.redirect_to',
                        {'url': '/static/images/favicon.ico'}),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^accounts/', include('userena.urls')),
    (r'^search/', include('haystack.urls')),
    (r'', include('wheelcms_axle.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

