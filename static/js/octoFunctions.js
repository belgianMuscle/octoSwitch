$(function(){

    console.log("It works");


    $('#zoneARange').on('mouseup', function(){

        var fData = {
            zoneALabel:$('#zoneALabel').text(),
            zoneBLabel:$('#zoneBLabel').text(),
            zoneAToggle:$('#zoneASwitch').is(":checked"),
            zoneBToggle:$('#zoneBSwitch').is(":checked"),
            zoneAVolume:$('#zoneARange').val(),
            zoneBVolume:$('#zoneBRange').val()
        };

        console.log("Range change on Zone A");
        $.ajax({
            type: "POST",
            url: '/volume',
            data: JSON.stringify(fData, null, '\t'),
            contentType: 'application/json;charset=UTF-8',
        }).done(function(res){
            //do something with the response from the server
        });
    });

    $('#zoneBRange').on('mouseup', function(){

        var fData = {
            zoneALabel:$('#zoneALabel').text(),
            zoneBLabel:$('#zoneBLabel').text(),
            zoneAToggle:$('#zoneASwitch').is(":checked"),
            zoneBToggle:$('#zoneBSwitch').is(":checked"),
            zoneAVolume:$('#zoneARange').val(),
            zoneBVolume:$('#zoneBRange').val()
        };

        console.log("Range change on Zone B");
        $.ajax({
            type: "POST",
            url: '/volume',
            data: JSON.stringify(fData, null, '\t'),
            contentType: 'application/json;charset=UTF-8',
        }).done(function(res){
            //do something with the response from the server
        });
    });


    $('#zoneASwitch').on('mouseup', function(){
        
        var zAT = $('#zoneASwitch').is(":checked");
        var zBT = $('#zoneBSwitch').is(":checked");

        if (zAT){
            zAT = false;
        }else{
            zAT = true;
        }

        var fData = {
            zoneALabel:$('#zoneALabel').text(),
            zoneBLabel:$('#zoneBLabel').text(),
            zoneAToggle:zAT,
            zoneBToggle:zBT,
            zoneAVolume:$('#zoneARange').val(),
            zoneBVolume:$('#zoneBRange').val()
        };

        console.log("Switch change on Zone A");
        $.ajax({
            type: "POST",
            url: '/toggle',
            data: JSON.stringify(fData, null, '\t'),
            contentType: 'application/json;charset=UTF-8',
        }).done(function(res){
            //do something with the response from the server
            $('#zoneARange').prop('disabled', !zAT);
            $('#zoneBRange').prop('disabled', !zBT);
        });
    });

    $('#zoneBSwitch').on('mouseup', function(){

        var zAT = $('#zoneASwitch').is(":checked");
        var zBT = $('#zoneBSwitch').is(":checked");

        if (zBT){
            zBT = false;
        }else{
            zBT = true;
        }

        var fData = {
            zoneALabel:$('#zoneALabel').text(),
            zoneBLabel:$('#zoneBLabel').text(),
            zoneAToggle:zAT,
            zoneBToggle:zBT,
            zoneAVolume:$('#zoneARange').val(),
            zoneBVolume:$('#zoneBRange').val()
        };

        console.log("Switch change on Zone B");
        $.ajax({
            type: "POST",
            url: '/toggle',
            data: JSON.stringify(fData, null, '\t'),
            contentType: 'application/json;charset=UTF-8',
        }).done(function(res){
            //do something with the response from the server
            $('#zoneARange').prop('disabled', !zAT);
            $('#zoneBRange').prop('disabled', !zBT);
        });
    });
});