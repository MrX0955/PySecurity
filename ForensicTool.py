try:
    import requests
    import os
    import json
    import whois
    from colorama import Fore, Style
    from bs4 import BeautifulSoup
    from lxml import html
except Exception:
    print("Your Modules Are Missing.")

if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")

banner = f"""{Fore.LIGHTGREEN_EX} MRX - Forensic Tool"""

print(Fore.LIGHTGREEN_EX)
MENU = f"""
    MRX - Forensic Tool 
    If it gives an error saying {Fore.RED}'Quota Limit'{Fore.LIGHTGREEN_EX}, change your IP.

 [0] > Close ForensicTool.        [11] > TLS Scan.
 [1] > Reverse DNS.               [12] > DNS Record.
 [2] > DNS Lookup.                [13] > DNS Security Check.
 [3] > Geolocation IP.            [14] > Honeypot Check.
 [4] > Zone Transfer.             REV [15] > Hash Analyzer.
 [5] > DNS Host Records.          REV [16] > ClickJacking Security in Headers Check.
 [6] > Reverse IP Lookup.         REV [17] > XSS Vulnerability in Headers Check.
 [7] > ASN Lookup.                REV [18] > Whois Lookup.
 [8] > Email Validator.           REV [19] > CloudFlare Resolver.
 [9] > Have I been Pwned?         REV [20] > CloudFlare Resolver.
[10] > DMARC Lookup.              
"""
print(MENU)

choice = int(input("Choose an option: "))
if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")
if choice == 0:
    exit()
print(banner, "\n")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded"
}

headers2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
    "Content-Type": "application/json"
}

if choice == 1:
    def reverseDNS():
        print(f"{Fore.LIGHTRED_EX}Reverse DNS{Fore.LIGHTGREEN_EX}")
        dns = input("Enter the IP Address: ")
        izlegal = requests.get(f"https://api.hackertarget.com/reversedns/=q={dns}")
        print(izlegal.text, "| >> Press ENTER For Exit.")
        input()
    reverseDNS()

if choice == 2:
    def DNSLookup():
        print(f"{Fore.LIGHTRED_EX}DNS Lookup{Fore.LIGHTGREEN_EX}")
        lookup = input("Enter the Domain Name: ")
        two = requests.get(f"https://api.hackertarget.com/aslookup/?q={lookup}")
        print(two.text, "| >> Press ENTER For Exit.")
        input()
    DNSLookup()

if choice == 3:
    print(f"{Fore.LIGHTRED_EX}GEO IP{Fore.LIGHTGREEN_EX}")
    def geoip():
        geoip = input("Enter the IP Address: ")
        i = requests.get(f"https://api.hackertarget.com/geoip/?q={geoip}")
        print(i.text), "| => Press ENTER For Exit."
        input()
    geoip()

if choice == 4:
    print(f"{Fore.LIGHTRED_EX}Zone Transfer{Fore.LIGHTGREEN_EX}")
    def zonetransfer():
        zonetransfer = input("Enter the IP Address: ")
        z = requests.get(f"https://api.hackertarget.com/zonetransfer/?q={zonetransfer}")
        print(z.text), "| => Press ENTER For Exit."
        input()
    zonetransfer()

if choice == 5:
    print(f"{Fore.LIGHTRED_EX}DNS Host Records{Fore.LIGHTGREEN_EX}")
    def dnssubdomain():
        subdomain = input("Enter the Domain Name: ")
        k = requests.get(f"https://api.hackertarget.com/hostsearch/?q={subdomain}")
        print(k.text), "| => Press ENTER For Exit."
        input()
    dnssubdomain()

if choice == 6:
    print(f"{Fore.LIGHTRED_EX}Reverse IP Lookup{Fore.LIGHTGREEN_EX}")
    def reverseip():
        reverseip = input("Enter the IP Address: ")
        mrx = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={reverseip}")
        print(mrx.text), "| => Press ENTER For Exit."
        input()
    reverseip()

if choice == 7:
    print(f"{Fore.LIGHTRED_EX}ASN Lookup{Fore.LIGHTGREEN_EX}")
    def ASN():
        asnlookup = input(" IP Address or ASN: ")
        hasfa = requests.get(f"https://api.hackertarget.com/aslookup/?q={asnlookup}")
        print(hasfa.text), "| => Press ENTER For Exit."
        input()
    ASN()

