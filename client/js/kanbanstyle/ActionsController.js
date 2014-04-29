var actionsController = {
    BOARD_URL : "api/board",
    COLUMN_URL : "/api/column",
    TASK_URL : "/api/task",

    createBoard : function(){
        var formObj = this.parseForm($("#create-board-form"));
        connection.post(this.BOARD_URL, {title: formObj["board-name"]}, responsesManager.boardCreationResponse);

    },

    createColumn : function(){
        var formObj = this.parseForm($("#create-column-form"));
        connection.post(this.COLUMN_URL, {board_id: context.getBoardId(), title: formObj["column-title"]}, responsesManager.columnCreationResponse);
    },

    createTask : function(){
        var taskId;
        var description;
        var columnId;
        connection.post(this.TASK_URL, {task_id: taskId, description: description, column_id: columnId}, responsesManager.taskCreationResponse);
    },

    modifyBoardTitle : function(){
        presentationManager.makeVisible($(".board-title"));
        var $editForm = $("#edit");
        presentationManager.modifyBoardTitle(this.parseForm($editForm)["board-title"]);
        presentationManager.removeFromDOM($editForm);

    },

    modifyColumnTitle : function(){
        presentationManager.makeLastHiddenVisible();
        var $editForm = $("#edit");
        presentationManager.modifyColumnTitle(this.parseForm($editForm)["column-title"]);
        presentationManager.removeFromDOM($editForm)
    },

    parseForm : function(form){
        var formObj = {};
        $.each(form.serializeArray(), function(i, input){
            formObj[input.name] = input.value;
        });
        return formObj;
    }
};