import cherrypy
import datetime

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <body>
            <form method="get" action="generate_time">
              <button type="submit">Время</button>
            </form>
             <form method="get" action="generate_date">
              <button type="submit">Дата</button>
              <input tupe="reset" value="перезагрузка">
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate_time(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time

    @cherrypy.expose
    def generate_date(self):
        date = datetime.date.today()
        return str(date)

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())