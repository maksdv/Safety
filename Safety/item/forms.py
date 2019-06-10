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

class EmailForm(forms.Form):
    text = forms.CharField(widget= forms.TextInput(attrs={'placeholder':' Correo electrónico'}))

class NameForm(forms.Form):
    edad = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'type': 'email',
                'id': 'exampleFormControlInput1'
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