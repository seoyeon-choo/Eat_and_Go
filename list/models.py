from django.db import models
from django.urls import reverse

class Menu(models.Model):
    category = models.CharField(max_length=200)  # 카테고리(=메뉴/식권)
    name = models.CharField(max_length=200)  # 메뉴 이름
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)  # 메뉴 사진
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 가격
    content = models.TextField()  # 메뉴 설명
    available_display = models.BooleanField('Display', default=True)
    available_order = models.BooleanField('Order', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        index_together = [['id', 'slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list:menu_detail', args=[self.id, self.slug])

    def get_total_price(self):
        total_product = self.price
        return total_product