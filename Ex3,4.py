import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head>
            <style>
              body
              {
                background:	#800080
              }
              input[type=text]
              {
                width:300px;
                height:100px;
                font-size: 40px;
                margin-left:500px;
                margin-bottom:20px;
              }   
              button
              {
                width:300px;
                height:100px;
                font-size: 40px;
                margin-left:500px;
                margin-bottom:20px;
              }
            </style>
          </head>
          <body>
            <h1>Калькулятор </h1>
            <form method="get" action="Calculator">
              <div class="Number_1">
                <input type="text"  name="Number_1" placeholder="Первое число">
              </div>
              <div class="action">
                <input type="text" name = "action" placeholder="Действие">
              </div>
              <div class="Number_2">
                <input type="text" name ="Number_2" placeholder="Второе число">
              </div>
              <div class="button">
                <br><button type="submit"> = </button>
              </div>
            </form>
          </body>
        </html>"""
    
    @cherrypy.expose
    def Calculator(self,Number_1, action, Number_2):
      return str(eval(f"{Number_1}{action}{Number_2} "))
    

cherrypy.quickstart(StringGenerator())