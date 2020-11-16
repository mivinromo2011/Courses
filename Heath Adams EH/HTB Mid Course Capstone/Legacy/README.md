
HACK THE BOX MACHINE : LEGACY
IP: 10.10.10.4

#Was Blocking Ping Probes

1.RECON:

NMAP
 a) nmap -A -T4 -p- 10.10.10.4 -Pn
 b) Port open : 139,445,3389
	\__ port 139 and 445 are related to SMB
 c) Security mode of SMB:
	#message signing is disabled --> used for higher level concepts
 d) Trying to connect using SMB client:
	smbclient -L \\10.10.10.4\
 e) Trying to enumerate the SMB version using Metasploit
	auxiliary/scanner/smb/smb_version
	INFO FOUND:
		OS: Windows XP SP3
		Workgroup: HTB

