import openai
import pandas as pd
import os
from dotenv import load_dotenv

from proxy import config
from proxy.utils import exception
from proxy.utils import CandidateQuestion

load_dotenv()

def check_if_model_supported(model_name):
    if model_name not in config.LIST_OF_SUPPORTED_MODELS:
        raise exception.InvalidModelName(f"{model_name} is not supported, please choose model from the list of supported models below")

def check_if_user_see_list_of_sample_question(candidate_object: CandidateQuestion):
    if candidate_object.is_empty_list:
        raise exception.NotSeeListOfQuestionYet("You have not seen the list of sample questions yet, please proceed to look at sample questions and choose one of your interest")

def check_if_sample_question_number_valid(question_number,candidate_question: CandidateQuestion.CandidateQuestion):
    if question_number-1 not in list(range(candidate_question.get_number_of_question())):
        raise exception.InvalidRequestBody(f"The question number {question_number} you entered is not valid, valid question number range from 1 to {candidate_question.get_number_of_question()}")

def check_if_inference_mode_valid(is_sample_question,is_custom_question):
    print("sample: ",is_sample_question)
    print("custom: ",is_custom_question)
    if is_sample_question==is_custom_question:
        raise exception.InvalidModeModelSelection("You are only allowed to choose either make custom question or pick one from the list of sample questions")

def retrieve_list_of_supported_model():
    models={"open_ai_models":[],"fined_tune_model":[],"mock_model":[]}
    for model in config.LIST_OF_SUPPORTED_MODELS:
        models["fined_tune_model" if "louis" in model else "mock_model" if "mock" in model else "open_ai_models"].append(model)
    return models

def retrieve_all_question_from_training_data_set():
    df=pd.read_excel(f'src/training_data_set.xlsx')
    return [row['Prompt'].strip() for idx,row in df.iterrows()]

def convert_questions_to_response(array_of_questions):
    return [f'question {idx+1}: {qns}' for idx,qns in enumerate(array_of_questions)]

def retrieve_all_training_answer_from_training_data_set():
    df=pd.read_excel(f'src/training_data_set.xlsx')
    return [row['Response'].strip()+"\n" for idx,row in df.iterrows()]

def check_if_fined_tune_model(model_name):
    return model_name==config.FINE_TUNED_MODEL_NAME