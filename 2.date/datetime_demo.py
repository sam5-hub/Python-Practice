from datetime import datetime

"""

%a Abbreviated weekday name 
%A Full weekday name 
%b Abbreviated month name 
%B Full month name 
%c Date and time representation appropriate for locale 
%d Day of month as decimal number (01 - 31) 
%H Hour in 24-hour format (00 - 23) 
%I Hour in 12-hour format (01 - 12) 
%j Day of year as decimal number (001 - 366) 
%m Month as decimal number (01 - 12) 
%M Minute as decimal number (00 - 59) 
%p Current locale's A.M./P.M. indicator for 12-hour clock 
%S Second as decimal number (00 - 59) 
%U Week of year as decimal number, with Sunday as first day of week (00 - 51) 
%w Weekday as decimal number (0 - 6; Sunday is 0) 
%W Week of year as decimal number, with Monday as first day of week (00 - 51) 
%x Date representation for current locale 
%X Time representation for current locale 
%y Year without century, as decimal number (00 - 99) 
%Y Year with century, as decimal number 
%z, %Z Time-zone name or abbreviation; no characters if time zone is unknown 
%% Percent sign

http://www.runoob.com/python/python-date-time.html

"""

# datetime转换成字符串

datetime.now().strftime('%y-%m-%d')  # '17-07-19'
datetime.now().strftime('%b-%d-%y %H:%M:%S')  # 'Jul-19-17 17:40:01'

# 这个字符串转换成datetime
datestr = datetime.strptime('Sep-21-09 16:34', '%b-%d-%y %H:%M')
