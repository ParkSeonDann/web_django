from django.forms import *

class MiPrimerFormulario(Form):
    primer_nombre =  CharField(
        required= True,
        min_length=3,
        max_length=15,
        label="Ingresa tu nombre",
        help_text="Este campo es obligatorio",
        widget=TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )

    edad_usuario = IntegerField(
        required=True,
        min_value=18,
        max_value=99,
        label="Ingresa tu edad",
        help_text="Edad entre  18 y 99 años",
        widget=NumberInput(
            attrs = {
                'class': 'form-control'
            }
        )    
    )

    contrasenia_usuario = CharField(
        required=True,
        min_length=3,
        max_length=20,
        label="Ingresa tu contraseña",
        help_text="Contraseña entre 3 y 20 caracteres",
        widget= PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    emaail_usuario =  EmailField(
        required= True,
        min_length=3,
        max_length=40,
        label="Ingresa tu correo",
        help_text="Este campo es obligatorio",
        widget=EmailInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )