import requests

u_in = raw_input()
count = 1
while True:
    r = requests.get('http://asciinema.com/a/'+str(count))
    count+=1
    if r.status_code != 200:
        continue
    if u_in in r.text:
        print 'http://asciinema.com/a/'+str(count)
    if count>100000:
        break

