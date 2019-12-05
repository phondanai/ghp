# -*- coding: utf-8 -*-
import csv
from collections import defaultdict
from pprint import pprint

from jinja2 import Environment, PackageLoader, select_autoescape


def get_data():
    DATA_FILE = 'data.csv'

    per_tag = defaultdict(list)

    with open(DATA_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for title, uri, tags in reader:
            per_tag[tags].append([title, uri])

    return per_tag


env = Environment(
    loader=PackageLoader("web")#, autoescape=select_autoescape(["html", "xml"])
)

template = env.get_template("index.html")
#print(template.render(data=get_data()))
with open("dist/index.html", 'w') as f:
    f.write(template.render(data=get_data()))


