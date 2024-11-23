import requests

def get_request(slug):
    url = f"https://funker530-fnc.azurewebsites.net/api/Get?code=sL3mjD-c0BJdI9b9h4s7WhIPU8ca9p6h3yiLyFczS-I9AzFupvbo9g==&slug={slug}&random=false&amount=1&hideNSFW=false&allowPrivate=true&allowUnpublished=true&allowInvalid=true"
    
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
        "GetType": "Video",
        "Host": "funker530-fnc.azurewebsites.net",
        "Origin": "https://funker530.com",
        "Referer": "https://funker530.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0"
    }

    response = requests.get(url, headers=headers)
    return response.json()

def main():
    slug = input("https://funker530.com/video/")
    response = get_request(slug)
    if response and isinstance(response, list) and 'id' in response[0]:
        print(f"[+]retrieved id use this for the liker post id: {response[0]['id']}")
    else:
        print("ID not found in the response")

if __name__ == "__main__":
    main()
