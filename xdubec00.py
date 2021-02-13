import sys
import socket
import json

'''
Funkcia shouldStrip(data) vrati: True, ak je v prijatych datach navratovy kod znaciaci uspech.
                               : False, ak neocakavany navratovy kod / kod znaciaci chybu.
Niektore navratove kody maju specificky chybovy vypis.                               

'''
def shouldStrip(received):
    responses = [["200 OK", True], ["401 Unauthorized", False], ["404 Not Found", False]]
    for i in range(3):
        retIndex = received.find(responses[i][0], 0, 25)
        if (retIndex != -1):
            if (i != 0):
                print("Error: %s" % (responses[i][0]))
            return responses[i][1]
    print("Error in server response.")    
    return False #V odpovedi nieje "200 OK", vraciam False.

'''
Funkcia stripToJson(data) najprv skusi najst index zaciatku suboru json,
potom ho ulozi do premennej, bez zbytocneho balastu, ktory sa povodne nachadzal v odpovedi.
'''

def stripToJson(readdata): 
    try:                
        JSONstart = readdata.index('{') 
        readdata = json.loads(readdata[JSONstart:])
    except:
        print("Error occured while loading json file.")
        exit(1)
    return readdata            

'''
Funkcia printData(data) vypisuje ziadane informacie o pocasii zo slovniku. (dictionary)
'''
def printData(dictionary): 
    try:                    
        print("Cityname: %s" % dictionary["name"])
        print("Weather: %s" % dictionary["weather"][0]["description"])
        print("Temperature: %s \xb0C" % dictionary["main"]["temp"]) 
        print("Humidity: %s %%" % dictionary["main"]["humidity"])
        print("Pressure: %s hPa" % dictionary["main"]["pressure"])      
        print("Wind-speed: %.2f km/h" % (3.6*(dictionary["wind"]["speed"]))) 
        if ("deg" in dictionary["wind"]):
            print("Wind-degree: %d" % dictionary["wind"]["deg"])
        else:
            print("Wind-degree: - ")
    except:
        print("Error while printing information about this city!")
        exit(1)

'''
V main() prebieha kontrola spravneho poctu argumentov (ak nespustam cez make run, napr na Windows, tak ma vyznam).
Pokracujem na nacitanie argumentov, vytvorim poziadavku, vytvorim socket a naviazem spojenie s HOSTom.
Poslem poziadavku, prijmem a skontrolujem odpoved, vypisem ziadanie informacie.
'''
      
def main():
    HOST = "api.openweathermap.org"
    PORT = 80
    argc = len(sys.argv)    
    if (argc == 3):         
        try:                
            api_key = sys.argv[1]
            city = sys.argv[2] #poziadavka je enkodovany retazec b -> byte
            request = b"GET /data/2.5/weather?q=" + city.lower().encode() + b"&APPID=" + api_key.encode() + b"&units=metric HTTP/1.1\r\nHost: api.openweathermap.org\r\n\r\n"
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #pouzivam with, aby som nemusel po skonceni volat s.close()
                s.connect((HOST, PORT)) 
                s.sendall(request) 
                data = s.recv(1024).decode('utf-8')
                if ((shouldStrip(data)) == True): #funkcia vrati True, ak sa v odpovedi(data) nachadza navratovy kod pre uspesny nalez mesta
                    data = stripToJson(data)      #funkcia ulozi do data json
                else:
                    return 1
    
        except: 
            print("An error ocurred while loading arguments.\n")
            exit(1)
    
    else:
        print("Wrong number of arguments! (Should be 3, is %d)" % argc)
        exit(1)
        
    printData(data)
    return 0

if __name__ == '__main__':
    main()

