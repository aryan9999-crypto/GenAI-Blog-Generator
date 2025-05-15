## Blog Generator Using GenAI 
This project provides a command-line tool (blog.py) that uses the Hugging Face Inference API to generate ~200-word, richly detailed blog paragraphs on any user-specified topic, leveraging the instruction-tuned google/flan-t5-large model for high-quality, non-repetitive text generation :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}. It loads your HF API key securely from a .env file via python-dotenv, constructs a customizable prompt, issues an HTTP POST with requests, and displays the generated text in an interactive CLI loop :contentReference[oaicite:2]{index=2}.

## Features  
- *Interactive CLI loop*: prompts for “Y”/“N” and topic input, repeating until exit :contentReference[oaicite:3]{index=3}  
- *Secure configuration*: reads HF_API_KEY from .env using python-dotenv (12-factor-app style) :contentReference[oaicite:4]{index=4}  
- *Model selection*: targets the sub-gigabyte google/flan-t5-large for cost-effective, instruction-tuned text generation :contentReference[oaicite:5]{index=5}  
- *Tunable sampling*: exposes max_length, temperature, top_p, repetition_penalty in code for easy experimentation :contentReference[oaicite:6]{index=6}  
- *Zero-dependency HTTP*: uses the industry-standard requests library to call the Inference API :contentReference[oaicite:7]{index=7}  

## Requirements  
- *Python 3.8+* (supports built-in input() and modern packaging) :contentReference[oaicite:8]{index=8}  
- *requests* (HTTP client library) :contentReference[oaicite:9]{index=9}  
- *python-dotenv* (loads .env into os.environ) :contentReference[oaicite:10]{index=10}  

## Installation  
```bash
python -m venv .venv                      # create virtual env  
source .venv/bin/activate                 # on Linux/Mac  
.venv\Scripts\activate                    # on Windows  
pip install requests python-dotenv        # install deps :contentReference[oaicite:11]{index=11} :contentReference[oaicite:12]{index=12}  
pip freeze > requirements.txt             # lock versions
