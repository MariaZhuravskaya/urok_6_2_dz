from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    #       Clean - метод. Валидация на уровне формы

    def clean_name(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        cleaned_data = self.cleaned_data.get('name')
        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError('Ошибка, связана с некорректным именем продукта')
        return cleaned_data


    def clean_description(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        cleaned_data = self.cleaned_data.get('description')
        for word in forbidden_words:
            if word in cleaned_data:
                raise forms.ValidationError('Ошибка, связана с некорректным описанием продукта')
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        #fields = '__all__'
        exclude = ('id',)



