from django import forms

import autocomplete_light_registry
import autocomplete_light

from models import salestax

class taxForm(forms.Form):
    city = forms.CharField(
        widget=autocomplete_light.TextWidget('salestaxAutocomplete'))

class USForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("UnitedStationers"))

class DMIFairplexForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("DMIFairplex"))
		
class CMAmberForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("CherrymanAmber"))
		
class BossForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("Boss"))
		
class FriantGitanaForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("FriantGitana"))

class CMRespondForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("CherrymanRespond"))
		
class CMVerdeForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("CherrymanVerde"))
		
class CMRubyForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("CherrymanRuby"))
		
class CMJadeForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("CherrymanJade"))
		
class CMEmeraldForm(forms.Form):
    request_sku = forms.CharField(
        widget=autocomplete_light.TextWidget("CherrymanEmerald"))