from rest_framework import serializers
from .models import HushemPrediction

class HushemPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HushemPrediction
        fields = '__all__'  # Inclut tous les champs du modèle dans le serializer
