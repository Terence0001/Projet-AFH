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
        return self.queryset

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
            image_tensor = preprocess(image).unsqueeze(0)
            
            # Charger le modèle à partir d'un fichier ONNX
            sess = rt.InferenceSession('C:\\Users\\teren\\Documents\\GitHub\\Projet-AFH\\backend\\dashboard\\hushem_model.onnx')

            # Préparer les données d'entrée
            input_name = sess.get_inputs()[0].name
            input_data = {input_name: image_tensor.expand(32, -1, -1, -1).numpy()}
            
            # Effectuer une prédiction
            outputs = sess.run(None, input_data)
            predicted = np.argmax(outputs[0])
            precision_array = outputs[0][predicted]
            precision = np.mean(precision_array)
            
            # Récupérer la classe prédite
            class_names = ['normal', 'abnormal', 'healthy', 'unhealthy']
            predicted_class = class_names[predicted]
            
            # Enregistrer la date et le résultat de la prédiction
            prediction = HushemPrediction(date=timezone.now(), results=predicted_class,  precision=precision)
            prediction.save()
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