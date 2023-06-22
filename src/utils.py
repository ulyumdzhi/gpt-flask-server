import json


def json_to_dict(json_data):
    dict_data = json.loads(json_data)
    return dict_data


def dict_to_json(dict_data):
    json_data = json.dumps(dict_data)
    return json_data


def json_parser(data):

    template_string = 'Вот текст задачи: {} Вот моё решение: {}. Помоги!'

    if not isinstance(data, dict):
        data = json_to_dict(data)  # из json объекта в python dict

    try:
        status = data['task_status']
        if not status:  # status == 0
            return template_string.format(data['task_text'], data['task_answer'])
        else:
            raise ValueError('Задача была решена')
    except Exception as e:
        raise e
