import requests
import json
import import_product

list_Xlinex = import_product.getXlinex(limitnumber = "1")
for i in list_Xlinex:
   productname = i['itemName']
   categoryname = i['brand']
   skucode = i['itemCode']

   print(f'productname:{productname}')
   print(f'categoryname:{categoryname}')
   print(f'skucode:{skucode}')

#  #  Category List 
   response_categories = import_product.getCategories()
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
         create_category = import_product.createCategory()
         print(f'create_category:{create_category}')
         response_categories = import_product.getCategories()
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
