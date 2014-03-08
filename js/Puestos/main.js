
var lista = new Array();
lista['createBoard'] = "create/board";
lista['createColumn'] = "create/column";
lista['createTask'] = "create/task";

lista['loadBoard'] = "load/board";
lista['loadColumn'] = "load/column";
lista['loadTask'] = "load/task";





//  ---- Class Main
function Main() {
    this.init = function() {
        initJquery();
    };

    this.initJquery = new function() {
        $(function() {    
            getBoard();

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

    this.getBoard = new function() {
        $.get("api.php/" + lista['loadBoard'],
                {valor: "Board"},
                function(response) {          
                    $('#template').tmpl(response).appendTo('body');
                    //$("body").html(response);
                },
                "json"
                );
    };
}


main = new Main();
main.init();