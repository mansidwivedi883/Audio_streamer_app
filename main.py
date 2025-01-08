from flask import Flask, render_template, request, session, redirect
from flask_socketio import join_room, send, SocketIO
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config["SECRET_KEY"] = "fghbcmutr"
socketio = SocketIO(app)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        # Handle logic for join or create here (if needed)
        return render_template("home.html", name=name, code=code)

    # For GET requests
    return render_template("home.html", name="", code="")

if __name__ == "__main__":
    socketio.run(app, debug=True)
