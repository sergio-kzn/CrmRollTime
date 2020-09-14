from django.forms import ModelForm, TextInput, Textarea
from .models import Order


class NewOrderForm(ModelForm):
    class Meta:
        attrs_form_190 = {'class': 'form-control',
                          'style': 'min-width: 190px;'}
        attrs_form_75 = {'class': 'form-control',
                         'style': 'max-width: 75px;'}

        model = Order
        fields = '__all__'
        labels = ''  # {'order_client_phone': ''}
        widgets = {'order_client_phone': TextInput(attrs=attrs_form_190),
                   'order_client_name': TextInput(attrs=attrs_form_190),
                   'order_delivery_street': TextInput(attrs=attrs_form_190),
                   'order_delivery_house': TextInput(attrs=attrs_form_75),
                   'order_delivery_entrance': TextInput(attrs=attrs_form_75),
                   'order_delivery_floor': TextInput(attrs=attrs_form_75),
                   'order_delivery_flat': TextInput(attrs=attrs_form_75),
                   'order_comment': TextInput(attrs=attrs_form_190),
                   'order_comment': Textarea(attrs={'rows': 3,
                                                    'class': 'form-control'})}
