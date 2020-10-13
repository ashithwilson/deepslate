# We can copy and paste html content of kb's so this convert the kb's to full text by uploading images imagebb so that we can give them to our clients. We can copy html from firefox>>Select the all the contenets we need to make kb >>Right click>>View selection

# initial setup :
# 1. install bs4 to your user directory, pip install bs4 --user
# 2. create an account in Imagebb and get an API key
# 3. Add the api key in api_key variable
# 4. Save this as python file in your wss machine
 

import requests,re,subprocess;
from bs4 import BeautifulSoup;
api_key="";
print "Paste the HTML. press Ctrl-D after pasting it."
with open("kb_test.html", 'w'): pass
with open("kb_test.html",'a+') as fc:
 while True:
    try:
        line = raw_input("")
    except EOFError:
        break
    fc.write(line+"\n");

with open("kb_test.html","r")as fd:
  soup=BeautifulSoup(fd,'html.parser');

images=soup.find_all('img');
#image_urls=[];
pt="curl -ks --location --request POST \"https://api.imgbb.com/1/upload?key="+api_key+"\" --form \"image="
for i in images:
 rt=pt+i['src']+"\""
 mt=subprocess.check_output(rt,shell=True);
 new_text=soup.new_tag("div");
 new_text.string=str(re.findall("display_url.*\"title\"",mt)).split("display_url\":\"")[1].split("\"")[0].replace("\\","");
 i.insert_after(new_text);
 #new_text.insert_after(new_brk);
all_text = soup.getText();
pt=all_text.split("\n");
my_regex="[https:\/\/i.ibb.co\/]\/.*\/.*"
for i in pt:
 if(re.search(my_regex,i)):
  print("\n===========================================")
  print(i);
  print("===========================================\n")
 else:
  print i.lstrip();

