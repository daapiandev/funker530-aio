import requests

def main():
    
    with open("output/session.txt", "r") as file:
        sessions = file.readlines()

    
    video_id = input("Enter the Video ID: ")

    for session in sessions:
        session_key, user_id = session.strip().split(":")

        
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.5",
            "AddType": "Vote",
            "Connection": "keep-alive",
            "Content-Type": "multipart/form-data; boundary=---------------------------233068388124181691903499655301",
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
            "-----------------------------233068388124181691903499655301\r\n"
            "Content-Disposition: form-data; name=\"Upvote\"\r\n\r\n"
            "true\r\n"
            "-----------------------------233068388124181691903499655301\r\n"
            "Content-Disposition: form-data; name=\"VideoId\"\r\n\r\n"
            f"{video_id}\r\n"
            "-----------------------------233068388124181691903499655301\r\n"
            "Content-Disposition: form-data; name=\"UserId\"\r\n\r\n"
            f"{user_id}\r\n"
            "-----------------------------233068388124181691903499655301--"
        )

        
        response = requests.post(
            "https://funker530-fnc.azurewebsites.net/api/Add?code=sL3mjD-c0BJdI9b9h4s7WhIPU8ca9p6h3yiLyFczS-I9AzFupvbo9g==",
            headers=headers,
            data=payload
        )

        
        print(f"Response for session {session_key}: {response.status_code}")

if __name__ == "__main__":
    main()
