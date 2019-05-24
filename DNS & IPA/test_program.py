from Blacklist import *

blacklist_domain = Blacklist()

while True:
    CommandDNS = input(">>> ")
    Command = CommandDNS.split()
    if Command[0] == "blacklist":
        blacklist_domain.newblacklist(Command[1])
    elif len(Command) == 2:
        if "find" in Command:
            print(blacklist_domain.domain_lookup(Command[1]))
    elif len(Command) == 3:
        if "update" in Command:
            print(blacklist_domain.update(Command[1], Command[2]))
        elif "add" in Command:
            print(blacklist_domain.change(Command[1], Command[2]))

    else:
        print("Error 👻")

"""
Scripting >>>

Program Input example:
    add domain_lookup bakarimustafa.com
    update domain_lookup google.com
    find domain_lookup
    add domain_lookup google.com
    find domain_lookup
    blacklist newblacklist griffith.edu.au
    update domain_lookup fb.com
"""
