
$("document").ready(function() {
    let productID = document.getElementById("product-id");
    let productName = document.getElementById("product-name");
    let productDescription = document.getElementById("product-description");
    let productPrice = document.getElementById("product-price");
    let productQuantity = document.getElementById('product-quantity');


    $("#product-id").hide(); 
    $("#product-name").hide();
    $("#product-description").hide();
    $("#product-price").hide();
    $("#product-quantity").hide();

    $("#id-id").click(function() {
        $("#product-id").fadeTo(5000, 0.5)
    })
    $("#id-name").click(function() {
        $("#product-name").fadeTo(5000, 0.5)
    })
    $("#id-description").click(function() {
        $("#product-description").fadeTo(5000, 0.5)
    })
    $("#id-price").click(function() {
        $("#product-price").fadeTo(5000, 0.5)
    })
    $("#id-quantity").click(function() {
        $("#product-quantity").fadeTo(5000, 0.5)
    })
})