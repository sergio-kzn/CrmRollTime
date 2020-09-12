function addRow(item_name, item_price){
    var tbody = document.getElementById('order').getElementsByTagName("TBODY")[0];
    var row = document.createElement("TR")

    var td1 = document.createElement("TH")
    td1.setAttribute("scope", "row")
    td1.appendChild(document.createTextNode(item_name))

    var td2 = document.createElement("TD")
    var div = document.createElement("DIV")
    var select = document.createElement("SELECT")
    var optionDel = document.createElement("OPTION")
    var option1 = document.createElement("OPTION")
    var option2 = document.createElement("OPTION")
    var option3 = document.createElement("OPTION")
    var option4 = document.createElement("OPTION")
    var option5 = document.createElement("OPTION")
    optionDel.setAttribute("value", 99)
    optionDel.appendChild(document.createTextNode("Удалить"))
    option1.setAttribute("value", 1)
    option1.setAttribute("selected", true)
    option1.appendChild(document.createTextNode("1"))
    option2.setAttribute("value", 2)
    option2.appendChild(document.createTextNode("2"))
    option3.setAttribute("value", 3)
    option3.appendChild(document.createTextNode("3"))
    option4.setAttribute("value", 4)
    option4.appendChild(document.createTextNode("4"))
    option5.setAttribute("value", 5)
    option5.appendChild(document.createTextNode("5"))
    select.className = "custom-select custom-quantity"
    select.appendChild(optionDel)
    select.appendChild(option1)
    select.appendChild(option2)
    select.appendChild(option3)
    select.appendChild(option4)
    select.appendChild(option5)
    div.className = "input-group"
    div.appendChild(select)
    td2.appendChild(div)

    var td3 = document.createElement("TD")
    td3.appendChild (document.createTextNode(item_price))

    var td4 = document.createElement("TD")
    td4.appendChild (document.createTextNode(item_price))

    row.appendChild(td1);
    row.appendChild(td2);
    row.appendChild(td3);
    row.appendChild(td4);
    tbody.appendChild(row);
  }
//<div class="input-group">
//<select class="custom-select custom-quantity">
//  <option value="99">Удалить</option>
//                                            <option value="1" selected>1</option>
//                                            <option value="2">2</option>
//                                            <option value="3">3</option>
//                                            <option value="4">4</option>
//                                        </select>
//                                    </div>