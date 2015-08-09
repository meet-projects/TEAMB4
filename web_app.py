from flask import Flask, render_template
app = Flask(__name__)

# SQLAlchemy stuff
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///crudlab.db')
base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


#YOUR WEB APP CODE GOES HERE
Base = declarative_base() 

class Place(Base): 
    __tablename__ = 'place' 
    id = Column(Integer, primary_key=True) 
    country = Column(String) 
    nameId = Column(Integer)

class Person(Base):
    __tablename__ = 'person' 
    id = Column(Integer, primary_key=True) 
    name = Column(String) 
    nationality = Column(String) 
    gender = Column(String) 
    hometown = Column(String)
    
class Story(Base):
    __tablename__ = 'story' 
    id = Column(Integer, primary_key=True) 
    placeId = Column(Integer) 
    personId = Column(Integer) 
    picture = Column(String)
    

@app.route('/')
def main():
    allCountries = session.query(Place).all()
    return render_template('main_page.html', countries=allCountries)


if __name__ == '__main__':
    app.run(debug=True)




