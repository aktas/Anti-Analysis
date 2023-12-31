import os
from colorama import Fore
import platform
import argparse

banner = """
   _____          __  .__  ________  .__                              
  /  _  \   _____/  |_|__| \______ \ |__| ___________    ______ ______
 /  /_\  \ /    \   __\  |  |    |  \|  |/  ___/\__  \  /  ___//  ___/
/    |    \   |  \  | |  |  |    `   \  |\___ \  / __ \_\___ \ \___ \ 
\____|__  /___|  /__| |__| /_______  /__/____  >(____  /____  >____  >
        \/     \/                  \/        \/      \/     \/     \/ 

 ---------------------------------------------------------------------
 | Twitter: https://twitter.com/zayotem                              |
 | Github: https://github.com/ZAYOTEM                                |
 | Authors:Alper AKTAŞ, Tolga YILMAZ, Ebubekir ERKAYA, Tuğba Nur CAN |
 ---------------------------------------------------------------------
"""

print(f"{Fore.RED}{banner}{Fore.RESET}")


ap = argparse.ArgumentParser(description="note: the script only works on Linux system and 32-bit programs.")
ap.add_argument('-s', '--show', action='store_true', required=False, help='only show addresses')
ap.add_argument('-f', '--file', required=True, help='file path')
args = vars(ap.parse_args())

fileName = args["file"]

if (os.path.exists(f"{fileName}")) == False:
    print(f"{Fore.GREEN}[!]{Fore.RESET} File not found.")
    exit()

system = platform.system()
checkBit = os.popen(f"file {fileName}").read()
if ("PE32+" in checkBit) or (system == "Windows"):
    print("The script only works on Linux system and 32-bit programs.")
    exit()


# baslangic
def is_hex_string(s, c): # c 1 ise opcode control ediliyor degilse adres
    hex_characters = set("0123456789abcdefABCDEF")
    if c == 1:
        if len(s) == 2:
            return all(char in hex_characters for char in s)
        else:
            return False
    else:
        return all(char in hex_characters for char in s)

instructions = {'jl', 'jg', 'je', 'jz', 'jne', 'jnb', 'jle', 'jge', 'jb', 'ja', 'jbe', 'jae', 'jnz'}

control = 1 if args["show"] == True else 0
print(f"{Fore.GREEN}[!]{Fore.RESET} Addresses will just be displayed instead of being changed.") if control == 1 else None

addressDic = {}
counter = 0 # kac adres bulunmus?

os.system(f"xxd -p -c 0 {fileName} > {fileName}.temp") # opcode degerleri degistirilmek uzere kaydediliyor

