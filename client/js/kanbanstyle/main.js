function boardCreationResponse(response) {
    $('#templateBoard').tmpl(JSON.parse(response)).appendTo(".board-area");
}

function columnCreationResponse(response) {
    $('#templateColumn').tmpl(JSON.parse(response)).appendTo(".column-area");
}

function taskCreationResponse(response) {
    var jsonResponse = JSON.parse(response);
    $('#templateTask').tmpl(jsonResponse).appendTo("#" + jsonResponse.column_id + "-task-area");
}

function createBoard(title) {
    $.post("api/board", {title: title}).done(function (response) {
        boardCreationResponse(response);
    })
}

function createColumn(title, board_id) {
    $.post("api/column", {title: title, board_id: board_id}).done(function (response) {
        columnCreationResponse(response);
    })
}

function createTask(title, description, column_id) {
    $.post("api/task", {title: title, description: description, column_id: column_id}).done(function (response) {
        taskCreationResponse(response);
    })
}


createBoard("Board 1");
setTimeout(function () {
        createColumn("Column 1", $(".board").attr("id"));
    }
    , 100);

setTimeout(function () {
        createColumn("Column 2", $(".board").attr("id"));
    }
    , 200);

setTimeout(function () {
        createTask("Task 1", "Hacer MDA", $(".column").map(function () {
            return $(this).attr("id");
        }).get()[0]);
    }
    , 600);

setTimeout(function () {
        createTask("Task 2", "description", $(".column").map(function () {
            return $(this).attr("id");
        }).get()[0]);
    }
    , 600);

setTimeout(function () {
        createTask("Task 3", "description", $(".column").map(function () {
            return $(this).attr("id");
        }).get()[1]);
    }
    , 600);