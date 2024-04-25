import openai
import pandas as pd
import os 
from dotenv import load_dotenv
import logging
import requests

from proxy.utils import CandidateQuestion
from proxy import config
from proxy.utils import exception
from proxy.utils import helpers

load_dotenv()

def handle_sample_question_inference(candidate_question_object: CandidateQuestion.CandidateQuestion,model_name,question_number):
    final_model_name=config.FINE_TUNED_MODEL_NAME if "louis" in model_name else model_name

    client=openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    sample_question=candidate_question_object.get_question_from_index(question_number-1)

    final_prompt=refine_prompt_for_custom_question(sample_question) if not helpers.check_if_fined_tune_model(final_model_name) else sample_question

    if "mock" in final_model_name:
        response=get_mock_model_response()
        return response

    try:
        # make api call
        completion = client.chat.completions.create(
        model=final_model_name,
        messages=[
            {"role": "system", "content": config.SYSTEM_PROMPT},
            {"role": "user", "content": final_prompt}
            ])
        
        print("Open ai response: ",completion.choices[0].message.content)

        return completion.choices[0].message.content
    except Exception as e:
        raise exception.ErrorSendingInferenceOpenAIModel(f"Error when sending inference to {model_name}, please try again")

def handle_custom_question_inference(model_name,custom_question):
    final_model_name=config.FINE_TUNED_MODEL_NAME if "louis" in model_name else model_name

    client=openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    final_prompt=refine_prompt_for_custom_question(custom_question) if not helpers.check_if_fined_tune_model(final_model_name) else custom_question

    if "mock" in final_model_name:
        response=get_mock_model_response()
        return response

    try:
        # make api call
        completion = client.chat.completions.create(
        model=final_model_name,
        messages=[
            {"role": "system", "content": config.SYSTEM_PROMPT},
            {"role": "user", "content": final_prompt}
            ])
        
        print("Open ai response: ",completion.choices[0].message.content)

        return completion.choices[0].message.content
    except Exception as e:
        raise exception.ErrorSendingInferenceOpenAIModel(f"Error when sending inference to {model_name}, please try again")


def refine_prompt_for_custom_question(custom_question):
    list_of_training_answer=helpers.retrieve_all_training_answer_from_training_data_set()

    combine_training_answer=" ".join(list_of_training_answer)

    final_prompt="base on the below information: \n" + combine_training_answer + "\n \n \n answer this question below: " + custom_question

    print(final_prompt)

    return final_prompt

def get_mock_model_response():
    url='http://localhost:5050/send_inference'

    data={"body":"tesing_mock_model"}

    try:
        response=requests.post(url,json=data)
        print("response from mock server: ",response.json())
        return response.json()['response']
    except exception as e:
        raise exception.ErrorSendingInferenceOpenAIModel("Encountered error when sending request to mock server, please send the inference again")