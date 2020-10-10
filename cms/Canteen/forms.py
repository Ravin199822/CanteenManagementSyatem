from django import forms
from .models import Items
class ItemsForm(forms.Form):
    class Meta:

        model = Items
        fields = "__all__"