function Connection() {
    this.boardCreationResponse = function (response) {
        $('#templateBoard').tmpl(JSON.parse(response)).appendTo(".board-area");
    };

    this.columnCreationResponse = function(response) {
        $('#templateColumn').tmpl(JSON.parse(response)).appendTo(".column-area");
    };

    this.taskCreationResponse = function(response) {
        var jsonResponse = JSON.parse(response);
        $('#templateTask').tmpl(jsonResponse).appendTo("#" + jsonResponse.column_id + "-task-area");
    };

    this.createBoard = function(title) {
        $.post("api/board", {title: title}).done(function (response) {
            boardCreationResponse(response);
        })
    };

    this.createColumn = function(title, board_id) {
        $.post("api/column", {title: title, board_id: board_id}).done(function (response) {
            columnCreationResponse(response);
        })
    };

    this.createTask = function(title, description, column_id) {
        $.post("api/task", {title: title, description: description, column_id: column_id}).done(function (response) {
            taskCreationResponse(response);
        })
    };
}
function Context(){
    this.boardId = [];
    this.columns = [];
    this.getBoardId = function(){return this.boardId;};
    this.setBoardId = function(boardId){this.boardId = boardId;};
    this.getNumberOfColums = function(){return this.columns.length};
}

var connection = new Connection();
var context = new Context();

