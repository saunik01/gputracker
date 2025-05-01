import requests
from bs4 import BeautifulSoup
import json

def fetch_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check if the request was successful (status code 200)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Try to find price using common patterns
        possible_selectors = [
            '.product-price',           # Example for Verkkokauppa (update with correct selector)
            '.price-value',             # Example for Multitronic (update with correct selector)
            '.price',                   # Example for Jimms (update with correct selector)
            'meta[itemprop=price]'      # Structured data
        ]

        for selector in possible_selectors:
            el = soup.select_one(selector)
            if el:
                return el.text.strip()

        return "❌ Price not found"

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return "❌ Price not found"

# List of all product URLs
urls = [
    # NVIDIA RTX 4070
    "https://www.verkkokauppa.com/fi/product/910810/AsusGeForce-DUAL-RTX4070-O12G-EVO-naytonohjain",  # Verkkokauppa
    "https://www.multitronic.fi/fi/products/3999119/gainward-geforce-rtx4070-ghost--naytonohjain",      # Multitronic

    # RX 7800 XT
    "https://www.verkkokauppa.com/fi/product/926983/AsusAMD-Radeon-DUAL-RX7800XT-O16G-naytonohjain",    # Verkkokauppa
    "https://www.multitronic.fi/en/products/4003889/gigabyteradeon-rx-7800-xt-gaming-oc-16gb---graphics-card", # Multitronic
    "https://www.jimms.fi/fi/Product/Show/195667/rx7800xt-cl16go/asrock-radeon-rx-7800-xt-challenger-oc-naytonohjain-16gb-gddr6", # Jimms

    # Intel Arc A770
    "https://www.multitronic.fi/en/products/4360927/asrock-intelarc-a770-challenger-16gb-oc",  # Multitronic
    "https://www.jimms.fi/fi/Product/Show/201583/sa770t16goc/sparkle-intel-arc-a770-titan-oc-edition-naytonohjain-16gb-gddr6",  # Jimms

    # NVIDIA RTX 4060 Ti
    "https://www.verkkokauppa.com/fi/product/918415/AsusGeForce-DUAL-RTX4060-O8G-EVO-naytonohjain",  # Verkkokauppa
    "https://www.multitronic.fi/fi/products/4093494/gigabytegeforce-rtx-4060-ti-windforce-oc-8g--naytonohjain",  # Multitronic
    "https://www.jimms.fi/fi/Product/Show/207299/dual-rtx4060ti-o8gevo-white/asus-geforce-rtx-4060-ti-dual-white-evo-oc-editionnaytonohjain-8gb-gddr6",  # Jimms

    # AMD RX 7900 XTX
    "https://www.verkkokauppa.com/fi/product/848143/AsusAMD-Radeon-TUF-RX7900XT-O20G-GAMING-naytonohjain",  # Verkkokauppa
    "https://www.multitronic.fi/en/products/3906766/xfx-radeonrx-7900-xt-speedster-merc-310-20-gb---graphics-card",  # Multitronic
    "https://www.jimms.fi/fi/Product/Show/188164/rx7900xtx-24g-loc/powercolor-radeon-rx-7900-xtx-hellhound-naytonohjain-24gb-gddr6",  # Jimms

    # NVIDIA RTX 4080 Super
    "https://www.verkkokauppa.com/fi/product/911419/MSIGeForce-RTX-4080-SUPER-16G-VENTUS-3X-OC-naytonohjain",  # Verkkokauppa
    "https://www.multitronic.fi/en/products/4367191/zotacgeforce-rtx-4080-super-trinity-black-edition-16gb---graphics-card"  # Multitronic
]

# Dictionary to store scraped prices
gpu_prices = {}

# Loop through all URLs and fetch prices
for url in urls:
    price = fetch_price(url)
    gpu_prices[url] = price

# Save results to JSON file
with open("gpu_prices.json", "w") as f:
    json.dump(gpu_prices, f, indent=4)

print("Scraping complete! Results saved to gpu_prices.json")
