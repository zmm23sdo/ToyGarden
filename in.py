import requests
import json

url = "https://api.xilnex.com/logic/v2/items?offset=0&limit=1"

payload={}
headers = {
   'User-Agent': 'apifox/1.0.0 (https://www.apifox.cn)',
   'appid':'ANzfahPCyX0IjsigpNoF8r0kpbm8jI8A',
   'auth':'5',
   'token':'v5_F3IsqxHzZoELrwApg2x/Q44VZuolGAASl7qeGQuBuyg='
}

response = requests.request("GET", url, headers=headers, data=payload)



for i in response.json()['data']['items']:
   print(i['itemName'])
   print(i['brand'])
   print(i['itemCode'])
   url = "https://gateway-tg-test.chunsutech.com/admin/product"
   payload = json.dumps({
      "userId": "1",
      "name": i['itemName'],
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
      "pic": [
         {
            "path": "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"
         }
      ],
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
      "templateId": 73,
      "relatedItemIds": [
         79
      ],
      "specs": [
         {
            "specInfo": [
               {
                  "id": 48,
                  "val": "adipisicing reprehenderit magna consectetur"
               },
               {
                  "id": 37,
                  "val": "cillum voluptate aliquip"
               }
            ],
            "setId": 21
         },
         {
            "setId": 13,
            "specInfo": [
               {
                  "id": 53,
                  "val": "ad exercitation elit sint aliqua"
               }
            ]
         },
         {
            "setId": 49,
            "specInfo": [
               {
                  "id": 15,
                  "val": "consectetur occaecat ut est"
               }
            ]
         },
         {
            "specInfo": [
               {
                  "id": 26,
                  "val": "adipisicing irure sit nisi"
               },
               {
                  "id": 42,
                  "val": "Ut"
               },
               {
                  "val": "ut fugiat",
                  "id": 94
               },
               {
                  "val": "sed nisi adipisicing sit",
                  "id": 45
               }
            ],
            "setId": 55
         },
         {
            "setId": 15,
            "specInfo": [
               {
                  "id": 64,
                  "val": "sunt cillum deserunt"
               },
               {
                  "id": 32,
                  "val": "consectetur aliqua sed"
               },
               {
                  "val": "proident labore",
                  "id": 34
               },
               {
                  "val": "labore",
                  "id": 73
               }
            ]
         }
      ],
      "spu": "commodo ut amet",
      "crossSellIds": [
         63
      ],
      "sku": [
         {
            "adminSku": i['itemCode'],
            "variations": [],
            "stock": 79,
            "barCode": "57",
            "weight": 73,
            "pic": [],
            "price": 45
         },
         {
            "adminSku": "nulla aliqua fugiat consequat",
            "barCode": "13",
            "price": 25,
            "stock": 37,
            "weight": 62,
            "pic": [{
            "path": "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"
         }],
            "variations": []
         },
         {
            "weight": 33,
            "barCode": "17",
            "variations": [],
            "adminSku": "ipsum qui laborum",
            "pic": [{
            "path": "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"
         }],
            "stock": 35,
            "price": 51
         },
         {
            "adminSku": "occaecat in aliquip",
            "price": 37,
            "variations": [],
            "pic": [{
            "path": "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"
         }],
            "stock": 73,
            "barCode": "26",
            "weight": 47
         },
         {
            "variations": [],
            "pic": [{
            "path": "https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"
         }],
            "barCode": "91",
            "adminSku": "dolore aliqua voluptate ullamco",
            "stock": 60,
            "weight": 3,
            "price": 53
         }
      ],
      "sizeY": 85,
      "sizeZ": 1,
      "preSale": False,
      "categoryIds": [
         "2",
         "82",
         "83",
         "49"
      ]
   })
   headers = {
      'X-Tester': '1',
      'Content-Type': 'application/json'
   }

   response = requests.request("POST", url, headers=headers, data=payload)

   print(response.json())
   print(response.text)
