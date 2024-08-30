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

@app.route ('/tripulacion/clima')
def climat():
    return render_template('climat.html')

@app.route ('/pasajeros/clima')
def climap():
    return render_template('climap.html')
