from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import Item
from machine_learning.models import CustomerChurn
from .serializers import ItemSerializer, CustomerChurnSerializer

from machine_learning.machine_learning import ML_prediction
from machine_learning.model_field_ETL import rmv_non_digit_dashes

import pandas as pd

@api_view(['GET'])
def getItem(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getSqlQuery(request):
   queryset = Item.objects.all()
   df = pd.DataFrame.from_records(queryset.values())
   data = df.to_json(orient="records", date_format="iso")
   return Response(data)

@api_view(['POST'])
def addCustomer(request):
    request.data["phone_number"] = rmv_non_digit_dashes(request.data["phone_number"])
    serializer = CustomerChurnSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"message":"update successfully"})    

@api_view(['GET'])
def getScores(request):
    queryset = CustomerChurn.objects.all()
    res_accracy, res_f1 = ML_prediction(queryset=queryset)
    all_score = {"f1_score": res_f1, "accuracy_score": res_accracy}
    return Response(all_score)