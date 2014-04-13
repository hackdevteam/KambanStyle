$(document).ready(function(){
    $('#templateCreateBoardForm').tmpl({name: "Create a new Board"}).appendTo("body");
});

function PresentationManager(){
    this.createBoard = function(boardData, boardArea){
        $("#createBoardForm").remove();
        boardArea.html(boardTemplate.tmpl(boardData));
    };
}

function Responses(){
    this.boardCreationResponse = function(response){
        new PresentationManager().createBoard(response, $(".board-area"));
    };

    this.columnCreationResponse = function(response){
        $('#templateColumn').tmpl(response).appendTo(".column-area");
    };

    this.taskCreationResponse = function(response){
        $('#templateTask').tmpl(response).appendTo("#" + response.column_id + "-task-area");
    };
}

function Connection(){
    this.createBoard = function(title){
        $.post("api/board", {title: title}, function(response){
            new Responses().boardCreationResponse(response);
        }, "json");
    };

    this.createColumn = function(title, board_id){
        $.post("api/column", {title: title, board_id: board_id}, function(response){
            new Responses().columnCreationResponse(response);
        }, "json");
    };

    this.createTask = function(title, description, column_id){
        $.post("api/task", {title: title, description: description, column_id: column_id}, function(response){
            new Responses().taskCreationResponse(response);
        }, "json")
    };
}
function Context(){
    this.boardId = [];
    this.boardTitle = [];
    this.columns = [];
    this.getBoardId = function(){
        return this.boardId;
    };
    this.setBoardId = function(boardId){
        this.boardId = boardId;
    };
    this.getNumberOfColums = function(){
        return this.columns.length
    };
}

var connection = new Connection();
var context = new Context();

function createBoard(){
    var formObj = {};
    var inputs = $("#formCreateBoard").serializeArray();
    $.each(inputs, function(i, input){
        formObj[input.name] = input.value;
    });
    connection.createBoard(formObj["nameBoard"]);
}
