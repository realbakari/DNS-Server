from DNS import*

class Blacklist(DNS):
    """ Domain Name Server System """
    def __init__(self):
        self._domainsblacklist = set()
        DNS.__init__(self)

    def newblacklist(self, IPA):
        self._domainsblacklist.add(IPA)

    def  domainlookup(self, domainName):
        print(domainName,self.table[domainName],self._domainsblacklist)
        if domainName in self.table and self.table[domainName] not in self._domainsblacklist:
            return (self.table[domainName])
        else:
            return ("None! ")
