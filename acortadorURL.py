import urllib.request

def tiny_url(url):
    apiurl = "http://tinyurl.com/api-create.php?url="
    tinyurl = urllib.request.urlopen(apiurl+url).read()
    return tinyurl.decode("utf-8")

url = input("ingrese aqui su direccion url a acortar:")
print(tiny_url(url))
