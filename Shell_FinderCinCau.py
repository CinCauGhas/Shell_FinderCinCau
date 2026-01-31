#!/usr/bin/env python3
import requests
import sys
import time
import os

# ================== COLOR ==================
RED   = "\033[1;31m"
WHITE = "\033[1;37m"
PINK  = "\033[1;35m"
RESET = "\033[0m"

# ================== BANNER ==================
print(f"""{RED}
███████╗██╗  ██╗███████╗██╗     ██╗     
██╔════╝██║  ██║██╔════╝██║     ██║     
███████╗███████║█████╗  ██║     ██║     
╚════██║██╔══██║██╔══╝  ██║     ██║     
███████║██║  ██║███████╗███████╗███████╗
╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝

███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
{RESET}
{WHITE}Author : CinCauGhast
GitHub : https://github.com/CinCauGhas
{RESET}
""")

# ================== LOAD PAYLOAD ==================
def load_payloads():
    payload_file = "payloads/shell_payloads.txt"
    if not os.path.exists(payload_file):
        print(f"{RED}PAYLOAD FILE NOT FOUND : {payload_file}{RESET}")
        sys.exit(1)

    with open(payload_file, "r") as f:
        return [line.strip() for line in f if line.strip()]

SHELL_PAYLOADS = load_payloads()

# ================== INPUT ==================
if len(sys.argv) != 2:
    print(f"{WHITE}Usage : python Shell_FinderCinCau.py https://target.com{RESET}")
    sys.exit(1)

target = sys.argv[1].rstrip("/")
print(f"{WHITE}[+] Target : {target}{RESET}\n")

# ================== SCAN ==================
found = False

for payload in SHELL_PAYLOADS:
    url = f"{target}/{payload}"
    try:
        r = requests.get(url, timeout=5)
        time.sleep(0.1)

        if r.status_code == 200:
            print(f"{PINK}[+] {target} : {payload}{RESET}")
            found = True
        else:
            print(f"{WHITE}[-] {target} : {payload}{RESET}")

    except requests.exceptions.RequestException:
        print(f"{WHITE}[-] ERROR : {payload}{RESET}")

# ================== RESULT ==================
print("\n====================")
if found:
    print(f"{RED}SCAN SELESAI - SHELL DITEMUKAN {RESET}")
else:
    print(f"{WHITE}TIDAK MENEMUKAN SHELL YANG VALID{RESET}")
print("====================")
