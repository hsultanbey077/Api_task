import json

from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
from fastapi import FastAPI
app = FastAPI()
m = '{"fullname":"George","characteristics":{"sex":"male","age":27},"skills":["smart","strong"],"experience":[{"position":"developer","workplace":"netflix","salary":"7000"},{"position":"engineer","workplace":"facebook","id_card":56117,"Country":"Scotland"}]}'

@app.get("/my-first-api")
def to_xml(data1):
    data = readfromstring(data1)
    return json2xml.Json2xml(data, item_wrap=False).to_xml()






