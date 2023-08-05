from django.urls import path
from .views import HushemPredictionList, HushemPredictionViewSet

urlpatterns = [
    path("predictions/", HushemPredictionList.as_view({"get": "list", "post": "create"}), name="prediction-list"),
    path("predict/", HushemPredictionViewSet.as_view({"post": "predict"}), name="start-prediction")
    # Autres URL de votre application dashboard si nécessaire
]



