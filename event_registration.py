'''
Created on Jul 27, 2020

@author: Daniel Granda
'''
import json
import os.path

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
        
class Registrants:
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
        #only adds if email and phone don't yet exist, otherwise updates contact
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
        else:
            print('Error: Contact not added')
        
    def findEmail(self, email):
        #searches through the contact list for a specified email and returns the contact
        #returns None if not found
        returnContact = None
        if(email is None):
            return returnContact
        for currentContact in self.contacts:
            if(currentContact.email == email):
                returnContact = currentContact
                break
        return returnContact
    
    def findPhone(self, phone):
        #searches through the contact list for a specified phone number and returns the contact
        #returns None if not found
        returnContact = None
        if(phone is None):
            return returnContact
        for currentContact in self.contacts:
            if(currentContact.phone == phone):
                returnContact = currentContact
                break
        return returnContact
    
    def printContacts(self):
        #prints contacts in an organized form
        print("Contacts")
        for h in self.contacts:
            print("\n\tName: " + str(h.name) + "\n\tEmail: " + str(h.email) + "\n\tPhone: " + str(h.phone))

class LeadsList:
    def __init__(self, leads):
        self.leads = leads
        
    def removeLead(self, lead, contactList):
        #removes lead from list given a specified lead
        #adds lead data into contacts
        if(lead is not None):
            if(lead.name is not None and (lead.email is not None or lead.phone is not None)):
                #only works if lead has a name and either/both email and phone
                contactList.addContact(lead.name, lead.email, lead.phone)
                self.leads.remove(lead);
        
    def findEmail(self, email):
        #searches through the lead list for a specified email and returns the lead
        #returns None if not found
        returnLead = None
        if(email is None):
            return returnLead
        for currentLead in self.leads:
            if(currentLead.email == email):
                returnLead = currentLead
                break
        return returnLead
    
    def findPhone(self, phone):
        #searches through the lead list for a specified phone number and returns the lead
        #returns None if not found
        returnLead = None
        if(phone is None):
            return returnLead
        for currentLead in self.leads:
            if(currentLead.phone == phone):
                returnLead = currentLead
                break
        return returnLead
    
    def printLeads(self):
        #prints leads in an organized form
        print("Leads")
        for h in self.leads:
            print("\n\tName: " + str(h.name) + "\n\tEmail: " + str(h.email) + "\n\tPhone: " + str(h.phone))
    
class RegistrantsList:
    def __init__(self, registrants):
        self.registrants = registrants
        
    def addFromJson(self, jsonFile):
        #given a file name, loads the registrant data from file and adds a registrant object to the registrant list
        if(os.path.isfile(jsonFile)):
            with open(jsonFile, 'r') as myFile:
                newRegInfo = json.load(myFile)
                newRegName = newRegInfo['registrant']['name']
                newRegEmail = newRegInfo['registrant']['email']
                newRegPhone = newRegInfo['registrant']['phone']
                newRegistrant = Registrants(newRegName, newRegEmail, newRegPhone)
                self.registrants.append(newRegistrant)
                
    def match(self, contacts, leads):
        #matches registrants with entries found within contacts list and leads list
        for entry in self.registrants:
            contactEmail = contacts.findEmail(entry.email)
            contactPhone = contacts.findPhone(entry.phone)
            leadEmail = leads.findEmail(entry.email)
            leadPhone = leads.findPhone(entry.phone)
            if(contactEmail is not None):
                #1. tries to match registrant with email from contacts
                #updates existing contact in contact list
                contacts.updateContact(contactEmail, entry.name, entry.email, entry.phone)
            elif(contactPhone is not None):
                #2. tries to match registrant with phone from contacts
                #updates existing lead in leads list
                contacts.updateContact(contactPhone, entry.name, entry.email, entry.phone)
            elif(leadEmail is not None):
                #3. tries to match registrant with email from leads
                #if found, removes entry from leads list and adds it to contact list
                leads.removeLead(leadEmail, contacts)
                #adds leads data into contact first, then updates contact data with new entry
                contacts.addContact(entry.name, entry.email, entry.phone)
            elif(leadPhone is not None):
                #4. tries to match registrant with phone from leads
                #if found, removes entry from leads list and adds it to contact list
                leads.removeLead(leadPhone, contacts)
                #adds leads data into contact first, then updates contact data with new entry
                contacts.addContact(entry.name, entry.email, entry.phone)
            else:
                #5. add to contacts list
                contacts.addContact(entry.name, entry.email, entry.phone)
        
    def printRegistrants(self):
        #prints registrants in an organized form
        print("Registrants")
        for h in self.registrants:
            print("\n\tName: " + str(h.name) + "\n\tEmail: " + str(h.email) + "\n\tPhone: " + str(h.phone))
        
#contacts data
contact1 = Contacts("Alice Brown", None, "1231112223")
contact2 = Contacts("Bob Crown", "bob@crowns.com", None)
contact3 = Contacts("Carlos Drew", "carl@drewess.com", "3453334445")
contact4 = Contacts("Doug Emtry", None, "4564445556")
contact5 = Contacts("Egan Fair", "eg@fairness.com", "5675556667")
#stores contacts data into ContactsList
myContacts = ContactsList([contact1, contact2, contact3, contact4, contact5])


#leads data
lead1 = Leads(None, "kevin@keith.com", None)
lead2 = Leads("Lucy", "lucy@liu.com", None)
lead3 = Leads("Mary Middle", "mary@middle.com", "3331112223")
lead4 = Leads(None, None, "4442223334")
lead5 = Leads(None, "ole@olson.com", None)
#stores leads data into LeadsList
myLeads = LeadsList([lead1, lead2, lead3, lead4, lead5])

#registrants data, creates empty registrants list
myRegistrants = RegistrantsList([])
#loads json data into registrants list via external files
regArray = ['registrant1.json', 'registrant2.json', 'registrant3.json'];
for reg in regArray:
    myRegistrants.addFromJson(reg)
    

#for testing purposes
"""
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

print(myRegistrants.registrants[0].name)

testRemove = myLeads.findPhone(3331112223)
print(testRemove.name)
myLeads.removeLead(testRemove, myContacts)
testRemove2 = myContacts.findPhone(3331112223)
print(testRemove2.name)
"""
myContacts.printContacts()
myLeads.printLeads()
#myRegistrants.printRegistrants()

myRegistrants.match(myContacts, myLeads)

myContacts.printContacts()
myLeads.printLeads()
#myRegistrants.printRegistrants()