function showModal(element) {
    var modalId = $(element).attr("data-modal");
    $("#" + modalId).addClass("showmodal");
}
$(document).ready(function() {
    $(".close-modal").click(function() {
        $(".modal-container").removeClass("showmodal");
    })

})
$(document).click((event) => {
    if (!$(event.target).parents('.pf_dropdown').length && !$(event.target).is('.profile, .pbtnarrowdown')) {
        if ($(".pf_dropdown").hasClass("opacity")) {
            $(".pf_dropdown").removeClass("opacity");
        }
    }
});

function pfDropdown() {
    if ($(".pf_dropdown").hasClass("opacity")) {
        $(".pf_dropdown").removeClass("opacity");
    } else {
        $(".pf_dropdown").addClass("opacity");
    }
}