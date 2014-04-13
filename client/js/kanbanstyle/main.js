$(document).ready(function(){
    //$('#templateCreateBoardForm').tmpl({id: "createBoardForm", name: "Create a new Board"}).appendTo("body");
});

function PresentationManager(){
    this.createBoard = function(boardData, boardArea){
        boardArea.html($('#templateBoard').tmpl(boardData));
    };
}

function Responses(){
    this.boardCreationResponse = function(response){
        $("body").html($('#templateBoard').tmpl(JSON.parse(response)));
    };

    this.columnCreationResponse = function(response){
        $('#templateColumn').tmpl(JSON.parse(response)).appendTo(".column-area");
    };

    this.taskCreationResponse = function(response){
        var jsonResponse = JSON.parse(response);
        $('#templateTask').tmpl(jsonResponse).appendTo("#" + jsonResponse.column_id + "-task-area");
    };
}

function Connection(){
    this.createBoard = function(title){
        $.post("api/board", {title: title}).done(function(response){
            new Responses().boardCreationResponse(response);
        })
    };

    this.createColumn = function(title, board_id){
        $.post("api/column", {title: title, board_id: board_id}).done(function(response){
            new Responses().columnCreationResponse(response);
        })
    };

    this.createTask = function(title, description, column_id){
        $.post("api/task", {title: title, description: description, column_id: column_id}).done(function(response){
            new Responses().taskCreationResponse(response);
        })
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
    connection.createBoard(formObj["nameBoard"], boardArea);
}
