import openai
import whisper
from googleapiclient import discovery
from config import OPENAI_API_KEY, PERSPECTIVE_API_KEY

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

# Load Whisper model
whisper_model = whisper.load_model("base")

def generate_text(prompt: str) -> str:
    """Generate text using OpenAI GPT."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]


def summarize_text(prompt: str) -> str:
    """Summarize input text using GPT."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful AI that summarizes content."},
            {"role": "user", "content": f"Summarize this: {prompt}"}
        ]
    )
    return response["choices"][0]["message"]["content"]

def transcribe_audio(file_path: str) -> str:
    """Transcribe audio to text using Whisper."""
    result = whisper_model.transcribe(file_path)
    return result["text"]

def moderate_text(prompt: str) -> dict:
    """Analyze text for toxicity using Perspective API."""
    client = discovery.build(
        "commentanalyzer",
        "v1alpha1",
        developerKey=PERSPECTIVE_API_KEY,
        discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
        static_discovery=False,
    )

    analyze_request = {
        "comment": {"text": prompt},
        "requestedAttributes": {"TOXICITY": {}}
    }
    response = client.comments().analyze(body=analyze_request).execute()
    score = response["attributeScores"]["TOXICITY"]["summaryScore"]["value"]

    label = "Allow" if score < 0.25 else "Flag for Review" if score < 0.60 else "Block"
    return {"toxicity_score": score, "moderation_label": label}
