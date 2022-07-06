"""
Run a test server.
Its only job is to start the module nothing else
"""

from toxic import app
from flask_cors import CORS

CORS(app=app)
app.run(host="0.0.0.0", port=8080, debug=True)
