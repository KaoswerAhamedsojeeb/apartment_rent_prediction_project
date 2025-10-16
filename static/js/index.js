function onclickedEstimatePrice() {
    console.log("Estimate price button clicked");

    var city = document.getElementById("city").value;
    var area = document.getElementById("area").value;
    var bedroom = document.getElementById("bedroom").value;
    var bathroom = document.getElementById("bathroom").value;
    var balcony = document.getElementById("balcony").value;
    var tiles = document.getElementById("tiles").value;

    var url = "http://127.0.0.1:5000/predict";

    $.post(url, {
        city: city,
        area: parseFloat(area, 10),
        bedroom: bedroom,
        bathroom: bathroom,
        balcony: balcony,
        tiles: tiles
    }, function (data, status) {
        console.log(data.estimated_price);
        document.getElementById("estimated_price").innerHTML = "<h2>" + data.estimated_price.toString() + " BDT</h2>";
        console.log(status);
    }
    );
}