<!-- Logo of website -->
<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/SAP_2011_logo.svg/2560px-SAP_2011_logo.svg.png" width="450px" align="center">

</div>


<div align="center">
  
# LLM Proxy Access - Gen AI App

</div>

# Application Overview

The project concerns designing and developing the Gen AI application, capable of answering questions pertaining to candidate Louis. These questions encompass but are not limited to his educational background, academic achievements, software-related work experiences, hobbies, etc. To enhance the application's robustness, microservices architecture has been adopted, alongside leveraging the power of  fine-tuned model. The scope has been expanded to allow the application to perform as an LLM Proxy, which will route client inference requests to OpenAI Models, Fine-tuned model, as well as Mock model for testing and cost efficiency. The fine-tuned model was trained using a training dataset based on GPT-3.5-Turbo as the base model and deployed to OpenAI model hosts for seamless inference serving. In addition to handling requests, this LLM Proxy was designed to manage errors from both client and server sides, with robust exception logic handling. Therefore, this repository provides a comprehensive and practical guide on running the LLM proxy app and sending inference requests in both local and Docker virtualized environments. More importantly, it offers a detailed justification of the application architecture and best practice folder structure for modularity.

# Used Models & Performance:

<div align="center">

![model_list](https://github.com/LouisAnhTran/llm_proxy_access_gen_ai_sap/assets/110736617/f806667f-89d1-4850-8328-e2df8c23b9da)

</div>


This application uses 8 models, which are classified into 3 groups: fine-tuned models, mock models, and OpenAI base models. The fine-tuned model was trained using raw training data sets, which can be found [training data set](https://github.com/LouisAnhTran/llm_proxy_access_gen_ai_sap/blob/main/src/training_data_set.xlsx). 
In terms of speed, the fine-tuned model consumes less time to generate a response because it was trained based on the training data, thus requiring no prompt refinement. Conversely, for the OpenAI base models to generate specific responses related to candidate Louis, prompt refinement was necessary to provide relevant context. Consequently, the prompt eventually becomes much larger than the user's original prompt, causing the model to take longer to process the prompt and learn context.
To achieve the desired level of accuracy with the fine-tuned model, it's necessary to seed a substantial training dataset, ideally comprising at least 1000 rows of conversation. However, due to time constraints, only 10 instances of training conversations were introduced to the fine-tuning process. Consequently, the accuracy of the fine-tuned model's responses is significantly impacted. I am closely monitoring this situation and continuously adding more training conversations to expand the training dataset.

# Architecture Overview:

## Local development:

<div align="center">

![architecture](https://github.com/LouisAnhTran/llm_proxy_access_gen_ai_sap/assets/110736617/dca2eb67-6400-4076-af95-e9bf955ed685)

</div>

The diagram provides an overview of the LLM Proxy application architecture, making it intuitive to understand the flow of request traffic and data. The LLM Proxy receives the client request, inspects the request body to retrieve the model name, and then sends an inference request to the model of interest. While the fine-tuned model and OpenAI base models are deployed on the OpenAI model hosting platform, the mock model runs locally
## Docker virtualized environment

<div align="center">

![architecture_2 jpg](https://github.com/LouisAnhTran/llm_proxy_access_gen_ai_sap/assets/110736617/cf9b33ca-9697-409a-814f-bb6a61d5aa2e)

</div>

Before deploying the application to an AWS K8s cluster, it's necessary to containerize and dockerize the LLM Proxy application and check its functionality in a Docker virtualized environment. In this setup, as depicted in the diagram, both the Mock model and LLM Proxy are containerized. Clients can access them through the gateway at port 6000 on localhost.

# Fine-tune model implementation:



# Getting Started

## Installation 

### 1. Clone the remote repo:

Clone the project remote repo to your local machine using the following command in your terminal or command line prompt.

```
git clone https://github.com/LouisAnhTran/llm_proxy_access_gen_ai_sap.git
```

### 2. Change directory to main proxy folder 

```
cd src
```

### 3. Install required packpages

In order to run the application, we need to install the following packages:

```
openai
pandas
openpyxl
python-dotenv
requests
```

Simply run the following command to install all required packages

```
pip install -r requirements.txt
```

# Run The Application & Sending Inference Request 

## Local Development 

### Run the application:

- After installing all packages, navigate up one directory level
```
cd ../
```
- Run the proxy application in localhost port 8000
``` python
python src/app.py
```
- Open the second terminal and run the mock model server in localhost port 5050
``` python
python mock_server/main.py
```
If all steps are done correctly, at this momment you should see two servers up and running in two separate terminals as belows:

<div align="center">

![correct_2_terminals](https://github.com/LouisAnhTran/llm_proxy_access_gen_ai_sap/assets/110736617/e424504f-54ad-479c-a02b-0d051eda57ae)

</div>

### Send inference request:

There are two ways you can interact with the application: either using the Postman Graphical User Interface (GUI) or cURL requests.

#### Using cURL requests:

##### 1. Retrieve the list of all supported models:
- Set up cURL request 
```
# For windows command prompt
curl --location http://localhost:8000/get_suppored_models

# For Linux terminal
curl --location 'http://localhost:8000/get_suppored_models'
```
- You will see there are 8 models classified into 3 groups, namely fine-tune model, mock model and openai based models.
```
{
    "message": {
        "fined_tune_model": [
            "louis-gpt-3.5-fined-tune-model"
        ],
        "mock_model": [
            "mock-gpt-model-0701"
        ],
        "open_ai_models": [
            "gpt-4",
            "gpt-4-turbo",
            "gpt-4-turbo-preview",
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-16k",
            "gpt-3.5-turbo-1106"
        ]
    }
}
```

##### 2. Retrieve the list of all sample questions:

- Set up cURL request 
```
# For windows command prompt
curl --location http://localhost:8000/get_sample_questions

# For Linux terminal
curl --location 'http://localhost:8000/get_sample_questions'
```
- You will see a list of all sample questions for asking the models. You can simply select a question by its corresponding number, eliminating the need to type out the entire question
```
{
  "response": [
    "question 1: What is the candidate name?",
    "question 2: Tell me fun fact about Louis?",
    "question 3: Which university does Louis or Tran Cong Nam Anh or Nam Anh come from ?",
    "question 4: How many programming languages has Louis employed in his projects?",
    "question 5: Please provide a list of the software development projects Louis completed and detail his roles in each of these projects.",
    "question 6: What were the job responsibilities that Louis undertook during his previous internship at SAP AI Labs Singapore with the AI Workbench team?",
    "question 7: What is his current CGPA as well as his academic achievements?",
    "question 8: What sports can Louis play  ?",
    "question 9: When is his birthday ?",
    "question 10: What is his  favorite football club and his favorite football player?"
  ]
}
```

##### 3. Send inference request to selected model:

###### 3.1 Send inference request using sample question to OpenAi base models
In previous step, you can select one question from the list of questions based on its corresponding number.
For example, question 4 corresponds to question "How many programming languages has Louis employed in his projects?".
From previous step, you also know the list of supported model, so you can choose one and specify it in the request body, e.g gpt-3.5-turbo-16k.
Users can make a custom questions or use the sample question, they can explicitly specify that in body request, e.g set true in sample question's status field to use sample question and vice versa. 
  - Set up cURL request 
```
# For windows command prompt
curl --location --request POST "http://localhost:8000/send_inference" --header "Content-Type: application/json" --data "{\"model\": {\"model_name\": \"gpt-3.5-turbo-16k\"}, \"inference\": {\"sample_question\": {\"status\": true, \"selected_question\": 4}, \"custom_question\": {\"status\": false, \"your_question\": \"Tell me more about his hobbies ?\"}}}"


# For Linux terminal
curl --location 'http://localhost:8000/send_inference' \
--header 'Content-Type: application/json' \
--data '{
    "model": {
        "model_name": "gpt-3.5-turbo-16k"
    },
    "inference": {
        "sample_question": {
            "status": true,
            "selected_question": 4
        },
        "custom_question": {
            "status": false,
            "your_question": "Tell me more about his hobbies ?"
        }
    }
}
'

```
- You will see your selected model name, your prompt (selected sample question) and model's response.
```
{
    "model_name": "gpt-3.5-turbo-16k",
    "response": {
        "response": "Louis has employed five programming languages in his projects. The languages he has utilized extensively are Java, Python, Ruby, JavaScript, and C.",
        "your_question": "How many programming languages has Louis employed in his projects?"
    }
}
```

###### 3.2 Send inference request using custom question to fine-tune model
The only difference to previous step is you will use fine-tune model instead of OpenAI base models and fine-tune model name is `louis-gpt-3.5-fined-tune-model`. More importantly, in this request, we will make our own custom question, so remember to switch it on in the request body.
  - Set up cURL request 
```
# For windows command prompt
curl --location --request POST "http://localhost:8000/send_inference" --header "Content-Type: application/json" --data "{\"model\": {\"model_name\": \"louis-gpt-3.5-fined-tune-model\"}, \"inference\": {\"sample_question\": {\"status\": false, \"selected_question\": 4}, \"custom_question\": {\"status\": true, \"your_question\": \"Tell me more about his hobbies ?\"}}}"

# For Linux terminal
curl --location 'http://localhost:8000/send_inference' \
--header 'Content-Type: application/json' \
--data '{
    "model": {
        "model_name": "louis-gpt-3.5-fined-tune-model"
    },
    "inference": {
        "sample_question": {
            "status": false,
            "selected_question": 4
        },
        "custom_question": {
            "status": true,
            "your_question": "Tell me more about his hobbies ?"
        }
    }
}
'
'

```
- You will see your selected fine-tune model name, your prompt, which is ""Tell me more about his hobbies ?" in this case and model's response. Keep in mind that the fine-tune model response is not quite accurate due to the lack of training data set. I will continuously expand the training data set as well as retrain the model and hopefully at that time where you send the request, it will return a much more sensible and accurate response. 
```
{
    "model_name": "louis-gpt-3.5-fined-tune-model",
    "response": {
        "response": "Louis is passionate about cooking and exploring diverse recipes, connecting him with different cultures. He also enjoys working out at the gym, running, and hiking to stay fit and maintain a healthy lifestyle. Additionally, he has a keen interest in reading books across various genres, such as personal development, business, history, and science, aiming to unwind and gain knowledge outside of his academic and professional spheres. Additionally, he is also enthusiastic about watching movies and TV series, considering them a form of relaxation and entertainment, allowing him to unwind and recharge after a long day. In particular, he is fond of action, sci-fi, psychological, and thriller genres, where he can escape from reality and immerse himself in exciting, thought-provoking, or mysterious plotlines. \n\n\n\n\n",
        "your_question": "Tell me more about his hobbies ?"
    }
}
```

###### 3.3 Send inference request using custom question to mock model
Let examine the microservices architecture by sending inference request to mock server. Select `mock-gpt-model-0701' as model name in request body.
  - Set up cURL request 
```
# For windows command prompt
curl --location --request POST "http://localhost:8000/send_inference" --header "Content-Type: application/json" --data "{\"model\": {\"model_name\": \"mock-gpt-model-0701\"}, \"inference\": {\"sample_question\": {\"status\": true, \"selected_question\": 4}, \"custom_question\": {\"status\": false, \"your_question\": \"Tell me more about his hobbies ?\"}}}"

# For Linux terminal
curl --location 'http://localhost:8000/send_inference' \
--header 'Content-Type: application/json' \
--data '{
    "model": {
        "model_name": "mock-gpt-model-0701"
    },
    "inference": {
        "sample_question": {
            "status": true,
            "selected_question": 4
        },
        "custom_question": {
            "status": false,
            "your_question": "Tell me more about his hobbies ?"
        }
    }
}
'
```
- You will receive the response from mock model as below.
```
{
    "model_name": "mock-gpt-model-0701",
    "response": {
        "response": "Louis is computer science student from Singapore Univerversity of Technology and Design, and this is response generated from mock model",
        "your_question": "How many programming languages has Louis employed in his projects?"
    }
}
```
- Expected log from mock-model server
<div align="center">

![mock_server](https://github.com/LouisAnhTran/llm_proxy_access_gen_ai_sap/assets/110736617/3a0cf14d-d599-4c1b-90a4-3596070ef258)

</div>

# Error handling:
Many custom exception handlers have been defined to capture any errors that might occur during client-server interaction.
## Custom Exception Types:
```python
class InvalidRequestBody(Exception):
    """Custom exception class."""
    
    def __init__(self, message="An error occurred."):
        self.message = message
        super().__init__(self.message)

class InvalidModelName(Exception):
    """Custom exception class."""
    
    def __init__(self, message="An error occurred."):
        self.message = message
        super().__init__(self.message)

class InvalidModeModelSelection(Exception):
    """Custom exception class."""
    
    def __init__(self, message="An error occurred."):
        self.message = message
        super().__init__(self.message)

class NotSeeListOfQuestionYet(Exception):
    """Custom exception class."""
    
    def __init__(self, message="An error occurred."):
        self.message = message
        super().__init__(self.message)

class ErrorSendingInferenceOpenAIModel(Exception):
    """Custom exception class."""
    
    def __init__(self, message="An error occurred."):
        self.message = message
        super().__init__(self.message)

class ErrorSendingInferenceMockModel(Exception):
    """Custom exception class."""
    
    def __init__(self, message="An error occurred."):
        self.message = message
        super().__init__(self.message)
```
## Testing Error Handling:

### Invalid model name:
- Purposely set invalid model name in request body.
```
curl --location 'http://localhost:8000/send_inference' \
--header 'Content-Type: application/json' \
--data '{
    "model": {
        "model_name": "wrong_model"
    },
    "inference": {
        "sample_question": {
            "status": false,
            "selected_question": 4
        },
        "custom_question": {
            "status": true,
            "your_question": "Tell me more about his hobbies ?"
        }
    }
}
'
```
- Output: you will see error message and a list of valid model names which are supported.
```
{
    "error": "wrong_model is not supported, please choose model from the list of supported models below",
    "suppored_models": [
        "gpt-4",
        "gpt-4-turbo",
        "gpt-4-turbo-preview",
        "gpt-3.5-turbo",
        "gpt-3.5-turbo-16k",
        "gpt-3.5-turbo-1106",
        "louis-gpt-3.5-fined-tune-model",
        "mock-gpt-model-0701"
    ]
}
```
### Invalid selection of option:
- Purposely set both status data fields to true, meaning you want to use sample question and custom question at the same time, making it invalid.
```
curl --location 'http://localhost:8000/send_inference' \
--header 'Content-Type: application/json' \
--data '{
    "model": {
        "model_name": "gpt-4-turbo-preview"
    },
    "inference": {
        "sample_question": {
            "status": true,
            "selected_question": 4
        },
        "custom_question": {
            "status": true,
            "your_question": "Tell me more about his hobbies ?"
        }
    }
}
'
```
- Output: you will see error message as below
```
{
    "error": "You are only allowed to choose either make custom question or pick one from the list of sample questions"
}
```

### Set sample question number before inspecting it:
- Let say, you have re-started the proxy server and send inference request with sample question number, you should be expected to see an error because you have yet to see the list of questions.
```
curl --location 'http://localhost:8000/send_inference' \
--header 'Content-Type: application/json' \
--data '{
    "model": {
        "model_name": "gpt-4-turbo-preview"
    },
    "inference": {
        "sample_question": {
            "status": true,
            "selected_question": 4
        },
        "custom_question": {
            "status": false,
            "your_question": "Tell me more about his hobbies ?"
        }
    }
}
'
```
- Output: you will see error message.
```
{
    "error": "You have not seen the list of sample questions yet, please proceed to look at sample questions and choose one of your interest"
}
```

### Invalid sample question number:
- Set up this request with the sample question number set to 100
```
curl --location 'http://localhost:8000/send_inference' \
--header 'Content-Type: application/json' \
--data '{
    "model": {
        "model_name": "gpt-4-turbo-preview"
    },
    "inference": {
        "sample_question": {
            "status": true,
            "selected_question": 100
        },
        "custom_question": {
            "status": false,
            "your_question": "Tell me more about his hobbies ?"
        }
    }
}
'
```
- Output: you will see error message as below
```
{
    "error": "The question number 100 you entered is not valid, valid question number range from 1 to 10"
}
```


