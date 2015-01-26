from django.conf.urls import patterns, include, url
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'askGaga.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^hello/'  , views.helloworld, 	name='helloworld'),
	url(r'^profile' , views.profile, 	name='profile'),

	url(r'^likeIt/', views.likeIt, 	name='likeIt'),

	url(r'^reg_user/', views.reg_user, 	name='reg_user'),
	url(r'^register', views.register, 	name='register'),

	url(r'^ask/', 	  views.ask, 		name='ask'),	
	url(r'^answer/',  views.answer, 	name='answer'),

	url(r'^log_in/', views.log_in,		name='log_in'),
	url(r'^login/'  , views.login, 		name='login'),

	url(r'^logout'  , views.logout, 	name='logout'),

	
	
	url(r'^question/', views.qw, 	name='qw'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^'	, views.index, 		name='index'),
	url(r'^default/', views.default, 	name='default'),
	
	
)
