from flask import Flask, render_template
app = Flask(__name__)

# SQLAlchemy stuff
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Person, Place, Story

engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def main():
    return render_template('main_page.html')

def disp_countries():
    allCountries = session.query(Place).all()
    return render_template('list_of_countries.html', countries=allCountries)

if __name__ == '__main__':
    app.run(debug=True)




