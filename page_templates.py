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
        .bit img { width:{{ bit.width }}px; height:{{ bit.height }}px; }
        .digit { width:{{ char.width }}px; }
        .digit-container { float:left; width:{{ char.width }}px; display:inline-block; }
        #copy { font-family: 'Verdana'; margin:10px; clear:both; }
    </style>
</head>
<body>
    <div id="copy">
        <h1>'Font' from images created from PNG mask</h1>
    </div>
    {% for digit in digits %}
        <div class="digit-container">{{ digit }}</div>
    {% endfor %}
</body>
</html>
"""