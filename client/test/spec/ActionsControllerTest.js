describe("Testing all the actions of the application", function(){
    describe("createBoard()", function(){
        it("should do a POST call to /api/board", function(){
            const BOARD_URL = "api/board";
            var data = {title: DEFAULT_BOARD_TITLE};
            spyOn(connection, "post").and.callFake(function(){
                responsesManager.boardCreationResponse({board_id: "MOCKED ID", title: DEFAULT_BOARD_TITLE});
            });
            spyOn(context, "setBoardId");
            actionsController.createBoard();
            expect(connection.post).toHaveBeenCalledWith(BOARD_URL, data, responsesManager.boardCreationResponse);
            expect(context.setBoardId).toHaveBeenCalled();
        });
    });

    describe("createColumn()", function(){
        it("should do a POST call to /api/column", function(){
            const COLUMN_URL = "/api/column";
            const board_id = "testBoardID";
            context.setBoardId(board_id);
            presentationManager.addBoardToDOM({title: "Test Board Title", board_id: board_id}, $(".board-area"));
            var columnData = {board_id: board_id, title: "New Column"};
            spyOn(connection, "post");
            actionsController.createColumn();
            expect(connection.post).toHaveBeenCalledWith(COLUMN_URL, columnData, responsesManager.columnCreationResponse);
        });
    });

    describe("createTask()", function(){
        it("should do a POST call to /api/column", function(){
            const TASK_URL = "/api/task";
            var columnId = "TestColumnID";
            var taskData = {title: "Task Title", description: "This is a test Task", column_id: columnId};
            spyOn(connection, "post");
            actionsController.createTask();
            expect(connection.post).toHaveBeenCalledWith(TASK_URL, taskData, responsesManager.taskCreationResponse);
        });
    });

    describe("modifyBoardTitle()", function(){
        it("should put the introduced title as board title", function(){
            var newBoardTitle = "New Board Title";
            var $boardTitle = $(".board-title");
            presentationManager.showEditForm($boardTitle, editBoardTitleTemplate.tmpl({text: newBoardTitle}));
            var $editForm = $("#edit");
            $editForm.submit();
            expect($boardTitle.text()).toBe(newBoardTitle);
            expect($editForm).not.toBeInDOM();
        });
    });

    describe("modifyColumnTitle()", function(){
        it("should put the introduced title as column title", function(){
            var newColumnTitle = "New Column Title";
            var $columnTitle = $("#" + COLUMN_ID + ">.column-title");
            presentationManager.showEditForm($columnTitle, editColumnTitleTemplate.tmpl({text: newColumnTitle, columnId:COLUMN_ID}));
            var $editForm = $("#edit");
            $editForm.submit();
            expect($columnTitle.text()).toBe(newColumnTitle);
            expect($editForm).not.toBeInDOM();
        });
    });

    var COLUMN_TITLE = "Old Column";
    var COLUMN_ID = "clm1234";

    beforeEach(function(){
        $("body").append($("<section class='board-area'></section>"));
        presentationManager.addBoardToDOM({title: "Old Board Title", board_id: "brd1234"}, $(".board-area"));
        presentationManager.addColumnToDOM({title: COLUMN_TITLE, column_id: COLUMN_ID}, $(".column-area"));

    });

    afterEach(function(){
        $("#create-board-form-area").remove();
        $($(".board-area")).remove();
    });
});