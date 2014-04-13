describe("Double click allows to edit", function(){
    beforeEach(function(){
        $(".html-reporter").before("<section class='board-area'></section>");
    });

    describe("double click on board title", function(){
        it("should change the board title label for a text box", function(){
            var presentationManager = new PresentationManager();
            var boardArea = $(".board-area");
            var boardId = "brdtest";
            var boardTitle = "TestBoard";
            var boardData = {board_id: boardId, title: boardTitle};
            presentationManager.createBoard(boardData, boardArea);
            expect($("#"+boardId)).toBeInDOM();
        });
    });
});