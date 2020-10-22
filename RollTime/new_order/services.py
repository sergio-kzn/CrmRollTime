from .models import Category, Item, Order
import datetime as dt


def check_date_time(date_time_from_post):
    """
    если дата не введена, то возвращает текущие дату и время
    """
    if str(date_time_from_post) == '' or date_time_from_post is None:
        return dt.datetime.now()
    else:
        return date_time_from_post


def prepare_context_for_html(form, formset):
    """
    собирает все данные, которые передаются в шаблон, в одну кучу context
    :param form: нужно указать форму, которую передаем в шаблон
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

def create_new_order(form, formset):
    pass