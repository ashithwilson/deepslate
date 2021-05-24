import os
import errno
import pwd
import grp
import sys
import subprocess
from subprocess import Popen
def info(name):
    try:
        with open(name, "x") as file:
            file.write("""<?php
phpinfo();
?>""")
        cwd = os.getcwd()
        tt = cwd.split('/');
        user=tt[2]
        shutil.chown(path, user=user, group=user)
    except FileExistsError as tt:
        print(tt);
        pt = input("Enter a new name")
        if "php" not in pt:
            pt=pt+".php";
        info(pt)
def info_old(name):
    if os.path.isfile(name):
        pt = raw_input("Enter a new name : ")
        if "php" not in pt:
             pt=pt+".php";
        info_old(pt)

    else:

        with open(name, "w") as file:
            file.write("""<?php
phpinfo();
?>""")
        cwd = os.getcwd()
        tt = cwd.split('/');
        user=tt[2]
        uid = pwd.getpwnam(user).pw_uid
        gid = grp.getgrnam(user).gr_gid
        os.chown(cwd+"/"+name, uid, gid)
        output=Popen(['bash', '-c', '. <(curl -ks wget -q https://gitlab.com/deepslate/MyBash/raw/master/bash_alias  && source bash_alias); cul'],stdout=subprocess.PIPE)
        print output.stdout.read().strip()+name
        
        

def mailNOAuth_old(name):
    if os.path.isfile(name):
        pt = raw_input("Enter a new name : ")
        if "php" not in pt:
                pt=pt+".php";
        mailNOAuth_old(pt)
    else:
        frmo=raw_input("Enter the From address : ")
        to=raw_input("Enter the TO address : (Leave blank to use default one : mailhostingserver@gmail.com) ")
        if to == "":
            to="mailhostingserver@gmail.com"
        with open(name, "w") as file:
            file.write("""<?php
ini_set( 'display_errors', 1 );
error_reporting( E_ALL );
$from = "%s";
$to = "%s";
$subject = "PHP Mail Test script";
$message = "This is a test to check the PHP Mail functionality";
$headers = "From:" . $from;
mail($to,$subject,$message, $headers);
echo "Test email sent";
?>""" %(frmo,to))
        cwd = os.getcwd()
        tt = cwd.split('/');
        user=tt[2]
        uid = pwd.getpwnam(user).pw_uid
        gid = grp.getgrnam(user).gr_gid
        os.chown(cwd+"/"+name, uid, gid)
        output=Popen(['bash', '-c', '. <(curl -ks wget -q https://gitlab.com/deepslate/MyBash/raw/master/bash_alias  && source bash_alias); cul'],stdout=subprocess.PIPE)
        print output.stdout.read().strip()+name



def mailNOAuth(name):
    frmo=input("Enter the From address : ")
    to=input("Enter the TO address : (Leave blank to use default one : mailhostingserver@gmail.com) ")
    if to == "":
        to="mailhostingserver@gmail.com"
    try:
        with open(name, "x") as file:
            file.write("""<?php
ini_set( 'display_errors', 1 );
error_reporting( E_ALL );
$from = "%s";
$to = "%s";
$subject = "PHP Mail Test script";
$message = "This is a test to check the PHP Mail functionality";
$headers = "From:" . $from;
mail($to,$subject,$message, $headers);
echo "Test email sent";
?>""" %(frmo,to))
        cwd = os.getcwd()
        tt = cwd.split('/');
        user=tt[2]
        shutil.chown(path, user=user, group=user)
    except FileExistsError as tt:
        print(tt);
        pt = input("Enter a new name")
        if "php" not in pt:
            pt = pt + ".php";
        mailNOAuth(pt)

def mailAUTh(name):
    frmo = input("Enter the From address : ")
    to = input("Enter the TO address : (Leave blank to use default one : mailhostingserver@gmail.com) ")
    hostnam=os.uname()[1];
    hosty=input("Enter the hostname : (Leave blank to use server hostname : " +hostnam)
    passy=input("Enter the Password : ")
    if hosty == "" :
        hosty=hostnam;
    if to == "":
        to = "mailhostingserver@gmail.com"
    try:
        with open(name, "x") as file:
            file.write("""<?php
require_once "Mail.php";
$from = "%s";
$to = "%s";
$subject = " Test email to check SMTP mailer functionality ";
$body = " Just testing ";
$host = "%s";
$username = "%s";
$password = "%s";
$headers = array ('From' => $from,
'To' => $to,
'Subject' => $subject);
$smtp = Mail::factory('smtp',
array ('host' => $host,
'auth' => true,
'username' => $username,
'password' => $password));
$mail = $smtp->send($to, $headers, $body);
if (PEAR::isError($mail)) {
echo("<p>" . $mail->getMessage() . "</p>");
} else {
echo("<p>Message successfully sent!</p>");
}
?> """ % (frmo, to,hosty,frmo,passy))
        cwd = os.getcwd()
        tt = cwd.split('/');
        user=tt[2]
        shutil.chown(path, user=user, group=user)
    except FileExistsError as tt:
        print(tt);
        pt = input("Enter a new name")
        if "php" not in pt:
            pt = pt + ".php";
        mailNOAuth(pt)

