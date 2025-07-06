#TTS(gTTS & Elevenlabs)
import os
import elevenlabs
from elevenlabs.client import ElevenLabs
import subprocess
import platform
ELVENLABS_API_KEY=os.getenv("ELEVENLABS_API_KEY")



def tts(text,output_path):
   client = ElevenLabs(api_key=ELVENLABS_API_KEY)
   audio = client.text_to_speech.convert(
      text = text,
      voice_id= "UgBBYS2sOqTuMpoF3BR0",
      output_format = "mp3_22050_32",
      model_id = "eleven_turbo_v2"
   )
   elevenlabs.save(audio, output_path)
   os_name = platform.system()
   try:
      if os_name == "Darwin":
         subprocess.run(['afplay',output_path])
      elif os_name == "Windows":
         subprocess.run(['ffplay', '-nodisp', '-autoexit', output_path])
      if os_name == "Linux":
         subprocess.run(['aplay',output_path])
      else:
         raise OSError("OS Not supported")

   except Exception as e:
      print(f"An error occured while trying to play the audio: {e}")

# tts("Hi, this is Muhammad Adnan.","elvenlabs_test_autoplay.mp3")

#Use model for TTVoice