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
        context.setBoardId(response.board_id);
    };

    this.columnCreationResponse = function(response){
        presentationManager.showColumn(response, $(".column-area"));
    };

    this.taskCreationResponse = function(response){
        presentationManager.showTask(response, $("#" + response.column_id + "-task-area"));
    };
}

function Connection(){
    this.post = function(url, data, responseCallback){
        $.post(url, data, responseCallback, "json");
    };
}

function ActionsController(connection, responsesManager){
    const BOARD_URL = "api/board";
    const COLUMN_URL = "/api/column";
    const TASK_URL = "/api/task";
    this.connection = connection;
    this.responsesManager = responsesManager;

    this.createBoard = function(){
        var formObj = parseForm($("#create-board-form"));
        this.connection.post(BOARD_URL, {title: formObj["board-name"]}, this.responsesManager.boardCreationResponse);
    };

    this.createColumn = function(){
        var formObj = parseForm($("#create-column-form"));
        this.connection.post(COLUMN_URL, {board_id: context.getBoardId(), title: formObj["column-title"]}, this.responsesManager.columnCreationResponse);
    };

    this.createTask = function(){
        var taskId;
        var description;
        var columnId;
        this.connection.post(TASK_URL, {task_id: taskId, description: description, column_id: columnId}, responsesManager.taskCreationResponse);
    };

    function parseForm(form){
        var formObj = {};
        $.each(form.serializeArray(), function(i, input){
            formObj[input.name] = input.value;
        });
        return formObj;
    }
}

var context = {
    boardId: {},
    getBoardId: function(){return this.boardId;},
    setBoardId: function(boardId){this.boardId = boardId;}
};

const DEFAULT_BOARD_TITLE = "My Board";
var actionsController;
$(document).ready(function(){
    actionsController = new ActionsController(new Connection(), new ResponsesManager());
    $("body").append(createBoardForm.tmpl({default_title: DEFAULT_BOARD_TITLE}));

    $("#nameBoard").focus();
    $("#nameBoard").select();
});
