from django.conf.urls import url
from django.urls import path
from .views import IndexView, FullListView, AdDetail, ad_favor, ad_create, category_choice, CategoryView, AdEdit, AdDelete
from django.views.generic import TemplateView

app_name = 'ads'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    url(r'(?P<ad_id>[0-9]+)/$', AdDetail.as_view(), name='ad_detail'),
    path('full_list/', FullListView.as_view(), name='full_list'),
    path('<int:ad_id>/edit/', AdEdit.as_view(), name='ad_edit'),
    path('<int:ad_id>/ad_favor/', ad_favor, name='ad_favor'),
    path('<int:ad_id>/ad_delete/', AdDelete.as_view(), name='ad_delete'),
    path('ad_delete/', TemplateView.as_view(template_name='ads/ad_delete_success.html'), name='ad_delete_success'),
    path('ad_create/', ad_create, name='ad_create'),
    path('category_list/', category_choice, name='category_list'),
    path('category_list/<int:category_id>', CategoryView.as_view(), name='category_view'),
]
