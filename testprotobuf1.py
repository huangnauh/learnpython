import addressbook_pb2
import sys

def ListPeople(address_book):
	for person in address_book.person:
		print "Person ID:", person.id
		print "Name:",person.name
		if person.HasField('email'):
			print "  E-mail address:", person.email
		if person.HasField('ha'):
			print "  age:", person.ha.age
			print "  sex:", person.ha.sex
		for pho in person.phone:
			if pho.type == addressbook_pb2.Person.MOBILE:
				print "  Mobile phone #: ",
			elif pho.type == addressbook_pb2.Person.HOME:
				print "  Home phone #: ",
			elif pho.type == addressbook_pb2.Person.WORK:
				print "  Work phone #: ",
			print pho.number

def main():
	if len(sys.argv)!=2:
		print "Usage:", sys.argv[0], "ADDRESS_BOOK_FILE"
		sys._exit(-1)
	address_book = addressbook_pb2.AddressBook()
	f = open(sys.argv[1],'rb')
	address_book.ParseFromString(f.read())
	f.close()
	ListPeople(address_book)
	
main()