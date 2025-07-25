#Setup audio recorder
import logging

import os
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from groq import Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=20, phrase_time_limit=None):
  """
  Simplified function to record audio from the mic and save it as an MP3 file.

  Args:
  file_path(str) : Path to save the recording
  timeout(int) : Max time to wait for a phase to start(in sec)
  phrase_time_limit(int) : Max time for the phrase to be recorder (in sec)
  """
  
  
  
  recognizer = sr.Recognizer()
  try:
    with sr.Microphone() as source:
      logging.info("Adjusting for ambient noise...")
      recognizer.adjust_for_ambient_noise(source,duration=1)
      logging.info("Start speaking now...")

      #Record the audio
      audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
      logging.info("Recording complete.")

      #Convert the recorded audio to an MP3 file
      wav_data = audio_data.get_wav_data()
      audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
      audio_segment.export(file_path,format='mp3',bitrate='128k')

      logging.info(f"Audio save to {file_path}") 
    
  except Exception as e:
    logging.error(f"An error occured:{e}")

audio_file_path = "patient_voice_test.mp3"
# record_audio(file_path=audio_file_path)

#Setup speech to text-STT-model for transccript

def transcribe(api,audio_file_path,model):
  client = Groq(api_key=api)
  model = 'whisper-large-v3'
  with open(audio_file_path,'rb') as file:

  # audio_file = open(audio_file_path,'rb')
    transcription = client.audio.transcriptions.create(

      model=model,
      file=(audio_file_path,file.read()),
      language='en',
      response_format='verbose_json'

    )

  return transcription.text