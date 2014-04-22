var boardTemplate =$(
    "<div>" +
        "<article class='board' id='${board_id}'>" +
            "<h1 class='board-title'>${title}</h1>" +
            "<form id='create-column-form' action='javascript:actionsController.createColumn()'>" +
                "<button id='create-column-button' type='submit' name='create-column-button'>+Column</button>" +
                "<input type='text' name='column-title' value='New Column'>" +
            "</form>" +
            "<div class='column-area'></div>" +
        "</article>" +
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

var createBoardForm = $(
    "<div>" +
        "<div id='create-board-form-area'>" +
            "<div id='page-title'><h1>KanBan Style</h1></div>" +
                "<form id='create-board-form' action='javascript:actionsController.createBoard()'>" +
                    "<label><input type='text' name='board-name' value='${default_title}' id = 'nameBoard'></label>" +
                    "<input type='submit' name='create-board-button'>" +
                "</form>"+
            "</div>" +
        "</div>" +
    "</div>");

var editBoardTitleTemplate = $("<form id='edit-title' action='javascript:modifyBoardTitle()'><input type='text'></form>");
var editColumnTitleTemplate = $("<form id='edit-title' action='javascript:modifyColumnTitle()'><input type='text'></form>");
var editTaskTitleTemplate = $("<form id='edit-title' action='javascript:modifyTaskTitle()'><input type='text'></form>");
var editTaskDescriptionTemplate = $("<div><form id='edit-description' action='javascript:modifyTaskDescription()'><textarea>${description}</textarea></form></div>");