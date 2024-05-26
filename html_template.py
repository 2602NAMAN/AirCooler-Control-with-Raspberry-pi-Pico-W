HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Cooler Control</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f2f2f2;
        }
        .container {
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #2551cc;
        }
        .button {
            display: inline-block;
            background-color: #2ba615;
            color: #ffffff;
            font-size: 18px;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            margin: 10px;
            transition: background-color 0.3s;
        }
        .button:hover {
            background-color: #1e8d15;
        }
        .button-off {
            background-color: #f44336;
        }
        .button-off:hover {
            background-color: #d32f2f;
        }
        .form-container {
            margin-top: 20px;
        }
        .form-container input[type="number"] {
            padding: 10px;
            font-size: 18px;
            width: 100px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        .form-container input[type="submit"] {
            padding: 10px 20px;
            font-size: 18px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            background-color: #4CAF50;
            color: white;
            transition: background-color 0.3s;
        }
        .form-container input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Cooler Control</h1>
        <p>%s</p>
        <div class="form-container">
            <form action="/global-timer" method="get">
                <label for="hours">Hours:</label>
                <input type="number" id="hours" name="hours" min="0" required>
                <label for="minutes">Minutes:</label>
                <input type="number" id="minutes" name="minutes" min="0" max="59" required>
                <p><input type="submit" value="Set Timer">
                <a href="/stop-global-timer" class="button button-off">Stop Timer</a></p>
            </form>
        </div>
        <p><a href="/relay1/on" class="button">Fan On</a><a href="/relay1/off" class="button button-off">Fan Off</a></p>
        <p><a href="/relay2/on" class="button">Swing On</a><a href="/relay2/off" class="button button-off">Swing Off</a></p>
        <p><a href="/relay3/on" class="button">Pump On</a><a href="/relay3/off" class="button button-off">Pump Off</a></p>
        <p><a href="/relays/on" class="button">All Relays On</a><a href="/relays/off" class="button button-off">All Relays Off</a></p>
        <div class="form-container">
            <form action="/loop" method="get">
                <p><label for="on-duration">Pump On Duration (Min):</label>
                <input type="number" id="on-duration" name="on-duration" min="1" required></p>
                <label for="off-duration">Pump Off Duration (Min):</label>
                <input type="number" id="off-duration" name="off-duration" min="1" required>
                <p><input type="submit" value="Start">
                <a href="/stop-loop" class="button button-off">Stop</a></p>
            </form>
        </div>
        <p><a href="/reset" class="button button-off">Reset All</a></p>
    </div>
</body>
</html>
"""