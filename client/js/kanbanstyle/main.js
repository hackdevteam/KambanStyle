
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
        this.initJquery;
    };

    this.initJquery = new function() {
        $(function() {    
            this.getBoard;
        });
    };

    this.getBoard = new function() {
        $.post("localhost/api/board",
        {title: "nuevo"},
        function (response){
           $('#template').tmpl(response).appendTo('body');
        },
        "json");
    };
}

main = new Main();
main.init();