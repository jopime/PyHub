# Parsing and manipulating URL using the furl library

from furl import furl

f = furl('http://www.google.com/?one=1&two=2')
f /= 'path'
del f.args['one']
f.args['three'] = '3'
f.args['username'] = 'vijay'
f.args['password'] = 'svijayb'
print(f.url)

x = furl('http://www.google.com/?one=1').add({'two':'2'}).url
print(x)
y = furl('http://www.google.com/?one=1&two=2').set({'three':'3'}).url
print(y)
z = furl('http://www.google.com/?one=1&two=2').remove(['one']).url
print(z) 

f = furl('https://user:pass@www.google.com:8080/')
print(f.scheme, f.username, f.password, f.host, f.port)

f = furl('http://www.google.com/')
f.fragment.path.segments = ['two', 'directories']
f.fragment.args = {'one': 'argument'}
print(f.url)

f.path = 'hello/i/am/vijay%20how%20you/'
print(f.path.segments)

f.path.segments = ['My', 'God', 'Python is', 'Awesome', '^`<>[]"#/?']
print(str(f.path))