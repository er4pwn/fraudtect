import ssl
import socket
import colorama
from colorama import Fore
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from tqdm import tqdm
import time


def check_ssl_legitimacy_code1(website_url):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((website_url, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=website_url) as ssock:
                cert = ssock.getpeercert()

                issuer = dict(x[0] for x in cert['issuer'])
                subject = dict(x[0] for x in cert['subject'])
                valid_from = cert['notBefore']
                valid_until = cert['notAfter']

                print(f"Issuer: {issuer}")
                print(f"Subject: {subject}")
                print(f"Valid From: {valid_from}")
                print(f"Valid Until: {valid_until}")

        print(Fore.GREEN + "Website SSL certificate appears to be legitimate.")

    except ssl.SSLError as e:
        return f"SSL Error: {e.strerror}"

    except socket.error as e:
        return f"Socket Error: {e.strerror}"
ascii_art = '''

+-----------------------------------------------------+
| A fraud website detector that scans SSL Certificate |  
+-----------------------------------------------------+

$$$$$$$$\                                 $$\ $$$$$$$$\                    $$\     
$$  _____|                                $$ |\__$$  __|                   $$ |    
$$ |    $$$$$$\  $$$$$$\  $$\   $$\  $$$$$$$ |   $$ | $$$$$$\   $$$$$$$\ $$$$$$\   
$$$$$\ $$  __$$\ \____$$\ $$ |  $$ |$$  __$$ |   $$ |$$  __$$\ $$  _____|\_$$  _|  
$$  __|$$ |  \__|$$$$$$$ |$$ |  $$ |$$ /  $$ |   $$ |$$$$$$$$ |$$ /        $$ |    
$$ |   $$ |     $$  __$$ |$$ |  $$ |$$ |  $$ |   $$ |$$   ____|$$ |        $$ |$$\ 
$$ |   $$ |     \$$$$$$$ |\$$$$$$  |\$$$$$$$ |   $$ |\$$$$$$$\ \$$$$$$$\   \$$$$  |
\__|   \__|      \_______| \______/  \_______|   \__| \_______| \_______|   \____/ 

Coded by Mark Rhogie Purok | www.github.com/jihyoppa
'''
print(Fore.RED + ascii_art)
def check_ssl_legitimacy_code2(website_url, legitimate_website_url):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((website_url, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=website_url) as ssock:
                cert = ssock.getpeercert()

        with socket.create_connection((legitimate_website_url, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=legitimate_website_url) as ssock:
                legitimate_cert = ssock.getpeercert()

        if cert['issuer'] == legitimate_cert['issuer'] and cert['subject'] == legitimate_cert['subject']:
            print(f"Issuer: {cert}")
            print(f"Subject: {legitimate_cert}")
            print(Fore.GREEN + "Website SSL certificate appears to be legitimate.")
        else:
            return "Website SSL certificate does not match the legitimate website."

    except ssl.SSLError as e:
        return f"SSL Error: {e.strerror}"

    except socket.error as e:
        return f"Socket Error: {e.strerror}"

choice = int(prompt("Choose 1 if you want to detect fraud websites by scanning SSL Certificate | Choose 2 if you want to compare legitimate and not legitimate webssites: ", style=Style.from_dict({'prompt': '#0000ff bold'})))
website_url = prompt("Enter the website URL to check: ", style=Style.from_dict({'prompt': '#0000ff bold'}))

if choice == 1:
    with tqdm(total=100) as pbar:
        for i in range(10):
            time.sleep(0.5)  
            pbar.update(10)
    result = check_ssl_legitimacy_code1(website_url)
elif choice == 2:
    legitimate_website_url = prompt("Enter the URL of the legitimate website: ", style=Style.from_dict({'prompt': '#0000ff bold'}))
    with tqdm(total=100) as pbar:
        for i in range(10):
            time.sleep(0.5)  
            pbar.update(10)
    result = check_ssl_legitimacy_code2(website_url, legitimate_website_url)
else:
    result = "Invalid choice. Please select either 1 or 2."

print(result)
