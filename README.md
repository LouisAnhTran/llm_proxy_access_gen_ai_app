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

