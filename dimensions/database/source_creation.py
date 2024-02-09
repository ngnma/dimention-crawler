import requests
import json
import pandas as pd 
url = "https://app.dimensions.ai/viz/data/publication/source_title/aggregated-citations.json?or_facet_publication_type=article&viz-st:aggr=mean"

payload = {}
headers = {
  'Accept': 'application/json',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cache-Control': 'no-cache, no-store, must-revalidate',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json',
  'Cookie': 'intercom-device-id-ilx5k1fm=99edab8a-a6ab-47e3-bc44-070b8257d181; _gcl_au=1.1.1416844146.1707413904; _ga=GA1.1.1098850320.1707419421; OptanonAlertBoxClosed=2024-02-08T19:10:23.090Z; _ga_Y26MGCNDNL=GS1.1.1707497562.1.1.1707498194.0.0.0; intercom-session-ilx5k1fm=RGZER09rMmpFMjlna0RjcWlJcmNmaXI0QnA4Qk9XcVAzOGFZbFRFZ1EwdndvSzR6bkFDM0lxUHdOeEFOVkVGdC0tQ1lRL1UyeVVvRW1mQmtVSnp4RW9oZz09--fa79964d35b160856576c10869311a1071c30b1b; aws-waf-token=fe37ef2f-f227-47e9-b02c-28e13cfdd591:EQoAdtiTsf4CAAAA:qwMeE8QyXyH4ZL8ea0MQeGFNfeM1TDJBq6Uujhm85rjRxqm2HebsPexjRt6kx+MZujWtsSRu7FPLhldC1BVtt3bS2ZODu8xZIsHdwJsm4EDth6XVMxpBruDfTAxKk7yl+USZndF8ivMEPTG0F0Xr/JaklrCIxJzEVpgcLwjMMGarTQIQ7tWD3Vnnwh4ns9koFki3tIeZxTaO1vUafFk6ZjcE7DNuZJV/kbv450OL07bOREiW9AIa9YU5; _ga_KH7CX71Y5X=GS1.1.1707512432.3.0.1707512647.0.0.0; uber_auth_tkt=4f02281fb77889dd70827446e72c53b409535afe6f04a2465267263447b2fe12d841fa13c11165ce7294d6aabfcf642f18761b9f934e52972c3712446984a29665c69356YWFjYzk4MThAZ21haWwuY29t!A7f47b3516942805735b71d30590c7a!userid_type:b64unicode; uber_auth_tkt=4f02281fb77889dd70827446e72c53b409535afe6f04a2465267263447b2fe12d841fa13c11165ce7294d6aabfcf642f18761b9f934e52972c3712446984a29665c69356YWFjYzk4MThAZ21haWwuY29t!A7f47b3516942805735b71d30590c7a!userid_type:b64unicode; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Feb+10+2024+00%3A42%3A56+GMT%2B0330+(Iran+Standard+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=6140ce0d-5f43-490a-afcc-537d77783362&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0&AwaitingReconsent=false&geolocation=NL%3BUT; session=WBdXsyfYBzJBi-jMdZKFm2VMuelYvc9bZJr2_zkTK9NwCplHcX2ed-U-85FFToDDMcRxUzBGisj8irrXpJTIfFsxNzA3NTEzMjEyLCAxNzA3NDk5MzIxLjI4Mjc2NjgsIHsiYXV0aGVudGljYXRpb24iOiBudWxsLCAiX2NzcmZ0XyI6ICJlZTU5NTZiODIyMDJmNzljYWY0MTMwZjQwZWMyNWE3MzRlODM3MzIwIiwgImF1dGhfbWV0aG9kIjogImRpbWVuc2lvbnMifV0; session=uJtBq90fb3VkpvCcsftUN1ecXN2M_jcCS-NSepueUQ8oXU3MTPtK6VYoljhfO5MthESsvCTWnT5jmTn94bz0MlsxNzA3NTEzMjcxLCAxNzA3NDczMzk4LjA4NDEwODYsIHsiYXV0aGVudGljYXRpb24iOiBudWxsLCAiX2NzcmZ0XyI6ICIwMjZkZTJmNzY3MWNiOWJmZjg5MWZlMWI4OGE0NWFmOWZhNzI0OTEwIiwgImF1dGhfbWV0aG9kIjogImRpbWVuc2lvbnMifV0',
  'Expires': '0',
  'Pragma': 'no-cache',
  'Referer': 'https://app.dimensions.ai/analytics/publication/source_title/aggregated?or_facet_publication_type=article',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
  'X-CSRF-Token': 'ee5956b82202f79caf4130f40ec25a734e837320',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}


import pandas as pd 
sources = list()
while True:
   try:
      response = requests.request("GET", url, headers=headers, data=payload)
      data = response.json()
      res = data.get('results')
      for i in res:
         var_dict = {'id':i.get('id'), 'name':i.get('name').get('label')}
         sources.append(var_dict)

      np = data['navigation']['data_json']
      url = f"https://app.dimensions.ai{np}&or_facet_publication_type=article&viz-st:aggr=mean"
   except Exception as err:
        print(err)
        break
   
pd.DataFrame(sources).to_csv('sources.csv',index=False)