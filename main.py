from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template("index.html")
 

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome="mundo"):
    return render_template("nome.html",nome=nome)
 
if __name__ == '__main__':
    app.run(debug=True)