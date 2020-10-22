from django.utils import timezone
from loguru import logger

from .models import Category, Item, Order


def check_date_time(date_time_from_post):
    """
    если дата не введена, то возвращает текущие дату и время
    """
    if date_time_from_post is None:
        logger.info('Новая Дата {}', timezone.now())
        return timezone.now()
    else:
        logger.info('Старая Дата {}', date_time_from_post)
        return date_time_from_post


def prepare_context_for_html(form, formset):
    """
    собирает все данные, которые передаются в шаблон, в одну кучу context
    :param form: нужно указать форму, которую передаем в шаблон
    :param formset: указать набор форм для добавленных товаров
    :return: возвращает словарь с данными
    """
    category_list = Category.objects.all()
    item_list = Item.objects.all()
    context = {'category_list': category_list,
               'item_list': item_list,
               'form': form,
               'formset': formset,
               }
    return context


@logger.catch
def create_new_order(form, formset) -> bool:
    """
    функиця проверят формы и сохраняет данные в бд
    :param form: форма с данными заказа
    :param formset: набор форм с товарами в заказе
    :return: Возвращает True - если все формы прошли валидацию
    """

    if form.is_valid() and formset.is_valid():
        logger.success("form is valid")

        f = form.save(commit=False)
        f.order_date_time = check_date_time(form.cleaned_data['order_date_time'])
        f.save()
        logger.success("form is saved")


        logger.success("formset is valid")
        formset.save()
        return True

    if not form.is_valid():
        logger.error("FORM NO VALID")
        logger.error(form.errors)

    if not formset.is_valid():
        logger.error("FORMSET NO VALID")
        logger.error(formset.errors)

    return False


def create_new_order_number():
    order_numbers = Order.objects.all().only('order_number')
    new_order_number = 0

    for order_number in order_numbers:
        if order_number.order_number > new_order_number:
            new_order_number = order_number.order_number
    new_order_number += 1
    return new_order_number
