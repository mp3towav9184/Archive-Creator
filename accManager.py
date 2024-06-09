from pytempmail import TempMail
from time import sleep
import re

tm = TempMail()

def getMail(): return tm.email

def getLink():
    a = 0
    while a<36:
        for mail in tm.get_mails():
            if mail.from_name == 'Internet Archive' and mail.subject.__contains__('verify'):
                # open('mail.html', 'w').write(mail.html)
                m = re.findall(r'<p>http(?:s?)://.*</p>', mail.html)
                if not m: raise Exception('Link not matched.')
                link = m[0].split('</p>')[0].replace('<p>', '')
                return link
        sleep(5)
        a+=1
    raise Exception('Mail not received.')



