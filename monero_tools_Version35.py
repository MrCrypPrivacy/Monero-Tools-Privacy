#!/usr/bin/env python3
import os
import random
import json
import requests
import shutil
import webbrowser

SETTINGS_FILE = "settings.txt"
FAVORITES_FILE = "favorites.txt"

THEMES = {
    "dark": {
        "GREEN_BOLD": "\033[1;92m",
        "ORANGE_BOLD": "\033[38;5;208m",
        "CYAN": "\033[96m",
        "YELLOW": "\033[93m",
        "BLUE": "\033[94m",
        "MAGENTA": "\033[95m",
        "RED": "\033[91m",
        "WHITE": "\033[97m",
        "BOLD": "\033[1m",
        "RESET": "\033[0m",
        "DIM": "\033[2m",
        "NOTICE": "\033[1;93m",
        "GRAY": "\033[90m"
    },
    "light": {
        "GREEN_BOLD": "\033[1;32m",
        "ORANGE_BOLD": "\033[38;5;208m",
        "CYAN": "\033[36m",
        "YELLOW": "\033[33m",
        "BLUE": "\033[34m",
        "MAGENTA": "\033[35m",
        "RED": "\033[31m",
        "WHITE": "\033[97m",
        "BOLD": "\033[1m",
        "RESET": "\033[0m",
        "DIM": "\033[2m",
        "NOTICE": "\033[1;33m",
        "GRAY": "\033[37m"
    }
}

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                theme = data.get("theme", "dark")
                return theme if theme in THEMES else "dark"
        except Exception:
            return "dark"
    return "dark"

def save_settings(theme):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump({"theme": theme}, f)

def load_favorites():
    favs = []
    if os.path.exists(FAVORITES_FILE):
        with open(FAVORITES_FILE, "r", encoding="utf-8") as f:
            for line in f:
                fav = line.strip()
                if fav:
                    favs.append(fav)
    return favs

def save_favorites(favs):
    with open(FAVORITES_FILE, "w", encoding="utf-8") as f:
        for fav in favs:
            f.write(fav + "\n")

EMOJIS = {
    "Official Website": "🌐",
    "Docs & Guides": "📚",
    "Wallet": "👜",
    "Purchase XMR": "💸",
    "Swap": "🔄",
    "Spend Monero": "🛒",
    "XMR Chat": "💬",
    "Best Accounts to Follow": "🌟",
    "Miner tools": "⛏️",
    "Privacy tools": "🕵️"
}

TIPS = [
    "Tip: Never share your seed phrase with anyone.",
    "Tip: Use a VPN for enhanced privacy.",
    "Tip: Check getmonero.org for the latest wallet versions.",
    "Tip: Monero transactions are confidential by default.",
    "Tip: Always verify downloads with hashes/signatures.",
    "Tip: For P2P swaps, use decentralized platforms.",
    "Tip: Use multiple wallets for extra privacy.",
    "Tip: XMR is accepted at more merchants every year!",
]

official_website = [
    {"id": "getmonero", "name": "getmonero.org", "url": "https://getmonero.org/", "x": "https://x.com/monero"}
]

docs_guides = [
    {"id": "localmonero", "name": "LocalMonero Knowledge", "url": "https://localmonero.co/knowledge", "x": "https://x.com/LocalMoneroCo"},
    {"id": "getmonerodev", "name": "getmonero.dev", "url": "https://getmonero.dev/", "x": ""},
    {"id": "monerostudy", "name": "docs.monero.study", "url": "https://docs.monero.study/", "x": ""},
    {"id": "sethprivacy", "name": "Seth For Privacy Guides", "url": "https://sethforprivacy.com/", "x": "https://x.com/sethforprivacy"},
]

wallets = [
    {"id": "cakewallet", "name": "Cake Wallet", "url": "https://cakewallet.com/", "x": "https://x.com/cakewallet"},
]

