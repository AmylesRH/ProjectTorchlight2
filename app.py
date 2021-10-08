import connection as connection
from flask import Flask
from getpass import getpass
from mysql.connector import connect, Error

app = Flask(__name__)


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='https://ccsdata.apps.ocp4.prod.psi.redhat.com',
                                       database='ccsdataplatformdb',
                                       user='userBO1',
                                       password=getpass("Enter password: ")
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()

select_product = """
 SELECT *
 FROM WebBehavior
 ORDER BY findability DESC
 """
with connection.cursor() as cursor:
     cursor.execute(select_rhel)
     for row in cursor.fetchall():
         print(row)

@app.route('/')
def main():
    """Entry point; the view for the main page"""
return render_template('main.html')

@app.route('/productview')
def productview():
    """The view for the Product Views page"""
    return render_template('productview.html')

@app.route('/contenttype')
def contenttype():
    """The view for the Content Type page"""
    return render_template('contenttype.html')

@app.route('/pageview')
def pageview():
    """The view for the Page Views page"""
    return render_template('pageview.html')



if __name__ == '__main__':
    app.run()
