import requests
import threading
import time

def send_request(session_key, user_id, post_id, content):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "AddType": "Comment",
        "Connection": "keep-alive",
        "Content-Type": "multipart/form-data; boundary=---------------------------37288687769282782872076166504",
        "DNT": "1",
        "Host": "funker530-fnc.azurewebsites.net",
        "Origin": "https://funker530.com",
        "Priority": "u=0",
        "Referer": "https://funker530.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "SessionKey": session_key,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0"
    }

    payload = (
        "-----------------------------37288687769282782872076166504\r\n"
        "Content-Disposition: form-data; name=\"postId\"\r\n\r\n"
        f"{post_id}\r\n"
        "-----------------------------37288687769282782872076166504\r\n"
        "Content-Disposition: form-data; name=\"userId\"\r\n\r\n"
        f"{user_id}\r\n"
        "-----------------------------37288687769282782872076166504\r\n"
        "Content-Disposition: form-data; name=\"_content\"\r\n\r\n"
        f"{content}\r\n"
        "-----------------------------37288687769282782872076166504--"
    )

    response = requests.post(
        "https://funker530-fnc.azurewebsites.net/api/Add?code=sL3mjD-c0BJdI9b9h4s7WhIPU8ca9p6h3yiLyFczS-I9AzFupvbo9g==",
        headers=headers,
        data=payload
    )

    print(f"Response for session {session_key}: {response.status_code}")

def main():
    with open("output/session.txt", "r") as file:
        sessions = file.readlines()

    post_id = input("Enter the Post ID: ")
    content = input("Enter the content: ")

    for session in sessions:
        session_key, user_id = session.strip().split(":")
        send_request(session_key, user_id, post_id, content)
        time.sleep(0.3) # i added a delay to bypass the ratelimit system put it lower if ya want!

if __name__ == "__main__":
    main()
