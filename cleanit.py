# For initial scraping, I used wget:
# wget --mirror --page-requisites --adjust-extension --no-parent --convert-links --directory-prefix=rubioissues https://marcorubio.com/issues/ 

# Then I ran this script once for each candidate
# to account for different website structures

import os
import re

mastertext = ""
for root, dirs, files in os.walk(os.getcwd(), topdown=False):
    for name in files:
	text = open(os.path.join(root, name)).read()
	#For most sites, just grab the paragraph tags
	newtext = re.findall('<p.*?>(.+?)</p>',text)
	#Then remove headers/footers
	newtext = newtext[1:(len(newtext)-4)]
	combtext = ' '.join(newtext)
	#Used differently for different sites, based on a stackoverflow forum
	combtext = combtext.decode('utf-8')
	combtext = combtext.encode('ascii', 'ignore').decode('ascii')
	mastertext = mastertext + combtext

text_file = open("all.txt", "w")
text_file.write("%s" % mastertext)
text_file.close()
