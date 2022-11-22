import random
from rest_framework import generics, status, authentication, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .utils import verify
from apps.accounts.serializers import RegisterParentSerializer, LoginSerializer, \
    VerifySerializer, VerifyRegisterSerializer, UserSerializer
from apps.accounts.models import Account, VerifyPhone


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterParentSerializer

    def post(self, request):
        user = Account.objects.filter(phone=request.data['phone'])
        if user:
            return Response({'message': "User have already registered"}, status=status.HTTP_409_CONFLICT)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.data['phone']
        kod = str(random.randint(10000, 100000))
        if len(phone) == 13:
            verify(phone, kod)
            VerifyPhone.objects.create(phone=phone, code=kod)
        if len(phone) != 13:
            return Response({'message': 'Telefon nomer to`g`ri kiritilmagan'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': True, 'message': 'Please verify phone'}, status=status.HTTP_201_CREATED)


class AddConnectionAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        parent = self.request.data['phone']
        user = self.request.user
        if user.is_parent:
            account = Account.objects.filter(phone=parent).first()
            if account:
                user.student_id = account.id
                account.parent_id = user.id
                user.save()
                account.save()
                return Response({'message': 'Your child is added'}, status=status.HTTP_201_CREATED)
            return Response({'message': 'User not found with this phone'}, status=status.HTTP_404_NOT_FOUND)
        if not user.is_parent:
            account = Account.objects.filter(phone=parent).first()
            if account:
                user.parent_id = account.id
                user.save()
                return Response({'message': 'Your parent is added'}, status=status.HTTP_201_CREATED)
            return Response({'message': 'User not found with this phone'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user_data = serializer.data
            phone = user_data['phone']
            user = Account.objects.filter(phone=phone).first()
            if not user:
                return Response({"message": 'User is not found'}, status=status.HTTP_406_NOT_ACCEPTABLE)
            kod = str(random.randint(10000, 100000))
            if len(phone) == 13:
                verify(phone, kod)
                VerifyPhone.objects.create(phone=phone, code=kod)
            if len(phone) != 13:
                return Response({'message': 'Telefon nomer to`g`ri kiritilmagan'}, status=status.HTTP_400_BAD_REQUEST)
            if verify:
                return Response(
                    {'Phone': phone, 'message': 'Verification code was sent to your phone'},
                    status=status.HTTP_200_OK)
        return Response({'success': False, 'message': 'Phone or password is invalid'},
                        status=status.HTTP_404_NOT_FOUND)


class VerifyPhoneRegisterAPIView(generics.GenericAPIView):
    serializer_class = VerifyRegisterSerializer

    def post(self, request):
        try:
            phone = request.data.get('phone')
            code = request.data.get('code')
            password = request.data.get('password')
            sex = request.data.get('gender')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            is_parent = request.data.get('is_parent')
            age = request.data.get('age')
            student_class = request.data.get('student_class')
            verify = VerifyPhone.objects.filter(phone=phone, code=code).first()
            print(verify)
            if verify:
                print('aaa')
                user = Account.objects.filter(phone=phone)
                if user:
                    return Response({'message': 'User have already registered'}, status=409)
                user = Account.objects.create_user(phone=phone,
                                                   password=password,
                                                   sex=sex,
                                                   first_name=first_name,
                                                   last_name=last_name,
                                                   is_parent=is_parent,
                                                   age=age,
                                                   student_class=student_class
                                                   )
                user.is_verified = True
                user.save()
                verify.delete()
                return Response({
                    'msg': "Phone number is verified",
                }, status=status.HTTP_200_OK)
            else:
                return Response({'message': "Phone number or code invalid"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': "Phone number or code invalid"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(generics.GenericAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            user = self.request.user
            user.is_verified = False
            user.save()
            return Response({
                "message": "Logout Success"
            }, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class VerifyPhoneAPIView(APIView):
    def post(self, request):
        try:
            phone = request.data.get('phone')
            code = request.data.get('code')
            verify = VerifyPhone.objects.filter(phone=phone, code=code).first()
            if verify:
                user = Account.objects.filter(phone=phone).first()
                user.is_verified = True
                user.save()
                verify.delete()
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'msg': "Phone number is verified ",
                    'token': token.key
                }, status=status.HTTP_200_OK)
            else:
                return Response("Phone number or code invalid", status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Phone number or code invalid", status=status.HTTP_400_BAD_REQUEST)


class MyAccountRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = Account.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
