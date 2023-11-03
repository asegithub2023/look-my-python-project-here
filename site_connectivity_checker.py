
#Importing module for making HTTP requests
import urllib.request as urllib

def check_site(url):
    print("checking connectivity")
    # Opening the provided URL and storing the response
    response=urllib.urlopen(url)
    print("Connected to",url,"succesfully")
    # Retrieving response code from the HTTP response
    print("The reponse code was:",response.getcode())


print("This is site connetivity checker in python\n")
input_url=input("enter url of your site?: ")
check_site(input_url)
