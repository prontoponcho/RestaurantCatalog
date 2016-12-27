from catalog import app

# For Local Deployment
if __name__ == "__main__":
    app.debug = True
    app.secret_key = 'super-secret-key'
    app.run(host='0.0.0.0', port=5000)
# For Heroku Deployment
else:
    app.debug = False
    app.secret_key = 'super-secret-key'
