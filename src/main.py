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
        
        
class SearchPageHandler(webapp2.RequestHandler):
    def get(self):
        values = dict()
        doRender(self, 'search.html', values)
    
    def post(self):
        values = dict()
        searchString = self.request.get("searchbox")
        
        index = search.Index(name="modIdx")
        querystring = searchString.strip()
        doc_limit = 5        
        
        try:
            search_query = search.Query(
                                        query_string = querystring,
                                        options = search.QueryOptions(
                                                        limit = doc_limit,
                                                        snippeted_fields=["metatheory","propositions"],
                                                        returned_fields=["title","keywords","metatheory","terms","propositions"]
                                                                      ),
                                        )
            
            
            results = index.search(search_query)
        
        except search.Error:
            logging.exception('search failed')
        c1 = 0
        for doc in results:
            logging.error('DOC ' + str(c1) + ':::::')
            
            """ doc = 
            search.ScoredDocument(
            doc_id=u'20d33410-dafc-409c-aaa4-02416ddaffee', 
            fields=[
                search.TextField(name=u'title', value=u'great news'),       
                search.TextField(name=u'keywords', value=u'bad news'), 
                search.TextField(name=u'metatheory', value=u'neutral news'), 
                search.TextField(name=u'terms', value=u'ok news'), 
                search.TextField(name=u'propositions', 
                    value=u'djalkjdfla cnn news djsadlfsjalfk, dfjd, jdskfjds, kajlj.')], 
            language=u'en', rank=102028823L, 
            expressions=[
                search.HtmlField(name=u'metatheory', value=u'...<b>news</b>...'), 
                search.HtmlField(name=u'propositions', value=u'...djalkjdfla cnn <b>news</b> djsadlfsjalfk dfjd jdskfjds kajlj...')
            ])
            
            """
            
            
            
            for expr in doc.expressions:
                logging.error("expr:" + str(expr))
                
                sth = expr.value
                logging.error("sth"+ str(c1) +str(sth))
                
                c1 += 1
                
            for field in doc.fields:
                
                sthelse = str(field.name) + " : " + str(field.value)
                
                logging.error('######## field ##################')
                logging.error("sthelse:::" + str(sthelse))
        
        
        
        
        
        doRender(self, 'search.html', values)
        



app = webapp2.WSGIApplication([
                               ('/search', SearchPageHandler),
                              ('/.*', MainPageHandler)
                              ],debug = True)


