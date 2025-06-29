from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.contrib import messages
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

@login_required(login_url='common:login')
def product_list(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'WMS/product_list.html', {'products': products})


@login_required(login_url='common:login')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # 작성자 설정
            product.save()
            messages.success(request, '상품이 성공적으로 추가되었습니다.')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'WMS/add_product.html', {'form': form})

@login_required(login_url='common:login')
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk, user=request.user)  # 본인 것만
    if request.method == 'POST':
        product.delete()
        messages.success(request, '상품이 삭제되었습니다.')
    return redirect('product_list')
