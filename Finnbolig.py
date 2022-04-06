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

    for i in range(len(data[0].select('dt'))):
        print(i)
        print(type(str(data[0].select('dt')[i].next).lower()))
        ad_data[str(data[0].select('dt')[i].next).lower()] = data[0].select('dd')[i].next
        #ad_data['fellesgjeld'] = data[0].select('dd')[0].next
        #ad_data['omkostninger'] = data[0].select('dd')[1].next
        #ad_data['totalpris'] = data[0].select('dd')[2].next
        #ad_data['felleskost'] = data[0].select('dd')[3].next

    for tall in ad_data:
        ad_data[tall] = cleanCurrencyFromWeb(ad_data[tall])
    #print(ad_data)

    #ad_data['bolig-data-head'] = data[2].dl.select('dt')
    #ad_data['bolig-data-data'] = data[2].dl.select('dd')



    #for i in range(len(ad_data['bolig-data-head'])):
    #    ad_data['bolig-data-head'][i] = data[2].dl.select('dt')[i].text.strip
    #    ad_data['bolig-data-head'][i][0] = data[2].dl.select('dd')[i].text.strip()

    #print(ad_data['bolig-data-data'])

def cleanCurrencyFromWeb(data):
    return data.get_text().strip().replace(" kr","").replace(" per år","").replace(u'\xa0', u'')

if __name__ == '__main__':
    main()