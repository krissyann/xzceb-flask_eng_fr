# sudo python3 -m pip install --upgrade --force pip
# pip3 install --upgrade ibm-watson
# pip3 install ibm-cloud-sdk-core
# pylint: disable=unused-import,line-too-long,bare-except,import-error,invalid-name,missing-final-newline

from deep_translator import MyMemoryTranslator

"""This is a translator module"""


def englishToFrench(englishText):
    """English to French Translation"""
    translatedText = MyMemoryTranslator(source='en-US', target='french').translate(englishText)
    return translatedText

def frenchToEnglish(frenchText):
    """French to English Translation"""
    translatedText = MyMemoryTranslator(source='fr-FR', target='en-US').translate(frenchText)
    return translatedText