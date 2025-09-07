from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'API do Carrinho funcionando 🚀'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
