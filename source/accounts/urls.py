from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import AuthorRegisterView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="../templates/accounts/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('registration/', AuthorRegisterView.as_view(), name="registration"),

]
