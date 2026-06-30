from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Scan(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    url = db.Column(db.String)
    final_url = db.Column(db.String)

    status_code = db.Column(db.Integer)

    server = db.Column(db.String)
    content_type = db.Column(db.String)
    encoding = db.Column(db.String)

    response_time = db.Column(db.Float)
    response_size = db.Column(db.Integer)

    title = db.Column(db.Text)
    meta_description = db.Column(db.Text)
    meta_keywords = db.Column(db.Text)

    canonical = db.Column(db.Text)
    language = db.Column(db.String)
    charset = db.Column(db.String)
    robots = db.Column(db.Text)

    favicon = db.Column(db.Text)

    headings = db.Column(db.Text)

    links = db.Column(db.Text)
    internal_links = db.Column(db.Integer)
    external_links = db.Column(db.Integer)

    images = db.Column(db.Text)

    css_files = db.Column(db.Text)
    js_files = db.Column(db.Text)

    forms = db.Column(db.Integer)

    emails = db.Column(db.Text)
    phones = db.Column(db.Text)

    social_links = db.Column(db.Text)

    word_count = db.Column(db.Integer)

    html_hash = db.Column(db.String)

    open_graph = db.Column(db.Text)

    twitter_cards = db.Column(db.Text)

    json_ld = db.Column(db.Text)

    robots_exists = db.Column(db.Boolean)

    sitemap_exists = db.Column(db.Boolean)

    scanned_at = db.Column(db.DateTime, default=datetime.utcnow)