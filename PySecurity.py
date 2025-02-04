import requests
import os
import json
from colorama import Fore, init

init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()

class Settings: 
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": "application/json",
    }

def print_menu():
    menu = f"""
    👾 Forensic Tool / PySecurity 👾
    💬 Telegram: {Fore.CYAN}@CleinKelvinn{Fore.RESET} 💬
    ✨ {Fore.LIGHTGREEN_EX}If you see {Fore.RED}'Quota Limit'{Fore.LIGHTGREEN_EX}, change your IP Address. ✨

{Fore.YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 [0] > Close PySecurity.          [10] > DMARC Lookup.
 [1] > Reverse DNS.               [11] > TLS Scan.
 [2] > DNS Lookup.                [12] > DNS Record.
 [3] > Geolocation IP.            [13] > DNS Security Extensions Check.
 [4] > Zone Transfer.             [14] > Privacy Detection API.
 [5] > DNS Host Records.          [15] > Check if your site can accept IPv6 Proxies.
 [6] > Reverse IP Lookup.         [16] > Check Front-End JavaScript Vulnerabilities.
 [7] > ASN Lookup.                [17] > URL Shortener Bypasser.
 [8] > Email Validator.
 [9] > Have I been Pwned?

{Fore.YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.RESET}
    """
    print(menu)

def make_request(url, params=None, data=None, headers=None, method="GET"):
    try:
        if method == "GET":
            response = requests.get(url, params=params, headers=headers)
        elif method == "POST":
            response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"{Fore.RED}Error: {e}{Fore.RESET}")
        return None

def process_and_print_request(url, params=None, data=None, headers=None, method="GET"):
    response = make_request(url, params, data, headers, method)
    if response:
        print("\n", response, "\n| >> Press ENTER to continue.")
    input()
    clear()

def get_validated_input(prompt, validation_func):
    while True:
        user_input = input(prompt).strip()
        if validation_func(user_input):
            return user_input
        else:
            print(f"{Fore.RED}Invalid input. Please try again.{Fore.RESET}")

def reverseDNS():
    dns = get_validated_input("Enter the IP Address: ", lambda x: x)
    process_and_print_request(f"https://api.hackertarget.com/reversedns/?q={dns}")
    
def IpPrivacy():
    ipaddress = get_validated_input("Enter the IP Address: ", lambda x: x)
    process_and_print_request(f"https://ipinfo.io/widget/demo/{ipaddress}?dataset=proxy-vpn-detection")

def DNSLookup():
    lookup = get_validated_input("Enter the Domain Name: ", lambda x: x)
    process_and_print_request(f"https://api.hackertarget.com/dnslookup/?q={lookup}")

def geoip():
    geoip = get_validated_input("Enter the IP Address: ", lambda x: x)
    process_and_print_request(f"https://api.hackertarget.com/geoip/?q={geoip}")

def zonetransfer():
    zonetransfer = get_validated_input("Enter the Domain Name: ", lambda x: x)
    process_and_print_request(f"https://api.hackertarget.com/zonetransfer/?q={zonetransfer}")

def dnssubdomain():
    subdomain = get_validated_input("Enter the Domain Name: ", lambda x: x)
    process_and_print_request(f"https://api.hackertarget.com/hostsearch/?q={subdomain}")

def reverseip():
    reverseip = get_validated_input("Enter the IP Address: ", lambda x: x)
    process_and_print_request(f"https://api.hackertarget.com/reverseiplookup/?q={reverseip}")

def ASN():
    asnlookup = get_validated_input("Enter the IP Address or ASN: ", lambda x: x)
    process_and_print_request(f"https://api.hackertarget.com/aslookup/?q={asnlookup}")

def emailvalid():
    mailvalid = get_validated_input("Enter the Email Address: ", lambda x: x)
    data = f"address=&email={mailvalid}&submit=Verify+Email+Address"
    response = make_request(
        "https://tools.iplocation.net/verify-email-address",
        data=data,
        headers=Settings.headers,
        method="POST"
    )
    if response:
        if "is a valid email" in response:
            print("[+] This email is valid and active.")
        elif "is an invalid email" in response:
            print(f"{Fore.RED}[-] This email is not working.{Fore.LIGHTGREEN_EX}")
    input("\nPress ENTER to continue.")
    clear()

