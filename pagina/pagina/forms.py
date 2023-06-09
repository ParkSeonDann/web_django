from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

    email_usuario =  EmailField(
        required= True,
        label="Ingresa tu correo",
        help_text="*Este campo es obligatorio",
        widget=EmailInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )

    opciones_genero = [
        (1,"No definido"),
        (1,"Femenino"),
        (1,"Masculino"),
    ]

    genero_usuario = ChoiceField(
        required=True,
        choices=opciones_genero,
        label="Selecciona tu genero*",
        help_text="*Campo requerido",
        widget=RadioSelect(
            attrs = {
                'class':'form-check'
            }
        )
    )

class FormularioRegistro(UserCreationForm):
    def __init__(self, *args,**kargs):
        super().__init__(*args,**kargs)
        self.fields['password1'].widget.attrs = { 'class': 'form-control'}
        self.fields['password2'].widget.attrs = { 'class': 'form-control'}
    class Meta:
        # Registramos este formulario para el modelo User
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email'
        ]
        # Le reemplazamos los estilos por defecto a los campos del modelo Usuario
        # completar los campos que faltan para poder terminar los estilos
        widgets = {
            'username': TextInput( attrs = { 'class' : 'form-control'} ),
            'first_name': TextInput( attrs = { 'class' : 'form-control'} ),
            'last_name': TextInput( attrs = { 'class' : 'form-control'} ),
            'email': EmailInput( attrs = { 'class' : 'form-control'} ),
        }

class FormularioEntrar(Form):
    usuario = CharField(
        min_length=1,
        max_length=18,
        required = True,
        label = 'Ingrese su usuario',
        widget = TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )
    contrasenia_usuario = CharField(
        required = True,
        min_length = 4,
        max_length = 16,
        label = 'Ingrese su contraseña',
        widget = PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )
    recuerdame = BooleanField(
        required = False,
        label = 'Recordarme',
        widget = CheckboxInput(

        )
    )