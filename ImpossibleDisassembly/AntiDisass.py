import os
import sys
from colorama import Fore


help_info = """
Usage: antidisass.py [OPTIONS] [VALUE]
  -r                Default. Remove all anti disass methods
  -s                Shows addresses only

  Exp:  python3 antidisass.py malicious.exe
"""

if len(sys.argv) > 1:
    pass
else:
    print(help_info)
    exit()

banner = """
   _____          __  .__  ________  .__                              
  /  _  \   _____/  |_|__| \______ \ |__| ___________    ______ ______
 /  /_\  \ /    \   __\  |  |    |  \|  |/  ___/\__  \  /  ___//  ___/
/    |    \   |  \  | |  |  |    `   \  |\___ \  / __ \_\___ \ \___ \ 
\____|__  /___|  /__| |__| /_______  /__/____  >(____  /____  >____  >
        \/     \/                  \/        \/      \/     \/     \/ 

                            by aktas
            https://www.linkedin.com/in/alperaktasm/
"""

print(f"{Fore.RED}{banner}{Fore.RESET}")

instructions = {'jl', 'jg', 'je', 'jz', 'jne', 'jnb', 'jle', 'jge', 'jb', 'ja', 'jbe', 'jae', 'jnz'}

fileName = str(sys.argv[1])


addressDic = {}

os.system(f"xxd -p -c 0 {fileName} > {fileName}.temp") # opcode degerleri degistirilmek uzere kaydediliyor

for x,instruction in enumerate(instructions):
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

                cArr.append(val)

                if cArr[0] > cArr[-1]: # Impossible Disassembly Teknigi Kullanilmis
                    #print(arr[1:-2]) # opcode
                    diff = (cArr[0] - cArr[-1]) # kac byte atlamis?

                    address = str(hex(cArr[-1])).strip("0x")
                    os.system(f"objdump -d {fileName} | grep -i -A 3 '{address}' > dump2.txt")
                    
                    
                    with open('dump2.txt', 'r') as file2: # opcode alinarak degistiriliyor
                        arr2 = []
                        for line2 in file2:
                            arrTemp = line2.strip().split()
                            arr2.extend(arrTemp[1:-2])
                        #print(''.join(arr2)) # degistirilecek opcode

                        with open(f"{fileName}.temp", "r") as file3:
                            lines = file3.readlines()[0]
                            
                            writeOn = "90"*diff
                            begin = diff*2
                            opcode = ''.join(arr2)
                            #print(f"Mevcut instruction : {instruction}")
                            if lines.count(''.join(arr2)) == 1:
                                print(f"{Fore.GREEN}[*]{Fore.RESET} Opcode patching process is being performed... Address : {Fore.GREEN}{address}{Fore.RESET}")
                                lines = lines.replace(opcode, (writeOn + opcode[begin:]))
                            if lines.count(''.join(arr2)) > 1:
                                print(f"{Fore.GREEN}[!]{Fore.RESET} Adres icerigine birden fazla yerde karsilasildi. Lutfen manuel olarak degistirin. Adres : {Fore.GREEN}{address}{Fore.RESET}")
                            

                        with open(f"{fileName}.temp", "w") as file4:
                            file4.write(lines)

                    

                cArr.clear()

            i = i + 1

    os.system(f"xxd -r -p {fileName}.temp > cleaned.{fileName}")



for x,instruction in enumerate(instructions):
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

                    address = str(hex(cArr[-1])).strip("0x")
                    os.system(f"objdump -d {fileName} | grep -i -A 3 '{address}' > dump2.txt")
                    
                    
                    with open('dump2.txt', 'r') as file2: # opcode alinarak degistiriliyor
                        arr2 = []
                        for line2 in file2:
                            arrTemp = line2.strip().split()
                            arr2.extend(arrTemp[1:-2])
                        #print(''.join(arr2)) # degistirilecek opcode

                        with open(f"{fileName}.temp", "r") as file3:
                            lines = file3.readlines()[0]
                            
                            writeOn = "90"*diff
                            begin = diff*2
                            opcode = ''.join(arr2)
                            #print(f"Mevcut instruction : {instruction}")
                            if lines.count(''.join(arr2)) == 1:
                                print(f"{Fore.GREEN}[*]{Fore.RESET} Opcode patching process is being performed... Address : {Fore.GREEN}{address}{Fore.RESET}")
                                lines = lines.replace(opcode, (writeOn + opcode[begin:]))
                            if lines.count(''.join(arr2)) > 1:
                                print(f"{Fore.GREEN}[!]{Fore.RESET} Adres icerigine birden fazla yerde karsilasildi. Lutfen manuel olarak degistirin. Adres : {Fore.GREEN}{address}{Fore.RESET}")
                            

                        with open(f"{fileName}.temp", "w") as file4:
                            file4.write(lines)

                    

                cArr.clear()

            i = i + 1

    os.system(f"xxd -r -p {fileName}.temp > cleaned.{fileName}")





print(f"{Fore.GREEN}[*]{Fore.RESET} Removing logs...")
os.remove("dump.txt")
if os.path.exists("dump2.txt"):
    os.remove("dump2.txt")
if os.path.exists(f"{fileName}.temp"):
    os.remove(f"{fileName}.temp")
print(f"{Fore.GREEN}[*]{Fore.RESET} Output -> cleaned.{fileName}")

