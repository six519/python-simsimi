GET YOUR KEY AT
--------------
http://developer.simsimi.com/signUp


HOW TO INSTALL
--------------
To install run ``pip install python_simsimi`` or ``easy_install python_simsimi``.

HOW TO USE
------------
::

from python_simsimi import SimSimi
from python_simsimi.language_codes import LC_FILIPINO
from python_simsimi.simsimi import SimSimiException

simSimi = SimSimi(
	conversation_language=LC_FILIPINO,
	conversation_key='<API KEY>'
)

try:
	response = simSimi.getConversation('Kamusta ka?')
	print response['response']
except SimSimiException as e:
	print e