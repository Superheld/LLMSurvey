import sqlite3
from datetime import datetime
from survey.request import CompleteResponseFormat, SingleResponseFormat


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
            "SELECT id, name, system_path, message_path FROM strategies WHERE name LIKE ?",
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
    def write_respone(run_id, question_id, response, type):

        with get_connection() as connection:

            # DEBUG - Was kommt zurück?
            # print(response)

            cursor = connection.cursor()
            
        
            # Antworten je nach typ validieren
            if type == 'COMPLETE':

                parsed_response = CompleteResponseFormat.model_validate_json(response.choices[0].message.content)

                # Antworten speichern
                for item in parsed_response.answers:
                    cursor.execute(
                        "INSERT INTO responses (run_id, question_id, answer) VALUES (?,?,?)",
                        (run_id, item.question, item.answer)
                    )

            elif type == 'SINGLE':
                parsed_response = SingleResponseFormat.model_validate_json(response.choices[0].message.content)

                # Antworten speichern
                cursor.execute(
                    "INSERT INTO responses (run_id, question_id, answer) VALUES (?,?,?)",
                    (run_id, question_id, parsed_response.answer)
                )
            
            connection.commit()


class RunModel():
    
    @staticmethod
    def write_run(model_db_id, strategy_db_id):

        with get_connection() as connection:

            cursor = connection.cursor()

            # Run speichern
            cursor.execute(
                "INSERT INTO runs (model_id, strategy_id, timestamp) VALUES (?,?,?)",
                (model_db_id, strategy_db_id, datetime.now().isoformat())
            )

            run_id = cursor.lastrowid
            connection.commit()

            return run_id
    
    @staticmethod
    def update_run(prompt_tokens, completion_tokens, duration_time, run_id):

        with get_connection() as connection:

            cursor = connection.cursor()

            # Run speichern
            cursor.execute(
                "UPDATE runs SET prompt_tokens=?, completion_tokens=?, duration_time=? WHERE id=?",
                (prompt_tokens, completion_tokens, duration_time, run_id)
            )

            connection.commit()
