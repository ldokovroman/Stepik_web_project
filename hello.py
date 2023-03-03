bind = "0.0.0.0:8080"

def wsgi_app(environ, start_response):
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    body = environ["QUERY_STRING"].replace('&', "\r\n").encode()
    start_response(status, headers)
    return [body]