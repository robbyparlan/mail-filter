#!/usr/bin/env python

from optparse import OptionParser
import os.path
import re

class warna():
    cetak = '\033[0m'
    ijo ='\033[1;32m'
    putih = '\033[1;37m'
    biru = '\033[1;34m'
    kuning = '\033[1;33m'
    abang = '\033[1;31m'

def author():
    print('''%s
______  ___      ___________________________________
___   |/  /_____ ___(_)__  /___  ____/__(_)__  /_  /_____________
__  /|_/ /_  __ `/_  /__  / __  /_   __  /__  /_  __/  _ \_  ___/
_  /  / / / /_/ /_  / _  /___  __/   _  / _  / / /_ /  __/  /
/_/  /_/  \__,_/ /_/  /_____/_/      /_/  /_/  \__/ \___//_/
                                                       v.01
%s
[+] Author      : Ruitze
[+] Tool        : MailFilter v.01
[+] Description : Filter mailist Gmail, Yahoo, Hotmail
[+] Usage       : python mailFilter.py nameMailist -o %s''' % (warna.ijo,warna.putih, warna.cetak))



regex = re.compile(r'''(
                   ([a-zA-Z0-9._%+-]+)
                    @
                    (gmail|yahoo|hotmail)
                    (\.com)
                    )''', re.VERBOSE)

def file_to_str(filename):
    with open(filename) as f:
        return f.read().lower()

def get_emails(s):
    return (email[0] for email in re.findall(regex, s) if not email[0].startswith('//'))

def main():
    parser = OptionParser()
    parser.add_option('-o','--output',dest='output',help='output file to saveFile.txt', action='store_true')
    (options, args) = parser.parse_args()
    try:
        if args and options.output:
            for arg in args:
                if os.path.isfile(arg):
                    for email in get_emails(file_to_str(arg)):
                        if 'gmail' in email:
                            f =open('gmailFile.txt', 'a')
                            f.write(email+'\n')
                            f.close()
                        elif 'yahoo' in email:
                            f = open('yahooFile.txt', 'a')
                            f.write(email + '\n')
                            f.close()
                        else:
                            f = open('hotmailFile.txt', 'a')
                            f.write(email + '\n')
                            f.close()
                    author()
                    print(warna.cetak)
                    print('%s[+] Succes filter to gmailFile.txt   [+]%s' % (warna.biru, warna.cetak))
                    print('%s[+] Succes filter to yahooFile.txt   [+]%s' % (warna.kuning, warna.cetak))
                    print('%s[+] Succes filter to hotmailFile.txt [+]%s' % (warna.abang, warna.cetak))
                else:
                    print('"{}" is not a file.').format(arg)

        else:
            author()
            print(warna.cetak)
    except Exception as e:
        print('Error Description', e)


if __name__=='__main__':
    main()
