from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

metadata = MetaData()
engine = create_engine('sqlite:///user_database', connect_args={'check_same_thread': False}, echo=False)  # echo=False
Base = declarative_base()
db_session = sessionmaker(bind=engine)()


# Table web_behavior
class web_behavior (Base):
    __tablename__ = 'web_behavior'
    city_id = Column(Integer, primary_key=True)
    city_name = Column(String)
    city_climate = Column(String)
    city_meteo_data = relationship("Meteo", backref="city")

# Retrieving data from the database
def get_cities():
    return db_session.query(City)


# Generating the set of average temperature values for a particular city
def get_city_temperature(city):
    return [month.average_temperature for month in city.city_meteo_data]


# Generating the set of average humidity values for a particular city
def get_city_humidity(city):
    return [month.average_humidity for month in city.city_meteo_data]


data = get_cities()
MONTHS = [record.month for record in data[0].city_meteo_data]
CITIES = [city.city_name for city in data]
