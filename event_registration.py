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
        
    def updateContact(self, contact, name, email, phone):
        #updates contact list at a specified contact
        #only updates data points assigned to None
        contactIndex = self.contacts.index(contact)
        if(contactIndex is not None):
            if(self.contacts[contactIndex].name is None):
                self.contacts[contactIndex].name = name
            if(self.contacts[contactIndex].email is None):
                self.contacts[contactIndex].email = email
            if(self.contacts[contactIndex].phone is None):
                self.contacts[contactIndex].phone = phone
        
    def addContact(self, name, email, phone):
        #adds a contact to the existing contact list
        #only adds if email and phone don't yet exist
        updateEmail = self.findEmail(email)
        updatePhone = self.findPhone(phone)
        if(updateEmail is None and updatePhone is None):
            #if neither email or phone are already input
            newContact = Contacts(name, email, phone)
            self.contacts.append(newContact)
        elif(updateEmail is not None):
            #if a contact exists with an existing email, update that contact
            self.updateContact(updateEmail, name, email, phone)
        elif(updatePhone is not None):
            #if a contact exists with an existing phone number, update that contact
            self.updateContact(updatePhone, name, email, phone)
        
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
        
    def removeLead(self, lead, contactList):
        #removes lead from list given a specified lead
        #adds it to a given contact list
        leadIndex = self.leads.index(lead)
        if(leadIndex is not None):
            contactList.addContact(lead.name, lead.email, lead.phone)
            self.leads.remove(lead);
        
    def findEmail(self, email):
        #searches through the lead list for a specified email and returns the lead
        #returns None if not found
        returnLead = None
        for currentLead in self.leads:
            if(currentLead.email == email):
                returnLead = currentLead
                break
        return returnLead
    
    def findPhone(self, phone):
        #searches through the lead list for a specified phone number and returns the lead
        #returns None if not found
        returnLead = None
        for currentLead in self.leads:
            if(currentLead.phone == phone):
                returnLead = currentLead
                break
        return returnLead

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


#for testing purposes
print('Hello World')
print(myLeads.leads[2].name)
testEmailSearch = myContacts.findEmail('bob@crowns.com')
testEmailSearch2 = myContacts.findEmail('nope')
print(testEmailSearch.name)
print(testEmailSearch2)
testPhoneSearch = myContacts.findPhone(5675556667)
testPhoneSearch2 = myContacts.findPhone(123412341234)
print(testPhoneSearch.name)
print(testPhoneSearch2)

testContact = myContacts.findEmail('carl@drewess.com')
tc2 = myContacts.contacts.index(testContact);
print(testContact.name)
print(myContacts.contacts[tc2].name)

testUpdate = myContacts.findEmail('bob@crowns.com')
print(testUpdate.name)
print(testUpdate.email)
print(testUpdate.phone)
myContacts.updateContact(testUpdate, 'Bob', 'bob@crowns.com', 2222222222)
testUpdate2 = myContacts.findEmail('bob@crowns.com')
print(testUpdate2.name)
print(testUpdate2.email)
print(testUpdate2.phone)