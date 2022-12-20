
$("document").ready(function() {
    $("span").hide();

    $("#show-btn").click(function() {
        $(".span-id").fadeTo(5000, 0.8);
        $(".span-name").fadeTo(6000, 0.8);
        $(".span-description").fadeTo(7000, 0.8);
        $(".span-price").fadeTo(8000, 0.8);
        $(".span-quantity").fadeTo(9000, 0.8);
    })

    $("#hide-btn").click(function() {
        $("span").hide();
    })
})