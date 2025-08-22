from flask import Flask, Response

app = Flask(__name__)

@app.after_request
def add_security_headers(resp: Response):
    resp.headers["X-Frame-Options"] = "DENY"
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["Referrer-Policy"] = "no-referrer"
    # Em produção com HTTPS, ative HSTS:
    # resp.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains; preload"
    return resp

@app.route("/", methods=["GET"])
def pagina_inicial():
    return "Continuous Integration and Continuous Delivery"
