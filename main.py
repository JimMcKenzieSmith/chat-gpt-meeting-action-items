import openai
import os
from flask import Flask, request, jsonify

openai_model = 'gpt-4'

app = Flask(__name__)


@app.route('/api/meeting-summary', methods=['POST'])
def get_meeting_summary():
    try:
        openai.api_key = os.getenv('CHATGPT_API_KEY')

        # Get the POST request's JSON data
        data = request.get_json()

        file_loc = data['file_loc']

        f = open(file_loc, "r")

        system_prompt = """You will be provided with a meeting transcript, and your task is to summarize the meeting as follows:
                            -Overall summary of discussion
                            -Action items (what needs to be done and who is doing it)
                            -If applicable, a list of topics that need to be discussed more fully in the next meeting."""

        # Get a response from Chat GPT-4
        response = get_response_from_chat_gpt(system_prompt, f.read(), 0.2)

        return response, 200

    except KeyError:
        return jsonify({'error': 'file_loc is required input in the POST request JSON data'}), 400
    
def get_response_from_chat_gpt(system_prompt, user_request, chat_temerature):
        openai_response = openai.ChatCompletion.create(
            model = openai_model,
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_request}
            ],
            # The sampling temperature can be a range between 0 and 2. Higher values like 0.8 will make the output more random, 
            # while lower values like 0.2 will make it more focused and deterministic. 
            temperature = chat_temerature
        )

        return {'response': openai_response.choices[0].message.content}

if __name__ == '__main__':
    app.run(debug=True)