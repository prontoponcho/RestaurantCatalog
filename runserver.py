import os
from catalog import app

if __name__ == 'main':
    port = int(os.environ.get("PORT", 33507))
    app.debug = True
    app.secret_key = 'super-secret-key'
    app.run(host='0.0.0.0', port=5000)
