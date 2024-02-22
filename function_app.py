import azure.functions as func
import logging
# import os
# import tempfile
# import requests
#import whisper
# from urllib.parse import 
import torch
# from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="whisperai")
def whisperai(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Initialize the model and processor
    # device = "cuda:0" if torch.cuda.is_available() else "cpu"
    # torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
    # model_id = "openai/whisper-large-v3"
    # model = AutoModelForSpeechSeq2Seq.from_pretrained(
    #     model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
    # ).to(device)
    # processor = AutoProcessor.from_pretrained(model_id)
    # pipe = pipeline(
    #     "automatic-speech-recognition",
    #     model=model,
    #     tokenizer=processor.tokenizer,
    #     feature_extractor=processor.feature_extractor,
    #     max_new_tokens=128,
    #     chunk_length_s=30,
    #     batch_size=16,
    #     return_timestamps=True,
    #     torch_dtype=torch_dtype,
    #     device=device,
    # )

    name = req.params.get('name')
    # file_url = req.params.get('file')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
            # file_url = req_body.get('file')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # if file_url:
    #     model = whisper.load_model("base")
    #     result = model.transcribe(file_url)
    #     my_result = result["text"]
    #     return func.HttpResponse(f"{my_result}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )