document.addEventListener('DOMContentLoaded', function () {
    let progress_delivery = document.getElementById('progress-delivery');
    let order_client_phone_flag = 0;
    let order_client_name_flag = 0;
    let order_delivery_street_flag = 0;
    let order_delivery_house_flag = 0;
    let order_delivery_entrance_flag = 0;
    let order_delivery_floor_flag = 0;
    let order_delivery_flat_flag = 0;

    let progress_del = function (step = 0) {
        let current = parseInt(progress_delivery.style.width, 10);
        let new_pos = current + step;
        progress_delivery.style.width = new_pos + '%';
        progress_delivery.setAttribute('aria-valuenow', new_pos);

        if (new_pos > 45) {
            progress_delivery.classList.add('bg-success');
            progress_delivery.classList.remove('bg-warning');
        } else {
            progress_delivery.classList.add('bg-warning');
            progress_delivery.classList.remove('bg-success');
        }
    }

    // телефон
    document.getElementsByName('order_client_phone')[0].oninput = function () {
        if (this.value && order_client_phone_flag === 0) {
            order_client_phone_flag = 1;
            progress_del(9);
        }
        if (!this.value) {
            progress_del(-9);
            order_client_phone_flag = 0;
        }
    };

    // имя
    document.getElementsByName('order_client_name')[0].oninput = function () {
        if (this.value && order_client_name_flag === 0) {
            order_client_name_flag = 1;
            progress_del(10);
        }
        if (!this.value) {
            progress_del(-10);
            order_client_name_flag = 0;
        }
    };

    // улица
    document.getElementsByName('order_delivery_street')[0].oninput = function () {
        if (this.value && order_delivery_street_flag === 0) {
            order_delivery_street_flag = 1;
            progress_del(10);
        }
        if (!this.value) {
            progress_del(-10);
            order_delivery_street_flag = 0;
        }
    };

    // дом
    document.getElementsByName('order_delivery_house')[0].oninput = function () {
        if (this.value && order_delivery_house_flag === 0) {
            order_delivery_house_flag = 1;
            progress_del(5);
        }
        if (!this.value) {
            progress_del(-5);
            order_delivery_house_flag = 0;
        }
    };

    // подъезд
    document.getElementsByName('order_delivery_entrance')[0].oninput = function () {
        if (this.value && order_delivery_entrance_flag === 0) {
            order_delivery_entrance_flag = 1;
            progress_del(5);
        }
        if (!this.value) {
            progress_del(-5);
            order_delivery_entrance_flag = 0;
        }
    };

    // этаж
    document.getElementsByName('order_delivery_floor')[0].oninput = function () {
        if (this.value && order_delivery_floor_flag === 0) {
            order_delivery_floor_flag = 1;
            progress_del(5);
        }
        if (!this.value) {
            progress_del(-5);
            order_delivery_floor_flag = 0;
        }
    };

    // квартира
    document.getElementsByName('order_delivery_flat')[0].oninput = function () {
        if (this.value && order_delivery_flat_flag === 0) {
            order_delivery_flat_flag = 1;
            progress_del(5);
        }
        if (!this.value) {
            progress_del(-5);
            order_delivery_flat_flag = 0;
        }
    };

    /////////////////////////////////////////////////////////////////////////////////////////

    let progress_main = document.getElementById('progress-main');
    let items_flag = 0;
    let order_payment_flag = 0;
    let order_marks_flag = 0;

    let progress_ma = function (step = 0) {
        let current = parseInt(progress_main.style.width, 10);
        let new_pos = current + step;
        progress_main.style.width = new_pos + '%';
        progress_main.setAttribute('aria-valuenow', new_pos);

        if (new_pos > 49) {
            progress_main.classList.add('bg-success');
        } else {
            progress_main.classList.remove('bg-success');
        }
    }


    // варианты оплаты
    let order_payments = document.getElementsByName('order_payment');
    let max_value_payment = order_payments[order_payments.length - 1].getAttribute('value');
    for (let i = 0; i < order_payments.length; i++) {
        order_payments[i].onchange = function () {
            if (order_payments[i].value !== max_value_payment) {
                if (order_payment_flag === 0) {
                    order_payment_flag = 1;
                    progress_ma(20);
                }
            } else {
                if (order_payment_flag !== 0) {
                    progress_ma(-20);
                    order_payment_flag = 0;
                }
            }

        }
    }

    // отметки
    let order_marks = document.getElementsByName('order_marks');
    let max_value_marks = order_marks[order_marks.length - 1].getAttribute('value');
    for (let i = 0; i < order_marks.length; i++) {
        order_marks[i].onchange = function () {
            if (order_marks[i].value !== max_value_marks) {
                if (order_marks_flag === 0) {
                    order_marks_flag = 1;
                    progress_ma(20);
                }
            } else {
                if (order_marks_flag !== 0) {
                    progress_ma(-20);
                    order_marks_flag = 0;
                }
            }

        }
    }

    // товары items_flag
    let rows = document.getElementById("table-for-goods").rows

    window.change_progress_from_items = function () {
        let count_items = rows.length - 1;
        for (let i = 0; i < rows.length; i++) {
            let classList = rows[i].className.split(/\s+/);
            for (let j = 0; j < classList.length; j++)
                if (classList[j] === 'd-none') count_items -= 1;
        }
        if (items_flag === 0) {
            items_flag = 1;
            progress_ma(10);
        }
        if (count_items === 0) {
            progress_ma(-10);
            items_flag = 0;
        }
    };

    ////////////////////////////////////////////////////////////////

    document.getElementsByName('order_client_phone')[0].oninput();
    document.getElementsByName('order_client_name')[0].oninput();
    document.getElementsByName('order_delivery_street')[0].oninput();
    document.getElementsByName('order_delivery_house')[0].oninput();
    document.getElementsByName('order_delivery_entrance')[0].oninput();
    document.getElementsByName('order_delivery_floor')[0].oninput();
    document.getElementsByName('order_delivery_flat')[0].oninput();
    for (let i = 0; i < order_payments.length; i++)
        order_payments[i].onchange();
    for (let i = 0; i < order_marks.length; i++)
        order_marks[i].onchange();
    change_progress_from_items();
})