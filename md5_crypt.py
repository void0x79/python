import requests
import hashlib
import re



url="http://docker.hackthebox.eu:32527/"

r=requests.session()
out=r.get(url)
out=re.search("<h3 align='center'>+.*?</h3>",out.text)
out=re.search("'>.*<",out[0])
out=re.search("[^|'|>|<]...................",out[0])

out=hashlib.md5(out[0].encode('utf-8')).hexdigest()

print("sending md5 :-{}".format(out))

data={'hash': out}
out = r.post(url, data = data)

print(out.text)
