#Importing required libraries for this project
from bs4 import BeautifulSoup
import urllib.request


#url to scrap from
urlpage='https://www.secondechance.org/animal/chat-europeen-feerie-343620'

urlpagearray= ['https://www.secondechance.org/animal/chat-europeen-feerie-343620','https://www.secondechance.org/animal/lapin-race-indefinie-emma-916136','https://www.secondechance.org/animal/lapin-race-indefinie-lupin-910870', 'https://www.secondechance.org/animal/lapin-race-indefinie-lea-916134','https://www.secondechance.org/animal/lapin-race-indefinie-valou-916125','https://www.secondechance.org/animal/lapin-race-indefinie-adora-916137']

i=0
while i<len(urlpagearray): #Make it loop as many time as we have things in our array.
    page = urllib.request.urlopen(urlpagearray[i]) #Query webpage corresponding to the array and stock it under variable 'page'


    #analyse the webpage with BeautifulSoup4 and store it under a variable named 'soup'. Soup seems to be the way to name it, according to the web.
    soup = BeautifulSoup(page,  'html.parser')
    #Searching to see if we can find the contact shelter id in the page
    contact = soup.find(id="email-contact-shelter")
    name = soup.h1.get_text()

    # Trying to get the text contained inside the email contact shelter id
    try:
        calling = contact.get_text()
        if 'Ecrire au refuge' in calling:
            print(name +' est disponible au lien suivant :', urlpagearray[i])
        elif contact == 'None' or 'Ecrire au refuge' not in calling:
            print('Non disponible')

    except AttributeError: # If the id we're searching for isn't found on the website,
        house = soup.find(id="bs-callout")
        print(name +" est non disponible sur la page: " + urlpagearray[i])
    i+=1

