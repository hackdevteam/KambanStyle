var boardTemplate =$(
    "<div>" +
        "<div class='board' id='${board_id}'>" +
            "<div class='board-title-area'>" +
                "<h1 id='board-title'>${title}</h1>" +
            "</div>" +
            "<button id='create-column-button'>Create Column</button>" +
            "<div class='column-area'></div>" +
        "</div>" +
    "</div>");

var columnTemplate = $(
    "<div>" +
        "<div class='column' id='${column_id}'>" +
            "<h1>${title}</h1>" +
            "<div class='task-area'></div>" +
        "</div>" +
    "</div>");

var taskTemplate = $(
    "<div>" +
        "<div id=${task_id} class='task'>" +
            "<h2>${title}</h2>" +
            "<p>${description}</p>" +
        "</div>" +
    "</div>");

var editBoardTitleTemplate = $("<form id='edit-board-title' action='javascript:modifyBoardTitle()'><input type='text'></form>");
var editColumnTitleTemplate = $("<form id='edit-column-title' action='javascript:modifyColumnTitle()'><input type='text'></form>");
var editTaskTitleTemplate = $("<form id='edit-task-title' action='javascript:modifyTaskTitle()'><input type='text'></form>");