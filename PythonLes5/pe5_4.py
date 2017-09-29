import os.path
import datetime
from time import strftime, gmtime

if os.path.isfile('hardlopers.txt') == False:
    file = open('hardlopers.txt', 'w')
    file.close()

else:
    file = open('hardlopers.txt', 'a')
    datum = datetime.date(2016, 3, 10)
    mooiedatum = datetime.date.strftime(datum, '%a %d %b %Y')
    huidigetijd = strftime("%H:%M:%S", gmtime())
    naam = 'Martha'
    file.write(mooiedatum + ', ' + huidigetijd + ', ' + naam + '\n')
    file.close()
