import requests

student = 000000
files = ['target', 'input']

for file in files:
    print(file)
    r = requests.get('http://156.17.43.89:8080/psw/%s_%i.npy' % (file, student), allow_redirects=True)
    open('%s.npy' % file , 'wb').write(r.content)
