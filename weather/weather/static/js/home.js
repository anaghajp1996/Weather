$(document).ready(function() {
    getLocation();

    var lat;
    var lon;

    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition);
        
    }};

    function showPosition(position) {
        var lat = position.coords.latitude;
        var lon = position.coords.longitude;


        $.ajax({
            url: "/senddata/",
            type: "GET",
            dataType: "json",
            data: {
                "Latitude": lat,
                "Longitude": lon
            },
            success: function(response) {
                console.log(response);
                $(".cityname").html(response['city']);
                $(".region").html(response['region'] + "," + response['country']);
                $(".temp_f").html(response['temperature_c']+"°"+"C");
                $(".temp_c").html(response['temperature_f']+"°"+"F");

                $(".description").html(response['description']);
               
                $(".humidity").html("Humidty: " + response['humidity']+" %");
                $(".pressure").html("Pressure: " + response['pressure']);
                $(".windspeed").html("Wind Speed: " + response['wind_speed']+" kph");

                $(".date").html("Date And Time: " + response['dt_txt']);
                // $("img").attr('src', "http://icons.iconarchive.com/icons/papirus-team/papirus-apps/256/weather-icon.png");
                $(".card-img-top").attr('src',response['icon']);
                




                $(".all1").html(response['all_date1']);
                $(".all2").html(response['all_date2']);
                $(".all3").html(response['all_date3']);
                $(".all4").html(response['all_date4']);
                $(".all5").html(response['all_date5']);
                $(".all6").html(response['all_date6']);


                $(".sunrise1").html("Sunrise at : " + response['sunrise1']);
                $(".sunrise2").html("Sunrise at : " + response['sunrise2']);
                $(".sunrise3").html("Sunrise at : " + response['sunrise3']);
                $(".sunrise4").html("Sunrise at : " + response['sunrise4']);
                $(".sunrise5").html("Sunrise at : " + response['sunrise5']);
                $(".sunrise6").html("Sunrise at : " + response['sunrise6']);


                $(".sunset1").html("Sunset at : " + response['sunset1']);
                $(".sunset2").html("Sunset at : " + response['sunset2']);
                $(".sunset3").html("Sunset at : " + response['sunset3']);
                $(".sunset4").html("Sunset at : " + response['sunset4']);
                $(".sunset5").html("Sunset at : " + response['sunset5']);
                $(".sunset6").html("Sunset at : " + response['sunset6']);


                $(".desc1").html(response['desc1']);
                $(".desc2").html(response['desc2']);
                $(".desc3").html(response['desc3']);
                $(".desc4").html(response['desc4']);
                $(".desc5").html(response['desc5']);
                $(".desc6").html(response['desc6']);




                $(".icon1").attr('src',response['icon1']);
                $(".icon2").attr('src',response['icon2']);
                $(".icon3").attr('src',response['icon3']);
                $(".icon4").attr('src',response['icon4']);
                $(".icon5").attr('src',response['icon5']);
                $(".icon6").attr('src',response['icon6']);











            }
        });
    }

});










