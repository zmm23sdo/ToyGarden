import requests
import json


def getXlinex(offsetnumber,limitnumber):
    url_xlinex = "https://api.xilnex.com/logic/v2/items?offset="+offsetnumber+"&limit="+limitnumber

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

def searchCategory(categoryname):
   url_category_name = "https://gateway-tg-test.chunsutech.com/admin/categories/name?name="+categoryname

   payload_category_name={}
   headers_category_name = {
      'X-Tester': '1',
      'X-Tenant-Type': 'admin',
      'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)'
   }

   response_category_name = requests.request("GET", url_category_name, headers=headers_category_name, data=payload_category_name)
   list_response_category_name = response_category_name.json()
   # print(response_category_name.text)
   return list_response_category_name


def createCategory(categoryname,parentId):
    url_category = "https://gateway-tg-test.chunsutech.com/admin/category"
    headers_category = {'X-Tester': '1', 'Content-Type': 'application/json'}
    payload_category = json.dumps({
            "spuNo": [],
            "name": categoryname,
            "enableCategory": False,
            "parentId": parentId,
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

# def createProduct(productname,categoryname,skucode,categories_id):

   

def list_create(offsetnumber,limitnumber):
   list_Xlinex = getXlinex(offsetnumber = offsetnumber, limitnumber = limitnumber)
   count = 0
   for i in list_Xlinex:
      productname = i['itemName']
      categoryname = i['brand']
      skucode = i['itemCode']
      count += 1

      print(f'productname:{productname}')
      print(f'categoryname:{categoryname}')
      print(f'skucode:{skucode}')
   
      #  Search categroy with categroyname
      list_response_category_name = searchCategory(categoryname)
      # print(f'list_response_category_name:{list_response_category_name}')

      categroies_data = list_response_category_name['categories']
      # print(f'categroies_data:{categroies_data}')
      if categroies_data == []:
         create_category = createCategory(categoryname,24)
         print(f'create_category:{create_category,create_category.json()}')
         categories_id = str(create_category.json()['id'])
         print(f'categories_id:{categories_id}')
      else:
         categories_id = categroies_data[0]['id']
         print(f'categories_id:{categories_id}')

      url = "https://gateway-tg-test.chunsutech.com/admin/product"
      payload = json.dumps({
            "userId": "1",
            "name": productname,
            "preSaleEnd": {
         "seconds": 20,
         "nanos": 10
      },
            "preSaleRate": 57,
            "overbook": False,
            "balanceStart": {
         "seconds": 20,
         "nanos": 10
      },
               "pic": [],
            "deliveryType": 1,
            "upSellsIds": [
               59
            ],
            "deliveryDay": 20,
            "balanceEnd": {
         "seconds": 20,
         "nanos": 10
      },
            "location": "voluptate",
            "preSaleStart": {
         "seconds": 20,
         "nanos": 10
      },
         "preSaleAmount": 65,
         "sizeX": 64,
         "transPrice": 80,
         "describe": "non",
         "isPublish": False,
         "locationId": 85,
         "templateId": 0,
         "relatedItemIds": [
            79
         ],
         "specs": [
         ],
         "spu": skucode,
         "crossSellIds": [
            63
         ],
         "sku": [
            {
               "adminSku": skucode,
               "variations": [],
               "stock": 79,
               "barCode": "57",
               "weight": 73,
               "pic": [],
               "price": 45
            }
         ],
         "sizeY": 85,
         "sizeZ": 1,
         "preSale": False,
         "categoryIds": [
            categories_id
            
         ]
      })
      headers = {
         'X-Tester': '1',
         'Content-Type': 'application/json'
      }

      response_createproduct = requests.request("POST", url, headers=headers, data=payload)
      print(f'Number={count}','@'*100)
      print(f'response_createproduct:{response_createproduct,response_createproduct.json()},success!','\n','='*100)
      # break

# list_create(offsetnumber = "0",limitnumber = "1")
# print(f'调试','='*100)

# list_create(offsetnumber = "0",limitnumber = "1000")
# print("0-1000","#"*100)
# pass
# list_create(offsetnumber = "1000",limitnumber = "1000")
# print("1000-1000","#"*100)
# pass
# list_create(offsetnumber = "2000",limitnumber = "1000")
# print("2000-1000","#"*100)
# pass
# list_create(offsetnumber = "3000",limitnumber = "1000")
# print("3000-1000","#"*100)
# pass
# list_create(offsetnumber = "4000",limitnumber = "1000")
# print("4000-1000","#"*100)
# pass
# list_create(offsetnumber = "5000",limitnumber = "1000")
# print("5000-1000","#"*100)
# pass
# list_create(offsetnumber = "6000",limitnumber = "1000")
# print("6000-1000","#"*100)



