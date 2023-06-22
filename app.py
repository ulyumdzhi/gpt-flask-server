from flask import Flask, request, jsonify

from src.utils import dict_to_json, json_parser
from src.gpt import gpt_process


app = Flask('gpt')


@app.route('/', methods=['POST'])
def hello():
    try:
        data = request.get_data()
        return 'hello world', 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api', methods=['POST'])
def process_json():
    try:
        json_data = request.get_json()
        text = json_parser(json_data)
        response = gpt_process(text)
        response = dict_to_json(response)

        return response, 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(port=5000)
