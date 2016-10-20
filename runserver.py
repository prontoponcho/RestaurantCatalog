from catalog import app

app.debug = True
app.secret_key = 'super-secret-key'
app.run(host='0.0.0.0', port=5000)
