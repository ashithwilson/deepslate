import argparse,re,os,sys,subprocess
#from collections import Counter
def progressBar(value, endvalue, bar_length=20):
        percent = float(value) / endvalue
        arrow = '-' * int(round(percent * bar_length)-1) + '>'
        spaces = ' ' * (bar_length - len(arrow))
        sys.stdout.write("\rProgress: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
        sys.stdout.flush()

parser=argparse.ArgumentParser(
    description="To print  cPanel access log in more readable format"
)
pink='\033[95m'
reset='\033[0m'
parser.add_argument('user', help="Domain name")
args=parser.parse_args()
array2=[]
if re.search(".",args.user):
        subprocesscalls="/scripts/whoowns"+" "+args.user
        out=subprocess.Popen(subprocesscalls,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        user=out.stdout.readline().replace("\n","");
        if user:
                args.user=user;
        else:
                print(pink+"Username or domain name doesn't exist"+reset)
                exit();
print(args)
subprocess_call="grep "+args.user+" /usr/local/cpanel/logs/access_log"
sizey=subprocess.Popen(subprocess_call+"|wc -l",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
county=int(sizey.stdout.readline());
pt = subprocess.Popen(subprocess_call,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
progress=0
while True:
  line = pt.stdout.readline();
  progress=progress+1
  progressP=(float(progress))/county
  progressBar(int(progressP*100),100)
  #skipping our IP's
  if line.split()[0] not in ["115.110.127.198","122.15.255.69","115.110.71.146","182.73.214.22","111.93.159.50","220.227.162.29","124.79.131.170","182.74.165.114"]:
    array2.append(line)
  if not line:
    break
           
keywords={
    'addb.html' : ['Database addition'],
    'deldb.html' : ['Database deletion','(?<=html\?db=).*(?=\sHTTP\/)|\s(?=2083)|\s(?=2082)'],
    'simple.html' : ['Simple DNS Zone editor'],
    'advanced.html' : ['Advanced DNS Zone Editor'],
    'The+row+has+been+deleted   ' : ['Database Deletion (phpMyAdmin)'],
    'passwd' : ['cPanel password change'],
    'add_pop' : ['Email account creation'],
    'delpop' : ['Email account deletion'],
    'passwdpop' : ['Email account password reset '],
    'doaddfwd' : ['Email forwarder creation '],
    'dodelfwd' : ['Email forwarder deletion','(?<=html\?email=).*(?=&emaildest=)|(?<=&emaildest=).*(?=\sHTTP\/)|(?<=\s2083)[-]|(?<=\s2082)\s[-]'],
    'doaddparked' : ['Park Domain Addition','(?<=\?domain=).*(?=&)|\s(?=2083)|\s(?=2082)'],
    'dodelparked' : ['Park Domain deletion','(?<=dodelparked.html\?domain=).*(?=\sHTTP\/)|[\s](?=2083)|[\s](?=2082)'],
    'doadddomain' : ['Addon Domain addition '],
    'confirmdodeldomain' : ['Addon Domain deletion '],
    'subdomain/doadddomain.html' : ['Sub Domain addition','(?<=domain=)[a-zA-z.-0-9]+(?=&rootdomain)|(?<=rootdomain=)[a-zA-Z0-9.-]+(?=&dir)|[.]$'],
    'dodeldomainconfirm.html' : ['Sub Domain deletion','(?<=\?domain=).*(?=_)|(?<=_)[a-zA-Z.0-9-]+(?=&domain)|[.]$'],
    'add_ftp' : ['FTP account addition','(?<=user=).*(?=&domain)|(?<=domain=).*(?=&pass)|[@]'],
    'delete_ftp' : ['FTP account deletion','(?<=user=).*(?=\%40)|(?<=\%40).*(?=&cache)|[@]'],
    'addredirect.html' : ['Redirection addition'],
    'delredirectconfirm.html' : ['Redirection deletion'],
    'scripts/chrootpass' : ['Root Password Reset '],
    'doadddfwd.html' : ['Addition of Domain forwarder [email]'],
    'dodeldfwdconfirm.html' : ['Deletion of domain forwarder [email]'],
    'mxcheck=local' : ['Change in Email Routing settings (local)'],
    'mxcheck=remote' : ['Change in Email Routing settings (remote)'],
    'Cron&cpanel_jsonapi_func=add_line' : ['Cron-job addition'],
    'Cron&cpanel_jsonapi_func=remove_line' : ['Cron-job deletion'],
    'remove_email_id' : ['Email account deletion'],
    'add_email_id' : ['Email account creation'],

}



def count_IPs():
 m=[]
 print("\n=============================================================")
 print("IPAddress               "+"Number of access")
 print("=============================================================")
 b = {}
 for i in array2:
         b[i.split()[0]] = b.get(i.split()[0], 0) + 1
         #Counter(m).keys()
         #Counter(m).values()
 for key,value in sorted(b.items(), key=lambda x:x[1],reverse=True):
  print(pink+str(key)+reset+"\t\t"+str(value))
count_IPs()
#a_keywords = {'fileman':['POST','fileman']}
print("\n=============================================================")
print("Time"+"                    "+"IP"+"              "+"Operation")
print("=============================================================")
for i in array2:
        for key,value in keywords.items():
          if key in i:
              if len(value)==2:
                  g=re.findall(value[1],i.strip("\n")+"-"+"@"+".")
                  addinfo=g[-1].join(g[:-1])
                  print(i.split()[3].replace("[","")+"\t"+pink+i.split()[0]+reset+"\t"+value[0]+"("+addinfo.replace('%40','@').strip("\n")+")")
              elif len(value)==1:
                  print(i.split()[3].replace("[","")+"\t"+pink+i.split()[0]+reset+"\t"+value[0])

        if "POST" in i and "fileman" in i:
                 print(i.split()[3].replace("[","")+"\t"+pink+i.split()[0]+reset+"\t"+"Filemanager POST")
        elif "POST" in i and "phpMyAdmin" in i:
                 print(i.split()[3].replace("[","")+"\t"+pink+i.split()[0]+reset+"\t"+"phpMyAdmin POST")
print(pink+"The above details are parsed from cpanel logs. If you find the information to be incomplete or invalid , please contact HPS "+reset)

                 