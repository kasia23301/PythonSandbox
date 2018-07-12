from datetime import datetime

if __name__ == "__main__":
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55,
            57,
            59]
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("Ta minuta wydaje się dość nieparzysta.")
    else:
        print("Minuta parzysta.")

import sys
import os
import datetime
import time
import html

if __name__ == "__main__":
    print(sys.platform)
    print(sys.version)
    print(os.getcwd())
    print(os.environ)
    print(os.getenv('HOME'))
    print(datetime.date.today())
    print(datetime.date.isoformat(datetime.date.today()))
    print(time.strftime("%H:%M"))
    print(time.strftime("%A %p"))
    print(html.escape("Ten fragment dokumentu HTML zawiera znacznik <script>skryptu</script>."))
    print(html.unescape("Kocham &lt;bibliotekę standardową&gt; Pythona."))