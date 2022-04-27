from config import app

@app.get('/message')
def greetnow():
    return "This is some message page...Hi How arey you?"

@app.get('/number')
def fun():
    return " 09876543211234567890"