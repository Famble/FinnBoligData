#! /usr/bin/python

#from bs4 import BeautifulSoup
import bs4, requests    

def main():
    res = requests.get("https://www.finn.no/realestate/homes/ad.html?finnkode=220868018") #enebolig
    #res = requests.get("https://www.finn.no/realestate/homes/ad.html?finnkode=252913381")  #leilighet

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    content = soup.find('div', {'class':'u-word-break'})
    content.div.decompose()
    
    #Fetch address
    address = content.find('p',{'class':'u-caption'}).next
    print(address)


    #------Fetch money data from the ad-------
    panels = content.select('.panel')
    data = panels[1:4]
    #print(len(data[0].select('dt')))
    #print(data[0])

    ad_data = {} #Array containing all the money related values
    ad_data['prisantydning'] = data[0].select('span')[1].next

    #Looping over the needed values
    for i in range(len(data[0].select('dt'))):
        ad_data[str(data[0].select('dt')[i].next).lower()] = data[0].select('dd')[i].next
        #ad_data['fellesgjeld'] = data[0].select('dd')[0].next
        #ad_data['omkostninger'] = data[0].select('dd')[1].next
        #ad_data['totalpris'] = data[0].select('dd')[2].next
        #ad_data['felleskost'] = data[0].select('dd')[3].next

    for tall in ad_data:
        ad_data[tall] = cleanCurrencyFromWeb(ad_data[tall])
    #print(ad_data)

    
    dimensions = content.find('dl', {'class':'definition-list definition-list--cols1to2'})

    dimensions_data = {}
    dimensions_headers = dimensions.select('dt')
    dimensions_len = len(dimensions.select('dt'))
    #print(dimensions.select('dt'))

    for i in range(dimensions_len):
            if(str(dimensions.select('dt')[i].next).lower()=='energimerking'):
                dimensions_data[str(dimensions.select('dt')[i].next).lower()] = dimensions.select('dd')[i].div.next.strip().replace(' -','')
            else:
                dimensions_data[str(dimensions.select('dt')[i].next).lower()] = dimensions.select('dd')[i].next.strip().replace(' m²','').replace(u'\xa0', u'')
    print(dimensions_data)
    #END--------------Main-----------------

def cleanCurrencyFromWeb(data):
    return data.get_text().strip().replace(" kr","").replace(" per år","").replace(u'\xa0', u'')

if __name__ == '__main__':
    main()