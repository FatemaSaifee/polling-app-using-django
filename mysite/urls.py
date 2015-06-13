from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^accounts/login/$', 'mysite.views.login'),
    url(r'^accounts/auth/$', 'mysite.views.auth_view'),
    url(r'^accounts/logout/$', 'mysite.views.logout'),
    url(r'^accounts/loggedin/$', 'mysite.views.loggedin'),
    url(r'^accounts/invalid/$', 'mysite.views.invalid_login'),
    url(r'^accounts/register/$', 'mysite.views.register_user'),
    url(r'^accounts/register_employer/$', 'mysite.views.register_employer'),
    url(r'^accounts/register_success/$', 'mysite.views.register_success'),
    url(r'^accounts/register_employer_success/$', 'mysite.views.register_success'),
)
