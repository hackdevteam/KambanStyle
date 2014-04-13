describe("Double click allows to edit", function(){
    var TEST_BOARD_TITLE = "Test Board Title";
    var TEST_BOARD_ID = "testBoardId";

    beforeEach(function(){
        $(".html-reporter").before("<section class='board-area'></section>");
    });

    describe("double click on board title", function(){
        it("should change the board title label for a text box", function(){
            var boardData = {board_id: TEST_BOARD_ID, title: TEST_BOARD_TITLE};
            var boardArea = $(".board-area");
            new PresentationManager().createBoard(boardData, boardArea);
            $("#board-title").dblclick();
            expect("#board-title").toBeHidden();
            expect("#edit-board-title").toBeVisible();
        });
    });

    describe("double click on column title", function(){
        it("should change the column title label for a text box", function(){
            var presentationManager = new PresentationManager();
            presentationManager.createBoard({board_id: TEST_BOARD_ID, title: TEST_BOARD_TITLE}, $(".board-area"));
            presentationManager.createColumn({column_id: "column1Id", title: "Column 1"}, $(".column-area"));
            expect("#column1Id").toBeVisible();
        });
    });
});