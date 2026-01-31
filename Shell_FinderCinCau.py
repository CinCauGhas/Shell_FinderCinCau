#!/usr/bin/env python3
import requests
import sys
import time

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

# ================== PAYLOAD ==================
SHELL_PAYLOADS = [
    "shell.php",
    "ws.php",
    "cmd.php",
    "upload.php",
    "adminer.php",
]

for i in range(1, 81):
    SHELL_PAYLOADS.append(f"ws{i}.php")

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
    print(f"{RED}SCAN SELESAI - SHELL DITEMUKAN (EDUCATIONAL){RESET}")
else:
    print(f"{WHITE}TIDAK MENEMUKAN SHELL YANG VALID{RESET}")
print("====================")
