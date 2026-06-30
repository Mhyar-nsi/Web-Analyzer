import hashlib
import json
import re
import time
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from collections import Counter


def scrape(url):

    headers = {
        "User-Agent": "Educational-WebScraper/1.0"
    }

    start = time.time()

    response = requests.get(
        url,
        headers=headers,
        timeout=10,
        allow_redirects=True
    )

    elapsed = time.time() - start

    soup = BeautifulSoup(response.text, "lxml")

    domain = urlparse(response.url).netloc

    data = {}

    data["url"] = url
    data["final_url"] = response.url

    data["status_code"] = response.status_code

    data["server"] = response.headers.get("Server")

    data["content_type"] = response.headers.get("Content-Type")

    data["encoding"] = response.encoding

    data["response_size"] = len(response.content)

    data["response_time"] = elapsed

    data["title"] = soup.title.text.strip() if soup.title else ""

    meta = soup.find("meta", attrs={"name": "description"})
    data["meta_description"] = meta.get("content") if meta else ""

    meta = soup.find("meta", attrs={"name": "keywords"})
    data["meta_keywords"] = meta.get("content") if meta else ""

    canonical = soup.find("link", rel="canonical")
    data["canonical"] = canonical.get("href") if canonical else ""

    html = soup.find("html")
    data["language"] = html.get("lang") if html else ""

    charset = soup.find("meta", charset=True)
    data["charset"] = charset.get("charset") if charset else ""

    robots = soup.find("meta", attrs={"name": "robots"})
    data["robots"] = robots.get("content") if robots else ""

    favicon = soup.find("link", rel=lambda x: x and "icon" in x.lower())
    data["favicon"] = favicon.get("href") if favicon else ""

    headings = []

    for tag in soup.find_all(["h1","h2","h3","h4","h5","h6"]):
        headings.append({
            "tag": tag.name,
            "text": tag.get_text(strip=True)
        })

    data["headings"] = json.dumps(headings)

    links = []

    internal = 0
    external = 0

    for a in soup.find_all("a", href=True):

        href = urljoin(response.url, a["href"])

        if urlparse(href).netloc == domain:
            internal += 1
        else:
            external += 1

        links.append(href)

    data["links"] = json.dumps(links)

    data["internal_links"] = internal
    data["external_links"] = external

    images = []

    for img in soup.find_all("img"):

        images.append({

            "src": img.get("src"),

            "alt": img.get("alt"),

            "loading": img.get("loading")

        })

    data["images"] = json.dumps(images)

    css = []

    for c in soup.find_all("link", rel="stylesheet"):
        css.append(c.get("href"))

    data["css_files"] = json.dumps(css)

    js = []

    for s in soup.find_all("script", src=True):
        js.append(s.get("src"))

    data["js_files"] = json.dumps(js)

    data["forms"] = len(soup.find_all("form"))

    text = soup.get_text(" ")

    data["emails"] = json.dumps(
        list(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)))
    )

    data["phones"] = json.dumps(
        list(set(re.findall(r"\+?\d[\d\-\s]{7,}\d", text)))
    )

    social = []

    for l in links:

        if any(x in l for x in [
            "facebook",
            "twitter",
            "linkedin",
            "instagram",
            "youtube",
            "github",
            "t.me"
        ]):
            social.append(l)

    data["social_links"] = json.dumps(social)

    words = re.findall(r"\w+", text.lower())

    data["word_count"] = len(words)

    data["html_hash"] = hashlib.sha256(response.text.encode()).hexdigest()

    og = {}

    for tag in soup.find_all("meta", property=True):

        if tag["property"].startswith("og:"):

            og[tag["property"]] = tag.get("content")

    data["open_graph"] = json.dumps(og)

    twitter = {}

    for tag in soup.find_all("meta", attrs={"name": True}):

        if tag["name"].startswith("twitter:"):

            twitter[tag["name"]] = tag.get("content")

    data["twitter_cards"] = json.dumps(twitter)

    ld = []

    for script in soup.find_all(
        "script",
        attrs={"type": "application/ld+json"}
    ):
        ld.append(script.string)

    data["json_ld"] = json.dumps(ld)

    robots = requests.get(
        urljoin(response.url, "/robots.txt"),
        headers=headers,
        timeout=5
    )

    data["robots_exists"] = robots.status_code == 200

    sitemap = requests.get(
        urljoin(response.url, "/sitemap.xml"),
        headers=headers,
        timeout=5
    )

    data["sitemap_exists"] = sitemap.status_code == 200

    return data