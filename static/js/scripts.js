/*
|----------------------------------------------------------------
| Función que desabilita la edición del campo de fecha_solicitud.
|----------------------------------------------------------------
*/
$("document").ready(function () {
  //$("#id_fecha_solicitud").prop('disabled', true);
});

/*
|----------------------------------------------------------------------
| Función que hace desaparecer las notificaciones(alerts) de bootstrap.
|----------------------------------------------------------------------
*/
$("document").ready(function () {
  $(".alert").fadeTo(3000, 800).slideUp(50, function(){
    $(".alert").effect('blind');
  });
});

/*
|-------------------------------------------------------------------
| Funciones para cargar el datepicker jquery en los campos de fecha.
|-------------------------------------------------------------------
*/
$(function() {
  /*
  $("#id_fecha_solicitud").datepicker ({
      //dateFormat: "yy-mm-dd",
      dateFormat: "dd/mm/yy",
      dayNames: [ "Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado" ],
      dayNamesMin: [ "Do", "Lu", "Ma", "Mi", "Ju", "Vi", "Sa" ],
      firstDay: 1,
      gotoCurrent: true,
      monthNames: [ "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Deciembre" ]
    }
  );
  */
  $("#id_fecha_respuesta").datepicker ({
      //dateFormat: "yy-mm-dd",
      dateFormat: "dd/mm/yy",
      dayNames: [ "Domingo", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado" ],
      dayNamesMin: [ "Do", "Lu", "Ma", "Mi", "Ju", "Vi", "Sa" ],
      firstDay: 1,
      gotoCurrent: true,
      monthNames: [ "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Deciembre" ]
    }
  );
});

/*
|-------------------------------------------------------------------------
| Funcion que carga los métodos de DataTables sobre la tabla especificada.
|-------------------------------------------------------------------------
*/
$(document).ready(function() {
  var t = $('#example').DataTable({
    /* Poner la tabla en español */
    "language": {
      "lengthMenu": "Mostrar _MENU_ registros por página",
      "zeroRecords": "No hay datos",
      "info": "Mostrando página _PAGE_ de _PAGES_",
      "infoEmpty": "No hay datos",
      "infoFiltered": "(Filtrado para _MAX_ de registros)",
      "search": "Buscar",
      "paginate": {
        "first": "Primero",
        "last": "Último",
        "next": "Siguiente",
        "previous": "Anterior"
      },
    },
    /* Poner la columna index, es decir el contador de columnas */
    "columnDefs": [{
        "searchable": false,
        "orderable": false,
        "targets": 0
      }],
      "order": [[ 1, 'asc' ]]
      });
      t.on( 'order.dt search.dt', function () {
        t.column(0, {search:'applied', order:'applied'}).nodes().each( function (cell, i) {
          cell.innerHTML = i+1;
        });
      }).draw();
});

/*
|--------------------------------------------------------------------------
| Función que convierte los textos que sean enlaces en enlaces funcionales.
|--------------------------------------------------------------------------
*/
$("document").ready(function () {
  var exp = /(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/ig;
  var exp2 =/(^|[^\/])(www\.[\S]+(\b|$))/gim;
  $(".area_enlaces").each(function (index){
    var text1=$(this).text().replace(exp, "<a href='$1'>$1</a>");
    $(this).html(text1.replace(exp2, '$1<a target="_blank"href="http://$2">$2</a>'));
  });
});