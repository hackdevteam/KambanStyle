var boardTemplate =$(
    "<div>" +
        "<article class='board' id='${board_id}'>" +
            "<h1 class='board-title'>${title}</h1>" +
            "<form id='create-column-form' action='javascript:actionsController.createColumn()'>" +
                "<input class='hidden' type='text' name='column-title' value='New Column'>" +
                "<button class='myButton' id='create-column-button' type='submit' name='create-column-button'>+Column</button>" +
            "</form>" +
            "<div class='column-area'></div>" +
            "<div id='trashIcon'> </div>" +
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
                    "<label><input type='text' name='board-name' value='${default_title}'></label>" +
                    "<input class='myButton' type='submit' name='create-board-button'>" +
                "</form>"+
            "</div>" +
        "</div>" +
    "</div>");

var editBoardTitleTemplate = $("<div><form id='edit' action='javascript:actionsController.modifyBoardTitle()'><input type='text' name='board-title' value='${text}'></form></div>");
var editColumnTitleTemplate = $("<div><form id='edit' action='javascript:actionsController.modifyColumnTitle()'><input type='text' name='column-title' value='${text}'><input class='hidden' type='text' name='columnId' value='${columnId}'></form></div>");
var editTaskTitleTemplate = $("<div><form id='edit' action='javascript:actionsController.modifyTaskTitle()'><input type='text' value='${text}'></form></div>");
var editTaskDescriptionTemplate = $("<div><form id='edit' action='javascript:actionsController.modifyTaskDescription()'><textarea>${text}</textarea></form></div>");
