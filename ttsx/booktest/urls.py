from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cart/$',views.cart),
    url(r'^detail/$',views.detail),
    url(r'^index/$',views.index),
    url(r'^list/$',views.list),
    url(r'^login/$',views.login),
    url(r'^place_order/$',views.place_order),
    url(r'^register/$',views.register),
    url(r'^user_center_infor/$',views.user_center_info),
    url(r'^user_center_order/$',views.user_center_order),
    url(r'^user_center_site/$',views.user_center_site),
]