from DrissionPage import ChromiumPage, ChromiumOptions
from random import randint
from accManager import *

pwd = 'Strasburger@'+str(randint(11111, 99999))

opt = ChromiumOptions()
opt.add_extension('./hrsf_ext')
opt.set_argument('--start-maximized')
opt.auto_port()

page = ChromiumPage(opt)
sleep(5)
page.get('chrome-extension://enkaklgnonabiokamjcfdchgfjfchfmj/popup/popup.html')
sleep(5)
page.get('https://archive.org/account/signup')

page.ele('css:[name="username"]').input(getMail())
page.ele('css:[name="screenname"]').input(f'HOOC-COOH{randint(111111111, 999999999)}')
page.ele('css:[name="password"]').input(pwd)
page.ele('css:[name="submit-to-signup"]').click()

page.get(getLink())
sleep(3)
open('creds.txt', 'w').write('Email: %s\nPassword: %s' % (tm.email, pwd))
page.quit()