#!/bin/bash
# Written by: Soumya <soumya.t@directi.com>
# Tweaked by: Ashith.w
# Tasks performed:
# * Block all outgoing ports for a user
# * Unblock port 80,443,465,587,8080 or all outgoing ports for a user
 
 
LOGFILE="/var/log/scripts/block_unblock_outgoing_port.log"
BLOCK_USERS="/etc/fw/user_port_block.conf"
BLOCK_USERS_DIR="/opt/blocked_users"
IFACE=`/sbin/route -n | awk '/^0.0.0.0/ {print $NF}'`
LOGNAME=`logname`
ARGS=2
CHAIN="BAN_USER"
BLOCKED_PORT_LIST="465,587"
 
option=$1
user=$2
 
# Create logfile if it doesn't exist, and limit the size to 512MB
if [ ! -f $LOGFILE ]
then
        /bin/touch $LOGFILE
fi
 
LOG_SIZE=`/usr/bin/du $LOGFILE | awk '{print $1}'`
 
if [ $LOG_SIZE -gt 5120 ]
then
        rm -rf $LOGFILE
        touch $LOGFILE
fi
 
if [ ! -f $BLOCK_USERS ]
then
        /bin/touch $BLOCK_USERS
fi
 
function usage()
{
        echo -e "\nUsage: $0  <option>  <user_name>\n\nOptions:\n --block-all-ports\t\t- To block a users all outgoing ports via iptables\n --block-http-mail-ports\t- To block a users outgoing ports $BLOCKED_PORT_LIST via iptables\n --unblock-ports\t\t- To unblock a users outgoing ports from iptables\n"
        exit 1                    # Exit and explain usage.                                                                                                                                           # Usage: scriptname <option> <user_name>                                                                                
}                                                                                                                                                              
 
