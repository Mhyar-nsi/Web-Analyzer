from flask import Flask, render_template, request, redirect, abort

from sqlalchemy.inspection import inspect

from models import db, Scan
from scraper.scraper import scrape

import json


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.template_filter("fromjson")
def fromjson(value):
    if not value:
        return []
    return json.loads(value)

@app.template_filter("to_dict")
def to_dict(model):
    return {
        c.key: getattr(model, c.key)
        for c in inspect(model).mapper.column_attrs
    }
@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        url = request.form["url"]

        data = scrape(url)

        scan = scan = Scan(**data)

        db.session.add(scan)
        db.session.commit()
        result = data

    return render_template(
        "index.html",
        result=result
    )


@app.route("/reports")
def logs():

    scans = Scan.query.order_by(
        Scan.scanned_at.desc()
    ).all()

    return render_template(
        "reports.html",
        scans=scans
    )

@app.route("/report/<int:scan_id>")
def report(scan_id):

    scan = Scan.query.get(scan_id)

    if scan is None:
        abort(404)

    return render_template(
        "report.html",
        scan=scan
    )

if __name__ == "__main__":
    app.run(debug=True)