from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Label URLs
    path('labels/', views.LabelListCreate.as_view(), name='label-list-create'),
    path('labels/<int:pk>/', views.LabelRetrieveUpdateDestroy.as_view(), name='label-retrieve-update-destroy'),

    # Task URLs
    path('tasks/', views.TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroy.as_view(), name='task-retrieve-update-destroy'),
     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]