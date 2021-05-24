#To regenerate missing shadow file enteries: this will re-add missing shadow entries with default values.(customer need to reset the password for the missing emails) Use it only as a final resort
#warning: This will re-add missing sahdow enteries with deafult value.
import os,argparse
import subprocess
from os.path import expanduser
parser=argparse.ArgumentParser(
    description="To regenerate shadow file with a deafult value. This will only create shadow entry for missing email address with default value. so user to reset his password to use his passord"
)
parser.add_argument('user', help="cPanel user name")
args=parser.parse_args()
home=expanduser("~"+args.user)
dir=os.listdir(home+"/etc")
str=[]
pt=[]
print("\033[92m")
for i in dir:
    try:
        with open(home+"/etc/"+i+"/shadow","r") as file:
            for k in file:
                str.append(k.split(':')[0]+"@"+i)
                #print(str)
    except:
        pass
for i in os.listdir(home+"/mail"):
        if '@' in i:
         pt.append(i.split('.')[1].replace('_','.'))

#with open("test","r") as file2:
#   for kj in file2:
  #    pt.append(kj.split()[0])
      #print(pt)
print("====================")
print("Enteries in mail directory: \n")
print(pt)
print("Enteries in shadow file : \n")
print(str)
new_array=(list(set(pt)-set(str)))
if len(new_array) == 0:
    print("\033[0m")
    print("Enteries in mail directories is subset of shadow enteries : Nothing to do here")
    quit() 
print("\033[93m")
print("The shadow entry of following accounts are missing")
print("=====================")
print("\033[0m")
for i in new_array:
        print i
#print(new_array "\n")
print("\033[93m")
txt = raw_input("Do you need to proceed with restoration: (yes|no) ")
print("\033[0m")
if txt == "yes":
        print("Backing up all shadow files")
        os.chdir(home)
        subprocess.call("t=$RANDOM;for i in $(find . -iname 'shadow');do cp $i $i'_backup_'$t;done",shell=True)
        for i in new_array:
         print(i)
         r=i.split('@')[0]
         m=i.split('@')[1]
         print(r+"\n"+m)
         with open(home+"/etc/"+m+"/shadow","ab+") as file:
          file.write(r+":\$6\$roottn\$lCukmfCJGtLN.vP9WSQlpcTSNYNHKz81YAmbxW/iuZ7cZD4AYt7AjnX.FR1F/lC2SSM3P5hfQsM811Qgk85iN/:16249:::::")
          file.write("\n")
elif txt == "no":
    quit()