def proxycheck():
    proxy = get_validated_input("Enter the Email Address: ", lambda x: x.replace("@", "%40"))
    data = f"email={proxy}&submit=Breached%3F"
    response = make_request(
        "https://tools.iplocation.net/data-breach-check",
        data=data,
        headers=Settings.headers,
        method="POST"
    )
    if response:
        if "Congratulations" in response:
            print("[+] Private email address")
        elif "We found" in response:
            print(f"{Fore.RED}[-] Email is public!{Fore.LIGHTGREEN_EX}")
    input("\nPress ENTER to continue.")
    clear()

def DMARC():
    domain = get_validated_input("Enter the Domain Address: ", lambda x: x)
    data = f"url={domain}&submit="
    response = make_request(
        "https://tools.iplocation.net/dmarc-lookup",
        data=data,
        headers=Settings.headers,
        method="POST"
    )
    if response:
        if "v=DMARC1" in response:
            print("[+] DMARC record found")
        elif "No record found" in response:
            print(f"{Fore.RED}[-] No DMARC record found!{Fore.LIGHTGREEN_EX}")
    input("\nPress ENTER to continue.")
    clear()

def TLS():
    domain = get_validated_input("Enter the Domain Address: ", lambda x: x)
    data = json.dumps({"url": f"https://{domain}"})
    response = make_request(
        "https://siterelic.com/siterelic-api/tlsscan",
        data=data,
        headers=Settings.headers2,
        method="POST"
    )
    if response:
        tls_info = json.loads(response).get("data", {}).get("protocols", {})
        print("TLS Information: ", tls_info)
    input("\nPress ENTER to continue.")
    clear()

def DNSRECORD():
    domain = get_validated_input("Enter the Domain Address: ", lambda x: x)
    data = json.dumps({"url": f"https://{domain}"})
    response = make_request(
        "https://siterelic.com/siterelic-api/dnsrecord",
        data=data,
        headers=Settings.headers2,
        method="POST"
    )
    if response:
        dns_info = json.loads(response).get("data", {})
        print("DNS Records Info: ", dns_info)
    input("\nPress ENTER to continue.")
    clear()

def DNSSEC():
    domain = get_validated_input("Enter the Domain Address: ", lambda x: x)
    data = json.dumps({"url": f"https://{domain}"})
    response = make_request(
        "https://siterelic.com/siterelic-api/dnssec",
        data=data,
        headers=Settings.headers2,
        method="POST"
    )
    if response:
        dnssec_info = json.loads(response).get("data", {})
        print("DNSSEC Info: ", dnssec_info)
    input("\nPress ENTER to continue.")
    clear()

def CF():
    domain = get_validated_input("Enter the Domain Address: ", lambda x: x)
    data = json.dumps({"url": f"https://{domain}"})
    response = make_request(
        "https://siterelic.com/siterelic-api/cloudflare",
        data=data,
        headers=Settings.headers2,
        method="POST"
    )
    if response:
        cf_info = json.loads(response).get("data", {})
        print("CloudFlare Info: ", cf_info)
    input("\nPress ENTER to continue.")
    clear()

