<?php
/**
 * Created by PhpStorm.
 * User: saurabh
 * Date: 22/8/16
 * Time: 6:44 AM
 */
?>
<html>
<head>
    <script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.0/jquery.min.js"></script>
    <link rel="stylesheet" href="style.css" />
    <title>jQuery Example</title>
    <script>
        $(document).ready(function() {
            $.ajaxSetup({ cache: true });
            $.getScript('//connect.facebook.net/en_US/sdk.js', function(){
                FB.init({
                    appId: '{your-app-id}',
                    version: 'v2.7' // or v2.1, v2.2, v2.3, ...
                });
                $('#loginbutton,#feedbutton').removeAttr('disabled');
                FB.getLoginStatus(updateStatusCallback);
            });
        });
    </script>
</head>
<body>

<script>
    function schedule(image_link) {
        FB.api(
            '/275476105939521/photos/',
            'POST',
            {"url":image_link,"scheduled_publish_time":"1471833000","published":"false"},
            function(response) {
                console.log(response);
                // Insert your code here
            }
        );
    }
</script>
</body>


