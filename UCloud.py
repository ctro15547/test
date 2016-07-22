import re
import urllib2

content = urllib2.urlopen('http://106.75.28.160/UCloud.txt').read()

uc=re.findall(r'U\w+p',content)

print 'UCloud:',len(uc)
