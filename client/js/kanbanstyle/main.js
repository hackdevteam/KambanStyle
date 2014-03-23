function boardCreationResponse(response) {
    $('#templateBoard').tmpl(JSON.parse(response)).appendTo(".board-area");
}

function columnCreationResponse(response) {
    console.log(JSON.parse(response));
    $('#templateColumn').tmpl(JSON.parse(response)).appendTo(".column-area");
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

createBoard("Board 1");
setTimeout(function () {
        createColumn("Column 1", $(".board").attr("id"));
    }
    , 200);

setTimeout(function () {
        createColumn("Column 2", $(".board").attr("id"));
    }
    , 200);

