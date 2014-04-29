var responsesManager = {
    boardCreationResponse : function(response){
        presentationManager.removeFromDOM($("#create-board-form-area"));
        presentationManager.addBoardToDOM(response, $(".board-area"));
        context.setBoardId(response.board_id);
    },

    columnCreationResponse : function(response){
        presentationManager.addColumnToDOM(response, $(".column-area"));
    },

    taskCreationResponse : function(response){
        presentationManager.addTaskToDOM(response, $("#" + response.column_id + "-task-area"));
    }
};