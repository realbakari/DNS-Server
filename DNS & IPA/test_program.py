from Blacklist import*

blacklist_domain = Blacklist()

while True:
    CommandDNS = input("👉 ")
    Command = CommandDNS.split()
    if Command[0] == "blacklist":
        blacklist_domain.newblacklist(Command[1])
    elif len(Command) == 2:
        if "find" in Command:
            print(blacklist_domain.domain_lookup(Command[1]))
    elif len(Command) == 3:
        if "change" in Command:
            print(blacklist_domain.uptodatedomain(Command[1],Command[2]))
        elif "add" in Command:
            print(blacklist_domain.change(Command[1],Command[2]))

    else:
        print("Error 👻")

"""
Scripting

Python Terminal
    1. Un-comment these lines
    2. Run find find domain_lookup bakarimustafa.com
    3. Find domain_lookup
    4. change domain_lookup / enter domain of choice
    
Common Scriptting lines
    Find / domain
    Change / domain
    Add / domain
    Blacklist / domain
"""