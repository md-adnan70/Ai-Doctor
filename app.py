from doctor import encode_img, analyze_img
from patient_voice import record_audio, transcribe
from doctor_voice import tts

import os
import gradio as gr
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""



def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe( api= os.getenv(GROQ_API_KEY) ,
                                                 audio_file_path=audio_filepath,
                                                 model="whisper-large-v3")

    # Handle the image input
    if image_filepath:
        doctor_response = analyze_img(query=system_prompt+speech_to_text_output, encoded_img=encode_img(image_filepath), model="meta-llama/llama-4-scout-17b-16e-instruct") #model="meta-llama/llama-4-maverick-17b-128e-instruct") 
    else:
        doctor_response = "No image provided for me to analyze"

    voice_of_doctor = tts(text=doctor_response, output_path="final.mp3") 

    return speech_to_text_output, doctor_response, voice_of_doctor

#Create the inteface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio("Temp.mp3")
    ],
    title="AI Doctor with Vision and Voice"
)

iface.launch(debug=True, server_name="0.0.0.0",server_port=7860)
