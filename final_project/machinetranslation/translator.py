"""This is a translator_instance."""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

# getting the credentials from the env
load_dotenv()
apikey = os.environ.get('apikey')
url = os.environ.get('url')

# Create the authenticator.
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2019-04-03',authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(text):
    """Function translating English to French."""
    if(text == "" or not text or text is None):
        return "please enter text to be translated"
    translation = language_translator.translate(text=text,model_id='en-fr').get_result()
    return translation['translations'][0]['translation']

def french_to_english(text):
    """Function translating French to English."""
    if(text == "" or not text or text is None):
        return "please enter text to be translated"
    translation = language_translator.translate(text=text,model_id='fr-en').get_result()
    return translation['translations'][0]['translation']
