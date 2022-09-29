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



list_Xlinex = getXlinex(limitnumber = "1")
for i in list_Xlinex:
   productname = i['itemName']
   categoryname = i['brand']
   skucode = i['itemCode']

   print(f'productname:{productname}')
   print(f'categoryname:{categoryname}')
   print(f'skucode:{skucode}')

#  #  Category List 
   response_categories = getCategories()
   print(f'response_categories:{response_categories}')
#  #  get Category_id & Category_name
   list_categories = {}
   for j in response_categories:
      # print(j['name'])
      # print(j['id'])
      list_categories[j['name']]=j['id']
   print(f'list_categories:{list_categories}')
#  #  if else Category had been exited
   for k in list_categories:
      if k == categoryname:
         categories_id = list_categories[k]
         print(f"categories_id:{categories_id}")
      else:
         create_category = createCategory(categoryname)
         print(f'create_category:{create_category,create_category.json()}')
         response_categories = getCategories()
         print(f'response_categories:{response_categories}')
         

         


   

# #    url = "https://gateway-tg-test.chunsutech.com/admin/product"
# #    payload = json.dumps({
# #       "userId": "1",
# #       "name": i['itemName'],
# #       "preSaleEnd": {
# #     "seconds": 20,
# #     "nanos": 10
# #   },
# #       "preSaleRate": 57,
# #       "overbook": False,
# #       "balanceStart": {
# #     "seconds": 20,
# #     "nanos": 10
# #   },
# #       "pic": [
# #          {
# #             "path": "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"
# #          }
# #       ],
# #       "deliveryType": 1,
# #       "upSellsIds": [
# #          59
# #       ],
# #       "deliveryDay": 20,
# #       "balanceEnd": {
# #     "seconds": 20,
# #     "nanos": 10
# #   },
# #       "location": "voluptate",
# #       "preSaleStart": {
# #     "seconds": 20,
# #     "nanos": 10
# #   },
# #       "preSaleAmount": 65,
# #       "sizeX": 64,
# #       "transPrice": 80,
# #       "describe": "non",
# #       "isPublish": False,
# #       "locationId": 85,
# #       "templateId": 73,
# #       "relatedItemIds": [
# #          79
# #       ],
# #       "specs": [
# #       ],
# #       "spu": "commodo ut amet",
# #       "crossSellIds": [
# #          63
# #       ],
# #       "sku": [
# #          {
# #             "adminSku": i['itemCode'],
# #             "variations": [],
# #             "stock": 79,
# #             "barCode": "57",
# #             "weight": 73,
# #             "pic": [{
# #             "path": "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"
# #          }],
# #             "price": 45
# #          }
# #       ],
# #       "sizeY": 85,
# #       "sizeZ": 1,
# #       "preSale": False,
# #       "categoryIds": [
# #          "2",
# #          "82",
# #          "83",
# #          "49"
# #       ]
# #    })
# #    headers = {
# #       'X-Tester': '1',
# #       'Content-Type': 'application/json'
# #    }

# #    response = requests.request("POST", url, headers=headers, data=payload)

# #    print(response.json())
# #    print(response.text)
