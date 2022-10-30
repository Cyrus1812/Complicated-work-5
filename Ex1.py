import cherrypy
import datetime


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time
        

if __name__=="__main__":
    cherrypy.quickstart(HelloWorld())