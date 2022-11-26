from rest_framework.response import Response
from rest_framework.views import APIView
from apps.accounts.models import Account
from .models import Order, MyVideos
from .serializers import OrderSerializer
from rest_framework import generics, status
from .payment import client, client_receipt


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CardCreate(APIView):
    def post(self, request, *args, **kwargs):
        number = self.request.data.get('number')
        expire = self.request.data.get('expire')
        save = True
        res = client._cards_create(number=number, expire=expire, save=save)
        # print(res)
        try:
            token = res['result']['card']['token']
        except:
            return Response({'message': 'Invalid information'}, status=status.HTTP_400_BAD_REQUEST)
        resp = client._card_get_verify_code(token)
        return Response({'message': 'Verification code has sent', 'token': token}, status=status.HTTP_200_OK)


class CardVerify(APIView):
    def post(self, request, *args, **kwargs):
        verify_code = self.request.data.get('verify_code')
        token = self.request.data.get('token')
        res = client._cards_verify(verify_code, token)
        print(res)
        try:
            token = res['result']['card']['token']
        except:
            return Response({'message': 'Invalid information'}, status=status.HTTP_404_NOT_FOUND)
        check = client._cards_check(token)
        return Response(str(check), status=status.HTTP_200_OK)


class ReceiptCreate(APIView):
    def post(self, request, *args, **kwargs):
        amount = float(self.request.data.get('amount'))  # * 100
        pk = self.request.data.get('course_id')
        videos = self.request.data.get('videos')
        if videos:
            my_video = MyVideos.objects.create(user=self.request.user, videos=videos)
            my_video.save()
        user = Account.objects.first()
        check = Order.objects.filter(client=user, course_id=pk)
        if check.is_paid:
            return Response({'message': 'This course already paid '})
        token = self.request.data.get('token')
        phone = '998977165434'
        res = client_receipt._receipts_create(123, amount, f'{user.id}')
        try:
            invoice_id = res['result']['receipt']['_id']
        except:
            return Response({'message': 'Invalid information'}, status=status.HTTP_404_NOT_FOUND)
        try:
            pay = client_receipt._receipts_pay(123, invoice_id, token, phone)
        except:
            return Response({'message': 'Invalid information'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'OK'}, status=status.HTTP_200_OK)
