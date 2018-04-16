import json
import connexion
import pycountry
from flask import request
from textblob import TextBlob

def do_check():
	data = json.loads(request.data)
	check = TextBlob(data['phrase'])
	output = pycountry.languages.get(alpha_2=check.detect_language())
	return json.dumps(output.name)
	
def do_trans():
	data = json.loads(request.data)
	targetlanguage =  pycountry.languages.get(name=data['trans_lang'])
	targetphrase = TextBlob(data['phrase'])
	translated_phrase = targetphrase.translate(to=targetlanguage.alpha_2)
	return json.dumps(str(translated_phrase))
