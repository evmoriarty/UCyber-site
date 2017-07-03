import re
def sha1Parse(indicators):

   '''Takes in a text dump and extracts SHA1's then stores them in an Array of tuples.  Formatted (TYPE, CONTENT, SOURCE)'''

   SHA1_regex = r'\b([a-f0-9]{40})\b'
   SHA1s = re.findall(SHA1_regex, indicators, re.IGNORECASE | re.MULTILINE)
   hashes = []
   if len(SHA1s) == 0:
       return 'No SHA1 hashes'
   elif len(SHA1s) == 1:
       SHA1s[0] = ('SHA1', SHA1s[0], 'SOURCE?')
       return SHA1s
   else:
       for SHA1 in xrange(len(SHA1s)):
           hashes.append(('SHA1', SHA1s[SHA1], 'SOURCE?'))
   return hashes

with open('dump.txt', 'r') as myfile:
    data = myfile.read().replace('\n', '')
print sha1Parse(data)
