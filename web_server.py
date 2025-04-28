from http.server import HTTPServer, BaseHTTPRequestHandler

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Cognito Inc.</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            background-color: #f4f4f4; 
            text-align: center; 
            padding-top: 50px; 
            margin-top: 100px
        }
        .bold { 
            font-weight: bold; 
            font-size: 24px; 
        }
        .italics { 
            color: #007BFF; 
            font-style: italic; 
            font-size: 20px; 
        }
        #intro, #tagline { 
            white-space: pre; 
        }
        .button { 
            background-color: #007BFF; 
            color: white; 
            border: none; 
            padding: 10px 20px; 
            font-size: 16px; 
            cursor: pointer; 
            margin: 10px; 
        }
        .button:hover { 
            background-color: #0056b3; 
        }
        .more_padding {
            padding-bottom: 50px; 
        }
    </style>
</head>
<body>
    <div id="intro" class="bold"></div>
    <br>
    <div id="tagline" class="italics more_padding"></div>
    <button class="button" style="display: none;" id="login_button">Login In</button>
    <button class="button" style="display: none;" id="signup_button">Create An Account</button>


    <script>
        const introText = "Welcome to Cognito Inc. Banking.";
        const taglineText = "Financials for the Future.";

        function typeEffect(elementId, text, delay, callback) {
            let i = 0;
            const element = document.getElementById(elementId);
            const timer = setInterval(() => {
                if (i < text.length) {
                    element.textContent += text.charAt(i);
                    i++;
                } else {
                    clearInterval(timer);
                    if (callback) callback();
                }
            }, delay);
        }

        typeEffect("intro", introText, 70, () => {
            setTimeout(() => {
                typeEffect("tagline", taglineText, 70, () => {
                    setTimeout(() => {
                        document.getElementById("login_button").style.display = "inline-block";
                        document.getElementById("signup_button").style.display = "inline-block";
                    }, 1200);
                });
            }, 1200);
        });
    </script>
</body>
</html>
"""

class WebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, WebHandler)
    print("Web version running at http://localhost:8000/")
    httpd.serve_forever()