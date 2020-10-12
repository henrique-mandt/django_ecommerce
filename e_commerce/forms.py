from django import forms

class ContactForm(forms.Form):
    nome_completo = forms.CharField(
        error_messages={'required': 'Obrigatório o preenchimento do nome!'},
        widget=forms.TextInput(
            attrs={
                "class": "form_control",
                "placeholder": "Digite seu nome completo"
            }
        )
    )
    email = forms.EmailField(
        error_messages={'invalid': 'Digite um email válido!'},
        widget=forms.TextInput(
            attrs={
                "class": "form_control",
                "placeholder": "Digite seu e-mail"
            }
        )
    )
    mensagem = forms.CharField(
        error_messages={'required': 'Obrigatório o preenchimento da mensagem!'},
        widget=forms.TextInput(
            attrs={
                "class": "form_control",
                "placeholder": "Digite sua mensagem"
            }
        )
    )
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("O email deve ser do gmail.com")
        return email