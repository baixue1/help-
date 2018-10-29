from django.views.generic import TemplateView

import xadmin
from django.urls import path, re_path, include
from users.views import LoginView, RegisterView, ActiveUserView, UploadImageView, UpdatePwdView, SendEmailCodeView, \
    UpdateEmailView

from users import views

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('captcha/',include('captcha.urls')),
    path('register/',RegisterView.as_view(),name = 'register'),
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),
    path("users/", include('users.urls', namespace="users")),
    path("image/upload", UploadImageView.as_view(),name='image_upload'),
    path("update/pwd/", UpdatePwdView.as_view(),name='update_pwd'),
    path("sendemail_code/", SendEmailCodeView.as_view(),name='sendemail_code'),
    path("update_email/", UpdateEmailView.as_view(),name='update_email'),
]
