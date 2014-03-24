from libmain import doRender
import webapp2



class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        values = dict()
        
        values['test'] = 'this is for my first test'
        doRender(self, 'index.html', values)
        
app = webapp2.WSGIApplication([
                              ('/.*', MainPageHandler)
                              ],debug = True)