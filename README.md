This repository contains a simple FastAPI app that serves a HuggingFace NER pipeline.

# [1] Install & deploy

1. After cloning this repository, install Python dependencies. For instance:
   ```
   python3 -m virtualenv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Modify settings as necessary. Check out `.env` and `nerc_api/settings.py`. Notice that the NERC model to be served must be compatible with HuggingFace's **ner** or **token-classification** pipeline.

3. Run the app with `./run.sh` (or follow the steps therein manually).

# [2] API

If the app is deployed successfully, you'll be able to access interactive API docs at `http://$HOST:$PORT/docs`.  
See also `test.http` for usage examples.  
At the moment, the API consists of a single entrypoint:

## POST /v1/nerc/extract

* **Accept**: text/plain -- the text to be tagged
* **Response**: application/json -- the detected named entity spans, type and confidence score given by the model
* **Curl example**: 
    ```shell
    curl -X 'POST' 'http://0.0.0.0:8000/v1/nerc/extract' -H 'accept: application/json' -H 'Content-Type: text/plain' -d 'Kaixo Xabier eta Joseba!'
    ```
    ```json
    [
        {
            "word": "Xabier",
            "start": 6,
            "end": 12,
            "entity_group": "PER",
            "score": 0.9952256679534912
        },
        {
            "word": "Joseba",
            "start": 17,
            "end": 23,
            "entity_group": "PER",
            "score": 0.9954593777656555
        }
    ]
    ```

# [3] TODOs

## Must
- [ ] Tests
- [ ] GPU management
- [ ] Root entrypoint for healthcheck
- [ ] Log management
- [ ] Frontend
- [ ] Dockerization

## Should
- [ ] Batch processing
- [ ] Endpoint with served model info

## Could
- [ ] Support different IO formats:
  - **Inputs**: free text or pre-tokenized text
  - **Outputs**: span-based, token-based, ...
- [ ] Dictionary lookup 
- [ ] Label whitelists/blacklists
- [ ] User data & feedback management 
