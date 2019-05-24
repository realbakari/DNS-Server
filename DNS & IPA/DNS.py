import socket

host_ip = []

class DNS:
    def __init__(self):
        """First Domain name and IPA"""
        self.table = dict()

    def domain_lookup(self,domainName):
        """Retrieve a domain name for a IPA"""
        if domainName in self.table:
            return ("IPA for domain name " + domainName + " is: ", self.table[domainName])
        else:
            return ("None")

    def change(self,web,ipa):
        """Change the domain name for an IPA"""

        host_ip = socket.gethostbyname(ipa)

        if web in self.table:
            self.table[web] = ipa
            return ("Domain " +web+ " IPA has been changed to ", ipa)
        elif web not in self.table:
            self.table[web] = ipa
            return ("New domain " +ipa+ " has been added to IPA ",  host_ip)

    def update(self, old, new):
        return ("Domain name " +old+ " for IPA " + self.table[old] +" has been changed to ", new)
        self.table[new] = self.table[old]
        del self.table[oldDomain]
