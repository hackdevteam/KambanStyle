function PresentationManager(){
    this.showBoard = function(boardData, boardArea){
        $("#create-board-form-area").remove();
        boardArea.html(boardTemplate.tmpl(boardData));
        $("#board-title").dblclick(function(event){
            $("#"+event.currentTarget.id).hide();
            $(".board-title-area").append(editBoardTitleTemplate);
        });
    };

    this.showColumn = function(columnData, columnArea){
        columnArea.append(columnTemplate.tmpl(columnData));
        $("#"+columnData.column_id+">h1").dblclick(function(event){
            $(event.currentTarget).hide();
            $(event.currentTarget).after(editColumnTitleTemplate);
        });
    };

    this.showTask = function(taskData, taskArea){
        taskArea.append(taskTemplate.tmpl(taskData));
        $("#"+taskData.task_id+">h2").dblclick(function(event){
            $(event.currentTarget).hide();
            $(event.currentTarget).after(editTaskTitleTemplate);
        });
    }
}

function Responses(){
    this.presentationManager = new PresentationManager();

    this.boardCreationResponse = function(response){
        this.presentationManager.showBoard(response, $(".board-area"));
    };

    this.columnCreationResponse = function(response){
        this.presentationManager.showColumn(response, $(".column-area"));
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
    var inputs = $("#create-board-form").serializeArray();
    $.each(inputs, function(i, input){
        formObj[input.name] = input.value;
    });
    connection.createBoard(formObj["board-name"]);
}
