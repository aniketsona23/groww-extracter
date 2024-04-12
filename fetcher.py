import requests
import json



def fetch_company_data(company):
    company = "-".join(map(lambda word: word.lower(),company.split(" ")))
    d = requests.get("https://groww.in/stocks/"+company)
    p=requests.get(f"https://groww.in/stocks/{company}/share-holding")
    promoters  = float(p.text.split('"promoters":{"individual":{"percent":')[-1].split("}")[0])
    data = json.loads((d.text.split('<script id=')[1].split('"stats":')[1].split(',"fundamentals":')[0]))
    data['promotersPerc'] = promoters
    return data

def just_fetch(company):
    company = "-".join(map(lambda word: word.lower(),company.split(" ")))
    p = requests.get("https://groww.in/stocks/"+company)
    return p.text

print(just_fetch("Coforge Ltd."))

