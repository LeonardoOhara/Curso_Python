import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen("https://www.google.com.br/")
except urllib.error.URLError:
    print("Não foi possível acessar o site google.com.br")
else:
    print("Site google.com.br acessado com sucesso!")
#   print(site.read()) <-- Comando para ver todos html do site
    