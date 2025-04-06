from flask import Flask
from flask.templating import render_template

app=Flask(__name__) #Instancia com Variável que aloca diversos scripts na Flask

@app.route('/') #Aplica uma função na seguinte
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)