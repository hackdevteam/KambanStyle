function Board() {
    this.board_id = [];
    this.board_title = [];
    this.columns = [];
}
var board = new Board();

function boardCreationResponse(response) {
    board.board_id = JSON.parse(response).board_id;
    board.board_title = JSON.parse(response).title;
    $('#templateBoard').tmpl(JSON.parse(response)).appendTo(".board-area");

}

function createBoard(title) {
    $.post("api/board", {title: title}).done(function (response) {
        boardCreationResponse(response);
    })
}

createBoard("Board 1");