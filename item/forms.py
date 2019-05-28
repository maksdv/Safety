from django import forms

modo = (
    ('precio', 'Calidad-Precio'),
    ('calidad', 'Lo más seguro'),
)

class NameForm(forms.Form):
    edad = forms.IntegerField(min_value=0, widget= forms.NumberInput(
        attrs={
            'class': 'form-control',
        }
    ))
    isofix = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={
            'class': 'checkbox'
        }
    ))
    modoo = forms.ChoiceField(
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        ),
        choices=modo,
    )