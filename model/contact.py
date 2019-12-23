from sys import maxsize

class Contact:
    def __init__(self, firstname = None, middlename = None, lastname = None, nickname = None, homephone = None, mobilephone = None, workphone = None, secondaryphone = None, address = None, title = None,
                 all_phones_from_home_page = None, company = None, email = None, email2 =None, email3 = None, all_email_from_home_page = None, id= None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.address = address
        self.title = title
        self.company = company
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_email_from_home_page = all_email_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page
        self.id = id

    def __repr__(self):
        return "id - %s, firstname - %s, middlename - %s, lastname - %s, nickname - %s,  title - %s, company - %s, email - %s" % (self.id, self.firstname, self.middlename, self.lastname, self.nickname, self.title,self.company, self.email)

    def __eq__(self, other):
        return (self.id == other.id or other.id is None or self.id is None) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
