from pydantic import BaseModel, Field 


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
