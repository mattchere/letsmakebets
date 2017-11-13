from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all/$', views.BetListView.as_view(), name='all-bets'),
    url(r'^bet/(?P<pk>\d+)$', views.BetDetailView.as_view(), name='bet-detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
