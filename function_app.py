import azure.functions as func
import logging
# import os
# import tempfile
# import requests
#import whisper
# from urllib.parse import quote

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="whisperai")
def whisperai(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

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