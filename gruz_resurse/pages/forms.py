import os

from django import forms
from multiupload.fields import MultiFileField

PHOTO_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif", ".svg", ".heic"]


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "form-field",
                "placeholder": "Ваше ім'я",
            }
        ),
        error_messages={"required": "Це поле обов'язкове"},
    )
    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                "class": "form-field",
                "placeholder": "Email",
            }
        ),
    )
    phone_number = forms.RegexField(
        regex=r"^\+?1?\d{9,15}$",
        widget=forms.TextInput(
            attrs={
                "class": "form-field",
                "placeholder": "Номер телефону",
            }
        ),
        error_messages={"invalid": "Введіть правильний номер телефону!"},
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-field",
                "placeholder": "{{ textarea_text }}",
            }
        ),
        error_messages={"required": "Це поле обов'язкове"},
    )
    photos = MultiFileField(
        min_num=1,
        max_num=5,
        max_file_size=1024 * 1024 * 5,
        required=False,
        error_messages={
            "max_num": "Максимальна кількість файлів: %(max_num)d.",
            "file_size": "Розмір файлу не повинен перевищувати 5 МБ.",
        },
    )

    def clean_photos(self):
        photos = self.cleaned_data.get("photos")

        for photo in photos:
            file_extension = os.path.splitext(photo.name)[1].lower()

            if file_extension not in PHOTO_EXTENSIONS:
                raise forms.ValidationError(
                    "Дозволені тільки фотографії з розширеннями JPG, JPEG, PNG, GIF, SVG або HEIC"
                )

        return photos
