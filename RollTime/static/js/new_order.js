let form_num = 0;

addRow = function(item_id, item_name, item_price) {
    //функция добавляет товары из правого столбика в таблицу с новым заказом
    let total_form_num = $('#id_form-TOTAL_FORMS').val();

    let tbody = document.getElementById('order').getElementsByTagName("TBODY")[0];
    let row = document.createElement("TR")

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

    // <input type="text" name="form-__prefix__-order_item_price" id="select_order_price" maxlength="10">
    let td3 = document.createElement("TD")
    let input_item_price = document.getElementsByName("form-__prefix__-order_item_price")[0].cloneNode(true);
    input_item_price.setAttribute("name", "form-" + total_form_num + "-order_item_price")
    $(input_item_price).val(item_price);
    td3.appendChild(input_item_price);

    let td4 = document.createElement("TD");
    let input_item_sum = document.createElement("INPUT");
    input_item_sum.className = "item_sum";
    input_item_sum.setAttribute("name", "form-" + total_form_num + "-order_item_sum");
    td4.appendChild(input_item_sum);

    row.appendChild(td1);
    row.appendChild(td2);
    row.appendChild(td3);
    row.appendChild(td4);
    tbody.appendChild(row);

    $(input_item_quantity).change(); // считаем сумму
    total_form_num++;
    $('#id_form-TOTAL_FORMS').val(total_form_num);
}

calcSummOnChangeQuantity = function(prefix) {
    // считает сумму, перемножая количество товара на цену.
    // результат добавляется в form-N-order_item_summa
    prefix = $(prefix).attr("name").replace(/\D+/g, "");

    let input_name_price = "form-" + prefix + "-order_item_price"
    let input_form_price = document.getElementsByName(input_name_price)
    let input_price = $(input_form_price).val()

    let input_name_quantity = "form-" + prefix + "-order_item_quantity"
    let input_form_quantity = document.getElementsByName(input_name_quantity)
    let input_quantity = $(input_form_quantity).val()

    let input_name_sum = "form-" + prefix + "-order_item_sum"
    let input_form_sum = document.getElementsByName(input_name_sum)
    $(input_form_sum).val(input_price * input_quantity)
    calcTotalPrice()
};

calcTotalPrice = function() {
    var sum = 0;
    $('.item_sum').each(function() {
        sum += parseInt($(this).val());
    });

    $('#total_price').html(sum)
};