import sys
import requests
import json
def main():
    if len(sys.argv) < 2:
        sys.exit
        print("No argument")
        exit()

    b = sys.argv[1]
    try:
        float(b)
    except:
        print("Argument Invalid")

    b = float(b)   #number of bitcoin
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')        # price of bitcoin
    p = json.loads(r.text)
    e = (p['bpi']['USD']['rate_float'])
    g = (e*b)
    print(f"${g:,.4f}")



if __name__ == "__main__":
    main()