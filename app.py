from simple_http_server import route, server
    
@route("/")
def index():
    return {"hello": "world"}   

server.start(port=8000)
