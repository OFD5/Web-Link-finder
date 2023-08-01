import re
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
import pyfiglet

def find_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any unsuccessful HTTP status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        links = set()

        # Extract links from anchor tags
        for anchor in soup.find_all('a', href=True):
            links.add(anchor['href'])

        # Extract links from image tags
        for img in soup.find_all('img', src=True):
            links.add(img['src'])

        # Filter out mailto and javascript links
        filtered_links = [link for link in links if not link.startswith('mailto:') and not link.startswith('javascript:')]

        return filtered_links

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error fetching the URL: {e}{Style.RESET_ALL}")
        return []

def print_banner():
    banner_text = pyfiglet.figlet_format("Web Link Finder")
    colored_banner = Fore.CYAN + banner_text + Style.RESET_ALL
    print(colored_banner)

def print_signature():
    signature = f"{Fore.MAGENTA}-- @ODF5 ,scripts can be incredibly powerful tools to automate tasks, gather information, or improve productivity, it's crucial to use them in an ethical and legal manner'.--{Style.RESET_ALL}\n"
    print(signature)

if __name__ == "__main__":
    print_banner()

    target_url = input("Enter the URL to find links: ")
    found_links = find_links(target_url)

    if found_links:
        print(f"{Fore.GREEN}Found {len(found_links)} links:{Style.RESET_ALL}")
        for link in found_links:
            print(Fore.BLUE + link + Style.RESET_ALL)
    else:
        print(f"{Fore.YELLOW}No links found.{Style.RESET_ALL}")

    print_signature()
