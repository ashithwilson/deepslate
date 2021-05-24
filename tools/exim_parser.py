import subprocess,re,sys,itertools;
import argparse;
parser=argparse.ArgumentParser(
    description="To summarize exim_log output "
    )
parser.add_argument('EmailId',help="The email id or domain of which we need to genrate summary")
parser.add_argument('-l', '--list', help="""Provide a list of values you need to search.seperate each input with coma(,) \n
 eg: exim_parser abc.com -l "hello world","hello@helo.com",abc2.com """, type=str)
args=parser.parse_args();
eximString="";
if args.list is not None:
 my_list = [str(item) for item in args.list.split(',')]
 print my_list;
 for i in my_list:
  eximString=eximString+"|"+"exigrep "+"\""+i+"\"";
 print eximString;
black='\033[30m'
redy='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
pink='\033[95m'
cyan='\033[36m'
reset='\033[0m'
print(args.EmailId);
spinner = itertools.cycle(['-', '/', '|', '\\'])
subprocesscalls="exigrep "+"\""+args.EmailId+"\""+" /var/log/exim_mainlog"+eximString+"|cat"
lines=[];
pt = subprocess.Popen(subprocesscalls,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
while True:
  line = pt.stdout.readline();
  lines.append(line);
  if not line:
    break
  sys.stdout.write(next(spinner))   
  sys.stdout.flush()                
  sys.stdout.write('\b')
#lines = pt.stdout.readlines();
intial_regex="T=.*from[\s]*<.*>"
fromaddress="";
j=0;
z=0;
if len(lines) == 1:
    print("No results found!")
    exit();
for i in lines:
 if(re.search(intial_regex,i)):
   print("}");
   currentstring=str(re.findall(intial_regex,i));
   #print(currentstring);
   #print(str(re.findall("from\s<.*@.*>",currentstring)).replace("from ",""))
   fromaddress=str(re.findall("from\s<.*@.*>",currentstring)).replace("from ","").replace("'"," ").strip("from").replace('<',"").replace(">","").replace(" ","").replace("[","").replace("]","")
   subject=str(re.findall("T=.*from\s<",currentstring)).replace("T=","").replace("from","").replace('<',"").strip("[]");
   print("{")
   print ("From: "+green+fromaddress+reset);
   print("Subject : "+cyan+subject+reset);
   if fromaddress and subject:
      eximID=i.split()[2];
      timestamp=i.split()[0]+" "+i.split()[1];
      print("EximID: "+blue+eximID+reset)
      print("TimeStamp: "+redy+timestamp+reset)
      
   z=z+1;
   #print("F=<"+fromaddress+">")
 elif ("F=<"+fromaddress+">") in i:
  #print fromaddress+"from"
  #toAdd=str(re.findall("<.*>[\s]+F",i));
  toAdd=str(re.findall("[^\s]+@.*[\s]+F=",i)).replace("F=']","").strip("[]<>'").replace(">","");
  status=re.sub('.*[$=]','',i).strip('""')
  print("TO : "+orange+toAdd+reset+reset);
  #print("EximID:"+blue+eximID+reset)
  print("Status:"+pink+status+reset)
  z=z+1;
if z == 0:
    print("Not able to extract contents!!Try manually..")
print(pink+"\nThe above details are parsed from the active exim main log and would not contain any details from old/archived logs"+reset)


