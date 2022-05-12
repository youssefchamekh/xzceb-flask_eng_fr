import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)


def englishToFrench(englishtext):

    language_translator.set_service_url(url)
    translation = language_translator.translate(
        text=englishtext,
        model_id='en-fr').get_result()
    translations = json.dumps(translation, indent=2, ensure_ascii=False)

    response_info = json.loads(translations)

    result = response_info.get("translations")[0]
    french_text = result.get("translation")
    return french_text


def frenchToEnglish(frenchtext):
    language_translator.set_service_url(url)
    translation = language_translator.translate(
        text=frenchtext,
        model_id='fr-en').get_result()
    translations = json.dumps(translation, indent=2, ensure_ascii=False)

    response_info = json.loads(translations)

    result = response_info.get("translations")[0]
    english_text = result.get("translation")
    return english_text
