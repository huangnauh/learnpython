import addressbook_pb2
import sys
def test():
	addressbook = addressbook_pb2.AddressBook()
	person = addressbook_pb2.Person()
	print person.HasField("name")
	person.id = 1234
	person.name = "huanglibo"
	print person.HasField("name")
	person.email = "huanglibo2010@gmail.com"
	phone = person.phone.add()
	phone.number = "13915998007"
	phone.type = addressbook_pb2.Person.HOME
	
	p = addressbook.person.add()
	
def PromptForAddress(person):
	person.id = int(raw_input("Enter person ID number:"))
	person.name = raw_input("Enter name:")
	email = raw_input("Enter email address (blank for none): ")
	if email != '':
		person.email = email
	age = raw_input("Enter age (blank for none): ")
	if age != '':
		age = int(age)
		person.ha.age = age
		sex = raw_input("Enter sex(male,female): ")
		if sex == "male":
			person.ha.sex = addressbook_pb2.Person.MALE
		elif sex == "female":
			person.ha.sex = addressbook_pb2.Person.FEMALE
		else:
			print "Unknown sex type; leaving as default value."
			
	while 1:
		number = raw_input("Enter a phone number (or leave blank to finish):")
		if number == "":
			break
		phone_number = person.phone.add()
		phone_number.number = number
		type = raw_input("Is this a mobile, home, or work phone? ")
		if type == "mobile":
			phone_number.type = addressbook_pb2.Person.MOBILE
		elif type == "home":
			phone_number.type = addressbook_pb2.Person.HOME
		elif type == "work":
			phone_number.type = addressbook_pb2.Person.WORK
		else:
			print "Unknown phone type; leaving as default value."
		
if len(sys.argv) != 2:
	print "Usage:", sys.argv[0], "ADDRESS_BOOK_FILE"
	sys.exit(-1)
		
address_book = addressbook_pb2.AddressBook()
		
try:
	print sys.argv[1]
	f = open(sys.argv[1],'rb')
	address_book.ParseFromString(f.read())
	f.close
except IOError,e:
	print e
	print sys.argv[1] + ": Could not open file.  Creating a new one."
	
PromptForAddress(address_book.person.add())
f = open(sys.argv[1], "wb")
f.write(address_book.SerializeToString())
f.close()
