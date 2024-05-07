$(document).ready(function () {
    $('#datepicker').datepicker({
        format: 'dd/mm/yyyy',
        language: 'ru'
    });

    $('#submitDateRange').click(function() {
        var startDate = $('input[name="start"]').datepicker('getFormattedDate');
        var endDate = $('input[name="end"]').datepicker('getFormattedDate');
        window.location.href = '/your-view-url?start=' + startDate + '&end=' + endDate;
    });
});

$(document).ready(function () {
    $('#datepicker2').datepicker({
        format: 'dd/mm/yyyy',
        language: 'ru'
    });

    $('#submitDateRange2').click(function() {
        var startDate = $('input[name="start"]').datepicker('getFormattedDate');
        var endDate = $('input[name="end"]').datepicker('getFormattedDate');
        window.location.href = '/reservation.html?start=' + startDate + '&end=' + endDate;
    });

});

$(document).ready(function () {
    // Инициализация datepicker для каждого элемента
    $('.input-daterange').each(function() {
      var roomId = $(this).attr('id').replace('datepicker', ''); // Извлекаем ID комнаты
      $('#start' + roomId).datepicker({
          format: 'dd/mm/yyyy',
          language: 'ru',
          autoclose: true
      });
      $('#end' + roomId).datepicker({
          format: 'dd/mm/yyyy',
          language: 'ru',
          autoclose: true
      });
    });
  });


// $(document).ready(function(){
//     $('#datepicker2').datepicker({
//       format: 'dd/mm/yyyy',
//       language: 'ru'
//     }).on('changeDate', function(e) {
//       var startDate = $('#datepicker2 .check-in .form-control').datepicker('getDate');
//       var endDate = $('#datepicker2 .col-6 .form-control').datepicker('getDate');
  
//       if (checkInDate && checkOutDate) {
//         var formattedCheckInDate = $.fn.datepicker.DPGlobal.formatDate(checkInDate, 'dd/mm/yyyy', 'en');
//         var formattedCheckOutDate = $.fn.datepicker.DPGlobal.formatDate(checkOutDate, 'dd/mm/yyyy', 'en');
  
//         var url = 'http://127.0.0.1:5501/index.html';
//         url += '?start=' + encodeURIComponent(formattedCheckInDate);
//         url += '&end=' + encodeURIComponent(formattedCheckOutDate);
//         url += '&guests=1'; // добавьте количество гостей, если это необходимо
  
//         window.location.href = url;
//       }
//     });
//   });



// $(document).ready(function () {
//     $('#datepicker, #datepicker2').datepicker({
//         format: 'dd/mm/yyyy',
//         language: 'ru'
//     }).on('change', function() {
//         var startDate = $('input[name="start"]').datepicker('getFormattedDate');
//         var endDate = $('input[name="end"]').datepicker('getFormattedDate');
        
//         $.ajax({
//             url: '/your-view-url',
//             type: 'get',
//             data: {
//                 start: startDate,
//                 end: endDate
//             },
//             success: function(response) {
//                 // Обработайте ответ сервера здесь
//             }
//         });
//     });
// });