if choice == 8:
    print(f"{Fore.LIGHTRED_EX}Email Validator{Fore.LIGHTGREEN_EX}")
    def emailvalid():
        mailvalid = input("Enter the Email Address: ")
        datas = f'address=&email={mailvalid}&submit=Verify+Email+Address'
        mrxvalid = requests.post("https://www.iplocation.net/verify-email-address/", data=datas, headers=headers)

        if 'is a valid email' in mrxvalid.text:
            print("[+] Bu Mail E-Posta alabilir.")
        elif "is an invalid email" in mrxvalid.text:
            print(f"{Fore.RED}[-] This Email is Not Working.{Fore.LIGHTGREEN_EX}")
        input("Press ENTER For Exit.")
    emailvalid()

if choice == 9:
    print(f"{Fore.LIGHTRED_EX}Have I Been Pwned{Fore.LIGHTGREEN_EX}")
    def proxycheck():
        proxy = input("Enter the Mail Address: ")
        proxy.replace("@", "%40")
        datas = f'email={proxy}&submit=Breached%3F'
        proxyy = requests.post("https://www.iplocation.net/data-breach-check", data=datas, headers=headers)

        if "Congratulations" in proxyy.text:
            print("[+] Private Mail Address")
        elif "We found" in proxyy.text:
            print(f"{Fore.RED}[-] Mail Public!{Fore.LIGHTGREEN_EX}")
        input("Press ENTER For Exit.")
    proxycheck()

if choice == 10:
    print(f"{Fore.LIGHTRED_EX}DMARC Lookup{Fore.LIGHTGREEN_EX}")
    def DMARC():
        ece = input(" Domain Address: ")
        datas = f'url={ece}&submit='
        DMARCR = requests.post("https://tools.iplocation.net/dmarc-lookup", data=datas, headers=headers)

        if "v=DMARC1" in DMARCR.text:
            print("[+] Have Firewall")
        elif "No record found" in DMARCR.text:
            print(f"{Fore.RED}[-] No Firewall!{Fore.LIGHTGREEN_EX}")
        input("Press ENTER For Exit.")
    DMARC()

if choice == 11:
    print(f"{Fore.LIGHTRED_EX}TLS Scan{Fore.LIGHTGREEN_EX}")
    def TLS():
        tlszac = input("Enter the Domain Address: ")
        datam = {
            "url": "https://" + tlszac
        }
        zaclol = requests.post("https://geekflare.com/api/geekflare-api/tlsscan", json=datam, headers=headers2).text

        y = json.loads(zaclol)
        reqid = y["data"]["protocols"]
        print("TLS Bilgileri: ", reqid)
        input("Press ENTER For Exit.")
    TLS()

if choice == 12:
    print(f"{Fore.LIGHTRED_EX}DNS Record{Fore.LIGHTGREEN_EX}")
    def DNSRECORD():
        dnsrecord = input("Enter the Domain Address: ")

        datamiz = {
            "url": "https://" + dnsrecord
        }
        zacmrx = requests.post("https://geekflare.com/api/geekflare-api/dnsrecord", json=datamiz, headers=headers2).text
        xx = json.loads(zacmrx)
        xxyy = xx["data"]
        print("DNS Records Infos: ", xxyy)
        input("Press ENTER For Exit.")
    DNSRECORD()

if choice == 13:
    print(f"{Fore.LIGHTRED_EX}DNS Security Extensions Check{Fore.LIGHTGREEN_EX}")
    def DNSSEC():
        DNSSEC = input("Enter the Domain Address: ")
        datamizzz = {
            "url": "https://" + DNSSEC
        }
        rmrx = requests.post("https://geekflare.com/api/geekflare-api/dnssec", json=datamizzz, headers=headers2).text
        rr = json.loads(rmrx)
        print(rr["data"])
        input("Press ENTER For Exit.")
    DNSSEC()

if choice == 14:
    print(f"{Fore.LIGHTRED_EX}Honeypot Check{Fore.LIGHTGREEN_EX}")
    def Honeypot():
        honeypot = input("Enter the Token Address: ")
        honeydata = f"address={honeypot}&chain=bsc"
        honeyreq = requests.post(f"https://honeypot.api.rugdoc.io/api/honeypotStatus.js?address={honeypot}&chain=bsc",
                                 headers=headers, data=honeydata).text

        if "status\":\"OK" in honeyreq:
            print("Honeypot Passed")
        else:
            print(f"{Fore.RED}Invalid Token or Token've Honeypot{Fore.LIGHTRED_EX}")

        input("Press ENTER For Exit.")
    Honeypot()

