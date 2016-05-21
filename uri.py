import re

class uri:

   def __init__(self, uri_string):
      self.full = uri_string
      if '://' in uri_string: 
        self.schema = uri_string.split(':')[0]
        t = uri_string.replace(self.schema+'://','').split('/')
      else:
        self.schema = ''
        t = uri_string.split('/')
      if self.schema == '':
         self.domain = t[0]
      else:
         self.domain = t[0]
      if '/' in uri_string:
          self.path = t[1]
      else:
          self.path = ''
      if '?' in uri_string:
          self.query = uri_string.split('?')[len(uri_string.split('?'))-1]
      else:
          self.query = ''
      
      
