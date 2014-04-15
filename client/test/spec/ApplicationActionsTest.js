describe("Testing all the actions of the application", function(){
    beforeEach(function(){
        $(".html-reporter").before(createBoardForm);
    });

    afterEach(function(){
        $("#create-board-form-area").remove();
    });

    describe("create board", function(){
        it("should do a POST call to /api/board", function(){
            var connection = new Connection();
            spyOn(connection, "createBoard");
            var actionsController = new ActionsController(connection);
            actionsController.createBoard();
            expect(connection.createBoard).toHaveBeenCalledWith("My Board");
        });
    });
});