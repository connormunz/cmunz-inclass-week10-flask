from flask import Flask, render_template

# CRITICAL: Point Flask to the custom template location
app = Flask(__name__, template_folder="templates")


@app.route("/")
def hello():
    return "Hello World"


@app.route("/connor")
def connor():
    x = 6
    y = 15
    z = x + y
    name = "connor"
    return f"Hello {name}, the sum of {x} and {y} is {z}"


@app.route("/about")
def about():
    # Now this will search inside static/templates/ automatically
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
