#! /usr/bin/python

import bs4, requests   
res = requests.get("https://www.finn.no/realestate/homes/ad.html?finnkode=163195475")
soup = bs4.BeautifulSoup(res.text)
content = soup.find('div', {'class':'u-word-break'})
content.div.decompose()
panels = content.select('.panel')
data = panels[1:4]


ad_data = {}
#prisantydning
ad_data['prisantydning'] = (data[1].div).select('span')[1]
ad_data['fellesgjeld'] = (data[1].div).select('dd')[0]
ad_data['omkostninger'] = (data[1].div).select('dd')[1]
ad_data['totalpris'] = (data[1].div).select('dd')[2]
ad_data['felleskost'] = (data[1].div).select('dd')[3]

for tall in ad_data:
    if tall == 'prisantydning':
        ad_data[tall] = (data[1].div).select('span')[1].text.strip().replace(" kr","")
        #ad_data[tall] = (data[1].div).select('span')[1].text.strip().encode('utf-8', 'ignore').replace(" kr","")
    else:
        ad_data[tall] = ad_data[tall].get_text().strip().replace(" kr","")
        #ad_data[tall] = ad_data[tall].get_text().strip().encode('utf-8', 'ignore').replace(" kr","")


ad_data['bolig-data-head'] = data[2].dl.select('dt')
ad_data['bolig-data-data'] = data[2].dl.select('dd')



for i in range(len(ad_data['bolig-data-head'])):
    ad_data['bolig-data-head'][i] = data[2].dl.select('dt')[i].text.strip
    ad_data['bolig-data-head'][i][0] = data[2].dl.select('dd')[i].text.strip()

print(ad_data['bolig-data-data'])