for x,instruction in enumerate(instructions): # jmp kontrol ediliyor
    if x == 0:
        os.system(f"objdump -d {fileName} | grep -i -A 3 '{instruction}' | grep -i -B 1 'jmp' | grep -i -A 1 '{instruction}' > dump.txt")
    else:
        os.system(f"objdump -d cleaned.{fileName} | grep -i -A 3 '{instruction}' | grep -i -B 1 'jmp' | grep -i -A 1 '{instruction}' > dump.txt")

    
    with open('dump.txt', 'r') as file:
        i = 1
        cArr = []

        

        for line in file:
            if line.strip() == "--":
                i = 1
                continue

            arr = line.strip().split()
            if i == 1:
                val = int(arr[-1].strip(":"), 16)
                cArr.append(val)
            else:
                val = int("0x"+arr[0].strip(":"), 16)
                addressC = str(arr[-1].strip("0x"))
                
                if str(hex(cArr[0]))[2:4] == str(addressC[:2]): # esit ise obfuscated edilmemis
                    cArr.clear()
                    continue

                if str(addressC[:1]) == "*":
                    cArr.clear()
                    continue

                
                
                cArr.append(val)

                if cArr[0] > cArr[-1]: # Impossible Disassembly Teknigi Kullanilmis
                    #print(arr[1:-2]) # opcode
                    diff = (cArr[0] - cArr[-1]) # kac byte atlamis?
                    
                    address = str(hex(cArr[-1])).lstrip("0x")
                    
                    if control == 1:
                        counter = counter + 1
                        cArr.clear()
                        print(f"{Fore.GREEN}[*]{Fore.RESET} Address : {Fore.GREEN}{address}{Fore.RESET}")
                        continue
                    os.system(f"objdump -d {fileName} | grep -i -A 3 '{address}' > dump2.txt")
                    
                    
                    
                    with open('dump2.txt', 'r') as file2: # opcode alinarak degistiriliyor
                        arr2 = []
                        run = 0
                        for line2 in file2:
                            arrTemp = line2.strip().split()
                            for value in arrTemp[0:-1]:
                                if is_hex_string(value, 1):
                                    arr2.append(value)
                        #print(''.join(arr2)) # degistirilecek opcode

                        with open(f"{fileName}.temp", "r") as file3:
                            lines = file3.readlines()[0]
                            
                            writeOn = "90"*diff
                            begin = diff*2
                            opcode = ''.join(arr2)
                            #print(f"Mevcut instruction : {instruction}")
                            if (lines.count(''.join(arr2)) == 1) or (run == 1):
                                counter = counter + 1
                                print(f"{Fore.GREEN}[*]{Fore.RESET} Opcode patching process is being performed... Address : {Fore.GREEN}{address}{Fore.RESET}")
                                lines = lines.replace(opcode, (writeOn + opcode[begin:]))
                            if lines.count(''.join(arr2)) > 1:
                                counter = counter + 1
                                print(f"{Fore.GREEN}[!]{Fore.RESET} Address content was encountered in more than one place. Please change manually. Address : {Fore.GREEN}{address}{Fore.RESET}")
                            

                        with open(f"{fileName}.temp", "w") as file4:
                            file4.write(lines)

                    

                cArr.clear()

            i = i + 1

    os.system(f"xxd -r -p {fileName}.temp > cleaned.{fileName}")



for x,instruction in enumerate(instructions): # call kontrol ediliyor
    os.system(f"objdump -d cleaned.{fileName} | grep -i -A 3 '{instruction}' | grep -i -B 1 'call' | grep -i -A 1 '{instruction}' > dump.txt")
    
    with open('dump.txt', 'r') as file:
        i = 1
        cArr = []

        

        for line in file:
            if line.strip() == "--":
                i = 1
                continue

            arr = line.strip().split()
            if i == 1:
                val = int(arr[-1].strip(":"), 16)
                cArr.append(val)
            else:
                val = int("0x"+arr[0].strip(":"), 16)
                addressC = str(arr[-1].strip("0x"))

                if str(addressC[:1]) == "*":
                    cArr.clear()
                    continue

                if len(addressC) != 8:
                    cArr.clear()
                    continue

                cArr.append(val)

                if cArr[0] > cArr[-1]: # Impossible Disassembly Teknigi Kullanilmis
                    #print(arr[1:-2]) # opcode
                    diff = (cArr[0] - cArr[-1]) # kac byte atlamis?

                    address = str(hex(cArr[-1])).lstrip("0x")
                    if address == "401de" or address == "401df1":
                        continue
                    if control == 1:
                        counter = counter + 1
                        cArr.clear()
                        print(f"{Fore.GREEN}[*]{Fore.RESET} Address : {Fore.GREEN}{address}{Fore.RESET}")
                        continue

                    os.system(f"objdump -d {fileName} | grep -i -A 3 '{address}' > dump2.txt")
                    
                    
                    with open('dump2.txt', 'r') as file2: # opcode alinarak degistiriliyor
                        arr2 = []
                        for line2 in file2:
                            arrTemp = line2.strip().split()
                            for value in arrTemp[0:-1]:
                                if is_hex_string(value, 1):
                                    arr2.append(value)
                        #print(''.join(arr2)) # degistirilecek opcode

                        with open(f"{fileName}.temp", "r") as file3:
                            lines = file3.readlines()[0]
                            
                            writeOn = "90"*diff
                            begin = diff*2
                            opcode = ''.join(arr2)
                            #print(f"Mevcut instruction : {instruction}")
                            if lines.count(''.join(arr2)) == 1:
                                counter = counter + 1
                                print(f"{Fore.GREEN}[*]{Fore.RESET} Opcode patching process is being performed... Address : {Fore.GREEN}{address}{Fore.RESET}")
                                lines = lines.replace(opcode, (writeOn + opcode[begin:]))
                            if lines.count(''.join(arr2)) > 1:
                                counter = counter + 1
                                print(f"{Fore.GREEN}[!]{Fore.RESET} Address content was encountered in more than one place. Please change manually. Adres : {Fore.GREEN}{address}{Fore.RESET}")
                            

                        with open(f"{fileName}.temp", "w") as file4:
                            file4.write(lines)

                    

                cArr.clear()

            i = i + 1

    os.system(f"xxd -r -p {fileName}.temp > cleaned.{fileName}")



