from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

import inventory.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', inventory.views.ListPropertyView.as_view(), name='property-list'),
	url(r'^new$', inventory.views.CreatePropertyView.as_view(), name='property-new'),
    url(r'^feed/<pk=id>$', inventory.views.DetailPropertyView.as_view(), name='property-detail'),
    # Examples:
    # url(r'^$', 'unlyst.views.home', name='home'),
    # url(r'^unlyst/', include('unlyst.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	# Server statics and uploaded media
	urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
