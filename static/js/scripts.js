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
    /*
    |--------------------------------------------------
    | Funcion que carga los botones para exportar data.
    |--------------------------------------------------
    */
    new $.fn.dataTable.Buttons(t, {
    buttons: [
      /*{
        extend: 'copyHtml5',
      },*/
      {
        extend: 'csvHtml5',
        //fieldBoundary: '',
      },
      {
        extend: 'excelHtml5',
      },
      {
        extend: 'pdfHtml5',
      },
      /*{
        extend: 'print',
      },*/
      ],
    });
    t.buttons().container().appendTo(t.table().container());
});
