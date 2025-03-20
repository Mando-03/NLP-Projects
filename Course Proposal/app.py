from flask import Flask
from Routes import proposal_bp, base_bp


app = Flask(__name__)

app.register_blueprint(base_bp, url_prefix='/')
app.register_blueprint(proposal_bp, url_prefix='/text-generator')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