def ipv6():
    domain = get_validated_input("Enter the Domain Address: ", lambda x: x)
    print(f"{Fore.LIGHTYELLOW_EX}\n > Wait for result...{Fore.LIGHTGREEN_EX}")
    access_token = make_request(
        "https://domsignal.com/tools/api/api-accessToken/",
        data=json.dumps({"serviceType": "ipv6-test"}),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    if not access_token:
        print(f"{Fore.RED}Error retrieving access token.{Fore.RESET}")
        return

    token = json.loads(access_token)["credentials"]["accessToken"]
    headers = {
        "Host": "domsignal.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "public-authorization": token,
        "Origin": "https://domsignal.com",
        "Referer": "https://domsignal.com/ipv6-test",
    }
    response = make_request(
        "https://domsignal.com/tools/api/gf/dnsrecord/",
        data=json.dumps({"url": f"{domain}", "type": "ipv6-test"}),
        headers=headers,
        method="POST"
    )
    if response:
        if "AAAA" in json.loads(response)["data"]:
            print(f"{Fore.GREEN}[+] This website supports IPv6 proxy connections --> {domain}{Fore.LIGHTGREEN_EX}")
        else:
            print(f"{Fore.RED}[-] No IPv6 proxy support for this website --> {domain}{Fore.LIGHTGREEN_EX}")
    input("Press ENTER to continue.")
    clear()

def JSVuln():
    domain = get_validated_input("Enter the Domain Address: ", lambda x: x)
    print(f"{Fore.LIGHTYELLOW_EX}\n > Wait for result...{Fore.LIGHTGREEN_EX}")
    access_token = make_request(
        "https://domsignal.com/tools/api/api-accessToken/",
        data=json.dumps({"serviceType": "js-vulnerability-scanner"}),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    if not access_token:
        print(f"{Fore.RED}Error retrieving access token.{Fore.RESET}")
        return

    token = json.loads(access_token)["credentials"]["accessToken"]
    headers = {
        "Host": "domsignal.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "public-authorization": token,
        "Origin": "https://domsignal.com",
        "Referer": "https://domsignal.com/ipv6-test",
    }
    response = make_request(
        "https://domsignal.com/tools/api/gf/lighthouse/",
        data=json.dumps({"url": f"{domain}", "type": "js-vulnerability-scanner"}),
        headers=headers,
        method="POST"
    )
    
    if not response:
        print(f"{Fore.RED}Error: No response received for vulnerability scan.{Fore.RESET}")
        return

    try:
        lighthouse_url = json.loads(response).get("data")
        if not lighthouse_url:
            print(f"{Fore.RED}Error: Lighthouse URL not found in response.{Fore.RESET}")
            return
        
        vuln_response = requests.get(lighthouse_url).json()
        vulnerabilities = vuln_response["audits"]["no-vulnerable-libraries"]["details"]["items"]
        if vulnerabilities:
            print(json.dumps(vulnerabilities, indent=3))
        else:
            print(f"{Fore.RED}\n[-] No vulnerable libraries found for this website --> {domain}{Fore.LIGHTGREEN_EX}")
    except (KeyError, requests.RequestException, json.JSONDecodeError) as e:
        print(f"{Fore.RED}Error processing vulnerability scan for domain: {domain} - {e}{Fore.RESET}")
    input("\nPress ENTER to continue.")
    clear()

def ShortURL():
    url = get_validated_input("Enter the URL: ", lambda x: x)
    print(f"{Fore.LIGHTYELLOW_EX}\n > Wait for result...{Fore.LIGHTGREEN_EX}")
    try:
        response = requests.get(url, allow_redirects=True)
        if response.status_code == 200:
            print("\n", response.url)
        else:
            print("\n", response.status_code, response.reason, response.url)
    except requests.RequestException as e:
        print(f"{Fore.RED}Error: {e}{Fore.RESET}")
    input("\n Press ENTER to continue.")
    clear()

while True:
    print_menu()
    try:
        choice = int(input(f"{Fore.MAGENTA}🌐 Choose an option: {Fore.RESET}"))
    except ValueError:
        clear()
        continue

    if choice == 0:
        exit()
    
    clear()

    functions = {
        1: reverseDNS,
        2: DNSLookup,
        3: geoip,
        4: zonetransfer,
        5: dnssubdomain,
        6: reverseip,
        7: ASN,
        8: emailvalid,
        9: proxycheck,
        10: DMARC,
        11: TLS,
        12: DNSRECORD,
        13: DNSSEC,
        14: IpPrivacy,
        15: ipv6,
        16: JSVuln,
        17: ShortURL
    }

    func = functions.get(choice)
    if func:
        func()
    else:
        clear()
