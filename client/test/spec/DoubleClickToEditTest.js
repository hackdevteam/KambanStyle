describe("Double click allows to edit", function(){
    var TEST_BOARD_TITLE = "Test Board Title";
    var TEST_BOARD_ID = "testBoardId";
    var TEST_COLUMN_TITLE = "Column 1";
    var TEST_TASK_TITLE = "Task 1";
    var TEST_TASK_ID = "t1";
    var TEST_COLUMN_ID = "c1";
    var presentationManager;

    beforeEach(function(){
        $(".html-reporter").before("<section class='board-area'></section>");
        presentationManager = new PresentationManager();
        var boardData = {board_id: TEST_BOARD_ID, title: TEST_BOARD_TITLE};
        var columnData = {column_id: TEST_COLUMN_ID, title: TEST_COLUMN_TITLE};
        var taskData = {task_id: TEST_TASK_ID, title: TEST_TASK_TITLE};
        presentationManager.showBoard(boardData, $(".board-area"));
        presentationManager.showColumn(columnData, $(".column-area"));
        presentationManager.showTask(taskData, $("#" + TEST_COLUMN_ID + " .task-area"));
    });

    afterEach(function(){
        $(".board-area").remove();
    });

    describe("double click on board title", function(){
        it("should change the board title label for a text box", function(){
            $("#board-title").dblclick();
            expect("#board-title").toBeHidden();
            expect("#edit-board-title").toBeVisible();
        });
    });

    describe("double click on column title", function(){
        it("should change the column title label for a text box", function(){
            $("#" + TEST_COLUMN_ID + ">h1").dblclick();
            expect("#" + TEST_COLUMN_ID + ">h1").toBeHidden();
            expect("#edit-column-title").toBeVisible();
        });
    });

    describe("double click on task title", function(){
        it("should change the column title label for a text box", function(){
            $("#" + TEST_TASK_ID + ">h2").dblclick();
            expect("#"+TEST_TASK_ID + ">h2").toBeHidden();
            expect("#edit-task-title").toBeVisible();
        });
    });
});