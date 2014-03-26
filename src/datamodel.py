from google.appengine.ext import db

class Counter(db.Model):
    name = db.StringProperty()
    count = db.IntegerProperty()

class Module(db.Model):
    title = db.StringProperty()
    keywords = db.StringProperty()
    theoryMarkdown = db.TextProperty()
    theoryHtml = db.TextProperty()
    uid = db.IntegerProperty()
    version = db.IntegerProperty()
    scope = db.StringListProperty()
    propositions = db.StringListProperty()
    derivations = db.StringListProperty()
    evidence = db.TextProperty()

    date_submitted = db.DateTimeProperty(auto_now_add=True)
    last_update = db.DateTimeProperty(auto_now=True)
    
    editors = db.ListProperty(db.Key)
    
    published = db.BooleanProperty()
    current = db.BooleanProperty()
    

# #One Term to many TermDefinitions
class Term(db.Model):
    word = db.StringProperty(required=True)
    slug = db.StringProperty(required=True)
    date_submitted = db.DateTimeProperty(auto_now_add=True)
    uid = db.IntegerProperty()

#Many TermDefinitions to one Term
class TermDefinition(db.Model):
    term = db.ReferenceProperty(Term)
    definition = db.StringProperty()
    date_defined = db.DateTimeProperty(auto_now_add=True)
    uid = db.IntegerProperty()
     
#Describes the relation of module and terms
class ModuleTerm(db.Model):
    module = db.ReferenceProperty(Module)
    term = db.ReferenceProperty(Term)
    definition = db.ReferenceProperty(TermDefinition)
 
    