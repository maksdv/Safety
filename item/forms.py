from django import forms

modo = (
    ('precio', 'Calidad-Precio'),
    ('calidad', 'Lo más seguro'),
)

edadd = (
    ('1', 'Entre 0 y 6 meses'),
    ('2', 'Entre 6 meses 36'),
    ('3', 'Mayor de 36 meses y pesa 15kg o más'),

)

class NameForm(forms.Form):
    edad = forms.ChoiceField(
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        ),
        choices=edadd,
    )
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