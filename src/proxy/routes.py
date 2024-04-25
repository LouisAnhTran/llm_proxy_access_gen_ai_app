from flask import request, jsonify, make_response
import requests

from proxy.utils import helpers
from proxy.utils import CandidateQuestion
from proxy.utils import exception
from proxy import config
from proxy.utils import handle_openai_api_call

def get_list_supported_models():
    dict_model=helpers.retrieve_list_of_supported_model()
    return jsonify({"message":dict_model})

def get_sample_questions_handler(candidate_question_instance: CandidateQuestion.CandidateQuestion):
    list_of_question=helpers.retrieve_all_question_from_training_data_set()
    candidate_question_instance.question_list=list_of_question
    return jsonify({"response":helpers.convert_questions_to_response(list_of_question)})

def send_inference_handler(candidate_question_instance: CandidateQuestion.CandidateQuestion):
    data=request.get_json()
    try:
        # check model name
        model_name=data['model']['model_name']
        helpers.check_if_model_supported(model_name)

        # check inference mode selection
        inference_body=data['inference']
        is_sample_question=inference_body['sample_question']['status']
        is_custom_question=inference_body['custom_question']['status']
        helpers.check_if_inference_mode_valid(is_sample_question,is_custom_question)

        if is_sample_question:
            # check if user has seen the list of sample questions or not
            helpers.check_if_user_see_list_of_sample_question(candidate_question_instance)

            # check valid sample question number
            question_number=(data['inference']['sample_question']['selected_question'])
            helpers.check_if_sample_question_number_valid(question_number,candidate_question_instance)


        # handle sample question
        if is_sample_question:
            model_response=handle_openai_api_call.handle_sample_question_inference(candidate_question_object=candidate_question_instance,model_name=model_name,question_number=question_number)

            question_response={"your_question":candidate_question_instance.get_question_from_index(question_number-1),"response":model_response}

            final_response={"model_name":model_name,"response":question_response}
            return jsonify(final_response)
        
        # handle custom question
        custom_question=data['inference']['custom_question']['your_question']

        model_response=handle_openai_api_call.handle_custom_question_inference(model_name,custom_question)

        question_response={"your_question":custom_question,"response":model_response}

        final_response={"model_name":model_name,"response":question_response}
        return jsonify(final_response)

    except exception.InvalidRequestBody as e:
        return make_response(jsonify({
            'error': e.message
        }),404)
    except exception.InvalidModelName as e:
         return make_response(jsonify({
            'error': e.message,
        'suppored_models':config.LIST_OF_SUPPORTED_MODELS}),404)
    except exception.InvalidModeModelSelection as e:
         return make_response(jsonify({
            'error': e.message
        }),404)
    except exception.NotSeeListOfQuestionYet as e:
         return make_response(jsonify({
            'error': e.message
        }),404)
    except exception.ErrorSendingInferenceOpenAIModel as e:
          return make_response(jsonify({
            'error': e.message
        }),500)
    except Exception as e:
        return make_response(jsonify({
            'error':'An errored occured'
        }),500)
