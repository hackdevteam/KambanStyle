var boardTemplate =$(
    "<div>" +
        "<div class='board' id='${board_id}'>" +
            "<h1 class='board-title'>${title}</h1>" +
            "<button id='create-column-button'>+Column</button>" +
            "<div class='column-area'></div>" +
        "</div>" +
    "</div>");

var columnTemplate = $(
    "<div>" +
        "<div class='column' id='${column_id}'>" +
            "<h1 class='column-title'>${title}</h1>" +
            "<div class='task-area'></div>" +
        "</div>" +
    "</div>");

var taskTemplate = $(
    "<div>" +
        "<div id=${task_id} class='task'>" +
            "<h2 class='task-title'>${title}</h2>" +
            "<p class='task-description'>${description}</p>" +
        "</div>" +
    "</div>");

var editBoardTitleTemplate = $("<form id='edit-title' action='javascript:modifyBoardTitle()'><input type='text'></form>");
var editColumnTitleTemplate = $("<form id='edit-title' action='javascript:modifyColumnTitle()'><input type='text'></form>");
var editTaskTitleTemplate = $("<form id='edit-title' action='javascript:modifyTaskTitle()'><input type='text'></form>");
var editTaskDescriptionTemplate = $("<div><form id='edit-description' action='javascript:modifyTaskDescription()'><textarea>${description}</textarea></form></div>");