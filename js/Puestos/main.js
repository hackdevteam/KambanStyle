
var lista = new Array();
lista ['createBoard'] = "create/board";
lista ['createColumn'] = "create/column";
lista ['createTask'] = "create/task";

lista ['loadBoard'] = "load/board";
lista ['loadColumn'] = "load/column";
lista ['loadTask'] = "load/task";



//  ---- Class Main
function Main() {
    this.init = function() {
        initJquery();
    };

    this.initJquery = new function() {
        $(function() {

            $.ajax({
                url: "api.php",
                type: "post",
                data: {"valor" : "load"},
                dataType: 'jsonp',
                success: function(response) {
                    $.each(response, function(indice, valor) {
                        $("body").html(valor);
                    });
                },
                contentType: "application/json"
            });

            $(document).click(function(event) {

                $.ajax({
                    url: 'api.php/api/' + lista['loadBoard'],
                    dataType: 'jsonp',
                    success: function(response) {
                        $.each(response, function(indice, valor) {
                            $(indice).html(valor);
                        });
                    }
                });
            });
        });
    };
}


main = new Main();
main.init();