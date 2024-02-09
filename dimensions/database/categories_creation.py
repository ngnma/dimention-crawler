import requests
import json
import pandas as pd 
import numpy as np


# categories

url = "https://app.dimensions.ai/browse/categories/publication/for.json?or_facet_publication_type=article"

payload = {}
headers = {
  'Accept': 'application/json',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cache-Control': 'no-cache, no-store, must-revalidate',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json',
  'Cookie': 'intercom-device-id-ilx5k1fm=99edab8a-a6ab-47e3-bc44-070b8257d181; _gcl_au=1.1.1416844146.1707413904; aws-waf-token=7ac190f2-7850-4639-b888-1b60ef0a6171:EQoArSCGj+gJAAAA:kOk/PyXF4Kv75o/biH8ROPm06R/USaobDdV5LJA/9Nh4QR95hnsm4rTI1WIpTDAjDnNJ5mEH7mF0PERX++UXSop6DT+fZxZlXL64D3VAt+3ndFc2tI0wJVAquDGq0QeJWdzgNBATYuDc3Behxb+PWR1OzGV76ePdCcDeOvd2B/KDnc81/+9x5+gjc0jeg4wEnCoBcrbg7Pgwv7IBB9gpUpQ7RrSV0UOByTPD4PyTyrcUcDwhg267eLqe; _ga=GA1.1.1098850320.1707419421; OptanonAlertBoxClosed=2024-02-08T19:10:23.090Z; intercom-session-ilx5k1fm=OUhFbjNVMk94dE1wTnd1Q1dZZ29kSVYxUEpBbjBlSDFkeFk3V041WER0amZmVjQwRklNQ3JOeTF0Z0diRUYzMS0tMHBiR3lKaHRZRGRDZ0FkR21JVVlMdz09--1b4be3a144fda967ae026d7857995995a689701b; _ga_KH7CX71Y5X=GS1.1.1707419421.1.1.1707419475.0.0.0; _ga_Y26MGCNDNL=GS1.1.1707497562.1.1.1707498194.0.0.0; uber_auth_tkt=9ba3ef78ad83406150ebbfd2f74571406c00b35d4551925574f1d835899240ecd2c480fc2f795054935d800a7306237ce544d09899c54d95ec530f5c2ba27f6265c65f48YWFjYzk4MThAZ21haWwuY29t!A7f47b3516942805735b71d30590c7a!userid_type:b64unicode; uber_auth_tkt=9ba3ef78ad83406150ebbfd2f74571406c00b35d4551925574f1d835899240ecd2c480fc2f795054935d800a7306237ce544d09899c54d95ec530f5c2ba27f6265c65f48YWFjYzk4MThAZ21haWwuY29t!A7f47b3516942805735b71d30590c7a!userid_type:b64unicode; session=BWb3Mbt9j_4Xt1Ic76vpaQI_9CQ_rPYdLkMZojCS5t_iuFCScviRuZotplUpML_qtb4S337PrQF_SbRAL5IFQFsxNzA3NTA2ODUxLCAxNzA3NDk5MzIxLjI4Mjc2NjgsIHsiYXV0aGVudGljYXRpb24iOiBudWxsLCAiX2NzcmZ0XyI6ICIyYjEzYTE3MGZjODUwMjIzOWM5MTdmNDFkZjk0MWI4Y2ZjNTc2ZTRhIiwgImF1dGhfbWV0aG9kIjogImRpbWVuc2lvbnMifV0; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Feb+09+2024+22%3A57%3A37+GMT%2B0330+(Iran+Standard+Time)&version=202401.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=6140ce0d-5f43-490a-afcc-537d77783362&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0&AwaitingReconsent=false&geolocation=NL%3BUT; session=n3O8m15axkMp6XrG9vXhV_vOeCH2rOiO9XL1ZQMVb-d-tzMLywWBt4vQxD6SKpYkvcAxjaD3HZIciGM9vUrWFlsxNzA3NTEwMjg1LCAxNzA3NDczMzk4LjA4NDEwODYsIHsiYXV0aGVudGljYXRpb24iOiBudWxsLCAiX2NzcmZ0XyI6ICIwMjZkZTJmNzY3MWNiOWJmZjg5MWZlMWI4OGE0NWFmOWZhNzI0OTEwIiwgImF1dGhfbWV0aG9kIjogImRpbWVuc2lvbnMifV0',
  'Expires': '0',
  'Operations': 'sticky=vEa8b9UFoPTOzKBQuOIXw4cupqbrouYxJ2zZNEie',
  'Pragma': 'no-cache',
  'Referer': 'https://app.dimensions.ai/discover/publication?or_facet_year=2023&or_facet_publication_type=article&or_facet_journal_list=UGC%20Journal%20List%20Group%20II&or_facet_source_title=jour.1045337&or_facet_open_access_status=gold&and_facet_for=80013&and_facet_for=80141',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
  'X-CSRF-Token': '2b13a170fc8502239c917f41df941b8cfc576e4a',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

response = requests.request("GET", url, headers=headers, data=payload)
data = response.json().get('data').get('groups')

supertypes = list()
subcats = list()

for s in data:
    s_id = s.get('id')
    var_dict = {'id':s_id, 'code':s.get('code'), 'name':s.get('name')}
    supertypes.append(var_dict)

    for c in s.get('members'):
        var_dict = {'id':c.get('id'), 'code':c.get('code'), 'name':c.get('name'), 'supertype_id':s_id}
        subcats.append(var_dict)

subcats = pd.DataFrame(subcats)
supertypes = pd.DataFrame(supertypes)
supertypes.to_csv('supertypes.csv',index = False)
subcats.to_csv('subcats.csv',index = False)


# access
access = list(['gold','hybrid','bronze','green','oa_all','closed'])
pd.DataFrame(access,columns=['name']).to_csv('access.csv',index=False)

# years 
pd.DataFrame(list(np.arange(start=1665,step=1,stop=2024)), columns=['year']).to_csv('years.csv',index=False)

# journals (minus 13 milion)
journal_lists = list(['UGC%20Journal%20List%20Group%20II','ERA%202023','ERA%202018','ERA%202015','Norwegian%20register%20level%201','VABB-SHW','PubMed','Norwegian%20register%20level%202','DOAJ','ERIH%20PLUS','Non-APC%20journals','J-STAGE','Nature%20Index%20journals','Norwegian%20register%20level%200','SciELO','UGC%20Journal%20List%20Group%20I'])
pd.DataFrame(journal_lists,columns=['journal']).to_csv('journals.csv',index = False)

