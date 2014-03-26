from libmain import doRender
import webapp2
import logging


from google.appengine.api import search

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        values = dict()
        
        doRender(self, 'index.html', values)
        
        
    def post(self):
        values = dict()
        
        t1 = self.request.get("t1")
        t2 = self.request.get("t2")        
        t3 = self.request.get("t3")
        t4 = self.request.get("t4")        
        t5 = self.request.get("t5")
        
        my_doc = search.Document(
            fields = [
                      search.TextField(name="title", value=t1),  #title
                      search.TextField(name="keywords", value=t2),  #keywords
                      search.TextField(name="metatheory", value=t3),  #metatheory
                      search.TextField(name="terms", value = t4),  #terms and definitions
                      search.TextField(name="propositions", value=t5),  #propositions
                      ])
        
        try:
            index = search.Index(name="modIdx")
            index.put(my_doc)
            logging.info("document created")
        
        except search.Error:
            logging.exception('Document Put Failed')        
        
        self.redirect('/')
        
        
        
app = webapp2.WSGIApplication([
                               ('/.*', MainPageHandler),
                              ('/.*', MainPageHandler)
                              ],debug = True)


