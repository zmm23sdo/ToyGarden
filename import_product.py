import requests
import json

def getXlinex(limitnumber):
    url_xlinex = "https://api.xilnex.com/logic/v2/items?offset=0&limit="+limitnumber

    payload_xlinex={}
    headers_xlinex = {
    'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)',
    'appid':'ANzfahPCyX0IjsigpNoF8r0kpbm8jI8A',
    'auth':'5',
    'token':'v5_F3IsqxHzZoELrwApg2x/Q44VZuolGAASl7qeGQuBuyg='
    }

    response_xlinex = requests.request(
        "GET", 
        url_xlinex, 
        headers=headers_xlinex, 
        data=payload_xlinex)
    list_response_xlinex = response_xlinex.json()['data']['items']
    return list_response_xlinex

def getCategories():
    url_categories = "https://gateway-tg-test.chunsutech.com/admin/categories"
    payload_categories={}
    headers_categories = {'X-Tester': '1', 'Content-Type': 'application/json'}
    response_categories = requests.request(
        "GET", 
        url_categories, 
        headers=headers_categories, 
        data=payload_categories)
    list_response_categories = response_categories.json()['categories']
    return list_response_categories

def createCategory(categoryname):
    url_category = "https://gateway-tg-test.chunsutech.com/admin/category"
    headers_category = {'X-Tester': '1', 'Content-Type': 'application/json'}
    payload_category = json.dumps({
            "spuNo": [],
            "name": categoryname,
            "enableCategory": False,
            "parentId": 24,
            "pic": "http://dummyimage.com/400x400",
            "menuType": "Menu",
            "isMenu": False
         })
    response_category = requests.request(
            "POST", 
            url_category, 
            headers=headers_category, 
            data=payload_category)
    return response_category
