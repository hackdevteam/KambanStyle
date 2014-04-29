describe("Presentation Manager", function(){
    describe("when modifyBoard", function(){
        it("should change the board title to the new one passed via parameter", function(){
            var newBoardTitle = "new title";
            presentationManager.modifyBoardTitle(newBoardTitle);
            expect($(".board-title").text()).toBe(newBoardTitle);
        });
    });

    describe("when modifyColumnTitle", function(){
        it("should change the column title to the new one passed via parameter", function(){
            var newColumnTitle = "New Column Title";
            presentationManager.modifyColumnTitle(TEST_COLUMN_ID, newColumnTitle);
            expect($("#" + TEST_COLUMN_ID + ">.column-title").text()).toBe(newColumnTitle);
        });
    });

    var TEST_BOARD_TITLE = "Test Board Title";
    var TEST_BOARD_ID = "testBoardId";
    var TEST_COLUMN_ID = "1234";
    var TEST_COLUMN_TITLE = "Column Title";
    beforeEach(function(){
        $(".html-reporter").before("<section class='board-area'></section>");
        var boardData = {board_id: TEST_BOARD_ID, title: TEST_BOARD_TITLE};
        presentationManager.addBoardToDOM(boardData, $(".board-area"));
        presentationManager.addColumnToDOM({title: TEST_COLUMN_TITLE, column_id: TEST_COLUMN_ID}, $(".column-area"));
    });

    afterEach(function(){
        $(".board-area").remove();
    });

});