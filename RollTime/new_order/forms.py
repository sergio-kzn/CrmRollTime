from django.forms import ModelForm, TextInput, Textarea, Select
from .models import Order, LearningFrom


class NewOrderForm(ModelForm):
    class Meta:
        choices_learning_from = tuple(LearningFrom.objects.values_list('id', 'learning_from_name'))
        # choices_learning_from = tuple('')

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
                   'order_comment': Textarea(attrs={'class': 'form-control',
                                                    'style': 'min-width: 190px;',
                                                    'rows': 3}),
                   'order_date_time': TextInput(attrs={'class': 'form-control  datepicker-here',
                                                       'data-timepicker': "true",
                                                       'data-min-hours': "10",
                                                       'data-clear-button': "true",
                                                       'data-auto-close': "true",
                                                       'data-minutes-step': "5",
                                                       'data-toggle-selected': "false",
                                                       'id': "data-timepicker"
                                                       }),
                   'order_certificate': TextInput(attrs={'class': 'form-control'}),
                   'order_learning_from': Select(choices=choices_learning_from, attrs=attrs_form_190)}
