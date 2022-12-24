
$("document").ready(function() {
    let productID = document.getElementById("product-id");
    $("#product-id").hide(); $("#submit").hide();
    $("#id").click(function() {
        $("#product-id").fadeTo(5000, 0.5)
    })
    $("#product-id").mouseover(function() {
        $("#submit").fadeTo(5000, 1);
    })
    $("#submit").click(function() {
        if (productID.value == "") {
            alert("ID NOT FOUND!\nRetrieving Default Value...");
            productID.value = 1;
        }
    })

    $("#product").hide(); $("#product-del").hide(); $("#products").hide(); $(".btn").hide();
    $("#home").mouseover(function() {
        $("#product").fadeTo(5000, 0.8); $("#product-del").fadeTo(6000, 0.8); $("#products").fadeTo(7000, 0.8); $(".btn").fadeTo(7500, 0.8);
    })
})