from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/shop-detail")
def shop_detail():
    return render_template("shop-detail.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/chackout")
def chackout():
    return render_template("chackout.html")

@app.route("/testimonial")
def testimonial():
    return render_template("testimonial.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/chart")
def chart():
    return render_template("chart.html")


if __name__ == "__main__":
    app.run(debug=True)