from django.contrib import admin
from django.conf.urls.defaults import patterns, include

from django.conf import settings
from django.views.defaults import page_not_found


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from wheelcms_axle.urls import handler500, handler404

from django.views.generic import RedirectView

admin.autodiscover()

## basepatterns are usually not localized,
## wheelpatterns are.

basepatterns = staticfiles_urlpatterns()
wheelpatterns = patterns('')

## or import static_urls; urlpatterns = static_urls.urlpatterns

if not settings.ALLOW_SIGNUP:
    wheelpatterns += patterns('',
        ('^accounts/signup', page_not_found),
    )

basepatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^favicon.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    (r'^tinymce/', include('tinymce.urls')),
)
wheelpatterns += patterns('',
    (r'^accounts/', include('userena.urls')),
    (r'^search/', include('haystack.urls')),
    (r'', include('wheelcms_axle.urls')),
)

if settings.DEBUG:
    basepatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns = basepatterns + wheelpatterns
