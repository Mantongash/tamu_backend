from django.urls import path,re_path,include
from . import views as views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('api/user/', views.UserList.as_view()),
    # path('api/user/user-id/<username>/',views.UserDetails.as_view()),
    # path('api/auth/',ObtainAuthToken.as_view()),
    # path('api/auth/', include('rest_auth.urls')),
    
    path('api/profiles/' ,views.ProfileList.as_view()),
    path('api/images/', views.ImageList.as_view()),
    path('api/countries/' ,views.CountryList.as_view()),
    path('api/ingredients/', views.IngredientList.as_view()),
    path('api/recipeingredients/', views.RecipeIngredientList.as_view()),

    path('api/profile/profile_id/<pk>/', views.Profiledetails.as_view()),
    path('api/image/image_id/', views.Imagedetails.as_view()),
    path('api/country/country_id/', views.Countrydetails.as_view()),
    path('api/recipeingredient/recipeingredient_id/', views.RecipeIngredientdetails.as_view()),
    path('api/ingredient/ingredient_id/', views.Ingredientdetails.as_view()),
    
]

if settings.DEBUG:
  urlpatterns+= static(
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
  )
