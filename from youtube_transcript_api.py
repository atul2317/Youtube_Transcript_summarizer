from youtube_transcript_api import YouTubeTranscriptApi
import gradio as gr
from gradio.mix import Series

def generate_transcript(url):
    id = url[url.index("=")+1:]
        
    transcript = YouTubeTranscriptApi.get_transcript(id)
    script = ""

    for text in transcript:
        t = text["text"]
        if t != '[Music]':
            script += t + " "
		
    return script

transcriber = gr.Interface(generate_transcript, 'text', 'text')
summarizer = gr.Interface.load("huggingface/sshleifer/distilbart-cnn-12-6")

gradio_ui = Series(transcriber, summarizer,
                  inputs = gr.inputs.Textbox(label = "Enter the YouTube URL below:"),
                  outputs = gr.outputs.Textbox(label = "Transcript Summary"),
                  title = "YouTube Transcript Summarizer",
                  theme = "peach",
                  description = "Transcripts are a simple way of creating captions.You can enter a transcript directly in your video or follow the steps below to create a transcript file.")
               
gradio_ui.launch("share=true")