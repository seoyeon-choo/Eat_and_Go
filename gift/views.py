from twilio.rest import Client
from rest_framework import viewsets, status
from .models import Gift, User, Code
from django.shortcuts import render, redirect
from .serializers import GiftSerializer

class GiftViewSet(viewsets.ModelViewSet):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer


import qrcode
from io import BytesIO
import base64
from twilio.rest import Client
import json, os
from django.conf import settings

def create_gift(request):
    if request.method == "POST":
        quantity = request.POST.get('quantity')
        taker = request.POST.get('phone_number')
        message = request.POST.get('message')
        
        # Gift 모델에 새로운 기프트(Gift) 객체를 생성합니다.
        gift = Gift.objects.create(taker=taker, message=message, giver=request.user)

        # Code 모델에 새로운 코드(Code) 객체를 생성하고 Gift와 연결합니다.
        code = Code.objects.create(quantity=quantity, message=gift.message, phone_number=taker)
        
        # Gift와 Code 객체를 저장합니다.
        gift.save()
        code.save()

        # QR 코드에 포함될 데이터를 생성합니다.
        qr_data = f"Gift ID: {gift.id}\nGiver: {gift.giver}\nMessage: {gift.message}\nPhone Number: {gift.taker}"
        # QR 코드 생성
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        # QR 코드 이미지를 생성
        qr_img = BytesIO()
        qr.make_image(fill_color="black", back_color="white").save(qr_img, format="PNG")

        # QR 코드 이미지를 base64로 인코딩합니다.
        qr_img_base64 = base64.b64encode(qr_img.getvalue()).decode('utf-8')

        # 이미지 파일을 저장
        image_filename = os.path.join(settings.STATIC_ROOT, f'qr_code_{gift.id}.png')  # 이미지 파일 이름
        with open(image_filename, 'wb') as qr_file:
            qr_file.write(qr_img.getvalue())

        # 이미지 파일의 URL을 생성
        image_url = 'https://storage.googleapis.com/gift_send/qr_code.png'  # 이미지 파일의 공개 URL을 사용/qr_code.png

        #http://127.0.0.1:8000/gift/send/static/qr_code_{gift.id}.png

        # Gift 객체의 check 필드를 확인하여 'N'일 경우에만 Twilio를 통해 MMS를 보냅니다.
        if gift.check == 'N':
            # Twilio 클라이언트 초기화
            with open('secret.json') as secret_file:
                secrets = json.load(secret_file)

            account_sid = secrets["TWILIO_ACCOUNT_SID"]
            auth_token = secrets["TWILIO_AUTH_TOKEN"]
            client = Client(account_sid, auth_token)

            # QR 코드 이미지를 MMS로 전송
            message = client.messages.create(
                body=f"식권 {quantity}장 선물이 도착했습니다!\nGift ID: {gift.id}\n보낸 사람: {gift.giver}\n선물메시지: {gift.message}",
                media_url=[image_url],  # 이미지 URL로 첨부[image_url]
                from_='+14582415262',  # Twilio 전화 번호
                to='+8201056068772'  # 수신자 전화 번호
            )

        # gift_details.html 템플릿에 Gift와 base64로 인코딩된 QR 코드를 렌더링합니다.
        return render(request, 'gift/ticket_details.html', {'gift': gift, 'qr_img_base64': qr_img_base64})

    return render(request, 'gift/purchase_ticket.html')
