import requests, time, sys, json, config as c

def getCrypto(cname):

    if c.usd == True:
        crypto = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=" + cname + "&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=false")

    elif c.eur == True:
        crypto = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=" + cname + "&vs_currencies=eur&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=false")

    else:
        print("Enable 1 versus pair! Closing in 5s!")
        time.sleep(5)
        sys.exit(0)

    cryptol = json.loads(crypto.text)
    cryptob = cryptol[cname]

    if c.usd == True:
        cryptoprice = cryptob.get("usd")
        crypto24hc = round(cryptob.get("usd_24h_change"), 2)
        crypto24hv = round(cryptob.get("usd_24h_vol"))
        cryptomc = round(cryptob.get("usd_market_cap"))

    elif c.eur == True:
        cryptoprice = cryptob.get("eur")
        crypto24hc = round(cryptob.get("eur_24h_change"), 2)
        crypto24hv = round(cryptob.get("eur_24h_vol"))
        cryptomc = round(cryptob.get("eur_market_cap"))

    cname = cname.capitalize()

    print(u"\u2554", cname)

    if c.usd == True:
        print(u"\u2560", "Price:", cryptoprice, "$")
    elif c.eur == True:
        print(u"\u2560", "Price:", cryptoprice, "€")

    print(u"\u2560", "24h change:", crypto24hc, "%")

    if c.usd == True:
        print(u"\u2560", "24h volume:", crypto24hv, "$")
    elif c.eur == True:
        print(u"\u2560", "24h volume:", crypto24hv, "€")

    if c.usd == True:
        print(u"\u255A", "Market cap:", cryptomc, "$")
    elif c.eur == True:
        print(u"\u255A", "Market cap:", cryptomc, "€")

    print("\n")

r = requests.get("https://api.coingecko.com/api/v3/ping")
if r.status_code == 200:

    print("Starting CryptoFetcher! Powered by Coingecko!")
    print("\n")
    whilevalue = 1

    while whilevalue == 1:

        if c.btc == True:
            getCrypto("bitcoin")
            if c.eth == False | c.dot == False:
                time.sleep(c.request_time)

        if c.eth == True:
            getCrypto("ethereum")
            if c.dot == False:
                time.sleep(c.request_time)

        if c.dot == True:
            getCrypto("polkadot")
            time.sleep(c.request_time)

        else:
            print("Every pair is set to false! Closing in 5s!")
            time.sleep(5)
            sys.exit(0)


elif r.status_code == 404:
    print("Coingecko API is not available! Closing in 5s!")
    time.sleep(5)
    sys.exit(0)

else:
    print("Unknown Error! Closing in 5s!")
    time.sleep(5)
    sys.exit(0)