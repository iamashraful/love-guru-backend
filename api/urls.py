from django.urls import path

from api.views.transactions.category_views import CategoryListView
from api.views.transactions.transaction_views import TransactionListView, TransactionDetailView
from api.views.transactions.wallet_views import WalletDetailView, WalletListView
from api.views.users.auth_views import LoginView
from api.views.users.profile_view import ProfileListView

urlpatterns = [
    path('login/', LoginView.as_view(), name='api_login_view'),
    path('profiles/', ProfileListView.as_view(), name='profile_list_view'),
    path('wallets/', WalletListView.as_view(), name='wallet_list_view'),
    path('wallets/<int:pk>/', WalletDetailView.as_view(), name='wallet_details_view'),
    path('categories/', CategoryListView.as_view(), name='category_list_view'),
    path('transactions/', TransactionListView.as_view(), name='transaction_list_view'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction_details_view'),
]
