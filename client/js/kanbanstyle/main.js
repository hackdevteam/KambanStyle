function Board() {
    this.board_id = [];
    this.columns = [];
}


$(document).ready(function () {
    var my_board = new Board;
    createBoard("Example", my_board);
    createColumn("Column 1", my_board);
    createTask("Task 1", "First task", my_board);
    createTask("Task 2", "Second task", my_board);
    createTask("Task 3", "Third task", my_board);
});

function createBoard(boardName) {
    $.post("api/my_board",
        {name: boardName},
        function (response) {
            my_board.board_id = response.board_id;
            $('#templateBoard').tmpl(response).appendTo('body');
        },
        "json");
}

function createColumn(title, board_id) {
    $.post("api/column",
        {title: title, board_id: board_id},
        function (response) {
            my_board.columns.push(response.column_id);
            $('#templateColumn').tmpl(response).appendTo('#column-area');
        },
        "json");
}

function createTask(title, description, column_id) {
    $.post("api/task",
        {title: title, description: description, column_id: column_id},
        function (response) {
            $('#templateTask').tmpl(response).appendTo('#' + response.task_id + '-list-task-area');
        },
        "json");
}