# jmp -1 kullanilmis mi?
os.system(f"objdump -d cleaned.{fileName} | grep -i 'jmp' > dump.txt")
with open('dump.txt', 'r') as file:
    i = 1

    for line in file:

        arr = line.strip().split()
        try:
            index = arr.index('jmp')
        except:
            continue
        if (is_hex_string(str(arr[index + 1]), 2)) == False:
            continue
        val = int(arr[(index + 1)].strip(":"), 16)
        
        val2 = int("0x"+arr[0].strip(":"), 16)


        if (val - val2) == 1: # Impossible Disassembly Teknigi Kullanilmis
            diff = 1

            address = str(arr[0].strip(":"))

            if control == 1:
                counter = counter + 1
                print(f"{Fore.GREEN}[*]{Fore.RESET} Address : {Fore.GREEN}{address}{Fore.RESET}")
                continue
            
            os.system(f"objdump -d {fileName} | grep -i -A 3 '{address}' > dump2.txt")
            
            
            with open('dump2.txt', 'r') as file2: # opcode alinarak degistiriliyor
                arr2 = []
                for line2 in file2:
                    arrTemp = line2.strip().split()
                    for value in arrTemp[0:-1]:
                        if is_hex_string(value, 1):
                            arr2.append(value)
                #print(''.join(arr2)) # degistirilecek opcode

                with open(f"{fileName}.temp", "r") as file3:
                    lines = file3.readlines()[0]
                    
                    writeOn = "90"*diff
                    begin = diff*2
                    opcode = ''.join(arr2)
                    #print(f"Mevcut instruction : {instruction}")
                    if lines.count(''.join(arr2)) == 1:
                        counter = counter + 1
                        print(f"{Fore.GREEN}[*]{Fore.RESET} Opcode patching process is being performed... Address : {Fore.GREEN}{address}{Fore.RESET}")
                        lines = lines.replace(opcode, (writeOn + opcode[begin:]))
                    if lines.count(''.join(arr2)) > 1:
                        counter = counter + 1
                        print(f"{Fore.GREEN}[!]{Fore.RESET} Address content was encountered in more than one place. Please change manually. Adres : {Fore.GREEN}{address}{Fore.RESET}")
                    

                with open(f"{fileName}.temp", "w") as file4:
                    file4.write(lines)

        i = i + 1

os.system(f"xxd -r -p {fileName}.temp > cleaned.{fileName}")




print(f"{Fore.GREEN}[!]{Fore.RESET} {counter} addresses found.")
print(f"{Fore.GREEN}[*]{Fore.RESET} Removing logs...")
os.remove("dump.txt")
if os.path.exists("dump2.txt"):
    os.remove("dump2.txt")
if os.path.exists(f"{fileName}.temp"):
    os.remove(f"{fileName}.temp")
if control != 1:
    print(f"{Fore.GREEN}[*]{Fore.RESET} Output -> cleaned.{fileName}")
else:
    if os.path.exists(f"cleaned.{fileName}"):
        os.remove(f"cleaned.{fileName}")