purchase_xmr = [
    {"id": "kraken", "name": "Kraken", "url": "https://www.kraken.com/", "x": "https://x.com/krakenfx"},
    {"id": "cakewalletbuy", "name": "Cake Wallet In-App", "url": "https://cakewallet.com/", "x": "https://x.com/cakewallet"},
    {"id": "retoswap", "name": "RetoSwap", "url": "https://retoswap.app/", "x": "https://x.com/RetoSwap"},
]

swap = [
    {"id": "trocador", "name": "Trocador App", "url": "https://trocador.app/", "x": "https://x.com/TrocadorApp"},
    {"id": "basicswap", "name": "BasicSwap DEX", "url": "https://basicswapdex.com/", "x": "https://x.com/BasicSwapDEX"},
]

spend_monero = [
    {"id": "monerica", "name": "Monerica Project", "url": "https://monerica.com/", "x": "https://x.com/MonericaProject"},
    {"id": "xmrbazaar", "name": "XMR Bazaar", "url": "https://xmrbazaar.net/", "x": "https://x.com/xmrbazaar"},
]

xmr_chat = [
    {"id": "xmrchat", "name": "XMR Chat", "url": "https://xmr.chat/", "x": "https://x.com/xmr_chat"},
]

best_accounts = [
    {
        "id": "vikrantnyc",
        "name": "vikrantnyc (𝕏)",
        "url": "https://x.com/vikrantnyc",
        "x": "https://x.com/vikrantnyc"
    },
    {
        "id": "sethforprivacy",
        "name": "sethforprivacy (𝕏)",
        "url": "https://x.com/sethforprivacy",
        "x": "https://x.com/sethforprivacy"
    },
    {
        "id": "cakewallet",
        "name": "cakewallet (𝕏)",
        "url": "https://x.com/cakewallet",
        "x": "https://x.com/cakewallet"
    },
    {
        "id": "l0rdt0ken",
        "name": "𝕄𝕣ℂ𝕣𝕪𝕡 ㉿ (𝕏)",
        "url": "https://x.com/L0rd_t0ken",
        "x": "https://x.com/L0rd_t0ken"
    },
    {
        "id": "DontTraceMeBruh",
        "name": "ᴜɴᴛʀᴀᴄᴇᴀʙʟᴇ (𝕏)",
        "url": "https://x.com/DontTraceMeBruh",
        "x": "https://x.com/DontTraceMeBruh"
    },
    {
        "id": "xmrbazaar",
        "name": "xmrbazaar (𝕏)",
        "url": "https://x.com/xmrbazaar",
        "x": "https://x.com/xmrbazaar"
    },
]

