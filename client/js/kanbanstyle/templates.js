var boardTemplate =$(
    "<div>" +
        "<div class='board' id='${board_id}'>" +
            "<div class='board-title-area'>" +
                "<h1 id='board-title'>${title}</h1>" +
            "</div>" +
            "<button id='createColumnButton'>Create Column</button>" +
            "<div class='column-area'></div>" +
        "</div>" +
    "</div>");

var columnTemplate = $(
    "<div>" +
        "<div class='column' id='${column_id}'>" +
            "<h1>${title}</h1>" +
            "<div id='${column_id}-task-area' class='list-task'></div>" +
        "</div>" +
    "</div>");


var editBoardTitleTemplate = $("<form id='edit-board-title' action='javascript:modifyBoardTitle()'><input type='text'></form>");