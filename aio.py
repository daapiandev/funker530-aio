import subprocess
from colorama import init, Fore, Style
import os

init(autoreset=True)

def clear_terminal(title):
    os.system(f'title {title} && cls' if os.name == 'nt' else f'echo -ne "\033]0;{title}\007" && clear')

ascii_art = """
 _______ _     _ __   _ _     _ _______  ______      ______ _______ __   _
 |______ |     | | \  | |____/  |______ |_____/ ___ |  ____ |______ | \  |
 |       |_____| |  \_| |    \_ |______ |    \_     |_____| |______ |  \_|
"""

options = """
1. gen (use proxies fr fr)
2. chat-spammer 
3. like-spammer                          
4. retriever (use this shit to retrieve the post id)
"""
# HELP WHY DID I CALL IT LIKER-SPAMMER
def run_script(script_name):
    script_path = os.path.join("utils", script_name)
    subprocess.Popen(["cmd", "/c", f'start cmd /k python {script_path}'])

while True:
    clear_terminal("funker530 AIO made by Daapiandev ENJOY!")
    print(Fore.LIGHTBLUE_EX + ascii_art)
    print(options)
    choice = input("Choose an option (1-4) or 'q' to quit: ")
    if choice == '1':
        run_script("gen.py")
    elif choice == '2':
        run_script("comment.py")
    elif choice == '3':
        run_script("liker.py")
    elif choice == '4':
        run_script("retrieve.py")
    elif choice.lower() == 'q':
        break
    else:
        print("Invalid choice. Please try again.")
