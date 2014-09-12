from sqlalchemy import Table,Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sqlalchemy as sa
import sqlalchemy.orm as orm
Base = declarative_base()
class Customer(Base):
	__tablename__ = 'customer'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	billing_address_id = Column(Integer, ForeignKey("address.id"))
	shipping_address_id = Column(Integer, ForeignKey("address.id"))
	billing_address = relationship("Address",foreign_keys=[billing_address_id])
	shipping_address = relationship("Address",foreign_keys=[shipping_address_id])

class Address(Base):
	__tablename__ = 'address'
	id = Column(Integer, primary_key=True)
	street = Column(String)
	city = Column(String)
	state = Column(String)
	zip = Column(String)

node_to_node = Table("node_to_node", Base.metadata,
	Column("left_node_id", Integer, ForeignKey("node.id"), primary_key=True),
	Column("right_node_id", Integer, ForeignKey("node.id"), primary_key=True)
)
class Node(Base):
	__tablename__ = 'node'
	id = Column(Integer, primary_key=True)
	label = Column(String)
	right_nodes = relationship("Node",
	secondary=node_to_node,
	primaryjoin=id==node_to_node.c.left_node_id,
	secondaryjoin=id==node_to_node.c.right_node_id,
	backref="left_nodes"
	)
	
class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	firstname = Column(String)
	lastname = Column(String)
	fullname = orm.column_property(firstname+lastname)

engine = sa.create_engine("sqlite:///:memory:",echo=True)
Base.metadata.create_all(engine)
session = orm.sessionmaker(engine)()
u=User(firstname='huang',lastname="libo")
print(u.firstname,u.fullname)

