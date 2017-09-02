from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^employees/$', views.employees, name='employees'),
    url(r'^people/$', views.PersonListView.as_view(), name='people'),
    url(r'^person/(?P<pk>\d+)$', views.PersonDetailView.as_view(), name='book-detail')
]
