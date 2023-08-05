import torch
from PIL import Image
from .models import HushemPrediction
from rest_framework import viewsets, status
import torchvision.transforms as transforms
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import HushemPredictionSerializer



class HushemPredictionViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def predict(self, request):
        images = request.FILES.getlist('images')
        predictions = []

        for image_file in images:
            image = Image.open(image_file)
            
            # Prétraitement de l'image
            preprocess = transforms.Compose([
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
            ])
            image_tensor = preprocess(image)
            
            # Charger le modèle préentraîné
            model = torch.load('../../hushem_model.onnx', map_location='cpu')
            model.eval()
            
            # Faire une prédiction
            with torch.no_grad():
                outputs = model(image_tensor.unsqueeze(0))
                _, predicted = torch.max(outputs.data, 1)
            
            # Récupérer la classe prédite (vous devrez ajuster cela en fonction de votre modèle)
            class_names = ['normal', 'abnormal', 'healthy', 'unhealthy']
            predicted_class = class_names[predicted.item()]
            
            predictions.append(predicted_class)

        return Response(predictions)


class HushemPredictionList(viewsets.ViewSet):
     
    def get_queryset(self):
        return HushemPrediction.objects.all()

    def list(self, request):
            predictions = HushemPrediction.objects.all()
            serializer = HushemPredictionSerializer(predictions, many=True)
            return Response(serializer.data)
    
    def create(self, request):
        serializer = HushemPredictionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = HushemPredictionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)