from django.urls import path
from .views import contacts, entites, entite_detail, contact_detail, EntiteDetail, ContactDetail, page_login, register, logout_user, modification_profil
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns =[
    path('contacts/', contacts, name = "contacts"),
    path('entites/', entites, name = "entites" ),
    path('entite/<int:pk>/', entite_detail, name = "entite-detail"),
    path('entite-detail/<int:pk>/', EntiteDetail.as_view(), name ="entite-detail-class"),
    path ('contact/<int:pk>/', contact_detail, name = 'contact-detail'),
    path('contact-detail/<int:pk>/', ContactDetail.as_view(), name ="contact-detail-class"),
    path ('login/', LoginView.as_view(template_name='login.html'), name = "login"),
    path ('register/', register, name = "register"),
    path('logout/', logout_user, name='logout'),
    path('password_reset/', PasswordResetView.as_view(template_name='mdp_oublie/password_reset.html'), name = 'password_reset'),
	path('password_reset/done/', PasswordResetDoneView.as_view(template_name='mdp_oublie/password_reset_done.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='mdp_oublie/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='mdp_oublie/password_reset_complete.html'), name='password_reset_complete'),
    path('modification_profil/', modification_profil, name='modification_profil'),

]


  
