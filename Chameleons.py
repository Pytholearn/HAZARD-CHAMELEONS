from rich import *
from pystyle import *
import os
import time
import requests
import platform 
from update_file import update

load_banner = r"""
                              
   ________    Code By HAZARD       __        V1.1.2             
  / ____/ /_  ____ _____ ___  ___  / /__  ____  ____  _____
 / /   / __ \/ __ `/ __ `__ \/ _ \/ / _ \/ __ \/ __ \/ ___/
/ /___/ / / / /_/ / / / / / /  __/ /  __/ /_/ / / / (__  ) 
\____/_/ /_/\__,_/_/ /_/ /_/\___/_/\___/\____/_/ /_/____/  


                       <Press Enter>
"""
Anime.Fade(Center.Center(load_banner),Colors.cyan_to_blue, Colorate.Vertical, enter=True)

update()
#--------setting--------
print("[green]pls run this code `sudo` or `administrator` for run very good![/green]")
time.sleep(2)
Check_SYS = platform.system()
if Check_SYS == "Windows":
    print("[red]You Cant Run This Code In Windows Very Well[/red]")
    time.sleep(2)

proxy = {"http":"socks5://127.0.0.1:9050",
         "https":"socks5://127.0.0.1:9050"}

def getip_tor():
    try:
        response = requests.get('https://api.ipify.org?format=json',proxies= proxy)
        data = response.json()
        ip = data['ip']
        return ip
    except Exception as e:
        print(f"Error: {e}")
        return None

def getip_local():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        data = response.json()
        ip = data['ip']
        return ip
    except Exception as e:
        print(f"Error: {e}")
        return None

CTCON = "STOP"

