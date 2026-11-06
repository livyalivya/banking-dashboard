from flask import Flask, render_template, request
from products import PRODUCTS

app = Flask(__name__)

@app.route("/")
def home():
    category = request.args.get("category", "All")
    search = request.args.get("search", "")

    items = []
    for p in PRODUCTS:
        if (category == "All" or p["category"] == category) \
           and search.lower() in p["name"].lower():
            items.append(p)

    return render_template("index.html", products=items,
                           category=category, search=search)

if__name__= "__main__":
    app.run(debug=True)