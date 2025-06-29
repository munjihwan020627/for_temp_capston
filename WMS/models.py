from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)  # ✅ 없으면 추가
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # ✅ 없으면 추가
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Order(models.Model):
    customer = models.CharField(max_length=200)
    order_date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)  # 여러 개의 상품을 주문에 담을 수 있도록 ManyToManyField 사용
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # 필요한 다른 필드들을 정의할 수 있습니다.

    def __str__(self):
        return f"Order #{self.id} by {self.customer}"
