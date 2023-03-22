import io

import pandas as pd
from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

from .models import Purchase
from .serializers import PingPongSerializer, PurchaseSerializer
from rest_framework.response import Response
from datatransfer.serializers import CsvFilesSerializer


class PingPongView(APIView):
    @staticmethod
    def get(request):
        serializer = PingPongSerializer(data=request.GET)
        if serializer.is_valid():
            if serializer.data['ping'] == 'ping':
                return Response({'result': 'pong'})
            else:
                return Response({'result': 'What the hell?'})
        else:
            return Response('Wrong')


class CsvFilesView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = CsvFilesSerializer

        _dict_file_obj = request.data['file'].__dict__

        _csv = _dict_file_obj['_name'].endswith('.csv')

        _excel = _dict_file_obj['_name'].endswith('.xlsx')

        if request.data['file'] is None:
            return Response({"error": "No File Found"},
                            status=status.HTTP_400_BAD_REQUEST)

        if file_serializer.is_valid():
            data = self.request.data.get('file')

            if _csv is True:
                data_set = data.read().decode('UTF-8')

                io_string = io.StringIO(data_set)

                csv_file = pd.read_csv(io_string, low_memory=False)
                columns = list(csv_file.columns.values)

                id = columns[0]
                order_id, product, quantity_ordered = columns[1], columns[2], columns[3]
                price_each, order_date, purchase_adress = columns[4], columns[5], columns[6]
                total = columns[7]

                instances = [
                    Purchase(
                        id=row[index],
                        order_id=row[order_id],
                        product=row[product],
                        quantity_ordered=row[quantity_ordered],
                        price_each=row[price_each],
                        order_date=row[order_date],
                        purchase_adress=row[purchase_adress],
                        total=row[total],
                    )

                    for index, row in csv_file.iterrows()
                ]

                Purchase.objects.bulk_create(instances)

            elif _excel is True:
                xl = pd.read_excel(data)
                columns = list(xl.columns.values)

                id = columns[0]
                order_id, product, quantity_ordered = columns[1], columns[2], columns[3]
                price_each, order_date, purchase_adress = columns[4], columns[5], columns[6]
                total = columns[7]

                instances = [
                    Purchase(
                        id=row[index],
                        order_id=row[order_id],
                        product=row[product],
                        quantity_ordered=row[quantity_ordered],
                        price_each=row[price_each],
                        order_date=row[order_date],
                        purchase_adress=row[purchase_adress],
                        total=row[total],
                    )

                    for index, row in xl.iterrows()
                ]

                Purchase.objects.bulk_create(instances)

            else:
                return Response(data={"err": "Must be *.xlsx or *.csv File."},
                                status=status.HTTP_400_BAD_REQUEST
                                )

            file_serializer.save()
            return Response(
                {"message": "Upload Successfull",
                 "data": file_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(file_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )


class PurchaseListAPIView(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

