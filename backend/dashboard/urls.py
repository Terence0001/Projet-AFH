from django.urls import path
from .views import HushemPredictionList

urlpatterns = [
    path("predictions/", HushemPredictionList.as_view({"get": "list", "post": "create"}), name="prediction-list"),
    # Autres URL de votre application dashboard si nécessaire
]



