var boardTemplate = $(
    "<div>"+
        "<div class='board' id='${board_id}'>" +
            "<div id='title'>" +
                "<h1>${title}</h1>" +
                "<button id='createColumnButton'>Create Column</button>" +
            "</div>" +
            "<div>" +
                "<div class='column-area'></div>" +
            "</div>" +
        "</div>" +
    "</div>");