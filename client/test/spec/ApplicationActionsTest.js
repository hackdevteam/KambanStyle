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
            new PresentationManager().showBoard({title: "Test Board Title", board_id: board_id}, $(".board-area"));
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

    var responsesManager;
    var connection;
    var actionsController;

    beforeEach(function(){
        connection = new Connection();
        responsesManager = new ResponsesManager();
        actionsController = new ActionsController(connection, responsesManager);
        $("body").append($("<section class='board-area'></section>"));
        $(".html-reporter").before(createBoardForm.tmpl({default_title: DEFAULT_BOARD_TITLE}));
    });

    afterEach(function(){
        $("#create-board-form-area").remove();
        $(".board-area").remove();
    });
});