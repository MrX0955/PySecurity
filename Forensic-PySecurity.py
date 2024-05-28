import requests, os, json
from colorama import Fore


def clear():
    os.system("cls" if os.name == "nt" else "clear")


clear()
os.system("title PySecurity Forensic Tool")


class Settings:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": "application/json",
    }


def print_menu():
    print(Fore.LIGHTGREEN_EX)
    MENU = f"""
        👾 Forensic Tool / PySecurity 👾
        💬 Telegram: {Fore.CYAN}@CleinKelvinn{Fore.RESET} 💬
        ✨ {Fore.LIGHTGREEN_EX}If you saw {Fore.RED}'Quota Limit'{Fore.LIGHTGREEN_EX}, change your IP Address. ✨
        
{Fore.RESET}{Fore.WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.YELLOW}

     [0] > Close ForensicTool.        [10] > DMARC Lookup.
     [1] > Reverse DNS.               [11] > TLS Scan.
     [2] > DNS Lookup.                [12] > DNS Record.
     [3] > Geolocation IP.            [13] > DNS Security Extensions Check.
     [4] > Zone Transfer.             [14] > CloudFlare Resolver.
     [5] > DNS Host Records.          [15] > Check if your site can accept IPv6 Proxies.
     [6] > Reverse IP Lookup.         [16] > Check Front-End JavaScript Vulnerabilities.
     [7] > ASN Lookup.                [17] > URL Shortener Bypasser.
     [8] > Email Validator.
     [9] > Have I been Pwned?

{Fore.RESET}{Fore.WHITE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Fore.MAGENTA}
    """
    print(MENU)


def reverseDNS():
    dns = input("Enter the IP Address: ")
    izlegal = requests.get(f"https://api.hackertarget.com/reversedns/?q={dns}")
    print("\n", izlegal.text, "| >> Press ENTER For Exit.")
    input()
    clear()


def DNSLookup():
    lookup = input("Enter the Domain Name: ")
    two = requests.get(f"https://api.hackertarget.com/dnslookup/?q={lookup}")
    print("\n", two.text, "| >> Press ENTER For Exit.")
    input()
    clear()


def geoip():
    geoip = input("Enter the IP Address: ")
    i = requests.get(f"https://api.hackertarget.com/geoip/?q={geoip}")
    print("\n", i.text, "| => Press ENTER For Exit.")
    input()
    clear()


def zonetransfer():
    zonetransfer = input("Enter the IP Address: ")
    z = requests.get(f"https://api.hackertarget.com/zonetransfer/?q={zonetransfer}")
    print("\n", z.text, "| => Press ENTER For Exit.")
    input()
    clear()


def dnssubdomain():
    subdomain = input("Enter the Domain Name: ")
    k = requests.get(f"https://api.hackertarget.com/hostsearch/?q={subdomain}")
    print("\n", k.text, "| => Press ENTER For Exit.")
    input()
    clear()


def reverseip():
    reverseip = input("Enter the IP Address: ")
    mrx = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={reverseip}")
    print("\n", mrx.text, "| => Press ENTER For Exit.")
    input()
    clear()


def ASN():
    asnlookup = input(" IP Address or ASN: ")
    hasfa = requests.get(f"https://api.hackertarget.com/aslookup/?q={asnlookup}")
    print("\n", hasfa.text, "| => Press ENTER For Exit.")
    input()
    clear()


def emailvalid():
    mailvalid = input("Enter the Email Address: ")
    datas = f"address=&email={mailvalid}&submit=Verify+Email+Address"
    mrxvalid = requests.post(
        "https://tools.iplocation.net/verify-email-address",
        data=datas,
        headers=Settings.headers,
    )
    if "is a valid email" in mrxvalid.text:
        print("[+] Bu Mail E-Posta alabilir. Yani bu mail doğru ve kullanılıyor.")
    elif "is an invalid email" in mrxvalid.text:
        print(f"{Fore.RED}[-] This Email is Not Working.{Fore.LIGHTGREEN_EX}")
    input("\nPress ENTER For Exit.")
    clear()


def proxycheck():
    proxy = input("Enter the Mail Address: ")
    proxy.replace("@", "%40")
    datas = f"email={proxy}&submit=Breached%3F"
    proxyy = requests.post(
        "https://tools.iplocation.net/data-breach-check",
        data=datas,
        headers=Settings.headers,
    )
    if "Congratulations" in proxyy.text:
        print("[+] Private Mail Address")
    elif "We found" in proxyy.text:
        print(f"{Fore.RED}[-] Mail Public!{Fore.LIGHTGREEN_EX}")
    input("\nPress ENTER For Exit.")
    clear()


def DMARC():
    ece = input("Enter the Domain Address: ")
    datas = f"url={ece}&submit="
    DMARCR = requests.post(
        "https://tools.iplocation.net/dmarc-lookup",
        data=datas,
        headers=Settings.headers,
    )
    if "v=DMARC1" in DMARCR.text:
        print("[+] Have Firewall")
    elif "No record found" in DMARCR.text:
        print(f"{Fore.RED}[-] No Firewall!{Fore.LIGHTGREEN_EX}")
    input("\nPress ENTER For Exit.")
    clear()


def TLS():
    tlszac = input("Enter the Domain Address: ")
    datam = {"url": f"https://{tlszac}"}
    zaclol = requests.post(
        "https://siterelic.com/siterelic-api/tlsscan",
        json=datam,
        headers=Settings.headers2,
    ).text
    y = json.loads(zaclol)
    reqid = y["data"]["protocols"]
    print("TLS Bilgileri: ", reqid)
    input("\nPress ENTER For Exit.")
    clear()


