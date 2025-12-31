import sqlite3
from datetime import datetime
from survey.response import CompleteResponseFormat


def get_connection():

    connection = sqlite3.connect('../data/survey.db')
    connection.row_factory = sqlite3.Row
    return connection


class QuestionsModel():

    def __init__(self):

        self.connection = get_connection()
        cursor = self.connection.cursor()

        cursor.execute("SELECT id, text FROM questions")
        self.questions = cursor.fetchall()

    def get_questions(self):
        return self.questions


class StrategyModel():

    def __init__(self):

        self.connection = get_connection()
        self.cursor = self.connection.cursor()

        self.strategies = ''

    def load_strategies(self, strategy_prefix):
        self.cursor.execute(
            "SELECT id, system_path, message_path FROM strategies WHERE name LIKE ?",
            (strategy_prefix,)
        )
        self.strategies = self.cursor.fetchall()
    
    def get_strategies(self):
        return self.strategies

    def systemprompt_path(self, i):
        return self.strategies[i][1]

    def messageprompt_path(self, i):
        return self.strategies[i][2]


class ModelsModel():

    def __init__(self):

        self.connection = get_connection()
        self.cursor = self.connection.cursor()

        self.cursor.execute("SELECT id, model_id FROM models")
        self.models = self.cursor.fetchall()
    
    def get_models(self):
        return self.models

class ResponseModel():

    @staticmethod
    def write_respone(model_db_id, strategy_db_id, duration_time, response):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO runs (model_id, strategy_id, prompt_tokens, completion_tokens, duration_time, timestamp) VALUES (?,?,?,?,?,?)",
            (model_db_id, strategy_db_id, response.usage.prompt_tokens, response.usage.completion_tokens, duration_time, datetime.now().isoformat())
        )
        run_id = cursor.lastrowid

        # Antworten validieren
        parsed_response = CompleteResponseFormat.model_validate_json(response.choices[0].message.content)

        # Antworten speichern
        for item in parsed_response.answers:
            cursor.execute(
                "INSERT INTO responses (run_id, question_id, answer) VALUES (?,?,?)",
                (run_id, item.question, item.answer)
            )

        connection.commit()
        connection.close()
