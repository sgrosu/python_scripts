#!/home/sgrosu/anaconda2/bin/python

import docutils.core

rest = '''
=======
Heading
=======
Subheading
----------
This is just a little sample
subsection. Now we'll show a bulleted list:

- item 1
- item 2
- item 3
'''

html = docutils.core.publish_string(source=rest,writer_name='html')
print html[html.find('<body>') + 6:html.find('</body>')]
