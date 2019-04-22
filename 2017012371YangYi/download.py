import requests
url=""
r=requests.get(url,stream=True)
f=open("file_path","wb")
for chunk in r.iter_content(chunk_size=512):
    if chunk:
        f.write(chunk)
