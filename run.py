# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

#we are importing twilio client
from twilio.rest import Client

# This is a pretty simple script. The script downloads a page, and if it finds some text, emails me.
# If it does not find some text, it waits 60 seconds and downloads the page again.
#where i have used "your email" or "password" etc. replace this with your information.

# while this is true (it is true by default),
while True:
    # set the url as VentureBeat,
    url = "the url of the page you want to monitor"
    # set the headers like we are a browser,
    headers = {'User-Agent': 'Mozilla/5.0'}
    # download the homepage
    response = requests.get(url, headers=headers, timeout=10)
    # parse the downloaded homepage and grab all text, then,
    soup = BeautifulSoup(response.text, "lxml")
    
    # if the number of times the word "Keyword" occurs on the page is less than 1,
    if str(soup).find("Keyword") == -1:
        # wait 60 seconds,
        time.sleep(60)
        # continue with the script,
        continue
        
    # but if the word "Keyword" occurs any other number of times,
    else:
        # create an email message with just a subject line,
        msg = """Subject: Check website

        Your message"""
        # set the 'from' address,
        fromaddr = 'your email address'
        # set the 'to' addresses,
        toaddrs  = ['recipient1@example.com','recipient2@example.com', 'recipient3@example.com']
        
        # setup the email server,
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # add my email account login name and password,
        server.login("email", "password")
        
        # Print the email's contents
        print('From: ' + fromaddr)
        print('To: ' + str(toaddrs))
        print('Message: ' + msg)
        
        # send the email
        server.sendmail(fromaddr, toaddrs, msg)
        # disconnect from the server
        server.quit()
        



        # Your Account Sid and Auth Token from twilio.com/console
        # DANGER! This is insecure. See http://twil.io/secure
        account_sid = 'your twillio account sid'
        auth_token = 'your authentication token'
        client = Client(account_sid, auth_token)

        message = client.messages \
                  .create(
                      body="your text message",
                      from_='twillio number',
                      to='recipient number'
                      )
        print(message.sid) 
                               
        
        break
