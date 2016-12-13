from catalog import app

# if __name__ == 'main':
# app.debug = True
# app.secret_key = 'super-secret-key'
# app.run(host='0.0.0.0', port=5000)

# For Heroku Deployment
if __name__ == "__main__":
    app.debug = True
    app.secret_key = 'super-secret-key'
    app.run()