privacy_tools = [
    {
        "section": "Browsers & Web Privacy",
        "items": [
            {"id": "mullvadbrowser", "name": "Mullvad Browser", "url": "https://mullvad.net/en/download/browser/", "x": "https://x.com/mullvadnet"},
            {"id": "brave", "name": "Brave Browser", "url": "https://brave.com/", "x": "https://x.com/brave"},
            {"id": "librewolf", "name": "Librewolf", "url": "https://librewolf.net/", "x": "https://x.com/librewolfbrowser"},
            {"id": "torbrowser", "name": "Tor Browser", "url": "https://www.torproject.org/", "x": "https://x.com/torproject"},
            {"id": "ungoogledchromium", "name": "Ungoogled Chromium", "url": "https://ungoogled-software.github.io/", "x": ""}
        ]
    },
    {
        "section": "Messaging",
        "items": [
            {"id": "session", "name": "Session", "url": "https://getsession.org/", "x": "https://x.com/session_app"},
            {"id": "simplex", "name": "SimpleX", "url": "https://simplex.chat/", "x": "https://x.com/simplexchat"},
            {"id": "briar", "name": "Briar", "url": "https://briarproject.org/", "x": "https://x.com/BriarApp"},
            {"id": "element", "name": "Element (Matrix)", "url": "https://element.io/", "x": "https://x.com/element_hq"}
        ]
    },
    {
        "section": "Email Services",
        "items": [
            {"id": "protonmail", "name": "Proton Mail", "url": "https://proton.me/mail", "x": "https://x.com/ProtonPrivacy"},
            {"id": "tutanota", "name": "Tutanota", "url": "https://tutanota.com/", "x": "https://x.com/TutanotaTeam"},
            {"id": "mailbox", "name": "Mailbox.org", "url": "https://mailbox.org/en/", "x": "https://x.com/mailbox_org"},
            {"id": "simplelogin", "name": "SimpleLogin", "url": "https://simplelogin.io/", "x": "https://x.com/simplelogin"},
            {"id": "anonaddy", "name": "AnonAddy", "url": "https://anonaddy.com/", "x": "https://x.com/anonaddy"}
        ]
    },
    {
        "section": "Password Managers",
        "items": [
            {"id": "keepassxc", "name": "KeePassXC", "url": "https://keepassxc.org/", "x": "https://x.com/keepassxc"},
            {"id": "bitwarden", "name": "Bitwarden (self-hosted)", "url": "https://bitwarden.com/", "x": "https://x.com/bitwarden"},
            {"id": "lesspass", "name": "LessPass", "url": "https://lesspass.com/", "x": ""}
        ]
    },
    {
        "section": "VPN",
        "items": [
            {"id": "LNVPN.net", "name": "LNVPN.net", "url": "https://lnvpn.net/", "x": "https://x.com/ln_vpn"},
            {"id": "mullvad", "name": "Mullvad VPN", "url": "https://mullvad.net/", "x": "https://x.com/mullvadnet"},
            {"id": "protonvpn", "name": "Proton VPN", "url": "https://protonvpn.com/", "x": "https://x.com/ProtonPrivacy"},
            {"id": "ivpn", "name": "IVPN", "url": "https://www.ivpn.net/", "x": "https://x.com/ivpnnet"},
            {"id": "riseupvpn", "name": "Riseup VPN", "url": "https://riseup.net/en/vpn", "x": ""},
            {"id": "windscribe", "name": "Windscribe", "url": "https://windscribe.com/", "x": "https://x.com/windscribecom"}
        ]
    },
    {
        "section": "2FA Apps",
        "items": [
            {"id": "aegis", "name": "Aegis Authenticator", "url": "https://getaegis.app/", "x": "https://x.com/AEGISAuth"},
            {"id": "andotp", "name": "andOTP", "url": "https://github.com/andOTP/andOTP", "x": ""},
            {"id": "freeotp", "name": "FreeOTP", "url": "https://freeotp.github.io/", "x": ""},
            {"id": "raivootp", "name": "Raivo OTP (iOS)", "url": "https://raivo-otp.com/", "x": ""}
        ]
    },
    {
        "section": "Secure Cloud Storage",
        "items": [
            {"id": "internxt", "name": "Internxt", "url": "https://internxt.com/", "x": "https://x.com/internxt"},
            {"id": "protondrive", "name": "Proton Drive", "url": "https://proton.me/drive", "x": "https://x.com/ProtonPrivacy"},
            {"id": "tresorit", "name": "Tresorit", "url": "https://tresorit.com/", "x": "https://x.com/tresorit"}
        ]
    }
]

