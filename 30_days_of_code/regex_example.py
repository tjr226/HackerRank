import re

def hackerrankInString(s):
    p = re.compile('.*h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*')
    m = p.match(s)
    
    if m:
        return "YES"
    else:
        return "NO"




import string

alphabet = string.ascii_lowercase
def panagramTest(s):
    inputString = s.lower()
       
    
    if set(inputString) > alphabet:
        return "panagram"
    else:
        return "not panagram"
        

# ANOTHER EXAMPLE THAT WORKED: 
p = re.compile('.*\@gmail\.com$')