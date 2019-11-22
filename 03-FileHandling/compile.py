import re
a_text = '1234/5678'
re_expression = re.compile('(\d+)/(\d+)')
re_result = re.match(re_expression,a_text)
re_result.groups()