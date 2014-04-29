var context = {
    boardId: {},
    getBoardId: function(){return this.boardId;},
    setBoardId: function(boardId){this.boardId = boardId;}
};

const DEFAULT_BOARD_TITLE = "My Board";
$(document).ready(function(){
    $("body").append(createBoardForm.tmpl({default_title: DEFAULT_BOARD_TITLE}));
});
