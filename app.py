import connection as connection
from flask import Flask
from getpass import getpass
from mysql.connector import connect, Error

app = Flask(__name__)


try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="ccsdataplatformdb",
    ) as connection:
        print(connection)
except Error as e:
    print(e)

if __name__ == '__main__':
    app.run()

@app.route('/')
def main():
    """Entry point; the view for the main page"""
    cities = [(record.city_id, record.city_name) for record in data]
    return render_template('main.html', cities=cities)



select_rhel = """
 SELECT *
 FROM WebBehavior
 WHERE product_facet = 'rhel'
 ORDER BY findability DESC
 """
with connection.cursor() as cursor:
     cursor.execute(select_rhel)
     for row in cursor.fetchall():
         print(row)





@app.route('/productview')
def productview():
    """The view for the Product Views page"""
    cities = [(record.city_id, record.city_name) for record in data]
    return render_template('productview.html', cities=cities)

@app.route('/contenttype')
def contenttype():
    """The view for the Product Views page"""
    cities = [(record.city_id, record.city_name) for record in data]
    return render_template('contenttype.html', cities=cities)

@app.route('/pageview')
def pageview():
    """The view for the Product Views page"""
    cities = [(record.city_id, record.city_name) for record in data]
    return render_template('pageview.html', cities=cities)



if __name__ == '__main__':
    app.run()
