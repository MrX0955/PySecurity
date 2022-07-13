try:
    import requests
    import os
    import json
    import whois
    from colorama import Fore
    from bs4 import BeautifulSoup
    from lxml import html
except Exception:
    print("Modülleriniz Eksik.")

if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")

banner = f"""{Fore.LIGHTGREEN_EX} Izlegal[MrX] Forensic Tool"""

print(Fore.LIGHTRED_EX)
menu = """
    Izlegal[MrX] Forensic Tool
    Eğer 'Quoota Limit' diye hata verirse IP değiştirin.
    
 0 => Close The Program
 1 => Reverse DNS
 2 => DNS Lookup
 3 => Geolocation IP
 4 => Zone Transfer
 5 => DNS Host Records (Subdomains)
 6 => Reverse IP Lookup
 7 => ASN Lookup
 8 => Email Validator (ALL SMTP SERVER)
 9 => Have I Been Pwned?!
 10 => DMARC Lookup
 11 => TLS Scan
 12 => DNS Record ADVANCED
 13 => Screenshot Website
 14 => DNS Security Extensions Check
 15 => Honeypot Check (Default Binance Smart Chain)
 16 => HiJacking & Protocol Downgrade Attack in Headers Check
 17 => ClickJacking Security in Headers Check
 18 => XSS Vulnerability in Headers Check
 19 => WHOIS LOOKUP (JUST FOR DOMAIN ADDRESS)
 20 => CloudFlare Resolver
 21 => Hash Analyzer (Identifier)
"""

print(menu)

choice = int(input(" Choose ur want: "))
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

headerss = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
    "Content-Type": "application/json"
}

if choice == 1:
    def reversedns():
        dns = input(" IP Address: ")
        print("")
        r = requests.get(f"https://api.hackertarget.com/reversedns/?q={dns}")

        print(r.text, "| => Press ENTER For Exit.")
        input()

    reversedns()

if choice == 2:
    def dnslookup():
        lookup = input(" Domain Name: ")
        print("")
        x = requests.get(f"https://api.hackertarget.com/dnslookup/?q={lookup}")

        print(x.text), "| => Press ENTER For Exit."
        input()

    dnslookup()

if choice == 3:
    def geoip():
        geoip = input(" IP Address: ")
        print("")
        i = requests.get(f"https://api.hackertarget.com/geoip/?q={geoip}")

        print(i.text), "| => Press ENTER For Exit."
        input()

    geoip()

if choice == 4:
    def zonetransfer():
        zonetransfer = input(" IP Address: ")
        print("")
        z = requests.get(f"https://api.hackertarget.com/zonetransfer/?q={zonetransfer}")

        print(z.text), "| => Press ENTER For Exit."
        input()

    zonetransfer()

if choice == 5:
    def dnssubdomain():
        subdomain = input(" Domain Name: ")
        print("")
        k = requests.get(f"https://api.hackertarget.com/hostsearch/?q={subdomain}")

        print(k.text), "| => Press ENTER For Exit."
        input()

    dnssubdomain()

if choice == 6:
    def reverseip():
        reverseip = input(" IP Address: ")
        print("")
        mrx = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={reverseip}")

        print(mrx.text), "| => Press ENTER For Exit."
        input()

    reverseip()

if choice == 7:
    def ASN():
        asnlookup = input(" IP Address or ASN: ")
        print("")
        hasfa = requests.get(f"https://api.hackertarget.com/aslookup/?q={asnlookup}")

        print(hasfa.text), "| => Press ENTER For Exit."
        input()

    ASN()

if choice == 8:
    def emailvalid():
        mailvalid = input(" Email Gir: ")
        print("")

        datas = f'address=&email={mailvalid}&submit=Verify+Email+Address'
        mrxvalid = requests.post("https://www.iplocation.net/verify-email-address/", data=datas, headers=headers)

        if 'is a valid email' in mrxvalid.text:
            print("[+] Bu Mail E-Posta alabilir.")
        elif "is an invalid email" in mrxvalid.text:
            print("[-] Bu Mail Çalışmamaktadır.")
        input("Press ENTER For Exit.")

    emailvalid()

if choice == 9:
    def proxycheck():
        proxy = input(" Mail Address: ")
        print("")
        proxy.replace("@","%40")

        datas = f'email={proxy}&submit=Breached%3F'
        proxyy = requests.post("https://www.iplocation.net/data-breach-check", data=datas, headers=headers)

        if "Congratulations" in proxyy.text:
            print("[+] Private Mail Address")
        elif "We found" in proxyy.text:
            print("[-] Mail Public!!")
        input("Press ENTER For Exit.")

    proxycheck()

if choice == 10:
    def DMARC():
        ece = input(" Domain Address: ")
        print("")

        datas = f'url={ece}&submit='
        DMARCR = requests.post("https://tools.iplocation.net/dmarc-lookup", data=datas, headers=headers)

        if "v=DMARC1" in DMARCR.text:
            print("[+] Have Firewall")
        elif "No record found" in DMARCR.text:
            print("[-] No Firewall")
        input("Press ENTER For Exit.")

    DMARC()

if choice == 11:
    def TLS():
        tlszac = input(" Domain Address (örn: zaclol.dev): ")
        print()

        datam = {
            "url":"https://"+ tlszac
        }

        zaclol = requests.post("https://geekflare.com/api/geekflare-api/tlsscan", json=datam, headers=headerss).text

        y = json.loads(zaclol)
        reqid = y["data"]["protocols"]
        print("TLS Bilgileri: ", reqid)
        input("Press ENTER For Exit.")
    TLS()

