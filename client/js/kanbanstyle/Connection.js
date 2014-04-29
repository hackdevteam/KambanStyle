var connection = {
    post : function(url, data, responseCallback){
        $.post(url, data, responseCallback, "json");
    }
};
