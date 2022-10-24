import requests, base64

HEADERS = {'user-agent':'ReversoAio/1.0', 'content-type':'application/*+json'}

def correct(text, lang="eng", is_html=False):
    if lang in ['fra', "eng", "spa"]:
        resp = requests.post('https://orthographe.reverso.net/api/v1/Spelling/', headers=HEADERS, json={"englishDialect":"indifferent","autoReplace":True,"getCorrectionDetails":True,"interfaceLanguage":"fr","locale":"","language":lang,"text":text,"originalText":"","spellingFeedbackOptions":{"insertFeedback":True,"userLoggedOn":False},"origin":"interactive","isHtml":is_html}).json()
        correction = resp['text']
        return correction
    else: 
        correction = 'Language not recognize\nHere are the available languages: [fra, eng, spa (beta)]'
        return correction
        
def translate(text, lang="fra", to="eng"):
    resp = requests.post('https://api.reverso.net/translate/v1/translation', headers=HEADERS, json={"format":"text","from":lang,"to":to,"input":text,"options":{"sentenceSplitter":True,"origin":"translation.web","contextResults":True,"languageDetection":True}}).json()
    translation = resp['contextResults']['results'][0]['translation']
    return translation

def voice(text):
    b64 = base64.b64encode(text.encode("ascii")).decode("ascii")
    resp = requests.get(f'https://voice.reverso.net/RestPronunciation.svc/v1/output=json/GetVoiceStream/voiceName=Alice22k?voiceSpeed=100&inputText={b64}', headers={'user-agent':'ReversoAio/1.0', 'content-type':'audio/mpeg'})
    
    with open("output.mp3", "wb") as file:
        file.write(resp.content)

    return resp
