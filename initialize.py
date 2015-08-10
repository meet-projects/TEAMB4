from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Person, Place, Story

engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

session.query(Place).delete()
session.query(Person).delete()
session.query(Story).delete()

### These are the commands you just saw live.
sima = Person(name='Sima', nationality='Awesome', gender='female', hometown='Nazareth')
#session.add(sima)
session.commit()

il = Place(country='Israel', nameId=sima.id)
#session.add(il)
session.commit()

story = Story(placeId=il.id, personId=sima.id, picture='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Bright_red_tomato_and_cross_section02.jpg/1024px-Bright_red_tomato_and_cross_section02.jpg')
#session.add(story)
session.commit()


