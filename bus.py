from urllib import request
from xml.etree.ElementTree import parse
import webbrowser

class busTracker():

    def openAPI(self , urlLink):
        u = request.urlopen(urlLink)
        data = u.read()
        f = open('rt22.xml','wb')
        f.write(data)        
        f.close()
        print ("sucessfully exported")

    def parseDoc(self):
        #f = open('rt22.xml','r')
        doc = parse ('rt22.xml')
        for bus in doc.findall('bus'):
            d = bus.findtext('d')
            lat = float (bus.findtext('lat'))
            print (d)
            print (lat)

websiteLink = 'http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22'
my_obj = busTracker()
my_obj.openAPI(websiteLink)
my_obj.parseDoc()

# Open google map
# mapURL ='https://www.google.com/maps'
# webbrowser.open(mapURL)
