# Thomas Reaney
# Electronic & Computer Engineering Student
# National University of Ireland Galway

from ftplib import FTP

ftp = FTP("domainname.com")
ftp.login(user="username", passwd="password")

ftp.cwd("/specificdomain-or-location/")


def grab_file():
    filename = "file.txt"
    localfile = open(filename, "wb")
    ftp.retrbinary("RETR " + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()


def place_file():
    filename = "filename.txt"
    ftp.storbinary("STOR " + filename, open(filename, "rb"))
    ftp.quit()
