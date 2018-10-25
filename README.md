# Bulk Hashcat for Windows x64

Bulk hashcat is the Windows adaption of my mass-password cracker that runs Hashcat on Linux.

Bulk hashcat is easy to configure, and requires Python 2.7.15 installed. <a href="https://www.python.org/downloads/windows/">https://www.python.org/downloads/windows/</a>

![](https://raw.githubusercontent.com/tanc7/BulkHashcat-Windows-x64-/master/bulkhashcatpsh.png)

 After that, simply edit the script and change the following parameters

hashdir = "Your $PATH to your hccapx files"

hashlist = "A wordlist of hashes to crack"

pwwordlist = "Your password dictionary you will run a straight-attack on"

hcbinary = "$PATH to your Hashcat binary", get your copy at <a href="https://hashcat.net/hashcat/">https://hashcat.net/hashcat/</a>

pwAttackConfig = "STRAIGHT", which is a straight dictionary attack against your hccapx. Alternatives include ruleset mode and prince processor

To run it, simply open a (preferably) Powershell prompt and then "C:\Python27\python.exe bulkhashcat.py"

# Installation

Simply git clone this repo and edit the bulkhashcat.py file with a IDE such as atom.io or VSCode.

# So why the shift from Linux to Windows?

The reasons are many...

1. Poor or inconsistent video card driver support for NVidia video cards
2. Recent negative experiences with hardware installations of Ubuntu and Kali Linux (albeit they both can be used as a desktop OS)
3. Broken driver updates being pushed through the APT repo
4. Numerous hardware incompatibilities and regressions within Linux itself, particularly internal wireless cards

Windows has it's own fair share of problems, and I absolutely dread restarting my laptop after a big Windows Update fearing a endless black screen, but when it comes to hardware support for NVidia graphics cards, you will not see much of a issue.

# Converting .cap files from Aircrack-ng to .hccapx

You require the hashcat utilities package, specifically cap2hccapx.exe: <a href="https://github.com/hashcat/hashcat-utils/releases/">https://github.com/hashcat/hashcat-utils/releases/</a>