from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import PhoneNumberBannedError
import pickle, os
from colorama import init, Fore
from time import sleep

init()

n = Fore.RESET
lg = Fore.BLUE
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
gr = Fore.GREEN
m = Fore.MAGENTA
colors = [r]

try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    # fancy logo
    b = [
    

' ╔════╦═══╦╗──╔═══╦═══╦═══╦═══╦═╗╔═╗',
' ║╔╗╔╗║╔══╣║──║╔══╣╔═╗║╔═╗║╔═╗║║╚╝║║',
' ╚╝║║╚╣╚══╣║──║╚══╣║─╚╣╚═╝║║─║║╔╗╔╗║',
' ──║║─║╔══╣║─╔╣╔══╣║╔═╣╔╗╔╣╚═╝║║║║║║',
' ──║║─║╚══╣╚═╝║╚══╣╚╩═║║║╚╣╔═╗║║║║║║',
' ──╚╝─╚═══╩═══╩═══╩═══╩╝╚═╩╝─╚╩╝╚╝╚╝',

'╔═══╦═══╦═══╦═══╦═══╦═══╦═══╗',
'║╔═╗║╔═╗║╔═╗║╔═╗║╔═╗║╔══╣╔═╗║',
'║╚══╣║─╚╣╚═╝║║─║║╚═╝║╚══╣╚═╝║',
'╚══╗║║─╔╣╔╗╔╣╚═╝║╔══╣╔══╣╔╗╔╝',
'║╚═╝║╚═╝║║║╚╣╔═╗║║──║╚══╣║║╚╗',
'╚═══╩═══╩╝╚═╩╝─╚╩╝──╚═══╩╝╚═╝',

    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    #print('=============SON OF GOD==============')
    print(f'{gr}Version: {r}1.0{n} |{gr} Author: {r}@SOMOYADDER\n')
    print(cy+'-YOUR KEY IS SUCCESSFULLY ACTIVATED  BY @SOMOYADDER-')
  
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clr()
    banner()
    print(cy+' +---------------TELEGRAM SCRAPER---------------+'+n)
    print(r+'ACCOUNTS MANAGEMENT:'+n)
    print(lg+'╚═════════><01> ACCOUNTS LOGIN'+n)
    print(lg+'           <02> FILTER ALL BANNDED ACCOUNTS'+n)
    print(lg+'           <03> DELETE SPECIFIC ACCOUNT'+n)
    print(lg+'           <04> DISPLAY ALL ACCOUNTS'+n)
    print(r+'ADVANCED SCRAPER & FILTERS:'+n)
    print(lg+'╚═════════><05> SCRAPER '+n)
    print(lg+'           <06> PRIVATE SCRAPER'+n)
    print(lg+'           <07> SCRAP ADMIN '+n)
    print(lg+'           <08> SCRAP ACTIVE MEMBER  '+n)
    print(lg+'           <09> DAILY FILTER '+n)
    print(lg+'           <10>NON ACTIVE FILTER '+n)
    print(r+'ADVANCED ADDER OPTION:'+n)
    print(m+'╚═════════><11> DIRECT ADDER'+n)
    print(m+'           <12> ADDER'+n)
    print(m+'           <13> USER ID ADDER'+n)
    print(m+'           <14> ADDING MEMBER FROM CONTACT'+n)
    print(r+'ADVANCED TOOLS:'+n)
    print(lg+'╚═════════><15> AUTO CORRECT ADDER'+n)
    print(lg+'           <16> AUTO CORRECT DELETE'+n)
    print(lg+'           <17> POST VIEW INCREASER'+n)
    print(lg+'           <18> Report Scam'+n)
    print(r+'EDIT ACCOUNTS:'+n)
    print(lg+'╚═════════><19> CHANGE FIRST NAME'+n)
    print(lg+'           <20> CHANGE LAST NAME'+n)
    print(lg+'           <21> SET PROFILE PIC'+n)
    print(lg+'           <22> SET BIO'+n)
    print(lg+'           <23> SET USER NAME'+n)
    print(lg+'           <24> SET 2 STEP VERIFICATION'+n)
    print(lg+'           <25> REMOVE 2 STEP VERIFICATION'+n)
    print(r+'JOIN & LEAVE:'+n)
    print(gr+'╚═════════><26> JOIN GROUP & CHANNEL'+n)
    print(gr+'           <27> LEAVE GROUP & CHANNEL'+n)
    print(gr+'           <28> JOIN PRIVATE GROUP & CHANNEL'+n)
    print(gr+'           <29> LEAVE PRIVATE GROUP & CHANNEL'+n)
    print(r+'MY CONTACT INFORMATION:'+n)
    print(cy+'╚═════════><30> Subscribe My YouTube Channel'+n)
    print(cy+'           <31> Join My Telegram Channel'+n)
    print(cy+'           <32> Join My Telegram Group'+n)
    print(cy+'           <33> My Telegram Id'+n)
    print(r+'SHUTDOWN:'+n)
    print(lg+'╚═════════><34> EXIT'+n)
    print(lg+'           <35> EXIT & CLEAR'+n)
    
    a = int(input('\nEnter Your Choice: '))
    
    if a == 1:
        new_accs = []
        with open('vars.txt', 'ab') as g:
            number_to_add = int(input(f'\n{lg} [~] Enter number of accounts to add: {r}'))
            for i in range(number_to_add):
                phone_number = str(input(f'\n{lg} [~] Enter Phone Number: {r}'))
                parsed_number = ''.join(phone_number.split())
                pickle.dump([parsed_number], g)
                new_accs.append(parsed_number)
            print(f'\n{lg} [i] Saved all accounts in vars.txt')
            clr()
            print(f'\n{m} [*] Logging in from new accounts\n')
            for number in new_accs:
                c = TelegramClient(f'sessions/{number}', 8088717 , '7d1e0295ee1c2628f1933e9ffd2d8b78')
                c.start(number)
                print(f'{lg}[+] 𝐋𝐨𝐠𝐢𝐧 𝐬𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮L')
                c.disconnect()
            input(f'\n Press enter to goto main menu...')

        g.close() 
    elif a == 2:
        accounts = []
        banned_accs = []
        h = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(h))
            except EOFError:
                break
        h.close()
        if len(accounts) == 0:
            print(r+'[!] There are no accounts! Please add some and retry')
            sleep(3)
        else:
            for account in accounts:
                phone = str(account[0])
                client = TelegramClient(f'sessions/{phone}', 8088717 , '7d1e0295ee1c2628f1933e9ffd2d8b78')
                client.connect()
                if not client.is_user_authorized():
                    try:
                        client.send_code_request(phone)
                        #client.sign_in(phone, input('[+] Enter the code: '))
                        print(f'{blue}[+] {phone} is not banned{n}')
                    except PhoneNumberBannedError:
                        print(r+str(phone) + ' is banned!'+n)
                        banned_accs.append(account)
            if len(banned_accs) == 0:
                print(lg+'Congrats! No banned accounts')
                input('\nPress enter to goto main menu...')
            else:
                for m in banned_accs:
                    accounts.remove(m)
                with open('vars.txt', 'wb') as k:
                    for a in accounts:
                        Phone = a[0]
                        pickle.dump([Phone], k)
                k.close()
                print(lg+'[i] All banned accounts removed'+n)
                input('\nPress enter to goto main menu...')
    elif a == 3:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        i = 0
        print(f'{ye}[i] Choose an account to delete\n')
        for acc in accs:
            print(f'{lg}[{i}] {acc[0]}{n}')
            i += 1
        index = int(input(f'\n{lg}[+] Enter a choice: {n}'))
        phone = str(accs[index][0])
        session_file = phone + '.session'
        if os.name == 'nt':
            os.system(f'del sessions\\{session_file}')
        else:
            os.system(f'rm sessions/{session_file}')
        del accs[index]
        f = open('vars.txt', 'wb')
        for account in accs:
            pickle.dump(account, f)
        print(f'\n{lg}[+] Account Deleted{n}')
        input(f'\nPress enter to goto main menu...')
        f.close()   
    elif a == 4:
        accs = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accs.append(pickle.load(f))
            except EOFError:
                break
        f.close()
        print(f'\n{m}')
        print(f'\tList Of Phone Numbers Are')
        print(f'====================================================')
        i = 0
        for z in accs:
            print(f'\t{z[0]}')
            i += 1
        print(f'====================================================')
        input('\nPress enter to goto main menu')
        
    elif a == 11:
        clr()
        banner()
        os.system('python Adder.py')
        exit ()
    elif a == 12:
        clr()
        banner()
        os.system('python Adder.py')
        exit ()
    elif a == 13:
        clr()
        banner()
        os.system('python Adder.py')
        exit ()
    elif a == 14:
        clr()
        banner()
        os.system('python Adder.py')
        exit ()
        
    elif a == 11:
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break

        
        #print('\n' + info + lg + ' Checking for banned accounts...' + rs)
        print('\n' ' Checking for banned accounts...' )
        for a in accounts:
            phn = a[0]
            print(f'Checking {lg}{phn}')
            clnt = TelegramClient(f'sessions/{phn}', 8027196 , '9b70b20efd67e9b99edc395d78407cfa')
            clnt.connect()
            banned = []
            if not clnt.is_user_authorized():
                try:
                    clnt.send_code_request(phn)
                    print('kk')
                except PhoneNumberBannedError:
                    print(f'{error} {w}{phn} {r}is banned!{rs}')
                    banned.append(a)
            for z in banned:
                accounts.remove(z)
                print('{lg}Banned account removed[Remove permanently using manager.py]{rs}')
            time.sleep(0.5)
            clnt.disconnect()
        print(' Sessions created!')
        clr()
        banner()
        accounts = []
        f = open('vars.txt', 'rb')
        while True:
            try:
                accounts.append(pickle.load(f))
            except EOFError:
                break
        print(f'{lg} Total accounts: {w}{len(accounts)}')
        number_of_accs = int(input(f'{cy} Enter number of accounts to Report: {r}'))
        choice = str(input(f'{cy} Send Message For Report {r}'))
        to_use = [x for x in accounts[:number_of_accs]]
        for l in to_use: accounts.remove(l)
        with open('vars.txt', 'wb') as f:
            for a in accounts:
                pickle.dump(a, f)
            for ab in to_use:
                pickle.dump(ab, f)
            f.close()
        sleep_time = 1
        print(f'{lg} -- Sending Reports from {w}{len(to_use)}{lg} account(s) --')   
        send_status = 0
        
        approx_members_count = 0
        index = 0
        for acc in to_use:
            stop = index + 60
            c = TelegramClient(f'sessions/{acc[0]}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
            print(f'User: {cy}{acc[0]}{lg} -- {cy}Starting session... ')
            c.start(acc[0])
            acc_name = c.get_me().first_name
            try:
                c.send_message(scam,choice)
                print(f'Report Done From: {cy}{acc_name}{lg}  To Notoscam-- ')
                send_status += 1
            except Exception as e:
                print(f'{e}')
                continue
        if send_status != 0:
            print(f"\n{lg}session ended")
            input(f'\n{cy} Press enter to exit...')
        else:
            print(f"\n{lg}All reports done sucesfully")
            input(f'\n{cy} Press enter to exit...')
    elif a == 30:
    	os.system("termux-open-url https://youtube.com/@SOMOYADDER")
    elif a == 31:
    	os.system("termux-open-url https://t.me/SOMOYADDERV1")
    elif a == 32:
    	os.system("termux-open-url https://t.me/SOMOYADDERV11")
    elif a == 33:
    	os.system("termux-open-url https://t.me/SOMOYADDER")
    elif a == 34:
        exit()
    elif a == 35:    
        clr()
        banner()
        exit()
   
      