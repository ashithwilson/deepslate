#!/bin/bash

print_details()
{
  echo "
  ====
  Domain : $domain
  IP     : $ip
  PTR    : $rdns
  ====
  ";
}


do_telnet_check()
{
  telnet $1 25
}


process_plesk_details()

{
  windash=`echo $rdns | sed "s|.dummyhostname.net|.internal.dummyhostname.net/windash|g"`
  db="sdh"
  server_type=`echo $rdns | awk -F ".dummyhostname.net" '{print $1}'`
  is_bh=`echo $server_type | grep bh | wc -l `
  if [ $is_bh = "1" ]
  then
        db="rh"
  fi

  is_mdh=`echo $server_type | grep md | wc -l `
  if [ $is_mdh = "1" ]
  then
        db="mdh"
  fi

  echo "Windash: http://$windash"; echo ""
  echo "Generating Plesk link for $db package..."
  su -c "ssh -tqo StrictHostKeyChecking=no 10.86.210.2 \"python2.6 /usr/local/getSSOUrl-supportadmin servername=$rdns ip=115.110.71.146 type=$db\"" techsupp
}


process_cpanel_details()
{

echo $rdns
#commenting out as user access is revoked and access is via Eigsh

#  echo "
#  ssh $rdns
#  "
#  /home/ashith.w/ssh.sh $rdns

}



process_if_url()
{
 url=`echo $domain | egrep -i "http:|https:" | wc -l`

 if [ $url == 1 ]
 then
   domain=`echo $domain| sed "s,/$,,"`
   domain=`echo $domain | sed "s|^http://||" `
   domain=`echo $domain | sed "s|^https://||" `
 fi
}



process_input()
{
   if [ -z "$domain" ]
    then
    read -p "Domain: " domain;
  fi
  process_if_url
}


check_if_plesk()
{
  plesk=`echo $rdns | egrep -i "plesk|-pp-" | wc -l`
}






domain=$1;
process_input;

ip=`dig +short $domain| tail -1`;
rdns=`dig -x $ip +short | tail -1|sed "s|\.$||"`;
our_rdns=`echo $rdns | grep -i dummyhostname.net | wc -l`;

if [ $our_rdns == "0" ]
then
  print_details
  do_telnet_check $ip
else
  print_details

  check_if_plesk
  if [[ $plesk == 1 ]]
  then
    process_plesk_details
  else
    process_cpanel_details
  fi
fi
