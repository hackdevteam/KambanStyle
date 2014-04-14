function PresentationManager(){
    var lastEditedElement = {};

    this.showBoard = function(boardData, boardArea){
        $("#create-board-form-area").remove();
        boardArea.html(boardTemplate.tmpl(boardData));
        $("#" + boardData.board_id + " .board-title").dblclick(function(event){
            showEditTitle($(event.currentTarget), editBoardTitleTemplate);
        });
    };

    this.showColumn = function(columnData, columnArea){
        columnArea.append(columnTemplate.tmpl(columnData));
        $("#" + columnData.column_id + " .column-title").dblclick(function(event){
            showEditTitle($(event.currentTarget), editColumnTitleTemplate);
        });
    };

    this.showTask = function(taskData, taskArea){
        taskArea.append(taskTemplate.tmpl(taskData));
        $("#" + taskData.task_id + " .task-title").dblclick(function(event){
            showEditTitle($(event.currentTarget), editTaskTitleTemplate);
        });
        $("#" + taskData.task_id + " .task-description").dblclick(function(event){
            showEditTitle($(event.currentTarget), editTaskDescriptionTemplate.tmpl({description: $(event.currentTarget).text()}));
        });
    };

    function showEditTitle(targetElement, editTemplate){
        targetElement.hide();
        targetElement.after(editTemplate);
        lastEditedElement = targetElement;
        $(document).click(function(event){
            cancelEditOperation(event);
        });
    }

    function cancelEditOperation(event){
        lastEditedElement.show();
        $("#edit-title").remove();
        $("#edit-description").remove();
        $(document).off("click");
    }
}

function ResponsesManager(){
    var presentationManager = new PresentationManager();

    this.boardCreationResponse = function(response){
        presentationManager.showBoard(response, $(".board-area"));
    };

    this.columnCreationResponse = function(response){
        presentationManager.showColumn(response, $(".column-area"));
    };

    this.taskCreationResponse = function(response){
        presentationManager.showTask(response, $("#" + response.column_id + "-task-area"));
    };
}

function Connection(){
    var responsesManager = new ResponsesManager();

    this.createBoard = function(title){
        $.post("api/board", {title: title}, function(response){
            responsesManager.boardCreationResponse(response);
        }, "json");
    };

    this.createColumn = function(title, board_id){
        $.post("api/column", {title: title, board_id: board_id}, function(response){
            responsesManager.columnCreationResponse(response);
        }, "json");
    };

    this.createTask = function(title, description, column_id){
        $.post("api/task", {title: title, description: description, column_id: column_id}, function(response){
            responsesManager.taskCreationResponse(response);
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

function createBoard(){
    var formObj = {};
    var inputs = $("#create-board-form").serializeArray();
    $.each(inputs, function(i, input){
        formObj[input.name] = input.value;
    });
    connection.createBoard(formObj["board-name"]);
}

var connection;
var context;
$(document).ready(function(){
    connection = new Connection();
    context = new Context();
});