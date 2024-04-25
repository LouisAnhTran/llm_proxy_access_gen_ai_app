<!-- Logo of website -->
<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/SAP_2011_logo.svg/2560px-SAP_2011_logo.svg.png" width="450px" align="center">

</div>


<div align="center">
  
# LLM Proxy Access - Gen AI App

</div>

# Application Overview

The project concerns designing and developing the Gen AI application, capable of answering questions pertaining to candidate Louis. These questions encompass but are not limited to his educational background, academic achievements, software-related work experiences, hobbies, etc. To enhance the application's robustness, microservices architecture has been adopted, alongside leveraging the power of  fine-tuned model. The scope has been expanded to allow the application functioning as an LLM Proxy, which will route client inference requests to OpenAI Models, Fine-tuned model, as well as Mock model for testing and cost efficiency. The fine-tuned model was trained using a training dataset based on GPT-3.5-Turbo as the base model and deployed to OpenAI model hosts for seamless inference serving. In addition to handling requests, this LLM Proxy was designed to manage errors from both client and server sides, with robust exception logic handling. Therefore, this repository provides a comprehensive and practical guide on running the LLM proxy app and sending inference requests in both local and Docker virtualized environments. More importantly, it offers a detailed justification of the application architecture and best practice folder structure for modularity.

# Used Models & Performance:

<div align="center">

![model_list](https://github.com/LouisAnhTran/llm_proxy_access_gen_ai_sap/assets/110736617/f806667f-89d1-4850-8328-e2df8c23b9da)

</div>

# Architecture Overview:

## Local development:

<div align="center">

![architecture](https://github.com/LouisAnhTran/llm_proxy_access_gen_ai_sap/assets/110736617/dca2eb67-6400-4076-af95-e9bf955ed685)

</div>


## Docker virtualized environment:

<div align="center">

![architecture_2 jpg](https://github.com/LouisAnhTran/llm_proxy_access_gen_ai_sap/assets/110736617/cf9b33ca-9697-409a-814f-bb6a61d5aa2e)

</div>

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

# Run The Application $ Sending Inference Request 

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

#### cURL requests:

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
- You will see a list of all sample questions for the models. You can simply select a question by its corresponding number, eliminating the need to type out the entire question
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





