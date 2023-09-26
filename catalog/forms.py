from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

    #       Clean - метод. Валидация на уровне формы

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for word in self.FORBIDDEN_WORDS:
            if word in cleaned_data:
                raise forms.ValidationError('Ошибка, связана с некорректным именем продукта')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        for word in self.FORBIDDEN_WORDS:
            if word in cleaned_data:
                raise forms.ValidationError('Ошибка, связана с некорректным описанием продукта')
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        exclude = ('id',)



