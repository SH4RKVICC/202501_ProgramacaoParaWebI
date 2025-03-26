from flask import Flask

app=Flask(__name__) #Instancia com Variável que aloca diversos scripts na Flask

@app.route('/') #Aplica uma função na seguinte
def index():
    return 'Hello World'

if __name__=='__main__':
    app.run()