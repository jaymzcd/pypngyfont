PAGE_TEMPLATE = """<!DOCTYPE HTML>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
    <title>Sneakerpedia Images</title>
    <script type="text/javascript" src="http://code.jquery.com/jquery-1.6.1.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function() { }); 
    </script>
    <style type="text/css">
        .bit { width:{{ bit.width }}px; height:{{ bit.height }}px; overflow:hidden; float:left; }
        .bit > .hoverimage > img { width:{{ bit.width }}; height:{{ bit.height }}px; }
        .digit { width:600px; }
        .digit-container { float:left; width:600px; display:inline-block; }
        #copy { font-family: 'Verdana'; margin:10px; clear:both; }
    </style>
</head>
<body>
    <div id="copy">
        <h1>Sneakerpedia Live pull bitmask clock</h1>
        What you're seeing here is a live pull of the latest images
        from Sneakerpedia. The shapes are customizable via a bitmask. Images
        rotate through an array to avoid blanks and default images from the site
        are ignored.
    </div>
    {% for digit in digits %}
        <div class="digit-container">{{ digit }}</div>
    {% endfor %}
</body>
</html>
"""