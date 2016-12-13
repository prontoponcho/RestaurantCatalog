from catalog import app

# Heroku deployment
# if __name__ == 'main':
app.debug = False
app.secret_key = 'super-secret-key'
# app.run(host='0.0.0.0', port=5000)

# For Local Deployment
# if __name__ == "__main__":
#     app.debug = True
#     app.secret_key = 'super-secret-key'
#     app.run(host='0.0.0.0', port=5000)
