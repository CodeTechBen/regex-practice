import re

print(re.findall(r"([a-z]+@[a-z]+(:?[0-9]+)?\.(:?com|org))","Contact us at support@example.com or sales@shop123.org for help."))