Help = """
Hello buddy!
Chameleons:
                                  [cyan]╔═╗┌─┐┬─┐  ┬ ┬┌─┐┬ ┬   [/cyan][blue]┌┐ ┬  ┬ ┬┌─┐[/blue][cyan]  ┌─┐┬┬─┐┬  [/cyan]
                                  [cyan]╠╣ │ │├┬┘  └┬┘│ ││ │   [/cyan][blue]├┴┐│  │ │├┤ [/blue][cyan]  │ ┬│├┬┘│  [/cyan]
                                  [cyan]╚  └─┘┴└─   ┴ └─┘└─┘┘  [/cyan][blue]└─┘┴─┘└─┘└─┘[/blue][cyan]  └─┘┴┴└─┴─┘[/cyan]                                  
                   [cyan]Hey[/cyan] [blue]girl,[/blue] [cyan]Hazard's[/cyan] [blue]heart[/blue] [cyan]is[/cyan] [blue]very[/blue] [cyan]close[/cyan] [blue]to[/blue] [cyan]you[/cyan] [blue]:)[/blue] [cyan]But[/cyan] [blue]that[/blue] [cyan]friendship[/cyan] [blue]was[/blue] [cyan]toxic![/cyan]

[magenta]                        
This tool is made by Hazard and any copying is prosecuted
Aftabparast is a simple tool and actually an interface between you and the tor service to make your work easier!
[/magenta]
`Be careful! The world is dirty:)`

[blue]═══════════════════════════════════════════════Help═════════════════════════════════════════════════[/blue]
[[blue]1[/blue]] Start Change IP (Tor):
        [bold yellow]If you choose this option, you will definitely come across an input titled 
        [/bold yellow][green]"Enter Time For Change IP [>>>]"[/green] [bold yellow]where you have to enter a time (s)!
        But this option will automatically change your tor IP![/bold yellow]

[[blue]2[/blue]] Start Tor:
        [bold yellow]If you select this option, the tool will manually turn [/bold yellow][bold green]on[/bold green][bold yellow] your tor service:)[/bold yellow]

[[blue]3[/blue]] Stop Tor:
        [bold yellow]If you choose this one, the tool will manually turn [/bold yellow][bold red]off[/bold red][bold yellow] your tor service:|[/bold yellow]

[[blue]4[/blue]] IP Info:
        [bold yellow]By choosing this option, you will be faced with two options:[/bold yellow]
            [[blue]T[/blue]] Get Tor IP Info:
                    [bold yellow]You will receive a little information about your[/bold yellow] [magenta]tor[/magenta] IP.
            [[blue]L[/blue]] Get Local IP Info:
                    [bold yellow]You will receive a little information about your [/bold yellow][magenta]e-local[/magenta].

[[blue]5[/blue]] Install Tor:
        [bold yellow]This option installs the tor service manually on your operating system![/bold yellow]

[[blue]6[/blue]] Help & Info:
        [bold green]Ummm..Hey bro?! You clicked on this option nowXD [/bold green]
[blue]═══════════════════════════════════════════════Info═════════════════════════════════════════════════[/blue]
Hazard made this tool in memory of one of her old friends and dedicates it to her

This tool was created in 1/19/2024 and uploaded to GitHub
When I was at RZ Voice, I write this code with the help of Sadra and MMD(Zamin Takht GeraXD)
(helping me in design)

                ╔═════════════════════════HaZaRd═════════════════════════════╗
                ║        [red]Youtube: https://www.youtube.com/@IIIHaZaRd[/red]         ║
                ║        [black on white]Github: https://github.com/Pytholearn[/black on white]               ║
                ║        [cyan]Discord: https://discord.gg/YU7jYRkxwp[/cyan]              ║
                ╚════════════════════════════════════════════════════════════╝
                                   IRAN ON TOP FOR EVER
[blue]════════════════════════════════════════════════════════════════════════════════════════════════════[/blue]
"""
#--------setting---------
while True:
 os.system("clear")
 print(r"""                                                    V1.1.2
                            [blue] ________  [/blue][white]               [/white][blue]        __[/blue][white]                            Just For IRAN
                            [blue]/ ____/ /_ [/blue][white] ____ _____ ___[/white][blue]  ___  / /[/blue][white]__  ____  ____  [blue]_____[/blue]
                           [blue]/ /   / __ |[/blue][white]/ __ `/ __ `__ |[/white][blue]/ _ \/ /[/blue][white] _ \/ __ |/ __ |[blue]/ [blue]___/[/blue]
                          [blue]/ /___/ / / /[/blue][white] /_/ / / / / / [/white][blue]/  __/ /[/blue][white]  __/ /_/ / / / [/white][blue](__  ) [/blue]
                          [blue]\____/_/ /_/[/blue][white]\__,_/_/ /_/ /_/[/white][blue]\___/_/[/blue][white]\___/\____/_/ /_/[blue]____/[/blue]
>[cyan]Code By HAZARD[/cyan]""")                                     
 print(f">[cyan]IP Chenger[/cyan]                                        [red]IRAN[/red] [white]ON[/white] [green]TOP[/green]                                    Tor: [magenta]{CTCON}[/magenta]")
 Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════",Colors.blue,interval = 0.009)          
 print("""
[[blue]1[/blue]] : Start Change IP (Tor)                                                [[blue]4[/blue]] : IP Info
[[blue]2[/blue]] : Start Tor                                                            [[blue]5[/blue]] : Install Tor
[[blue]3[/blue]] : Stop Tor                                                             [[blue]6[/blue]] : Help & Info""")
 Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════",Colors.blue,interval = 0.010)

 Choice = Write.Input("\n\n[>>>] ",Colors.pink)

 if Choice == "1" :
    time_sleep = input("Enter Time For Change IP[>>>] ")
    while True:
        try:
            os.system("sudo service tor start")
            time.sleep(int(time_sleep))
            os.system("sudo service tor stop")
            print("[green]Your IP has been changed[/green]")
        except Exception as e:
            print(f"[red]Error: {e}[/red]")
            continue

 elif Choice == "2":
    os.system("sudo service tor start")
    print("[green]Tor Started![/green]")
    CTCON = "START"
    print(f"[magenta]Tor: {CTCON}[/magenta]")
    time.sleep(2)
    continue

 elif Choice == "3":
    os.system("sudo service tor stop")
    print("[red]Tor Stoped![/red]")
    CTCON = "STOP"
    print(f"[magenta]Tor: {CTCON}[/magenta]")
    time.sleep(2)
    continue
 
 elif Choice == "4":
    print("[[blue]T[/blue]] Get Tor IP Info")
    print("[[blue]L[/blue]] Get Local IP Info")
    Choice_4 = Write.Input("\nEnter[>>>] ",Colors.pink)
    if Choice_4 == "T" or Choice_4 == "t":
        print("[green]OK Your Tor IP Info:[/green]")
        ip = getip_tor()
        print(ip)

    if Choice_4 == "L" or Choice_4 == "l":
        print("[green]OK Your Local IP Info:[/green]")
        ip = getip_local()
        print(ip)

    input("Press ENTER to Continue...")
    continue
 
 elif Choice == "5":
    print("[yellow]Installing all the packages you need[/yellow]:")
    os.system("sudo apt update")
    os.system("sudo apt install python3-pip -y")
    os.system("sudo apt install tor -y")
    time.sleep(3)
    continue
 
 elif Choice == "6":
     print(Help)
     input("Press ENTER to Continue...")
 else:
     print(f"Error: This Command Not Found!!!!")




