#MODELS HERE USING SQLALCHEMY
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///issuetracker.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
#creates data persistence
sessions= Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    def __repr__(self):
        return "<User(fullname='%s', username='%s')>" % (self.fullname, self.username)
    def create_database(self):
        Base.metadata.create_all(engine)

    def logins(self,email,password):
        #data = session.query.filter(User.username == name).filter(User.password == passw)
        data = sessions.query(User).filter(User.username == username).\
        filter(User.password == password).all()
        return len(data)

    def User_count(self):
        return sessions.query(User).count() 

    def insert_data(self,**args):
        '''
        insert data
        '''
        add_user = User(**args)
        print (add_user)
        sessions.add(add_user)
        sessions.commit()
        return ''

    def get_all(self):
        return sessions.query(User).all()

    def search_email(self, email1):
        '''
        search by email
        '''
        user = sessions.query(User).filter(User.email ==email1).all()
        return user

    # def get_phonenumber(self, session_email):
    #     '''
    #     search by email
    #     '''
    #     phone = sessions.query(User).filter(User.email == session_email).all()
    #     phonenumber = ''
    #     for i in phone:
    #         phonenumber = i.phonenumber

    #     return phonenumber

class Transactions(Base):
    __tablename__='Transactions'
    id = Column(Integer,primary_key=True)
    date_created = Column(String)
    amount = Column(String)
    product_name = Column(String)
    username = Column(String)
    status = Column(String)
    def __repr__(self):
        return "<Transactions(date_created='%s',amount='%s',Product_name='%s',status='%s')>" %(self.date_created,self.amount,self.product_name,self.status)
    
    def create_database(self):
        Base.metadata.create_all(engine)

user1 = User()
user1.create_database()



