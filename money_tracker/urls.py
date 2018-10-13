from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('api/', include('api.urls'), name='API Urls'),
    path('', include_docs_urls(title='Money Tracker API', permission_classes=[])),
    path('api-auth/', include('rest_framework.urls')),
]
