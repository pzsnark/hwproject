from django import forms
from .models import Ad, Category


class ADForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ['title', 'description', 'photo', 'categories']
        labels = {
            'title': 'Заголовок',
            'description': 'Текст объявления',
            'photo': 'Выберите фото',
            'categories': 'Выберите категории'
        }

        widgets = {
            'title': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст объявления'}),
            'photo': forms.ClearableFileInput(attrs={'type': 'file', 'class': 'form-control-file'})
        }


class CategoryChoice(forms.Form):
    categories = forms.ModelChoiceField(
        queryset=Category.objects.all()
     )
    #
    # class Meta:
    #     model = Category
    #     fields = ['name']
    #     labels = {'name': 'Категория'}
