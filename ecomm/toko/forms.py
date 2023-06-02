from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PILIHAN_PEMBAYARAN = (
    ('P', 'Paypal'),
    ('S', 'Stripe'),
)

class CheckoutForm(forms.Form):
    alamat_1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your full address', 'class': 'textinput form-control'}))
    alamat_2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Apartement, house, or other (optional)', 'class': 'textinput form-control'}))
    negara = CountryField(blank_label='(Select Country)').formfield(widget=CountrySelectWidget(attrs={'class': 'countryselectwidget form-select'}))
    kode_pos = forms.CharField(widget=forms.TextInput(attrs={'class': 'textinput form-outline', 'placeholder': 'Zip Code'}))
    simpan_info_alamat = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    opsi_pembayaran = forms.ChoiceField(widget=forms.RadioSelect(), choices=PILIHAN_PEMBAYARAN)