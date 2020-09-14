from .models import *
import datetime as dt


def check_date_time(date_time_from_post):
    """
    если дата не введена, то возвращает текущие дату и время
    """
    if str(date_time_from_post) == '' or date_time_from_post is None:
        return dt.datetime.now()
    else:
        return date_time_from_post


def add_order_in_db(form_data_from_post):
    """
    Добавлем полученные данные из запроса POST в базу данных
    """

    new_order = form_data_from_post.copy()

    new_order.pop('csrfmiddlewaretoken')
    new_order.pop('options')
    new_order['order_date_time'] = check_date_time(new_order['order_date_time'])

    #print('Заказ', new_order)

def prepare_context_for_html(form):
    """
    собирает все данные, которые передаются в шаблон, в одну кучу context
    :param form: нужно указать форму, которую передаем в шаблон
    :return: возвращает словарь с данными
    """
    category_list = Category.objects.all()
    item_list = Item.objects.all()
    branch_list = Branch.objects.all()

    context = {'category_list': category_list,
               'item_list': item_list,
               'branch_list': branch_list,
               'form': form}

    return context