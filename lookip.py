import requests
import sys

def ip_lookup(ip_address):
    # API IPinfo
    ipinfo_url = f"https://ipinfo.io/{ip_address}/json"
    ipinfo_response = requests.get(ipinfo_url)
    ipinfo_data = ipinfo_response.json()

    # API ip-api
    ipapi_url = f"http://ip-api.com/json/{ip_address}"
    ipapi_response = requests.get(ipapi_url)
    ipapi_data = ipapi_response.json()

    # Agrégation des informations des deux sources
    result = {
        "Adresse IP": ip_address,
        "IPinfo": {
            "IP": ipinfo_data.get("ip"),
            "Nom d'hôte": ipinfo_data.get("hostname"),
            "Ville": ipinfo_data.get("city"),
            "Région": ipinfo_data.get("region"),
            "Pays": ipinfo_data.get("country"),
            "Localisation": ipinfo_data.get("loc"),
            "Organisation": ipinfo_data.get("org"),
            "Code postal": ipinfo_data.get("postal"),
            "Fuseau horaire": ipinfo_data.get("timezone"),
        },
        "ip-api": {
            "Pays": ipapi_data.get("country"),
            "Région": ipapi_data.get("regionName"),
            "Ville": ipapi_data.get("city"),
            "Code postal": ipapi_data.get("zip"),
            "Latitude": ipapi_data.get("lat"),
            "Longitude": ipapi_data.get("lon"),
            "FAI": ipapi_data.get("isp"),
            "Organisation": ipapi_data.get("org"),
            "AS": ipapi_data.get("as"),
            "DNS inversé": ipapi_data.get("reverse"),
            "Mobile": ipapi_data.get("mobile"),
            "Proxy": ipapi_data.get("proxy"),
        }
    }

    return result

def print_result(result):
    print(f"Informations pour l'adresse IP : {result['Adresse IP']}\n")
    
    print("Données IPinfo :")
    for key, value in result['IPinfo'].items():
        print(f"  {key}: {value}")
    
    print("\nDonnées ip-api :")
    for key, value in result['ip-api'].items():
        print(f"  {key}: {value}")
    
    # Ajout du message personnalisé en violet
    violet = "\033[35m"
    reset = "\033[0m"
    print(f"\n{violet}Himmler ・ discord.gg/searchhub{reset}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("---> python lookip.py <ADRESSE_IP>")
        sys.exit(1)

    ip_address = sys.argv[1]
    info = ip_lookup(ip_address)
    print_result(info)
