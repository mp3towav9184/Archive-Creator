from DrissionPage import ChromiumPage, ChromiumOptions
from random import randint
from accManager import *

pwd = 'Strasburger@'+str(randint(11111, 99999))

opt = ChromiumOptions()
opt.add_extension('./bcs_ext')
opt.set_argument('--start-maximized')
opt.auto_port()

page = ChromiumPage(opt)
page.get('https://archive.org/account/signup')

page.ele('css:[name="username"]').input(getMail())
page.ele('css:[name="screenname"]').input(f'HOOC-COOH-{randint(111111111, 999999999)}')
page.ele('css:[name="password"]').input(pwd)
page.ele('css:[name="submit-to-signup"]').click()

iframe = page.get_frame(page.ele('css:iframe[title="recaptcha challenge expires in two minutes"]'))
sr = iframe.ele('css:.help-button-holder').shadow_root
sb = sr.ele('css:#solver-button')
sb.click()

page.get(getLink())
sleep(3)
open('creds.txt', 'w').write('Email:\n%s\nPassword:\n%s\n' % (tm.email, pwd))
page.quit()