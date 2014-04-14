describe("Double click allows to edit", function(){
    var TEST_BOARD_TITLE = "Test Board Title";
    var TEST_BOARD_ID = "testBoardId";
    var TEST_COLUMN_TITLE = "Column 1";
    var TEST_TASK_TITLE = "Task 1";
    var TEST_TASK_ID = "t1";
    var TEST_TASK_DESCRIPTION = "This is just a short description of a task";
    var TEST_COLUMN_ID = "c1";
    var presentationManager;

    beforeEach(function(){
        $(".html-reporter").before("<section class='board-area'></section>");
        presentationManager = new PresentationManager();
        var boardData = {board_id: TEST_BOARD_ID, title: TEST_BOARD_TITLE};
        var columnData = {column_id: TEST_COLUMN_ID, title: TEST_COLUMN_TITLE};
        var taskData = {task_id: TEST_TASK_ID, title: TEST_TASK_TITLE, description: TEST_TASK_DESCRIPTION};
        presentationManager.showBoard(boardData, $(".board-area"));
        presentationManager.showColumn(columnData, $(".column-area"));
        presentationManager.showTask(taskData, $("#" + TEST_COLUMN_ID + " .task-area"));
    });

    afterEach(function(){
        $(".board-area").remove();
    });

    describe("double click on board title", function(){
        it("should change the board title label for a text box", function(){
            $(".board-title").dblclick();
            expect(".board-title").toBeHidden();
            expect("#edit-title").toBeVisible();
        });
    });

    describe("double click on column title", function(){
        it("should change the column title label for a text box", function(){
            $("#" + TEST_COLUMN_ID + " .column-title").dblclick();
            expect("#" + TEST_COLUMN_ID + " .column-title").toBeHidden();
            expect("#edit-title").toBeVisible();
        });
    });

    describe("double click on task title", function(){
        it("should change the column title label for a text box", function(){
            $("#" + TEST_TASK_ID + " .task-title").dblclick();
            expect("#" + TEST_TASK_ID + " .task-title").toBeHidden();
            expect("#edit-title").toBeVisible();
        });
    });

    describe("double click on task description", function(){
        it("should change the column title label for a text box", function(){
            var $taskDescription = $("#" + TEST_TASK_ID + ">p");
            var taskDescriptionText = $taskDescription.text();
            $taskDescription.dblclick();
            expect("#" + TEST_TASK_ID + " .task-description").toBeHidden();
            expect("#" + TEST_TASK_ID + " #edit-description").toBeVisible();
            expect($("#edit-description").text()).toEqual(taskDescriptionText);
        });
    });

    describe("Making click in any place outside the input box", function(){
        describe("Editing the board title", function(){
            it("should cancels the operation", function(){
                var $boardTitle = $(".board-title");
                $boardTitle.dblclick();
                $(".task-title").click();
                expect($boardTitle).toBeVisible();
                expect($("#edit-title")).not.toBeInDOM();
            });
        });
        describe("Editing a column title", function(){
            it("should cancels the operation", function(){
                var $columnTitle = $("#" + TEST_COLUMN_ID + " .column-title");
                $columnTitle.dblclick();
                $(".task-description").click();
                expect($columnTitle).toBeVisible();
                expect($("#edit-title")).not.toBeInDOM();
            });
        });
        describe("Editing a task title", function(){
            it("should cancels the operation", function(){
                var $taskTitle = $("#" + TEST_TASK_ID + " .task-title");
                $taskTitle.dblclick();
                $(".board-title").click();
                expect("#" + TEST_TASK_ID + " .task-title").toBeVisible();
                expect($("#edit-title")).not.toBeInDOM();
            });
        });

        describe("Editing a task description", function(){
            it("should cancels the operation", function(){
                var $taskDescription = $("#" + TEST_TASK_ID + " .task-description");
                $taskDescription.dblclick();
                $(".board-title").click();
                expect($taskDescription).toBeVisible();
                expect($("#edit-description")).not.toBeInDOM();
            });
        });
    });
});