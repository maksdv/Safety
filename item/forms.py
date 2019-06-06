from django import forms

modo = (
    ('', 'Elija una opción'),
    ('precio', 'Calidad-Precio'),
    ('calidad', 'Lo más seguro'),
)

edadd = (
    ('', 'Elija una opción'),
    ('1', 'Entre 0 y 6 meses'),
    ('2', 'Entre 6 meses 36'),
    ('3', 'Mayor de 36 meses y pesa 15kg o más'),

)

isofixx = (
    ('', 'Elija una opción'),
    ('si', 'Tengo IsoFix'),
    ('no', 'No tengo IsoFix'),
)

class Email(forms.Form):
    text = forms.EmailField()

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
    isofix = forms.ChoiceField(
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        ),
        choices=isofixx,
    )
    modoo = forms.ChoiceField(
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        ),
        choices=modo,
    )