if [ $# -ne "$ARGS" ]
then
        usage
fi
 
 
function fwproccount()
{
        # Exit if /etc/fw/fw related processes exists.
        FW_PROC_COUNT=`ps aux | grep "/etc/fw/fw" | grep -v grep | wc -l`
 
        if [ $FW_PROC_COUNT -ne 0 ]
        then
                echo -e "\nProcesses wrt /etc/fw/fw exist.\nPlease try after some time.\nQuiting...\n"
                exit 1
        fi
}
 
function checkuser()
{
        # Exit if user isn't in server
        cut -d: -f1 /etc/domainusers | egrep -wq $user
 
        if [ $? -ne 0 ]
        then
                echo -e "\nUser "$user" isn't present in this server.\nPlease recheck user name.\nQuiting...\n"
                exit 1
        fi
}
 
function unsuccess_msg()
{
        echo -e "\nSome issue with iptables $1 rule. Please contact sysads!!!\n"
        exit 1
}
 
function success_msg()
{
        echo  "`date +%F" "%R":"%S` Successfully $1 block rule for $user by $LOGNAME" >> $LOGFILE
        echo -e "\nSuccessfully $1 the rule!!!\n"
        exit 0
}
 
function exist_msg()
{
        echo -e "\nRule $1 exist\n"
        exit 2
}
 
# Function to block all outgoing ports
function block_all_ports()
{
        rule="no"
 
        # Check if block rule exist, if no add it.
        /sbin/iptables -nL $CHAIN | grep -q "Dropped all outgoing ports for $user " && rule="yes"
 
        if [ "$rule" == "yes" ]
        then
                exist_msg already
        else
                # Add block rule
                /sbin/iptables -I $CHAIN -o $IFACE -p tcp -m owner --uid-owner $user  -j DROP -m comment --comment "Dropped all outgoing ports for $user due to pps alerts" > /dev/null 2>&1 && rule_add="yes"
                if [ "$rule_add" == "yes" ]
                then
                        # Check if user name is added in $BLOCK_USERS, if no add it
                        grep "^F $user$" $BLOCK_USERS
 
                        if [ $? -ne 0 ]
                        then
                                echo "F $user" >> $BLOCK_USERS
                        fi
                        success_msg added
                else
                        unsuccess_msg addition
                fi
        fi
}
 
# Function to block http and mail outgoing ports
function block_http_mail_ports()
{
        rule="no"
 
        # Check if block rule exist, if no add it.
        /sbin/iptables -nL $CHAIN | grep -q "Dropped outgoing ports $BLOCKED_PORT_LIST for $user " && rule="yes"
 
        if [ "$rule" == "yes" ]
        then
                exist_msg already
        else
                # Add block rule
                /sbin/iptables -I $CHAIN -o $IFACE -p tcp -m multiport --dports $BLOCKED_PORT_LIST -m owner --uid-owner $user  -j DROP -m comment --comment "Dropped outgoing ports $BLOCKED_PORT_LIST for $user due to abuse" > /dev/null 2>&1 && rule_add="yes"
                if [ "$rule_add" == "yes" ]
                then
                        # Check if user name is added in $BLOCK_USERS, if no add it
                        grep "^P $user$" $BLOCK_USERS
 
                        if [ $? -ne 0 ]
                        then
                                echo "P $user" >> $BLOCK_USERS
                                touch "$BLOCK_USERS_DIR/$user"
                        fi
                        success_msg added
                else
                        unsuccess_msg addition
                fi
        fi
}
 
# Function to unblock outgoing ports
function unblock_ports()
{
        rule="no"
 
        # Check if block rule for port 80/443 exist for user
        /sbin/iptables -nL OUTPUT | grep -q "Dropped port 80 for $user " && rule="yes"
        /sbin/iptables -nL $CHAIN | grep -q "Dropped outgoing ports $BLOCKED_PORT_LIST for $user " && rule="yes"
        /sbin/iptables -nL $CHAIN | grep -q "Dropped all outgoing ports for $user " && rule="yes"
 
        # Exit if no rule
        if [ "$rule" != "yes" ]
        then
                exist_msg dosent
        else
                remove="no"
 
                /sbin/iptables -nL $CHAIN --line-number | egrep "for $user due to" | awk '{print $1}' | sort -r | xargs -n1 -I{} /sbin/iptables -D $CHAIN {} > /dev/null && remove="yes"
                /sbin/iptables -D OUTPUT -o $IFACE -p tcp -m multiport --dports 80 -m owner --uid-owner $user  -j DROP -m comment --comment "Dropped port 80 for $user by clamscan"  > /dev/null 2>&1 && remove="yes"
                /sbin/iptables -D $CHAIN -o $IFACE -p tcp -m owner --uid-owner $user  -j DROP -m comment --comment "Dropped all outgoing ports for $user due to pps alerts" > /dev/null 2>&1 && remove="yes"
                /sbin/iptables -D $CHAIN -o $IFACE -p tcp -m multiport --dports $BLOCKED_PORT_LIST -m owner --uid-owner $user  -j DROP -m comment --comment "Dropped outgoing ports $BLOCKED_PORT_LIST for $user due to abuse"  > /dev/null 2>&1 && remove="yes"
                /sbin/iptables -D $CHAIN -o $IFACE -p tcp -m multiport --dports $BLOCKED_PORT_LIST -m owner --uid-owner $user  -j DROP -m comment --comment "Dropped outgoing ports $BLOCKED_PORT_LIST for $user due to cryptophp abuse"  > /dev/null 2>&1 && remove="yes"
 
                if [ "$remove" == "yes" ]
                then
 
                        sed -i /^F\ $user$/d $BLOCK_USERS
                        sed -i /^P\ $user$/d $BLOCK_USERS
                        rm -f "$BLOCK_USERS_DIR/$user"
                        success_msg removed
                else
                        unsuccess_msg removing
                fi
        fi
}
 
case $option in
        "--block-all-ports")
                fwproccount
                checkuser
                block_all_ports
        ;;
 
        "--block-http-mail-ports")
                fwproccount
                checkuser
                block_http_mail_ports
        ;;
 
        "--unblock-ports")
                fwproccount
                checkuser
                unblock_ports
        ;;
 
        *)
                usage
        ;;
esac