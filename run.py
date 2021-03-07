from app import app
import os

app.secret_key = os.urandom(24)
port = os.environ.get("PORT", 5000)
app.run(host="0.0.0.0", port=port, debug=True, use_reloader=False)