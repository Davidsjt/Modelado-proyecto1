from flask import Flask, render_template
app = Flask ( __name__ )


@app.route ('/')
def inicio():
    return render_template('inicio.html')

@app.route ('/tripulacion')
def tripulacion():
    return render_template('tripulacion.html')

@app.route ('/pasajeros')
def pasajeros():
    return render_template('pasajero.html')


#flask --app --debug run
#export FLASK_APP=start
#export FLASK_ENV=development
#https://www.google.com/search?client=firefox-b-d&q=tutoriales+de+flask#fpstate=ive&vld=cid:506fc2ce,vid:W-SfC_V7P6o,st:0