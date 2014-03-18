
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
        $.post("column.php",
        {idb : "001", title: "FirtsColumn"},
        function (response){          
           var id = response.idc;
           $('#templateColumn').tmpl(response).appendTo('#column-area');
        },
        "json");
        
        $.post("column.php",
        {idb : "001", title: "SecondColumn"},
        function (response){           
           $('#templateColumn').tmpl(response).appendTo('#column-area');
        },
        "json");
    };
    
     this.getTask = new function() {
        $.post("task.php",
        {idc : "001c", title: "FirtsTask", description : "Primera Tarea"},
        function (response){  
           $('#templateTask').tmpl(response).appendTo('#'+response.idc+'-list-task-area');
        },
        "json");
        
        $.post("task.php",
        {idc : "001c", title: "SecondColumn", description : "Segund Tarea"},
        function (response){           
           $('#templateTask').tmpl(response).appendTo('#'+response.idc+'-list-task-area');
        },
        "json");
    };
}

main = new Main();
main.init();