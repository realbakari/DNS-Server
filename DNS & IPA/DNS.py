

class DNS:
    def __init__(self):
        """First Domain name and IPA"""
        self._IPAdict = dict()

    def domain_lookup(self,domainName):
        """Retrieve a domain name for a IPA"""
        if domainName in self._IPAdict:
            return ("IPA for domain name " + domainName + " is: ", self._IPAdict[domainName])
        else:
            return ("None")

    def change(self,changeDomain,changeIPA):
        """Change the domain name for an IPA"""
        if changeDomain in self._IPAdict:
            self._IPAdict[changeDomain] = changeIPA
            return ("Domain " +changeDomain+ " IPA has been changed to ", changeIPA)
        elif changeDomain not in self._IPAdict:
            self._IPAdict[changeDomain] = changeIPA
            return ("New domain " +changeDomain+ " has been added to IPA ", changeIPA)

    def uptodatedomain(self, old, new):
        return ("Domain name " +old+ " for IPA " + self._IPAdict[old] +" has been changed to ", new)
        self._IPAdict[new] = self._IPAdict[old]
        del self._IPAdict[oldDomain]