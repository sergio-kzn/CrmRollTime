from django.forms import ModelForm, TextInput, Textarea, Select, RadioSelect, HiddenInput, modelformset_factory
from .models import Order, OrderItem


class NewOrderForm(ModelForm):
    """создаем инпуты <input>, которые связаны с базой данных Order и OrderItem.
    используются в форме <form> на странице new_order.html"""

    class Meta:
        model = Order

        CHOICES_MARKS = ((2, 'Доставка'),
                         (3, 'С собой'),
                         (4, 'В зале'),
                         (1, 'x'))
        choices_persons = list()
        for i in range(1, 16):
            choices_persons.append((i, str(i)))
        CHOICES_PERSONS = tuple(choices_persons)

        attrs_form_190 = {'class': 'form-control',
                          'style': 'min-width: 190px;'}
        attrs_form_75 = {'class': 'form-control',
                         'style': 'max-width: 75px;'}
        attrs_select_pl = {'class': 'custom-select',
                           'style': 'padding-left: .5rem'}

        fields = '__all__'
        labels = ''
        widgets = {
            'order_number': HiddenInput(),
            'order_branch': Select(attrs=attrs_form_190),
            'order_client_phone': TextInput(attrs=attrs_form_190),
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
                                                'id': "data-timepicker",
                                                }),
            'order_certificate': TextInput(attrs={'class': 'form-control'}),
            'order_learning_from': Select(attrs=attrs_form_190),
            'order_payment': RadioSelect(attrs=attrs_form_190),
            'order_marks': RadioSelect(choices=CHOICES_MARKS,),
            'order_person': Select(choices=CHOICES_PERSONS, attrs=attrs_select_pl),
            'order_sale': Select(attrs={'class': 'custom-select'}),
            'order_price': HiddenInput(),
        }


class ItemForm(ModelForm):
    """создаем инпуты <input> для списка товаров, которые включаются в заказ"""

    class Meta:
        model = OrderItem

        choices_item_quantity = list()
        for i in range(1, 11):
            choices_item_quantity.append((i, str(i)))
        choices_item_quantity.append((99, 'Удалить'))
        CHOICES_ITEM_QUANTITY = tuple(choices_item_quantity)

        fields = '__all__'

        widgets = {
            'order_item_order_number': HiddenInput(),
            'order_item_item_id': Select(attrs={'scope': 'row',
                                                'class': 'bg-white'}),
            'order_item_price': TextInput(attrs={'id': 'select_order_price',
                                                 'class': 'text-center'}),
            'order_item_quantity': Select(choices=CHOICES_ITEM_QUANTITY,
                                          attrs={'id': 'select_order_quantity',
                                                 'onchange': 'calcSumOnChangeQuantity(this)'}),
            'order_item_summa': TextInput(attrs={'id': 'select_order_summa',
                                                 'class': 'text-center'}),
        }
