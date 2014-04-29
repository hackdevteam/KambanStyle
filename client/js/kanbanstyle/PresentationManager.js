var presentationManager = {
    lastHiddenElement : {},

    addBoardToDOM : function(boardData, boardArea){
        boardArea.html(boardTemplate.tmpl(boardData));
        $("h1.board-title").dblclick(function(event){
            presentationManager.showEditForm($(event.currentTarget), editBoardTitleTemplate.tmpl({text: $(event.currentTarget).text()}));
        });
    },

    addColumnToDOM : function(columnData, columnArea){
        columnArea.append(columnTemplate.tmpl(columnData));
        $("#" + columnData.column_id + " .column-title").dblclick(function(event){
            presentationManager.showEditForm($(event.currentTarget), editColumnTitleTemplate.tmpl({text: $(event.currentTarget).text()}));
        });
    },

    addTaskToDOM : function(taskData, taskArea){
        taskArea.append(taskTemplate.tmpl(taskData));
        $("#" + taskData.task_id + " .task-title").dblclick(function(event){
            presentationManager.showEditForm($(event.currentTarget), editTaskTitleTemplate.tmpl({text: $(event.currentTarget).text()}));
        });
        $("#" + taskData.task_id + " .task-description").dblclick(function(event){
            presentationManager.showEditForm($(event.currentTarget), editTaskDescriptionTemplate.tmpl({text: $(event.currentTarget).text()}));
        });
    },

    modifyBoardTitle : function(title){
        $(".board-title").text(title);
    },

    modifyColumnTitle : function(columnId, title){
        $("#" + columnId + ">.column-title").text(title);
    },

    showEditForm : function(targetElement, editTemplate){
        this.lastHiddenElement = targetElement;
        targetElement.hide();
        targetElement.after(editTemplate);
        $("#edit").keyup(function(event){
            presentationManager.keyUpEventActions.executeActionOf(event);
        });
    },

    removeFromDOM : function(element){
        element.remove();
    },

    makeVisible : function(element){
        element.show();
    },

    makeLastHiddenVisible : function(){
        this.lastHiddenElement.show();
        this.lastHiddenElement = {};
    },

    keyUpEventActions : {
        executeActionOf: function(event){
            this[event.which]();
        },

        13: function enter(){
            $("#edit").submit();
        },

        27: function escape(){
            presentationManager.lastHiddenElement.show();
            $("#edit").remove();
            $(document).off("click");
        }
    }
};
