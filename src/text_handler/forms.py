from django import forms

from text_handler.models import Document

ALLOWED_SUFFIX = ['txt',]


class DocumentForm(forms.ModelForm):

    class Meta:

        model = Document
        fields = ('file',)
        help_text = {'file': 'Выберите текстовый документ', }
        label = {'file': 'Документ', }

        def clean_text(self):
            file = self.cleaned_data['file']
            if not file:
                raise forms.forms.ValidationError('Необходимо выбрать файл')
            # TODO проверку расширения файла
            return file
