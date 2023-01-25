from google.cloud import texttospeech
import playsound
client = texttospeech.TextToSpeechClient()

voice_eng = texttospeech.VoiceSelectionParams(
language_code='en-US',
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)

voice_kor = texttospeech.VoiceSelectionParams(
    language_code='ko-KR',
    ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3)

def exchange_eng(input_text): # 영어를 음성으로 변형하기
    synthesis_input = texttospeech.SynthesisInput(text=input_text)
    response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice_eng,
    audio_config=audio_config
)
    return response.audio_content

def exchange_kor(input_text): # 한국어를 음성으로 변형하기
    synthesis_input = texttospeech.SynthesisInput(text=input_text)
    response = client.synthesize_speech(
    input=synthesis_input,
    voice=voice_kor,
    audio_config=audio_config
)
    return response.audio_content


def makeFile(textList, *adder):
    test=""
    if len(adder) == 0: adder = 'output'
    else : adder = adder[0]
    
    for i, text in enumerate(textList):
        if type(text) == type(list()):
            with open('C:/Users/ehdgn/Desktop/TTS/'+str(adder)+str(i)+'_eng.mp3', 'wb') as out:
                out.write(exchange_eng(text[0]))
                
            with open('C:/Users/ehdgn/Desktop/TTS/'+str(adder)+str(i)+'_kor.mp3', 'wb') as out:
                out.write(exchange_kor(text[1]))
                test = str(adder)+str(i)+'_kor.mp3'
        else:
            with open('C:/Users/ehdgn/Desktop/TTS/'+str(adder)+str(i)+'.mp3', 'wb') as out:
                out.write(exchange_eng(text))
    return test
             

input_text=[['abc','오늘은 TTS에 대해 공부를 해보았습니다. 쉽지않았지만 생각보다 금방 해결된 것 같아 다행이에요']]
data=makeFile(input_text, 'input_text')
playsound.playsound(data)