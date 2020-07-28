'''
Created on Jul 27, 2020

@author: Daniel Granda
'''

class Contacts:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        

class Leads:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class ContactsList:
    def __init__(self, contacts):
        self.contacts = contacts
        
    def updateContact(self, index, name, email, phone):
        #updates contact list at a specified index
        #only updates data points assigned to None
        print('no u')
        
    def addContact(self, name, email, phone):
        #adds a contact to the existing contact list
        newContact = Contacts(name, email, phone)
        self.contacts.append(newContact)
        
    def findEmail(self, email):
        #searches through the contact list for a specified email and returns the contact
        #returns None if not found
        returnContact = None
        for currentContact in self.contacts:
            if(currentContact.email == email):
                returnContact = currentContact
                break
        return returnContact
    
    def findPhone(self, phone):
        #searches through the contact list for a specified phone number and returns the contact
        #returns None if not found
        returnContact = None
        for currentContact in self.contacts:
            if(currentContact.phone == phone):
                returnContact = currentContact
                break
        return returnContact

class LeadsList:
    def __init__(self, leads):
        self.leads = leads

#contacts data
contact1 = Contacts('Alice Brown', None, 1231112223)
contact2 = Contacts('Bob Crown', 'bob@crowns.com', None)
contact3 = Contacts('Carlos Drew', 'carl@drewess.com', 3453334445)
contact4 = Contacts('Doug Emtry', None, 4564445556)
contact5 = Contacts('Egan Fair', 'eg@fairness.com', 5675556667)
#stores contacts data into ContactsList
myContacts = ContactsList([contact1, contact2, contact3, contact4, contact5])


#leads data
lead1 = Leads(None, 'kevin@keith.com', None)
lead2 = Leads('Lucy', 'lucy@liu.com', None)
lead3 = Leads('Mary Middle', 'mary@middle.com', 3331112223)
lead4 = Leads(None, None, 4442223334)
lead5 = Leads(None, 'ole@olson.com', None)
#stores leads data into LeadsList
myLeads = LeadsList([lead1, lead2, lead3, lead4, lead5])

print('Hello World')
print(myLeads.leads[2].name)
testEmailSearch = myContacts.findEmail('bob@crowns.com')
testEmailSearch2 = myContacts.findEmail('nope')
print(testEmailSearch.name)
print(testEmailSearch2)