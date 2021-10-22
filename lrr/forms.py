from allauth.account.forms import LoginForm, ResetPasswordForm, AddEmailForm, ChangePasswordForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div
from django.conf import settings


class DETChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super(DETChangePasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.label_class = 'sr-only'
        self.render_hidden_fields = True

        self.fields["oldpassword"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""

        self.fields['oldpassword'].help_text = "Введите текущий пароль"
        self.fields['password1'].help_text = "Введите новый пароль"
        self.fields['password2'].help_text = "Введите новый пароль еще раз"

        self.helper.layout = Layout(
            Field('oldpassword', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
            Field('password1', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
            Field('password2', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
        )


class DETLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(DETLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.label_class = 'sr-only'
        self.render_hidden_fields = True

        self.fields["login"].label = ""
        self.fields["password"].label = ""

        self.fields['login'].help_text = "Введите email, указанный при регистрации"
        self.fields['password'].help_text = "Введите пароль, указанный при регистрации"
        self.fields['remember'].label = "Запомнить меня до выхода из сервиса"

        self.helper.layout = Layout(
            Field('login', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
            Field('password', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
            Div(
                Field('remember', css_class="mt-4"),
                css_class="text-secondary my-4"
            )
        )

    def login(self, *args, **kwargs):
        return super(DETLoginForm, self).login(*args, **kwargs)


class DETResetPasswordForm(ResetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(DETResetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.label_class = 'sr-only'

        self.fields['email'].help_text = "Введите email, указанный при регистрации"

        self.helper.layout = Layout(
            Field('email', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
        )


class DETAddEmailForm(AddEmailForm):
    def __init__(self, *args, **kwargs):
        super(DETAddEmailForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.label_class = 'sr-only'

        self.fields['email'].help_text = "Введите email"

        self.helper.layout = Layout(
            Field('email', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
        )
