#################################
import whois                    #
import concurrent.futures       #
import requests                 #
from termcolor import colored   #
import os                       #
#################################

#####################################################################
#                                                                   #
#██████╗ ██████╗  ██████╗  ██████╗ ████████╗██╗   ██╗██████╗        #
#╚════██╗██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝██║   ██║╚════██╗       #
# █████╔╝██████╔╝██║   ██║██║   ██║   ██║   ██║   ██║ █████╔╝       #
#██╔═══╝ ██╔══██╗██║   ██║██║   ██║   ██║   ╚██╗ ██╔╝ ╚═══██╗       #
#███████╗██║  ██║╚██████╔╝╚██████╔╝   ██║    ╚████╔╝ ██████╔╝       #
#####################################################################



try:
    import whois
except ModuleNotFoundError:
    import os
    os.system('pip install whois')
    os.system('pip install python-whois')
    os.system('pip install --upgrade python-whois')

try:
    import requests
except ModuleNotFoundError:
    import os
    os.system('pip install requests')

try:
    import termcolor
except ModuleNotFoundError:
    import os
    os.system('pip install termcolor')
    from termcolor import colored


def clear_screen():
    # Clear screen command based on the operating system
    clear_command = "cls" if os.name == "nt" else "clear"
    os.system(clear_command)


if __name__ == "__main__":
    clear_screen()



print('')
text = "██████╗ ██████╗  ██████╗  ██████╗ ████████╗██╗   ██╗██████╗ \n╚════██╗██╔══██╗██╔═══██╗██╔═══██╗╚══██╔══╝██║   ██║╚════██╗\n █████╔╝██████╔╝██║   ██║██║   ██║   ██║   ██║   ██║ █████╔╝\n██╔═══╝ ██╔══██╗██║   ██║██║   ██║   ██║   ╚██╗ ██╔╝ ╚═══██╗\n███████╗██║  ██║╚██████╔╝╚██████╔╝   ██║    ╚████╔╝ ██████╔╝\n╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝     ╚═══╝  ╚═════╝"

colored_text = "\033[1;32m" + text + "\033[0m"
print(colored_text)


print('')
target_website = input('Enter your target website name: ')

if not target_website.startswith('http://') and not target_website.startswith('https://'):
    target_website = 'http://' + target_website





def webiste_info():
    result = whois.whois(target_website)


    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'

    print(f"{YELLOW}Domain Name:{ENDC} {GREEN}{result.domain_name}{ENDC}")
    print('')
    print(f"{YELLOW}Registrar:{ENDC} {GREEN} {result.registrar}{ENDC}")
    print('')
    print(f"{YELLOW}Creation Date:{ENDC} {GREEN}{result.creation_date}{ENDC}")
    print('')
    print(f"{YELLOW}Expiration Date:{ENDC} {GREEN}{result.expiration_date}{ENDC}")
    print('')
    print(f"{YELLOW}Name Servers:{ENDC} {GREEN}{result.name_servers}{ENDC}")
    print('')
    print(f"{YELLOW}Status:{ENDC} {GREEN}{result.status}{ENDC}")
    print('')
    print(f"{YELLOW}Emails:{ENDC} {GREEN}{result.emails}{ENDC}")
    print('')
    print(f"{YELLOW}Organization:{ENDC} {GREEN}{result.org}{ENDC}")
    print('')
    print(f"{YELLOW}Address:{ENDC} {GREEN}{result.address}v")
    print('')
    print(f"{YELLOW}City:{ENDC} {GREEN}{result.city}{ENDC}")
    print('')
    print(f"{YELLOW}State:{ENDC} {GREEN}{result.state}{ENDC}")
    print('')
    print(f"{YELLOW}Postal Code:{ENDC}{GREEN} {result.registrant_postal_code}{ENDC}")
    print('')
    print(f"{YELLOW}Country:{ENDC} {GREEN}{result.country}{ENDC}")
    print('')
    print('')

