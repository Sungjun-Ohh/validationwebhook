#!flask/bin/python
from app import app
import ssl

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_verify_locations('./cert/ca.crt')
    context.load_cert_chain('./cert/server.crt', './cert/server.key')
    app.run(host="0.0.0.0", debug=True, ssl_context=context)
    
