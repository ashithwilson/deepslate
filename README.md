# Deepslate <sub><sup>| Simple one-liners for webhosting tasks</sup></sub>

To simplify some of the common web hosting tasks.

## Usage

`wget -q https://github.com/ashith/deepslate/raw/master/bash_alias && source bash_alias`

## Help

```console
deepslate --help | ds

	Displays help menu for the commands suppoerted in deepslate repository.
	Read more: https://github.com/ashith/deepslate/

sd <domain>

	Switches the current working directory to the document root of given domain. 
	Does initial checks as follows.

	- If DNS IP is same as cPanel IP address.
	- Check quota.
	- Check server's Disk and inode.
	- Check iptables block.
	
gcar <username>

	Creates a comprehensive report from cPanel access log including the 
	Filemanager access, DB creation, Email adition, etc.
	
unblock_ports <username>
	
	Unblocks the ports blocked by the Port Block plugin in cPanel.
	
exim_parser <domain or Email address>
    
    Print exim logs in more readable way (Just from,to,subject and status)
    
    -l 
        Can pass more values to grep (seperated by coma 
        eg : exim_parser domain.com -l firstgrep, second grep)
		
ssl <domain name | username>

	Enables free SSL for the domain.
	
wml <email address or domain>

    To generate webmail logins if Email address passed 
    and list all email address if doman is passed.
	
cpl <domain name> | cpapi <domain name>

	Creates a cPanel login session.
	
cspam

	Generate SPAM report from a exim mail server.
	
cul

	Displays URL of the website from the current working directory.
	
inode

	Sorts directories with inode usage.
	
cb <file name>

	Uploads the file to our backup server and provides the downloadble link.
	
cphp 

    Create common test PHP files such as phpinfo page mailtesting etc.
		
wp

	Checks Wordpress version and database connectivity when executed 
	from directory with Wordpress install.
	
wp_user 

	Creates a Wordpress admin login using wpcli. If wpcli is not installed, 
	downloads the file and use the file temporarily for login.

	--delete

		Deletes the created Wordpress admin login
		
wp_theme [<theme name>]

	To list/change the Wordpress theme
```

## Contributors
A big thank you to the following contributors who have helped add features and/or fixes:

* Muhammed KV 
* Hari PN

## License

```
The MIT License (MIT)

Copyright (c) 2018 Rocky Madden (https://rockymadden.com/)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
