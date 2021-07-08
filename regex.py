import re
from datetime import datetime

s = 'Jul  1 03:27:12 syslog: [m_java][ 1/Jul/2013 03:27:12.818][j:[SessionThread <]^Iat com/avc/abc/magr/service/find.something(abc/1235/locator/abc;Ljava/lang/String;)Labc/abc/abcd/abcd;(bytecode:7) '
print(re.compile(r".*\[\s?(\d+/\D+?/.*?)\]").search(s).group(1))
date_time_str = re.compile(r".*\[\s?(\d+/\D+?/.*?)\]").search(s).group(1)
date_time_obj = datetime.strptime(date_time_str, '%d/%b/%Y %H:%M:%S.%f')
print(date_time_obj)
date_time_str = '18/09/19 01:55:19'
date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
print(date_time_obj)
date_time_str2 = '20/09/19 01:55:19'
date_time_obj2 = datetime.strptime(date_time_str2, '%d/%m/%y %H:%M:%S')
print(date_time_obj>date_time_obj2)
def convert_to_datetime(s):
    return dateutil.parser.parse(s, fuzzy=True)