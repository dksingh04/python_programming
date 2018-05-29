import re
def newStyleFormatting(s):
    s = re.sub('%%', '^', s)
    regex = re.compile("%[bcdefgnosxXEFG]")
    s = regex.sub('{}', s)
    s = re.sub('\^', '%%', s)
    s = re.sub('%%', '%', s)

    return s
print(newStyleFormatting("ancdfef%%zyf%%%%d%%%c%%%%"))

