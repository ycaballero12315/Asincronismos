import requests
import re as re

html:str = ''

url:str = 'https://www.apple.com/es/shop/buy-mac/macbook-air'

response = requests.get(url)

if response.status_code == 200:
    print('Exitos!!!')
    html = response.text
    pattern = r'<span class="rc-prices-fullprice" data-autom="full-price">([^<]+)</span>' 

    mach_patter = re.findall(pattern, html, re.S)

    if mach_patter:
        for elem in mach_patter:
            precio = elem.strip()
            precio = ''.join(c for c in precio if c.isdigit() or c in '.,')
            precio = precio.replace('$', ' ').replace('€', ' ').replace(',', ' ')
            print(precio)
    else:
        patt = f'<span[^>]*class="[^"]*price[^"]*"[^>]*>([^<]+)</span>'
        mach_patter_other = re.findall(patt,html, re.S)
        print('Aplicando otros patrones')
        if mach_patter_other:
            for elem in mach_patter_other[:5]:
                print(elem.strip())

else:
    print("Error en la carga de la requests")


