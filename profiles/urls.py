from django.urls import path
from .views import (
    profile_test_view,
    MyProfileView,
    MyProfileData,
)

app_name = 'profiles'

urlpatterns = [
    path('my/', MyProfileView.as_view(), name='my-profile-view'),
    path('my-profile-json/', MyProfileData.as_view(), name='my-profile-data'),
    path('test/', profile_test_view, name='profile-test')
]
