
# GPT-3 Transcript Summary


## PROJECT GOAL: Summarize long interview transcripts using GPT-3, also pull out important quotes that could be used to support findings

### PROJECT DESCRIPTION
1. WHAT IT DOES
    - This API endpoint takes in a text file of an interview transcript and answers a question about the long transcript based on a prompt

2. WHAT TECHNOLOGIES DOES THIS USE? 
    - Flask
    - gpt-index library
        - Allows for parsing of text with GPT-3 that is longer than 4096 tokens

3. CHALLENGES FACED
    - Optimizing the prompts will be key here. How much can we reduce the user input?
    - The querys on longer documents can take a long time to load. Is there any way we can speed this up? Is there any way we can show how long the query will take to load?
    - If the openAI servers are crowded, the app will run slower. We have to keep this in mind

4. FUTURE FEATURES
    - Upload docx? Upload other normal files?


### REQUIREMENTS: 

Python-3.9

Have an openai API key set as an environment variable called "OPENAI_API_KEY" (you can find this key in the dockerfile)


Read attached "requirements-prod.txt" 



### HOW TO USE : 

- Pull the code from the github repo.
- Install the requirements-prod.txt.
- To run locally, run the following command within local conda environment "GPT-Transcript": 
    - flask run