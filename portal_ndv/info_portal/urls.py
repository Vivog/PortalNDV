from django.urls import path
from info_portal.views import *

urlpatterns = [
    path('', index, name='index'),
    # path('register/', RegisterUser.as_view(), name='register'),
    # path('login/', LoginUser.as_view(), name='login'),
    # path('logout/', logout_user, name='logout'),
    # path('staff/', Staff_DivList.as_view(), name='staff'),
    # path('staff/<slug:div_slug>/', StaffDetailList.as_view(), name='div_staff-detail'),
    # path('staff/<slug:div_slug>/<slug:staff_slug>/', PersonDetailList.as_view(), name='person-detail'),
    # path('add_staff/<slug:div_slug>/', AddPersonView.as_view(), name='addstaff'),
    # path('staff/edit_info_person/<slug:staff_slug>/', EditInfoPersonView.as_view(), name='edit-info_person'),
    # path('divisions/', DivisionsList.as_view(), name='divisions'),
    # path('divisions/<slug:div_slug>/', DivisionsDetailList.as_view(), name='division-detail'),
    # path('add_division/', AddDivisionView.as_view(), name='add-division'),
    # path('documents/', DocList.as_view(), name='doc'),


]