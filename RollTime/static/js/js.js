$( document ).ready(function() {
$('.custom-calendar.date').datepicker({
    weekStart: 1,
    todayBtn: "linked",
    language: "ru",
    daysOfWeekHighlighted: "0,6",
    autoclose: true,
    todayHighlight: true,
    toggleActive: true
});
});

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})