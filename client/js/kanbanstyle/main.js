
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
            this.getColumn;
            this.getTask;
        });
    };

    this.getBoard = new function() {
        $.post("board.php",
        {title: "NewBoard"},
        function (response){           
           $('#templateBoard').tmpl(response).appendTo('body');
        },
        "json");
    };
    
    this.getColumn = new function() {
        $.post("api/board",
        {idb : "001", title: "FirtsColumn"},
        function (response){           
           $('#templateColumn').tmpl(response).appendTo('#column-area');
        },
        "json");
        
        $.post("api/board",
        {idb : "001", title: "SecondColumn"},
        function (response){           
           $('#templateColumn').tmpl(response).appendTo('#column-area');
        },
        "json");
    };
    
     this.getTask = new function() {
        $.post("api/task",
        {idc : "001c", title: "FirtsTask", description : "Primera Tarea"},
        function (response){  
           $('#templateTask').tmpl(response).appendTo('#'+response.idc+'-list-task-area');
        },
        "json");
        
        $.post("api/task",
        {idc : "001c", title: "SecondTask", description : "Segund Tarea"},
        function (response){           
           $('#templateTask').tmpl(response).appendTo('#'+response.idc+'-list-task-area');
        },
        "json");
    };
}

main = new Main();
main.init();