def DNSRECORD():
    dnsrecord = input("Enter the Domain Address: ")
    datamiz = {"url": f"https://{dnsrecord}"}
    zacmrx = requests.post(
        "https://siterelic.com/siterelic-api/dnsrecord",
        json=datamiz,
        headers=Settings.headers2,
    ).text
    xx = json.loads(zacmrx)
    xxyy = xx["data"]
    print("DNS Records Infos: ", xxyy)
    input("\nPress ENTER For Exit.")
    clear()


def DNSSEC():
    DNSSEC = input("Enter the Domain Address: ")
    datamizzz = {"url": f"https://{DNSSEC}"}
    rmrx = requests.post(
        "https://siterelic.com/siterelic-api/dnssec",
        json=datamizzz,
        headers=Settings.headers2,
    ).text
    rr = json.loads(rmrx)
    print(rr["data"])
    input("\nPress ENTER For Exit.")
    clear()


def CF():
    cloudflare = input("Enter the Domain Address: ")
    datax = f"action=PostData&string={cloudflare}"

    headersx = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "x-requested-with": "XMLHttpRequest",
        "referer": "https://webresolver.nl/tools/cloudflare",
        "origin": "https://webresolver.nl",
    }
    req = requests.post(
        "https://webresolver.nl/ajax/tools/cloudflare", data=datax, headers=headersx
    ).text
    var = req.replace("<br>", " ")
    varmi = var.replace("</b><br />", " ")
    varherhalde = varmi.replace("<b>", " ")
    KT = varherhalde.replace("Cloudflare Resolver", " ")
    print(KT)
    input("\nPress ENTER For Exit.")
    clear()


def ipv6():
    load = input("Enter the Domain Address: ").strip()

    access_token = requests.post(
        "https://domsignal.com/tools/api/api-accessToken/",
        json={"serviceType": "ipv6-test"},
        headers={"Content-Type": "application/json"},
    ).json()
    TK = access_token["credentials"]["accessToken"]

    header = {
        "Host": "domsignal.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/json",
        "public-authorization": TK,
        "Origin": "https://domsignal.com",
        "Connection": "keep-alive",
        "Referer": "https://domsignal.com/ipv6-test",
    }

    j = requests.post(
        "https://domsignal.com/tools/api/gf/dnsrecord/",
        json={"url": f"{load}", "type": "ipv6-test"},
        headers=header,
    ).json()

    if "AAAA" in j["data"]:
        print(
            f"{Fore.GREEN}[+] This Web Site Supporting IPv6 Proxy Connection --> {load}{Fore.LIGHTGREEN_EX}"
        )
        input("Press ENTER For Exit.")
    elif j["data"] == {}:
        print(
            f"{Fore.RED}[-] No Support For IPv6 Proxy For That Web Site --> {load}{Fore.LIGHTGREEN_EX}"
        )
        input("\nPress ENTER For Exit.")
        clear()


def JSVuln():
    load = input("Enter the Domain Address: ").strip()
    print(f"{Fore.LIGHTYELLOW_EX}\n > Wait For Result...{Fore.LIGHTGREEN_EX}")

    access_token = requests.post(
        "https://domsignal.com/tools/api/api-accessToken/",
        json={"serviceType": "js-vulnerability-scanner"},
        headers={"Content-Type": "application/json"},
    ).json()
    TK = access_token["credentials"]["accessToken"]

    header = {
        "Host": "domsignal.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/json",
        "public-authorization": TK,
        "Origin": "https://domsignal.com",
        "Connection": "keep-alive",
        "Referer": "https://domsignal.com/ipv6-test",
    }

    j = requests.post(
        "https://domsignal.com/tools/api/gf/lighthouse/",
        json={"url": f"{load}", "type": "js-vulnerability-scanner"},
        headers=header,
    ).json()

    try:
        if "lighthouse" in j["data"]:
            url = j["data"]
            req = requests.get(url).json()
            response = req["audits"]["no-vulnerable-libraries"]["details"]["items"]
            details = json.dumps(response, indent=3)
            if details == "[]":
                print(
                    f"{Fore.RED}\n[-] No Vulnerable Libraries For That Web Site --> {load}{Fore.LIGHTGREEN_EX}"
                )
            else:
                print("\n", details)
            input("\nPress ENTER For Exit.")
            clear()
        else:
            print("\nREST API Can not response correctly..")
            input("\nPress ENTER For Exit.")
            clear()
    except KeyError:
        print("\nWe can't resolve that domain...")
        input("\nPress ENTER For Exit.")
        clear()


def ShortURL():
    load = input("Enter the URL: ").strip()
    print(f"{Fore.LIGHTYELLOW_EX}\n > Wait For Result...{Fore.LIGHTGREEN_EX}")
    req = requests.get(f"{load}", allow_redirects=True)
    if req.status_code == 200:
        print("\n", req.url)
    else:
        print("\n", req.status_code, req.reason, req.url)
    input("\n Press ENTER For Exit.")
    clear()


while True:
    print_menu()
    choice = int(input("🌐 Choose an option: "))

    if choice == 0:
        exit()

    clear()

    if choice == 1:
        reverseDNS()

    elif choice == 2:
        DNSLookup()

    elif choice == 3:
        geoip()

    elif choice == 4:
        zonetransfer()

    elif choice == 5:
        dnssubdomain()

    elif choice == 6:
        reverseip()

    elif choice == 7:
        ASN()

    elif choice == 8:
        emailvalid()

    elif choice == 9:
        proxycheck()

    elif choice == 10:
        DMARC()

    elif choice == 11:
        TLS()

    elif choice == 12:
        DNSRECORD()

    elif choice == 13:
        DNSSEC()

    elif choice == 14:
        CF()

    elif choice == 15:
        ipv6()

    elif choice == 16:
        JSVuln()

    elif choice == 17:
        ShortURL()