if choice == 12:
    def DNSRECORD():
        dnsrecord = input(" Domain Address (örn: zaclol.dev): ")
        print()

        datamiz = {
            "url":"https://"+ dnsrecord
        }

        zacmrx = requests.post("https://geekflare.com/api/geekflare-api/dnsrecord", json=datamiz, headers=headerss).text

        xx = json.loads(zacmrx)
        xxyy = xx["data"]
        print("DNS Records Infos: ",xxyy)
        input("Press ENTER For Exit.")

    DNSRECORD()

if choice == 13:
    def screenshot():
        ss = input(" Domain Address For ScreenShot: ")
        print()

        datamizz = {
            "url":"https://"+ ss
        }

        reqss = requests.post("https://geekflare.com/api/geekflare-api/screenshot", json=datamizz, headers=headerss).text

        ii = json.loads(reqss)
        iibb = ii["data"]
        print("Screenshot URL => ",iibb)
        input("Press ENTER For Exit.")

    screenshot()

if choice == 14:
    def DNSSEC():
        DNSSEC = input(" Domain Address: ")
        print()

        datamizzz = {
            "url":"https://"+ DNSSEC
        }

        rmrx = requests.post("https://geekflare.com/api/geekflare-api/dnssec", json=datamizzz, headers=headerss).text

        rr = json.loads(rmrx)
        print(rr["data"])
        input("Press ENTER For Exit.")

    DNSSEC()

if choice == 15:
    def Honeypot():
        honeypot = input(" Token Address: ")
        print()

        honeydata = f"address={honeypot}&chain=bsc"

        honeyreq = requests.post(f"https://honeypot.api.rugdoc.io/api/honeypotStatus.js?address={honeypot}&chain=bsc", headers=headers, data=honeydata).text

        if "status\":\"OK" in honeyreq:
            print("Honeypot Passed")
        else:
            print("Invalid Token or Token've Honeypot")

        input("Press ENTER For Exit.")

    Honeypot()

if choice == 16:
    def JSVuln():
        # HiJacking & Protocol Downgrade Attack
        istek = input(" Domain addres: ")
        print()

        data = {"url": istek, "type": "hsts-test"}

        r = requests.post("https://geekflare.com/tools/api/http-header", headers=headerss, json=data).text
        if "strict-transport-security" in r:
            print("[+] ENABLED HTTP Strict Transport Security. in response headers")
        elif not "strict-transport-security" in r:
            print("[-] No Security. Have Vulnerability!!")
        input("Press ENTER For Exit.")
    JSVuln()

if choice == 17:
    def ClickJacking():

        wuhu = input(" Domain Address: ")
        print()

        dataa = {"url": wuhu, "type": "x-frame-options-test"}

        req = requests.post("https://geekflare.com/tools/api/http-header", headers=headerss, json=dataa).text

        if "x-frame-options" in req:
            print("[+] ENABLED ClickJacking Security in response headers.")
        elif not "x-frame-options" in req:
            print("[-] No Security. Have Vulnerability!!")
        input("Press ENTER For Exit.")
    ClickJacking()

if choice == 18:
    def XSS():

        istekxss = input(" Domain Address: ")
        print()

        datasss = {"url": istekxss, "type": "mime-sniffing-test"}

        reqs = requests.post("https://geekflare.com/tools/api/http-header", headers=headerss, json=datasss).text

        if "x-content-type-options" in reqs:
            print("[+] ENABLED XSS Protection! in response headers")
        elif not "x-content-type-options" in reqs:
            print("[-] No Security. Have Vulnerability!!")
        input("Press ENTER For Exit.")
    XSS()

if choice == 19:
    def WHOIS():

        whoiss = input(" Domain Address: ")
        print()
        w = whois.whois(whoiss)
        var = w.text
        print(w)
        input("Press ENTER For Exit.")

    WHOIS()

if choice == 20:
    def CF():

        cloudflare = input(" Enter Domain Address: ")
        print()

        datax = f"action=PostData&string={cloudflare}"

        headersx = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "Pragma": "no-cache",
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "x-requested-with": "XMLHttpRequest",
            "referer": "https://webresolver.nl/tools/cloudflare",
            "origin": "https://webresolver.nl"
        }

        req = requests.post("https://webresolver.nl/ajax/tools/cloudflare", data=datax, headers=headersx).text
        var = req.replace("<br>", " ")
        varmi = var.replace("</b><br />", " ")
        varherhalde = varmi.replace("<b>", " ")
        KT = varherhalde.replace("Cloudflare Resolver", " ")
        print(KT)
        input("Press ENTER For Exit.")

    CF()
if choice == 21:
    def Identifier():

        page = requests.get("https://hashes.com/en/tools/hash_identifier")
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(type="hidden")
        TK = title.attrs.get('value')
        coq = page.cookies.get_dict()

        hash = input("Hash Giriniz: ")
        print()

        headersi = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "Connection": "keep-alive",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Content-Type": "application/x-www-form-urlencoded",
            "referer": "https://hashes.com/en/tools/hash_identifier",
            "origin": "https://hashes.com"
        }

        data = f"csrf_token={TK}&hashes={hash}&submitted=true"
        req = requests.post("https://hashes.com/en/tools/hash_identifier", data=data, cookies=coq, headers=headersi)
        if "border-success text-success" in req.text:
            tree = html.fromstring(req.content)
            Final = tree.xpath('/html/body/div[1]/div[2]/div/div[3]/pre/div/text()')
            print(Final)
        else:
            print("Algoritma Bulunamadı")
        input("Press ENTER For Exit.")

    Identifier()
