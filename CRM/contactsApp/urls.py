from django.urls import path
from .views import contacts, entites, entite_detail, contact_detail, EntiteDetail, ContactDetail, page_login, register, logout_user, edit_profile, view_profile, change_password, CustomPasswordChangeView, repartition_source_acquisition, change_password, add_entite
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,  PasswordChangeDoneView


urlpatterns =[
    path('contacts/', contacts, name = "contacts"),
    path('entites/', entites, name = "entites" ),
    path('entite/<int:pk>/', entite_detail, name = "entite-detail"),
    path('entite-detail/<int:pk>/', EntiteDetail.as_view(), name ="entite-detail-class"),
    path ('contact/<int:pk>/', contact_detail, name = 'contact-detail'),
    path('contact-detail/<int:pk>/', ContactDetail.as_view(), name ="contact-detail-class"),
    path ('login/', page_login, name = "login"),
    path ('register/', register, name = "register"),
    path('logout/', logout_user, name='logout'),
    path('password_reset/', PasswordResetView.as_view(template_name='mdp_oublie/password_reset.html'), name = 'password_reset'),
	path('password_reset/done/', PasswordResetDoneView.as_view(template_name='mdp_oublie/password_reset_done.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='mdp_oublie/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='mdp_oublie/password_reset_complete.html'), name='password_reset_complete'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('profile/', view_profile, name='profile'),
    path('<int:user_id>/password/', change_password, name='change_password'),
    path('acquisition_source/', repartition_source_acquisition, name='acquisition_source'),
    path('profile/', view_profile, name='profile'),
    path('entite_new/', add_entite, name='entite_new'),
    
]


  
