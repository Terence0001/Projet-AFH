import os
import numpy as np
from PIL import Image
import onnxruntime as rt
from django.utils import timezone
from .models import HushemPrediction
from rest_framework import viewsets, status
import torchvision.transforms as transforms
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import HushemPredictionSerializer



class HushemPredictionViewSet(viewsets.ViewSet):
    queryset = HushemPrediction.objects.all()
    permission_classes = [AllowAny]  # Permet l'accès sans authentification

    def get_queryset(self):
        # Renvoie le queryset par défaut pour cette vue
        return self.queryset

    @action(detail=False, methods=['post'])
    def predict(self, request):
        # Récupère la liste des images envoyées avec la requête
        images = request.FILES.getlist('images')
        predictions = []

        for image_file in images:
            # Ouvre l'image à partir du fichier
            image = Image.open(image_file)
            
            # Prétraitement de l'image
            preprocess = transforms.Compose([
                # Redimensionne l'image à une taille de 224x224 pixels
                transforms.Resize((224, 224)),
                # Convertit l'image en un tenseur PyTorch
                transforms.ToTensor(),
                # Normalise les valeurs des pixels de l'image en utilisant les moyennes et les écarts-types spécifiés
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
            ])
            # Applique les transformations de prétraitement à l'image et ajoute une dimension supplémentaire pour créer un lot d'images contenant une seule image
            image_tensor = preprocess(image).unsqueeze(0)

            
            # Charge le modèle ONNX à partir du fichier
            model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), './hushem_model.onnx'))
            sess = rt.InferenceSession(model_path)

            # Préparer les données d'entrée pour le modèle
            input_name = sess.get_inputs()[0].name
            input_data = {input_name: image_tensor.expand(32, -1, -1, -1).numpy()}
            
            # Effectuer une prédiction avec le modèle
            outputs = sess.run(None, input_data)
            predicted = np.argmax(outputs[0])
            precision_array = outputs[0][predicted]
            precision = np.mean(precision_array) # Calcul de la moyenne de la précision
            
            # Récupérer la classe prédite à partir de l'indice de la prédiction
            class_names = ['normal', 'abnormal', 'healthy', 'unhealthy']
            predicted_class = class_names[predicted]
            
            # Enregistrer la date et le résultat de la prédiction dans la base de données
            prediction = HushemPrediction(date=timezone.now(), results=predicted_class, precision=precision)
            prediction.save()
            predictions.append(predicted_class)

        # Renvoie la liste des classes prédites en réponse à la requête
        return Response(predictions)



class HushemPredictionList(viewsets.ViewSet):
    # Renvoie un queryset contenant tous les objets HushemPrediction
    def get_queryset(self):
        return HushemPrediction.objects.all()

    # Gère les requêtes GET pour récupérer la liste des prédictions Hushem
    def list(self, request):
        # Récupère tous les objets HushemPrediction
        predictions = HushemPrediction.objects.all()
        # Sérialise les objets HushemPrediction en utilisant le HushemPredictionSerializer
        serializer = HushemPredictionSerializer(predictions, many=True)
        # Renvoie les données sérialisées en réponse à la requête
        return Response(serializer.data)
    
    # Gère les requêtes POST pour créer une nouvelle prédiction Hushem
    def create(self, request):
        # Valide les données de la requête en utilisant le HushemPredictionSerializer
        serializer = HushemPredictionSerializer(data=request.data)
        if serializer.is_valid():
            # Crée un nouvel objet HushemPrediction avec les données validées
            serializer.save()
            # Renvoie les données sérialisées du nouvel objet en réponse à la requête
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Si les données ne sont pas valides, renvoie les erreurs de validation en réponse à la requête
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Gère également les requêtes POST pour créer une nouvelle prédiction Hushem
    def post(self, request):
        # Valide les données de la requête en utilisant le HushemPredictionSerializer
        serializer = HushemPredictionSerializer(data=request.data)
        if serializer.is_valid():
            # Crée un nouvel objet HushemPrediction avec les données validées
            serializer.save()
            # Renvoie les données sérialisées du nouvel objet en réponse à la requête
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Si les données ne sont pas valides, renvoie les erreurs de validation en réponse à la requête
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
