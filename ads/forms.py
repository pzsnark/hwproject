from django import forms
from .models import Ad, Category, Profile


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


class UpdateProfileForm(forms.ModelForm):
    birth_date = forms.DateField(
        label='Дата рождения', input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(format=('%d-%m-%Y'), attrs={
            'class': 'form-control',
            'placeholder': 'Дата рождения в формате %d-%m-%Y'
        })
    )

    class Meta:
        model = Profile
        fields = ['avatar', 'birth_date']
        labels = {
            'avatar': 'Аватар'
        }
