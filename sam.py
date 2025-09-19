from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head> 
     <title>sam joel
     </title>
    </head>
    <body bgcolor="WHITE" ALIGN="CENTER" text="black">

        <h1>MY DEVICE:25001200</h1>
        <TABLE border="3" BGCOLOR="RED" ALIGN="CENTER">
            <tr BGCOLOR="GREEN">
                <th>
                    S.NO
                </th>
                <th>
                    SPECIFICATION</th>
                <th> DETAILS</th> 
               
                
            </tr>
            <tr>
                <td>1</td>
                <td>device name </td>
                <td>TMP215-75-G2</td>
            </tr>
            <tr>
                <td>2</td>
                <td>processor</td>
                <td>Intel(R) Core(TM) Ultra 5 125H (1.20 GHz)</td>

            </tr>
            <tr>
                <td>3</td>
                <td>Ram</td>
                <td>16GB</td>
            </tr>
            <tr>
                <TD>4</TD>
                <TD>Storage</TD>
                <TD>1TB</TD>
            </tr>
            <tr>
                <TD>5</TD>
                <TD>System type</TD>
                <TD>64-bit operating system, x64-based processor</TD>
            
            
        </TABLE>


    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()