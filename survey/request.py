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

class Request():

    @staticmethod
    def request_model(model_id, systemprompt, message):
        try:
            # Response Format - DeepSeek needs json_object, others use json_schema
            if model_id.startswith("deepseek/"):
                model_response_format = {"type": "json_object"}
            else:
                model_response_format = {
                    "type": "json_schema",
                    "json_schema": {
                        "name": "survey_response",
                        "schema": CompleteResponseFormat.model_json_schema()
                    }
                }

            # Build messages - system first (if not empty), then user
            messages = []
            if systemprompt and systemprompt.strip():
                messages.append({'role': 'system', 'content': systemprompt})
            messages.append({"role": "user", "content": message})

            response = completion(
                model = model_id,
                messages = messages,
                response_format=model_response_format
            )

            return response

        except Exception as e:
            print(f" ERROR: {e}")
            return None, None