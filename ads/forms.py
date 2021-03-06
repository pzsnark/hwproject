from django import forms
from .models import Ad, Category, Profile, Comment, Audio
from .widgets import AudioWidget


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
            'title': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Введите заголовок', 'rows': 1, 'autofocus': 'autofocus'
            }),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст объявления'}),
            'photo': forms.ClearableFileInput(attrs={'type': 'file', 'class': 'form-control-file'})
        }


class CategoryChoice(forms.Form):
    categories = forms.ModelChoiceField(
        queryset=Category.objects.all(), label='Категории', empty_label=None
     )


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


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст комментария'})
        }


class AdminFormAd(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ['title', 'description', 'favorite', 'photo', 'categories']
        labels = {
            'title': 'Заголовок',
            'description': 'Текст объявления',
            'favorite': 'В избранном',
            'photo': 'Выберите фото',
            'categories': 'Выберите категории'
        }

        widgets = {
            'title': forms.Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Введите заголовок', 'rows': 1, 'autofocus': 'autofocus'
            }),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст объявления'}),
            'photo': forms.ClearableFileInput(attrs={'type': 'file', 'class': 'form-control-file'})
            }


# class AudioForm(forms.ModelForm):
#
#     def __init__(self):
#         super(AudioForm).__init__()
#         self.fields['file'] = AudioWidget(
#             queryset=AudioWidget(Audio.objects.all()),
#             required=False,
#             widget=AudioWidget(
#                 file='file'
#             ),
#         )
#
#     class Meta:
#         model = Audio
#         fields = ['author', 'track', 'file']
#         labels = {
#             'author': 'Исполнитель',
#             'track': 'Трек'
#         }
#
#     widgets = {
#         'file': AudioWidget
#     }