categories = [
    {"title": "Official Website", "list": official_website},
    {"title": "Docs & Guides", "list": docs_guides},
    {"title": "Wallet", "list": wallets},
    {"title": "Purchase XMR", "list": purchase_xmr},
    {"title": "Swap", "list": swap},
    {"title": "Spend Monero", "list": spend_monero},
    {"title": "XMR Chat", "list": xmr_chat},
    {"title": "Best Accounts to Follow", "list": best_accounts},
    {"title": "Miner tools", "list": []},  # Section 9: under construction
    {"title": "Privacy tools", "list": privacy_tools},
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_width():
    try:
        columns = shutil.get_terminal_size().columns
        return max(columns, 60)
    except Exception:
        return 80

def center_text(text):
    width = get_terminal_width()
    return text.center(width)

def print_centered(text, color="", bold=False):
    width = get_terminal_width()
    style = ""
    if bold:
        style += COLORS["BOLD"]
    if color:
        style += color
    for line in text.splitlines():
        print(f"{style}{line.center(width)}{COLORS['RESET']}")

def print_horizontal_line(char="─"):
    width = get_terminal_width()
    print(char * width)

def open_url(url):
    webbrowser.open(url)

def print_tip():
    tip = random.choice(TIPS)
    print_centered(f"{COLORS['CYAN']}{COLORS['DIM']}{tip}{COLORS['RESET']}")

def print_error(msg):
    print(COLORS["RED"] + COLORS["BOLD"] + center_text(msg) + COLORS["RESET"])

def get_xmr_price():
    try:
        resp = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd", timeout=5)
        data = resp.json()
        price = data["monero"]["usd"]
        return price
    except Exception:
        return None

def save_theme_and_reload(new_theme):
    global COLORS
    COLORS = THEMES[new_theme]
    save_settings(new_theme)

def is_favorite(item_id, favorites):
    return item_id in favorites

def add_favorite(item_id, favorites):
    if item_id not in favorites:
        favorites.append(item_id)
        save_favorites(favorites)

def remove_favorite(item_id, favorites):
    if item_id in favorites:
        favorites.remove(item_id)
        save_favorites(favorites)

def ascii_header():
    logo = r"""
███╗    ███╗   ███╗ ██████╗ ███╗   ██╗███████╗██████╗  ██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗    ███╗
██╔╝    ████╗ ████║██╔═══██╗████╗  ██║██╔════╝██╔══██╗██╔═══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝    ╚██║
██║     ██╔████╔██║██║   ██║██╔██╗ ██║█████╗  ██████╔╝██║   ██║       ██║   ██║   ██║██║   ██║██║     ███████╗     ██║
██║     ██║╚██╔╝██║██║   ██║██║╚██╗██║██╔══╝  ██╔══██╗██║   ██║       ██║   ██║   ██║██║   ██║██║     ╚════██║     ██║
███╗    ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║███████╗██║  ██║╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗███████║    ███║
╚══╝    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚══╝
                                                                                                                      
    """
    print_horizontal_line()
    print_centered(logo, color=COLORS["ORANGE_BOLD"])
    print_centered("Created by Mr Cryp", color=COLORS["GREEN_BOLD"], bold=True)
    print_horizontal_line()

def welcome_screen():
    clear_screen()
    ascii_header()
    print()
    print_centered("Monero Tools Menu By Mr Cryp", color=COLORS["GREEN_BOLD"], bold=True)
    print()
    notice_text = "Notice: This tool does not store data and is for educational use only."
    print_centered(notice_text, color=COLORS["NOTICE"], bold=True)
    print_horizontal_line()
    print()
    print_tip()
    print()
    input(center_text("Press ENTER to continue..."))
    clear_screen()

def show_support():
    clear_screen()
    ascii_header()
    print()
    print_centered("Thank you for using Monero Tools Menu By Mr Cryp!", bold=True)
    print()
    print_centered("If you'd like to support this project, you can donate privately:")
    print()
    print_centered(f"{COLORS['YELLOW']}Monero (XMR):{COLORS['RESET']} 87k6ViTfSFGApzyyqr8jsuELYeBQ37yvndCWJcHgHDUf97LUz36JUutBtJiBYNBBDJeBCPN8gf6jW9f3HgJKeMsbUx3VsB5")
    print_centered(f"{COLORS['YELLOW']}Bitcoin Silent Payments (BTC):{COLORS['RESET']} sp1qqg2s548t58g5x32jdhl33rxm8zy5r9aw3r7vrqfvrgjjz2c88dz96qc8qdge727xkd8umlwfr88gutqtu4dslrtkza0p6j0u44hwsgglmuky4xjj")
    print()
    print_centered(f"𝕏: https://x.com/L0rd_t0ken")
    print_centered("Website: Under construction")
    print()
    input(center_text("Press ENTER to return to the menu..."))
    clear_screen()

def show_subsections(subsections, favorites, parent_title):
    while True:
        clear_screen()
        ascii_header()
        print()
        print_centered(f"{COLORS['BOLD']}{parent_title}{COLORS['RESET']}", bold=True)
        print_horizontal_line()
        for idx, sub in enumerate(subsections, start=1):
            print_centered(f"{COLORS['YELLOW']}[{idx}]{COLORS['RESET']} {sub['section']}")
        print()
        print_centered(f"{COLORS['YELLOW']}[B]{COLORS['RESET']} Back")
        print_centered(f"{COLORS['MAGENTA']}{COLORS['BOLD']}[M] Main menu{COLORS['RESET']}")
        print()
        choice = input("Choose a subsection: ").strip().upper()
        if choice == "B":
            break
        if choice == "M":
            return "main"
        try:
            idx = int(choice)
            if 1 <= idx <= len(subsections):
                ret = show_subsection_items(subsections[idx-1], favorites, parent_title)
                if ret == "main":
                    return "main"
            else:
                print_error("Invalid option. Please try again.")
                input(center_text("Press ENTER to continue..."))
        except ValueError:
            print_error("Invalid input. Please enter a number.")
            input(center_text("Press ENTER to continue..."))

def show_subsection_items(subsection, favorites, parent_title):
    while True:
        clear_screen()
        ascii_header()
        print()
        print_centered(f"{COLORS['BOLD']}{parent_title} - {subsection['section']}{COLORS['RESET']}", bold=True)
        print_horizontal_line()
        for idx, item in enumerate(subsection["items"], start=1):
            fav = "★" if is_favorite(item["id"], favorites) else " "
            print_centered(f"{COLORS['YELLOW']}[{idx}]{COLORS['RESET']} {fav}{item['name']}")
        print()
        print_centered(f"{COLORS['YELLOW']}[B]{COLORS['RESET']} Back")
        print_centered(f"{COLORS['MAGENTA']}{COLORS['BOLD']}[M] Main menu{COLORS['RESET']}")
        print()
        choice = input("Choose an item: ").strip().upper()
        if choice == "B":
            break
        if choice == "M":
            return "main"
        try:
            idx = int(choice)
            if 1 <= idx <= len(subsection["items"]):
                ret = show_item_detail(subsection["items"][idx-1], favorites)
                if ret == "main":
                    return "main"
            else:
                print_error("Invalid option. Please try again.")
                input(center_text("Press ENTER to continue..."))
        except ValueError:
            print_error("Invalid input. Please enter a number.")
            input(center_text("Press ENTER to continue..."))

def show_item_detail(item, favorites):
    show_only_x = (
        item.get("id") in ["vikrantnyc", "sethforprivacy", "cakewallet", "l0rdt0ken", "DontTraceMeBruh", "xmrbazaar"]
        and item.get("x", "").startswith("https://x.com")
    )

    while True:
        clear_screen()
        ascii_header()
        print()
        name_line = f"{COLORS['YELLOW']}{COLORS['BOLD']}{item['name']}{COLORS['RESET']}"
        print_centered(name_line, bold=True)
        print_centered(COLORS['DIM'] + "-" * len(item['name']) + COLORS['RESET'])
        print()
        option_map = {}
        optnum = 1
        if show_only_x:
            print_centered(f"{COLORS['YELLOW']}[{optnum}]{COLORS['RESET']} Open 𝕏 profile")
            option_map[str(optnum)] = "x"
            optnum += 1
        else:
            if item.get("url"):
                print_centered(f"{COLORS['YELLOW']}[{optnum}]{COLORS['RESET']} Open website")
                option_map[str(optnum)] = "website"
                optnum += 1
            if item.get("x"):
                print_centered(f"{COLORS['YELLOW']}[{optnum}]{COLORS['RESET']} Open 𝕏 profile")
                option_map[str(optnum)] = "x"
                optnum += 1
        if is_favorite(item["id"], favorites):
            print_centered(f"{COLORS['YELLOW']}[F]{COLORS['RESET']} Remove from favorites")
        else:
            print_centered(f"{COLORS['YELLOW']}[F]{COLORS['RESET']} Add to favorites")
        print()
        print_centered(f"{COLORS['YELLOW']}[B]{COLORS['RESET']} Back")
        print_centered(f"{COLORS['MAGENTA']}{COLORS['BOLD']}[M] Main menu{COLORS['RESET']}")
        print()
        choice = input("Choose an option: ").strip().upper()
        if choice in option_map:
            if option_map[choice] == "website":
                open_url(item['url'])
            elif option_map[choice] == "x":
                open_url(item['x'])
        elif choice == "B":
            break
        elif choice == "M":
            return "main"
        elif choice == "F":
            if is_favorite(item["id"], favorites):
                remove_favorite(item["id"], favorites)
                print_centered("Removed from favorites.", color=COLORS["CYAN"])
            else:
                add_favorite(item["id"], favorites)
                print_centered("Added to favorites.", color=COLORS["CYAN"])
            input(center_text("Press ENTER to continue..."))
        else:
            print_error("Invalid option. Please try again.")
            input(center_text("Press ENTER to continue..."))

def category_menu(title, items, description, favorites):
    if title == "Miner tools":
        clear_screen()
        ascii_header()
        print_centered("The Miner section is under construction.", color=COLORS["YELLOW"], bold=True)
        print()
        input(center_text("Press ENTER to return to the menu..."))
        return
    if title == "Privacy tools":
        ret = show_subsections(items, favorites, title)
        if ret == "main":
            return "main"
        return
    while True:
        clear_screen()
        ascii_header()
        print()
        print_centered(f"{COLORS['BOLD']}{title}{COLORS['RESET']}", bold=True)
        print()
        for idx, item in enumerate(items, start=1):
            fav = "★" if is_favorite(item["id"], favorites) else " "
            print_centered(f"{COLORS['YELLOW']}[{idx}]{COLORS['RESET']} {fav}{item['name']}")
        print()
        print_centered(f"{COLORS['YELLOW']}[B]{COLORS['RESET']} Back")
        print_centered(f"{COLORS['MAGENTA']}{COLORS['BOLD']}[M] Main menu{COLORS['RESET']}")
        print()
        choice = input("Choose an option: ")
        if choice.strip().upper() == "B":
            break
        if choice.strip().upper() == "M":
            return "main"
        try:
            idx = int(choice)
            if 1 <= idx <= len(items):
                ret = show_item_detail(items[idx-1], favorites)
                if ret == "main":
                    return "main"
            else:
                print_error("Invalid option. Please try again.")
                input(center_text("Press ENTER to continue..."))
        except ValueError:
            print_error("Invalid input. Please enter a number.")
            input(center_text("Press ENTER to continue..."))

def favorites_menu(favorites):
    fav_items = []
    for cat in categories:
        if isinstance(cat["list"], list) and cat["title"] in ("Miner tools", "Privacy tools"):
            for sub in cat["list"]:
                for item in sub["items"]:
                    if item["id"] in favorites:
                        fav_items.append(item)
        else:
            for item in cat["list"]:
                if item["id"] in favorites:
                    fav_items.append(item)
    if not fav_items:
        clear_screen()
        ascii_header()
        print_centered("No favorites yet!", color=COLORS["NOTICE"])
        input(center_text("Press ENTER to return..."))
        return
    ret = category_menu("Favorites", fav_items, "Your favorites tools and resources.", favorites)
    return ret

def search_menu(favorites):
    all_items = []
    for cat in categories:
        if isinstance(cat["list"], list) and cat["title"] in ("Miner tools", "Privacy tools"):
            for sub in cat["list"]:
                all_items.extend(sub["items"])
        else:
            all_items.extend(cat["list"])
    clear_screen()
    ascii_header()
    print()
    print_centered("Search tools by keyword (name):", color=COLORS["CYAN"])
    print()
    query = input("Enter keyword: ").strip().lower()
    results = []
    for item in all_items:
        if query in item["name"].lower():
            results.append(item)
    if not results:
        print_centered("No results found.", color=COLORS["RED"])
        input(center_text("Press ENTER to return..."))
        return
    ret = category_menu("Search Results", results, f"Results for '{query}'", favorites)
    return ret

def main_menu(theme, favorites):
    clear_screen()
    ascii_header()
    print()
    price = get_xmr_price()
    print()
    if price is not None:
        price_str = f"{COLORS['BOLD']}{COLORS['GREEN_BOLD']}XMR = ${price:.2f}{COLORS['RESET']}"
        print_centered(price_str, bold=True)
        print_centered(f"{COLORS['DIM']}Live XMR price (real-time){COLORS['RESET']}")
    else:
        print_centered(" XMR Price: Unavailable ", color=COLORS["RED"], bold=True)
    print()
    print_tip()
    print()
    width = get_terminal_width()
    total = len(categories)
    half = (total + 1) // 2
    left = categories[:half]
    right = categories[half:]
    col_width = width // 2 - 2
    for i in range(half):
        lcat = left[i] if i < len(left) else None
        rcat = right[i] if i < len(right) else None

        # For section 9, show "Miner (Under construction)"
        l_main = (
            f"[{i+1}] {EMOJIS.get(lcat['title'],'')} {COLORS['YELLOW']}{'Miner (Under construction)' if lcat and lcat['title'] == 'Miner tools' else lcat['title']}{COLORS['RESET']}".center(col_width)
            if lcat else "".center(col_width)
        )
        if rcat:
            r_idx = i + half + 1
            r_title = rcat['title']
            r_main = f"[{r_idx}] {EMOJIS.get(r_title,'')} {COLORS['YELLOW']}{'Miner (Under construction)' if r_title == 'Miner tools' else r_title}{COLORS['RESET']}".center(col_width)
        else:
            r_main = "".center(col_width)
        print_centered(l_main + "    " + r_main)
        print()
    print_horizontal_line()
    action_line1 = f"[S] Search Tools   [F] Favorites   [L] Light/Dark Mode"
    action_line2 = f"[C] Support / Donate   [0] Exit"
    print_centered(action_line1, color=COLORS["WHITE"])
    print_centered(action_line2, color=COLORS["WHITE"])
    print_horizontal_line()
    print()

def main():
    global COLORS
    theme = load_settings()
    COLORS = THEMES[theme]
    favorites = load_favorites()
    welcome_screen()
    while True:
        main_menu(theme, favorites)
        choice_raw = input("Choose an option: ")
        choice = choice_raw.upper()
        if choice == "C":
            show_support()
        elif choice == "0":
            clear_screen()
            ascii_header()
            print_centered("Goodbye! Stay private.", color=COLORS["GREEN_BOLD"], bold=True)
            print()
            break
        elif choice == "L":
            theme = "light" if theme == "dark" else "dark"
            save_theme_and_reload(theme)
        elif choice == "S":
            ret = search_menu(favorites)
            if ret == "main":
                continue
        elif choice == "F":
            ret = favorites_menu(favorites)
            if ret == "main":
                continue
        else:
            try:
                idx = int(choice)
                # Section 9: Miner tools (under construction)
                if idx == 9:
                    clear_screen()
                    ascii_header()
                    print_centered("The Miner section is under construction.", color=COLORS["YELLOW"], bold=True)
                    print()
                    input(center_text("Press ENTER to return to the menu..."))
                    continue
                if 1 <= idx <= len(categories):
                    ret = category_menu(categories[idx-1]['title'], categories[idx-1]['list'], "", favorites)
                    if ret == "main":
                        continue
                else:
                    print_error("Invalid option. Please try again.")
                    input(center_text("Press ENTER to continue..."))
            except ValueError:
                print_error("Invalid input. Please enter a number.")
                input(center_text("Press ENTER to continue..."))

if __name__ == "__main__":
    main()