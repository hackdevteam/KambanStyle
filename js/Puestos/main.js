
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
            $("body").load("api.php/api/" + lista['loadBoard']);

            $(document).click(function(event) {
                
                $.ajax({
                    url: 'api.php/api/' + lista[event.target.id]   ,
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