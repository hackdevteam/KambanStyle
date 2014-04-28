describe("Double click", function(){
    describe("on board title", function(){
        it("should replace the board title label with a text box", function(){
            var $boardTitle = $("h1.board-title");
            $boardTitle.dblclick();
            var $editTitle = $("#edit-title");
            expect($boardTitle).toBeHidden();
            expect($editTitle).toBeVisible();
            expect($editTitle.find("input").val()).toBe($boardTitle.text());
        });
    });

    describe("double click on column title", function(){
        it("should replace the column title label with a text box", function(){
            var $columnTitle = $("#" + TEST_COLUMN_ID + " .column-title");
            $columnTitle.dblclick();
            var $editTitle = $("#edit-title");
            expect("#" + TEST_COLUMN_ID + " .column-title").toBeHidden();
            expect($editTitle).toBeVisible();
            expect($editTitle.find(">input").val()).toBe($columnTitle.text());
        });
    });

    describe("double click on task title", function(){
        it("should change the column title label for a text box", function(){
            var $taskTitle = $("#" + TEST_TASK_ID + " .task-title");
            $taskTitle.dblclick();
            var $editTitle = $("#edit-title");
            expect("#" + TEST_TASK_ID + " .task-title").toBeHidden();
            expect($editTitle).toBeVisible();
            expect($editTitle.find("input").val()).toBe($taskTitle.text());
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

    describe("pressing escape ", function(){
        describe("Editing the board title", function(){
            it("should cancels the operation", function(){
                var $boardTitle = $(".board-title");
                $boardTitle.dblclick();
                pressKeyEvent(27);
                expect($boardTitle).toBeVisible();
                expect($("#edit-title")).not.toBeInDOM();
            });
        });
        describe("Editing a column title", function(){
            it("should cancels the operation", function(){
                var $columnTitle = $("#" + TEST_COLUMN_ID + " .column-title");
                $columnTitle.dblclick();
                pressKeyEvent(27);
                expect($columnTitle).toBeVisible();
                expect($("#edit-title")).not.toBeInDOM();
            });
        });
        describe("Editing a task title", function(){
            it("should cancels the operation", function(){
                var $taskTitle = $("#" + TEST_TASK_ID + " .task-title");
                $taskTitle.dblclick();
                pressKeyEvent(27);
                expect("#" + TEST_TASK_ID + " .task-title").toBeVisible();
                expect($("#edit-title")).not.toBeInDOM();
            });
        });

        describe("Editing a task description", function(){
            it("should cancels the operation", function(){
                var $taskDescription = $("#" + TEST_TASK_ID + " .task-description");
                $taskDescription.dblclick();
                pressKeyEvent(27);
                expect($taskDescription).toBeVisible();
                expect($("#edit-description")).not.toBeInDOM();
            });
        });
    });

    var TEST_BOARD_TITLE = "Test Board Title";
    var TEST_BOARD_ID = "testBoardId";
    var TEST_COLUMN_TITLE = "Column 1";
    var TEST_COLUMN_ID = "c1";
    var TEST_TASK_TITLE = "Task 1";
    var TEST_TASK_ID = "t1";
    var TEST_TASK_DESCRIPTION = "This is just a short description of a task";
    var presentationManager;
    var pressKeyEvent = function(keyCode){
        $.event.trigger({ type: 'keyup', which: keyCode });
    };

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
});