def adminpage_finder():
    directories = [
        "/admin1.html",
        "/dbadmin",
        "/logon",
        "/wp-login.php",
        "/user",
        "/webadmin",
        "/administr8.html",
        "/panel",
        "/login1/",
        "/login",
        "/admin/",
        "/administrator/",
        "/admin1/",
        "/admin2/",
        "/admin3/",
        "/admin4/",
        "/admin5/",
        "/usuarios/",
        "/usuario/",
        "/moderator/",
        "/webadmin/",
        "/adminarea/",
        "/bb-admin/",
        "/adminLogin/",
        "/admin_area/",
        "/panel-administracion/",
        "/instadmin/",
        "/memberadmin/",
        "/administratorlogin/",
        "/adm/",
        "/admin/account.php",
        "/admin/index.php",
        "/admin/login.php",
        "/admin/admin.php",
        "/admin_area/admin.php",
        "/admin_area/login.php",
        "/siteadmin/login.php",
        "/siteadmin/index.php",
        "/siteadmin/login.html",
        "/admin/account.html",
        "/admin/index.html",
        "/admin/login.html",
        "/admin/admin.html",
        "/admin_area/index.php",
        "/bb-admin/index.php",
        "/bb-admin/login.php",
        "/bb-admin/admin.php",
        "/admin/home.php",
        "/admin_area/login.html",
        "/admin_area/index.html",
        "/admin/controlpanel.php",
        "/admin.php",
        "/admincp/index.asp",
        "/admincp/login.asp",
        "/admincp/index.html",
        "/adminpanel.html",
        "/webadmin.html",
        "/webadmin/index.html",
        "/webadmin/admin.html",
        "/webadmin/login.html",
        "/admin/admin_login.html",
        "/admin_login.html",
        "/panel-administracion/login.html",
        "/admin/cp.php",
        "/cp.php",
        "/administrator/index.php",
        "/administrator/login.php",
        "/nsw/admin/login.php",
        "/webadmin/login.php",
        "/admin/admin_login.php",
        "/admin2.html",
        "/admin_login.php",
        "/administrator/account.php",
        "/administrator.php",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.php",
        "/admin/admin-login.php",
        "/admin-login.php",
        "/bb-admin/index.html",
        "/bb-admin/login.html",
        "/acceso.php",
        "/bb-admin/admin.html",
        "/admin/home.html",
        "/login.php",
        "/modelsearch/login.php",
        "/moderator.php",
        "/moderator/login.php",
        "/moderator/admin.php",
        "/account.php",
        "/pages/admin/admin-login.html",
        "/admin/admin-login.html",
        "/admin-login.html",
        "/controlpanel.php",
        "/admincontrol.php",
        "/admin/adminLogin.html",
        "/adminLogin.html",
        "/home.html",
        "/rcjakar/admin/login.php",
        "/server.html",
        "/adminarea/index.html",
        "/adminarea/admin.html",
        "/webadmin.php",
        "/webadmin/index.php",
        "/webadmin/admin.php",
        "/admin/controlpanel.html",
        "/admin.html",
        "/admin/cp.html",
        "/cp.html",
        "/adminpanel.php",
        "/moderator.html",
        "/administrator/index.html",
        "/administrator/login.html",
        "/user.html",
        "/administrator/account.html",
        "/administrator.html",
        "/login.html",
        "/modelsearch/login.html",
        "/moderator/login.html",
        "/adminarea/login.html",
        "/panel-administracion/index.html",
        "/panel-administracion/admin.html",
        "/modelsearch/index.html",
        "/modelsearch/admin.html",
        "/admincontrol/login.html",
        "/adm/index.html",
        "/adm.html",
        "/moderator/admin.html",
        "/user.php",
        "/account.html",
        "/controlpanel.html",
        "/admincontrol.html",
        "/panel-administracion/login.php",
        "/wp-login.php",
        "/adminLogin.php",
        "/admin/adminLogin.php",
        "/home.php",
        "/adminarea/index.php",
        "/adminarea/admin.php",
        "/adminarea/login.php",
        "/panel-administracion/index.php",
        "/panel-administracion/admin.php",
        "/sysadmin.html",
        "/fileadmin.html",
        "/modelsearch/index.php",
        "/modelsearch/admin.php",
        "/admincontrol/login.php",
        "/adm/admloginuser.php",
        "/admloginuser.php",
        "/admin2.php",
        "/admin2/login.php",
        "/admin2/index.php",
        "/usuarios/login.php",
        "/adm/index.php",
        "/adm.php",
        "/affiliate.php",
        "/adm_auth.php",
        "/memberadmin.php",
        "/administratorlogin.php",
        "/account.asp",
        "/admin/account.asp",
        "/admin/index.asp",
        "/admin/login.asp",
        "/admin/admin.asp",
        "/admin_area/admin.asp",
        "/admin_area/login.asp",
        "/admin_area/index.asp",
        "/siteadmin/login.asp",
        "/siteadmin/index.asp",
        "/admin_area/index.asp",
        "/bb-admin/index.asp",
        "/bb-admin/login.asp",
        "/bb-admin/admin.asp",
        "/admin/home.asp",
        "/admin/controlpanel.asp",
        "/admin.asp",
        "/pages/admin/admin-login.asp",
        "/admin/admin-login.asp",
        "/admin-login.asp",
        "/admin/cp.asp",
        "/cp.asp",
        "/administrator/account.asp",
        "/administrator.asp",
        "/acceso.asp",
        "/login.asp",
        "/modelsearch/login.asp",
        "/moderator.asp",
        "/moderator/login.asp",
        "/administrator/login.asp",
        "/moderator/admin.asp",
        "/controlpanel.asp",
        "/user.asp",
        "/admincontrol.asp",
        "/adminpanel.asp",
        "/webadmin.asp",
        "/webadmin/index.asp",
        "/webadmin/admin.asp",
        "/admin/admin_login.asp",
        "/admin_login.asp",
        "/panel-administracion/login.asp",
        "/adminLogin.asp",
        "/admin/adminLogin.asp",
        "/home.asp",
        "/adminarea/index.asp",
        "/adminarea/admin.asp",
        "/adminarea/login.asp",
        "/panel-administracion/index.asp",
        "/panel-administracion/admin.asp",
        "/modelsearch/index.asp",
        "/modelsearch/admin.asp",
        "/administrator/index.asp",
        "/admincontrol/login.asp",
        "/adm/admloginuser.asp",
        "/admloginuser.asp",
        "/admin2.asp",
        "/admin2/login.asp",
        "/admin2/index.asp",
        "/adm/index.asp",
        "/adm.asp",
        "/affiliate.asp",
        "/adm_auth.asp",
        "/memberadmin.asp",
        "/administratorlogin.asp",
        "/siteadmin/login.asp",
        "/siteadmin/index.asp",
        "/admin/account.cfm",
        "/admin/index.cfm",
        "/admin/login.cfm",
        "/admin/admin.cfm",
        "/admin_area/admin.cfm",
        "/admin_area/login.cfm",
        "/siteadmin/login.cfm",
        "/siteadmin/index.cfm",
        "/admin_area/index.cfm",
        "/bb-admin/index.cfm",
        "/bb-admin/login.cfm",
        "/bb-admin/admin.cfm",
        "/admin/home.cfm",
        "/admin/controlpanel.cfm",
        "/admin.cfm",
        "/admin/cp.cfm",
        "/cp.cfm",
        "/administrator/index.cfm",
        "/administrator/login.cfm",
        "/nsw/admin/login.cfm",
        "/webadmin/login.cfm",
        "/admin/admin_login.cfm",
        "/admin_login.cfm",
        "/administrator/account.cfm",
        "/administrator.cfm",
        "/pages/admin/admin-login.cfm",
        "/admin/admin-login.cfm",
        "/admin-login.cfm",
        "/login.cfm",
        "/modelsearch/login.cfm",
        "/moderator.cfm",
        "/moderator/login.cfm",
        "/moderator/admin.cfm",
        "/account.cfm",
        "/controlpanel.cfm",
        "/admincontrol.cfm",
        "/acceso.cfm",
        "/rcjakar/admin/login.cfm",
        "/webadmin.cfm",
        "/webadmin/index.cfm",
        "/webadmin/admin.cfm",
        "/adminpanel.cfm",
        "/user.cfm",
        "/panel-administracion/login.cfm",
        "/wp-login.cfm",
        "/adminLogin.cfm",
        "/admin/adminLogin.cfm",
        "/home.cfm",
        "/adminarea/index.cfm",
        "/adminarea/admin.cfm",
        "/adminarea/login.cfm",
        "/panel-administracion/index.cfm",
        "/panel-administracion/admin.cfm",
        "/modelsearch/index.cfm",
        "/modelsearch/admin.cfm",
        "/admincontrol/login.cfm",
        "/adm/admloginuser.cfm",
        "/admloginuser.cfm",
        "/admin2.cfm",
        "/admin2/login.cfm",
        "/admin2/index.cfm",
        "/usuarios/login.cfm",
        "/adm/index.cfm",
        "/adm.cfm",
        "/affiliate.cfm",
        "/adm_auth.cfm",
        "/memberadmin.cfm",
        "/administratorlogin.cfm",
        "/admin_panel/",
        "/admin_panel.html/",
        "/adm_cp//",
        "/administrator/index.brf",
        "/administrator/login.brf",
        "/nsw/admin/login.brf",
        "/webadmin/login.brfbrf",
        "/admin/admin_login.brf",
        "/admin_login.brf",
        "/administrator/account.brf",
        "/administrator.brf",
        "/acceso.brf",
        "/admin_area/admin.html",
        "/pages/admin/admin-login.brf",
        "/admin/admin-login.brf",
        "/admin-login.brf",
        "/bb-admin/index.html",
        "/bb-admin/login.html",
        "/bb-admin/admin.html",
        "/ur-adnim.html",
        "/admin/home.html",
        "/login.brf",
        "/modelsearch/login.brf",
        "/moderator.brf",
        "/moderator/login.brf",
        "/moderator/admin.brf",
        "/account.brf",
        "/pages/admin/admin-login.html",
        "/admin/admin-login.html",
        "/admin-login.html",
        "/sitemap.xml",
        "/robots.txt",
        "/private",
        "/yontim.html"
        "/index.php/login",
    ]

    link=set()

    print(colored('[*]Chacking .......'))
    def check_directory(url):
        with requests.Session() as session:
            response = session.get(url)

        if response.status_code == 200:
            print(colored(f'[+] Admin page found: {url}', 'green'))
            link.add(f'[+] Admin page Found {url}')
        else:
            print(colored(f'[-] Admin page not found: {url}', 'red'))

    # Adjust the max_workers parameter to increase concurrency
    max_workers = 15

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for directory in directories:
            url = target_website + directory
            futures.append(executor.submit(check_directory, url))

        for future in concurrent.futures.as_completed(futures):
            future.result()



webiste_info()
adminpage_finder()
