describe("Presentation Manager", function(){
    describe("when modifyBoard", function(){
        it("should change the board title to the new one passed via parameter", function(){
            var newTitle = "new title";
            presentationManager.modifyBoardTitle(newTitle);
            expect($(".board-title").text()).toBe(newTitle);
        });
    });

    var TEST_BOARD_TITLE = "Test Board Title";
    var TEST_BOARD_ID = "testBoardId";
    var presentationManager;
    beforeEach(function(){
        $(".html-reporter").before("<section class='board-area'></section>");
        presentationManager = new PresentationManager();
        var boardData = {board_id: TEST_BOARD_ID, title: TEST_BOARD_TITLE};
        presentationManager.showBoard(boardData, $(".board-area"));
    });

    afterEach(function(){
        $(".board-area").remove();
    });

});