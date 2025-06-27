from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity' ,'price', 'image','description'] # 폼에 보여줄 필드

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 2 * 1024 * 1024:  # ✅ 2MB 제한
                raise forms.ValidationError("이미지 용량은 2MB를 초과할 수 없습니다.")
        return image