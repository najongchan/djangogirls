from django import forms

from .models import Tenor


class Tenorform(forms.ModelForm):

    class Meta:
        model = Tenor
        fields = ('search_term',)

    def __init__(self, *args, **kwargs):
        super(Tenorform, self).__init__(*args, **kwargs)
        self.fields['search_term'].widget.attrs.update({
            'class': 'searchInput',
            'placeholder': 'ex) excited',
        })
