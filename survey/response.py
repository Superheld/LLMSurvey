import time
from dotenv import load_dotenv
from litellm import completion
from pydantic import BaseModel, Field 

load_dotenv()

class SingleResponseFormat(BaseModel):

    question: int
    answer: int = Field(
        ge=1, 
        le=4,
        description="Answer on 4-point scale: 1=strongly disagree, 2=somewhat disagree, 3=somewhat agree, 4=strongly agree"
    )

class CompleteResponseFormat(BaseModel):

    answers: list[SingleResponseFormat] = Field(
        min_length=29,
        max_length=29,
        description="Answers for all 29 questions in order"
    )

class Requests():

    @staticmethod
    def request_model(model_id, systemprompt, message):
        try:
            # Response Format Exception
            if model_id.startswith("deepseek/"):
                import json
                content = message + "Bitte antworte in diesem JSON Format:" + json.dumps(
                    CompleteResponseFormat.model_json_schema(),
                    indent=2
                )
                model_response_format = {"type": "json_object"}
            else:
                content = message
                model_response_format = {
                    "type": "json_schema",
                    "json_schema": {
                        "name": "survey_response",
                        "schema": CompleteResponseFormat.model_json_schema()
                    }
                }

            # Befragung
            start_time = time.time()
            response = completion(
                model = model_id,
                messages = [
                    {"role": "user", "content": content}
                ],
                response_format=model_response_format
            )
            duration_time = time.time() - start_time

            return response, duration_time

        except Exception as e:
            print(f" ERROR: {e}")