def mailAUTh_old(name):
    if os.path.isfile(name):
                pt = raw_input("Enter a new name : ")
                if "php" not in pt:
                        pt=pt+".php";
                mailAuth_old(pt)
    else:
        frmo = raw_input("Enter the From address : ")
        to = raw_input("Enter the TO address : (Leave blank to use default one : mailhostingserver@gmail.com) ")
        hostnam=os.uname()[1];
        hosty=raw_input("Enter the hostname : (Leave blank to use server hostname : " +hostnam)
        passy=raw_input("Enter the Password : ")
        if hosty == "" :
            hosty=hostnam;
        if to == "":
            to = "mailhostingserver@gmail.com"
        with open(name, "w") as file:
            file.write("""<?php
require_once "Mail.php";
$from = "%s";
$to = "%s";
$subject = " Test email to check SMTP mailer functionality ";
$body = " Just testing ";
$host = "%s";
$username = "%s";
$password = "%s";
$headers = array ('From' => $from,
'To' => $to,
'Subject' => $subject);
$smtp = Mail::factory('smtp',
array ('host' => $host,
'auth' => true,
'username' => $username,
'password' => $password));
$mail = $smtp->send($to, $headers, $body);
if (PEAR::isError($mail)) {
echo("<p>" . $mail->getMessage() . "</p>");
} else {
echo("<p>Message successfully sent!</p>");
}
?> """ % (frmo, to,hosty,frmo,passy))
        cwd = os.getcwd()
        tt = cwd.split('/');
        user=tt[2]
        uid = pwd.getpwnam(user).pw_uid
        gid = grp.getgrnam(user).gr_gid
        os.chown(cwd+"/"+name, uid, gid)
        output=Popen(['bash', '-c', '. <(curl -ks wget -q https://gitlab.com/deepslate/MyBash/raw/master/bash_alias  && source bash_alias); cul'],stdout=subprocess.PIPE)
        print output.stdout.read().strip()+name

        
def sample_PHPINI(name):
    if os.path.isfile(name):
        print("php.in is already present renaming currecnt one to php.ini_backup")
        os.rename("php.ini","php.ini_backup")
        sample_PHPINI(name)
    else:
        with open(name, "w") as file:
            file.write("""magic_quotes_gpc = Off
register_globals = Off
default_charset = UTF-8
memory_limit = 64M
max_execution_time = 36000
upload_max_filesize = 999M
safe_mode = Off
mysql.connect_timeout = 20
session.auto_start = Off
session.use_only_cookies = On
session.use_cookies = On
session.use_trans_sid = Off
session.cookie_httponly = On
session.gc_maxlifetime = 3600
allow_url_fopen = On
;display_errors = 1
;error_reporting = E_ALL""")
        cwd = os.getcwd()
        tt = cwd.split('/');
        user=tt[2]
        uid = pwd.getpwnam(user).pw_uid
        gid = grp.getgrnam(user).gr_gid
        os.chown(cwd+"/"+name, uid, gid)

cwd=os.getcwd()
if 'home' in cwd and len(os.getcwd().split('/'))>2:

        print("\033[1;32;40m1: Info.php")
        print("2: Mail Script without AUTH")
        print("3: Mail script with AUTH")
        print("4: Sample php.ini file \x1b[0m")
        ch = int(input("\033[94m Enter Your choice: \x1b[0m"))

        if  ch == 1:
                if sys.version_info[0] < 3:
                        info_old("info.php")
                else:
                        info("info.php")
        elif ch == 2:
                if sys.version_info[0] < 3:
                        mailNOAuth_old("mailtesting.php")
                else:
                        mailNOAuth("mailtesting.php")

        elif ch == 3:
                if sys.version_info[0] < 3:
                        mailAUTh_old("mailTestingAuth.php")
                else:
                        mailAUTh("mailTestingAuth.php")
        elif ch == 4:
            if sys.version_info[0] < 3:
                        sample_PHPINI("php.ini")
        else:
                print("Invalid choice! Try 1 , 2 or 3")
else:
        print("Not a user directory. Run this under a user directory")
