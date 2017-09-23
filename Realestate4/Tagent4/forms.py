from django.forms import ModelForm, inlineformset_factory
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class PropertyTypeForm (forms.ModelForm):
    class Meta:
        model = PropertyType
        fields = "__all__"
class AgentForm(ModelForm):
    class Meta:
        model = Agent
        exclude = ()

class LocationForm (forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ()

class AgentReferalForm(ModelForm):
    class Meta:
        model = AgentReferal
        exclude = ()

AddressFormSet = inlineformset_factory(Agent, Address,
                                            form=AddressForm, extra=1)


AgentReferalFormSet = inlineformset_factory(Agent, AgentReferal, form=AgentReferalForm, extra=1)



