from django.db import models
from users.models import User

class Gift(models.Model):
    giver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gifts_given', null=True)  # 선물한 사람 id
    taker = models.CharField(max_length=255)  # 선물 받은 사람 전화번호
    check = models.CharField(max_length=1, blank=True, null=True)
    message = models.TextField(blank=True, null=True) #메시지
    create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
    update_dt = models.DateTimeField('UPDATE DT', auto_now=True)

    def save(self, *args, **kwargs):
        try:
            # User 모델에서 전화번호가 taker 필드 값과 일치하는 사용자를 가져옵니다.
            user = User.objects.get(phone=self.taker)
            self.check = 'Y'
        except User.DoesNotExist:
            self.check = 'N'
        super(Gift, self).save(*args, **kwargs)


class Code(models.Model):
    quantity = models.IntegerField()
    message = models.TextField()
    phone_number = models.CharField(max_length=15)