// let form_num = 0;

addRow = function(order_number, item_id, item_name, item_price) {
    //функция добавляет товары из правого столбика в таблицу с новым заказом
    let total_form = $('#id_form-TOTAL_FORMS');
    let total_form_num = total_form.val();

    let tbody = document.getElementById('order').getElementsByTagName("TBODY")[0];
    let row = document.createElement("TR");
    row.setAttribute("id", "row_id_" + total_form_num);

    // <input type="hidden" name="form-__prefix__-order_item_order_number" id="id_form-__prefix__-order_item_order_number">
    let input_order_number = document.getElementsByName("form-__prefix__-order_item_order_number")[0].cloneNode(true);
    input_order_number.setAttribute("name", "form-" + total_form_num + "-order_item_order_number");
    input_order_number.setAttribute("id", "id_form-" + total_form_num + "-order_item_order_number");
    $(input_order_number).val(order_number)
    row.appendChild(input_order_number)


    let td1 = document.createElement("TH")
    let input_item_name = document.getElementsByName("form-__prefix__-order_item_item_id")[0].cloneNode(true);
    input_item_name.setAttribute("name", "form-" + total_form_num + "-order_item_item_id");
    input_item_name.setAttribute("id", "id_form-" + total_form_num + "-order_item_item_id");
    $(input_item_name).val(item_id);
    td1.appendChild(input_item_name);

    //<select name="form-__prefix__-order_item_quantity" id="select_order_quantity" maxlength="10">
    let td2 = document.createElement("TD")
    td2.className = "input_quantity";
    let input_item_quantity = document.getElementsByName("form-__prefix__-order_item_quantity")[0].cloneNode(true);
    input_item_quantity.setAttribute("name", "form-" + total_form_num + "-order_item_quantity")
    td2.appendChild(input_item_quantity)

    // <input type="checkbox" name="form-__prefix__-DELETE" id="id_form-__prefix__-DELETE">
    let input_item_delete = document.getElementsByName("form-__prefix__-DELETE")[0].cloneNode(true);
    input_item_delete.setAttribute("name", "form-" + total_form_num + "-DELETE");
    input_item_delete.setAttribute("id", "id_form-" + total_form_num + "-DELETE");
    input_item_delete.className = "d-none";
    td2.appendChild(input_item_delete)

    // <input type="text" name="form-__prefix__-order_item_price" id="select_order_price" maxlength="10">
    let td3 = document.createElement("TD")
    let input_item_price = document.getElementsByName("form-__prefix__-order_item_price")[0].cloneNode(true);
    input_item_price.setAttribute("name", "form-" + total_form_num + "-order_item_price")
    $(input_item_price).val(item_price);
    td3.appendChild(input_item_price);

    //<input type="text" name="form-__prefix__-order_item_summa" id="select_order_summa" maxlength="10">
    let td4 = document.createElement("TD");
    let input_item_summa = document.getElementsByName("form-__prefix__-order_item_summa")[0].cloneNode(true);
    input_item_summa.setAttribute("name", "form-" + total_form_num + "-order_item_summa");
    td4.appendChild(input_item_summa);

    row.appendChild(td1);
    row.appendChild(td2);
    row.appendChild(td3);
    row.appendChild(td4);
    tbody.appendChild(row);

    $(input_item_quantity).change(); // считаем сумму
    total_form_num++;
    total_form.val(total_form_num);
}

calcSumOnChangeQuantity = function(prefix) {
    // считает сумму, перемножая количество товара на цену.
    // результат добавляется в form-N-order_item_summa
    prefix = $(prefix).attr("name").replace(/\D+/g, "");

    let input_name_quantity = "form-" + prefix + "-order_item_quantity";
    let input_form_quantity = document.getElementsByName(input_name_quantity);
    let input_quantity = $(input_form_quantity).val();

    let check_delete = 1
    if (Number(input_quantity) === 99) {
        let id_delete = "id_form-" + prefix + "-DELETE";
        document.getElementById(id_delete).checked = true;

        let row_id = "row_id_" + prefix;
        document.getElementById(row_id).className = "d-none";

        check_delete = 0;
    }

    let input_name_price = "form-" + prefix + "-order_item_price";
    let input_form_price = document.getElementsByName(input_name_price);
    let input_price = $(input_form_price).val();

    let input_name_summa = "form-" + prefix + "-order_item_summa";
    let input_form_summa = document.getElementsByName(input_name_summa);
    $(input_form_summa).val(input_price * input_quantity * check_delete);
    calcTotalPrice();
};

calcTotalPrice = function() {
    // подсчет суммы всего заказа, отображается в нижней панели
    let sum = 0;
    let items = document.getElementsByClassName('item_sum')
    for (let i=0; i < items.length; i++) {
        sum += Number(items[i].value);
    }

    document.getElementById('total_price').innerHTML = sum.toString();
    document.getElementsByName('order_price')[0].value = sum;
};