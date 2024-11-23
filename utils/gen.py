import requests
import json
import random
import string
import threading
from colorama import Fore, Style, init
from unique_names_generator import get_random_name
from unique_names_generator.data import ADJECTIVES, ANIMALS
# don't skid stupid nigga! add u'r own shit if u like!

init()

def get_proxies():
    proxies = []
    with open("data/proxies.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                proxies.append(line)
    return proxies

def generate_account(proxy=None):

    username = get_random_name(separator='-', style='lowercase', combo=[ADJECTIVES, ANIMALS])

    email = f"{username}@outlook.com"

    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))

    print(Fore.YELLOW + "[" + Fore.GREEN + "+" + Fore.YELLOW + "]" + Fore.MAGENTA + f" created account {username}" + Style.RESET_ALL)

    register_url = "https://funker530-fnc.azurewebsites.net/api/Register?code=sL3mjD-c0BJdI9b9h4s7WhIPU8ca9p6h3yiLyFczS-I9AzFupvbo9g=="
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "582",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarySmaDEz0BcUokuAAb",
        "Host": "funker530-fnc.azurewebsites.net",
        "Origin": "https://funker530.com",
        "Referer": "https://funker530.com/register",
        "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
    }

    data = (
        "------WebKitFormBoundarySmaDEz0BcUokuAAb\r\n"
        f"Content-Disposition: form-data; name=\"Username\"\r\n\r\n{username}\r\n"
        "------WebKitFormBoundarySmaDEz0BcUokuAAb\r\n"
        f"Content-Disposition: form-data; name=\"Email\"\r\n\r\n{email}\r\n"
        "------WebKitFormBoundarySmaDEz0BcUokuAAb\r\n"
        f"Content-Disposition: form-data; name=\"Password\"\r\n\r\n{password}\r\n"
        "------WebKitFormBoundarySmaDEz0BcUokuAAb\r\n"
        "Content-Disposition: form-data; name=\"AgeOver18\"\r\n\r\ntrue\r\n"
        "------WebKitFormBoundarySmaDEz0BcUokuAAb\r\n"
        "Content-Disposition: form-data; name=\"BaseUrl\"\r\n\r\nhttps://funker530.com\r\n"
        "------WebKitFormBoundarySmaDEz0BcUokuAAb--\r\n"
    )

    if proxy:
        proxy_parts = proxy.split(":")
        proxy_dict = {
            "http": f"http://{proxy_parts[2]}:{proxy_parts[3]}@{proxy_parts[0]}:{proxy_parts[1]}",
            "https": f"http://{proxy_parts[2]}:{proxy_parts[3]}@{proxy_parts[0]}:{proxy_parts[1]}"
        }
        response = requests.post(register_url, headers=headers, data=data, proxies=proxy_dict)
    else:
        response = requests.post(register_url, headers=headers, data=data)

    try:
        response_data = response.json()
        session_key = response_data['session']['sessionKey']
        user_id = response_data['id']

        print(Fore.YELLOW + "[" + Fore.GREEN + "=" + Fore.YELLOW + "]" + Fore.MAGENTA + f" retrieved session {session_key}" + Style.RESET_ALL)

        with open("output/session.txt", "a") as session_file:
            session_file.write(f"{session_key}:{user_id}\n")

        with open("output/acc.txt", "a") as acc_file:
            acc_file.write(f"{username}:{password}\n")
    except json.JSONDecodeError:
        print(Fore.RED + "[!]prolly ratelimited try using proxies!" + Style.RESET_ALL)

num_threads = int(input(Fore.BLUE + "How many threads do you want to use: " + Style.RESET_ALL))
num_accounts = int(input(Fore.BLUE + "How many accounts do you want to generate: " + Style.RESET_ALL))
use_proxies = input(Fore.BLUE + "Do you want to use proxies? (y/n): " + Style.RESET_ALL).lower()

proxies = []
if use_proxies == 'y':
    proxies = get_proxies()

threads = []
for _ in range(num_threads):
    for _ in range(num_accounts // num_threads):
        proxy = random.choice(proxies) if proxies else None
        thread = threading.Thread(target=generate_account, args=(proxy,))
        threads.append(thread)
        thread.start()

for thread in threads:
    thread.join()
