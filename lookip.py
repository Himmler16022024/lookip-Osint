import requests
import os

def ip_lookup(ip_address):
    ipinfo_url = f"https://ipinfo.io/{ip_address}/json"
    ipinfo_response = requests.get(ipinfo_url)
    ipinfo_data = ipinfo_response.json()

    ipapi_url = f"http://ip-api.com/json/{ip_address}"
    ipapi_response = requests.get(ipapi_url)
    ipapi_data = ipapi_response.json()

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
    separator = "=" * 50
    header = f"""
\033[35m██╗      ██████╗  ██████╗ ██╗  ██╗██╗██████╗ 
██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║██╔══██╗
██║     ██║   ██║██║   ██║█████╔╝ ██║██████╔╝
██║     ██║   ██║██║   ██║██╔═██╗ ██║██╔═══╝ 
███████╗╚██████╔╝╚██████╔╝██║  ██╗██║██║     
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝     
\033[0m    """
    print(header)
    print(separator)
    print(f"Informations pour l'adresse IP : {result['Adresse IP']}")
    print(separator)
    
    print("🔍 Données IPinfo :")
    for key, value in result['IPinfo'].items():
        print(f"  {key}: {value}")
    
    print(separator)
    print("🌐 Données ip-api :")
    for key, value in result['ip-api'].items():
        print(f"  {key}: {value}")
    
    violet = "\033[35m"
    reset = "\033[0m"
    print(separator)
    print(f"\n{violet}Himmler / discord.gg/searchhub{reset}")
    print(separator)

if __name__ == "__main__":
    intro = """
\033[35m██╗      ██████╗  ██████╗ ██╗  ██╗██╗██████╗ 
██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║██╔══██╗
██║     ██║   ██║██║   ██║█████╔╝ ██║██████╔╝
██║     ██║   ██║██║   ██║██╔═██╗ ██║██╔═══╝ 
███████╗╚██████╔╝╚██████╔╝██║  ██╗██║██║     
╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝     
\033[0m    """
    print(intro)
    print("Bienvenue dans le tool lookip !")
    print("Veuillez entrer l'adresse IP cible pour commencer.")
    print("=" * 50)
    
    while True:
        ip_address = input("Entrez l'adresse IP : ")

        if not ip_address.strip():
            print("L'adresse IP ne peut pas être vide. Veuillez entrer une adresse IP valide.")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            info = ip_lookup(ip_address)
            print_result(info)
        
        repeat = input("Voulez-vous rechercher une autre adresse IP ? (o/n) : ").strip().lower()
        if repeat != 'o':
            print("Merci d'avoir utilisé lookip. Au revoir!")
            break
