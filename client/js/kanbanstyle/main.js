function PresentationManager(){
    var self = this;

    this.addBoardToDOM = function(boardData, boardArea){
        $("#create-board-form-area").remove();
        boardArea.html(boardTemplate.tmpl(boardData));
        $("h1.board-title").dblclick(function(event){
            self.showEditForm($(event.currentTarget), editBoardTitleTemplate.tmpl({text: $(event.currentTarget).text()}));
        });
    };

    this.addColumnToDOM = function(columnData, columnArea){
        columnArea.append(columnTemplate.tmpl(columnData));
        $("#" + columnData.column_id + " .column-title").dblclick(function(event){
            self.showEditForm($(event.currentTarget), editColumnTitleTemplate.tmpl({text: $(event.currentTarget).text()}));
        });
    };

    this.addTaskToDOM = function(taskData, taskArea){
        taskArea.append(taskTemplate.tmpl(taskData));
        $("#" + taskData.task_id + " .task-title").dblclick(function(event){
            self.showEditForm($(event.currentTarget), editTaskTitleTemplate.tmpl({text: $(event.currentTarget).text()}));
        });
        $("#" + taskData.task_id + " .task-description").dblclick(function(event){
            self.showEditForm($(event.currentTarget), editTaskDescriptionTemplate.tmpl({text: $(event.currentTarget).text()}));
        });
    };

    this.modifyBoardTitle = function(value){
        $(".board-title").text(value);
    };

    this.showEditForm = function(targetElement, editTemplate){
        targetElement.hide();
        targetElement.after(editTemplate);
        lastEditedElement = targetElement;
        $("#edit").keyup(function(event){
            keyUpEventActions.executeActionOf(event);
        });
    };

    this.removeEditForm = function(){
        $("#edit").remove();
    };

    this.makeVisible = function(element){
        element.show();
    };

    var keyUpEventActions = {
        executeActionOf: function(event){
            this[event.which]();
        },

        13: function enter(){
            $("#edit").submit();
        },

        27: function escape(){
            lastEditedElement.show();
            $("#edit").remove();
            $(document).off("click");
        }
    };
}

function ResponsesManager(){
    var presentationManager = new PresentationManager();

    this.boardCreationResponse = function(response){
        presentationManager.addBoardToDOM(response, $(".board-area"));
        context.setBoardId(response.board_id);
    };

    this.columnCreationResponse = function(response){
        presentationManager.addColumnToDOM(response, $(".column-area"));
    };

    this.taskCreationResponse = function(response){
        presentationManager.addTaskToDOM(response, $("#" + response.column_id + "-task-area"));
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
    var presentationManager = new PresentationManager();

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

    this.modifyBoardTitle = function(){
        presentationManager.makeVisible($(".board-title"));
        presentationManager.modifyBoardTitle(parseForm($("#edit"))["board-title"])
        presentationManager.removeEditForm();

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
});
