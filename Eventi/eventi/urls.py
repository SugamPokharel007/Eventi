from django.contrib import admin
from django.urls import path
from emsapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('ticket/', views.ticket, name='ticket'),
    path('buy-tickets/', views.submit_form, name='buy_tickets'),
    path('ticketslip/', views.ticketslip, name='ticketslip'),
    path('about/', views.about, name='about'),
    path('events/', views.events_view, name='events'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
