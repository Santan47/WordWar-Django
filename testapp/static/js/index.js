$(document).ready(function () {
    wordWarAppModel = new wordWarApp();
    wordWarAppModel.init();
});


function wordWarApp() {

    var fnAjaxRequest = function (ajaxURL, ajaxReqMethod, ajaxReqHeader, ajaxReqData, onSucess, onError) {
        $.ajax({
            type: ajaxReqMethod,
            url: ajaxURL,
            headers: ajaxReqHeader,
            data: ajaxReqData,
            success: onSucess,
            error: onError
        });
    };

    (function () {
        //  change nav tab
        $('body').off('click', '.navigationTab').on('click', '.navigationTab', function (e) {
            e.preventDefault();
            e.stopPropagation();
            $(".navigationTab").removeClass("active");
            $(this).addClass("active");
            if ($(this).attr("data-id") == "Home") {
                $("#postSomethingTemplet").addClass("hide");
                $("#userFeedsTemplet").removeClass("hide");
            }

        });

        // change selected card
        $('body').off('click', '.card').on('click', '.card', function (e) {
            e.preventDefault();
            e.stopPropagation();
            $(".card").removeClass("active");
            $(this).addClass("active");
        });

        // write somthing click
        $('body').off('click', '.rightTopBody .postSomething').on('click', '.rightTopBody .postSomething', function (e) {
            e.preventDefault();
            e.stopPropagation();
            $("#userFeedsTemplet").addClass("hide");
            $("#postSomethingTemplet").removeClass("hide");
        });

        // write upload content click
        $('body').off('click', '#uploadContent').on('click', '#uploadContent', function (e) {
            e.preventDefault();
            e.stopPropagation();
            uploadContentData("hello","my data is here");
        });

    })();


    function uploadContentData(title, content) {
        var url = 'uploadContentData/';
        var method = 'POST';
        var payload = {
            "title" : title,
            "content" : content
        }
        var fnSuccess = function (data) {
            console.log("success",data);
        }
        var fnError = function (err) {
            console.error('unexpected error', err);
        }

        fnAjaxRequest(url, method, {}, payload, fnSuccess, fnError);
    }

    return {
        init: function () {
            var initialize = 1;
        }
    }
}