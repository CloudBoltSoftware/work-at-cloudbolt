from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'make_it_work.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^jobs/', 'jobs.views.job_index', name='jobs'),
    url(r'^offices/', 'jobs.views.office_index', name='offices'),
]
