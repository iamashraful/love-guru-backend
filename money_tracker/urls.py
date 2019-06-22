from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('api/', include('api.urls'), name='API Urls'),
    path('', include_docs_urls(title='Money Tracker API', permission_classes=[])),
    path('api-auth/', include('rest_framework.urls')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
