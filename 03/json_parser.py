import json


def callback(arg, stat, cnt):
    try:
        stat[arg] += cnt
    except KeyError:
        stat[arg] = cnt
    return stat


def parse_json(json_str: str, required_fields=None, keywords=None, keyword_callback=callback):
    stat = {}
    json_str = json.loads(json_str)
    for field in required_fields:
        if field in json_str:
            for word in keywords:
                if word in json_str[field]:
                    cnt = json_str[field].split().count(word)
                    callback(field, stat, cnt)
    return stat


json_str_1 = '{"key1": "Word1 word2", "key2": "word2 word3"}'
required_fields_1 = ["key1"]
keywords_1 = ["word2"]
assert parse_json(json_str_1, required_fields_1, keywords_1) == {'key1': 1}

json_str_2 = '{"key1": "Word1 word2 word2 word2 word2 word2 word5 word5", '\
              '"key2": "word2 word3", '\
              '"key3": "word4 word5", '\
              '"key4": "word2 word3 word5"}'
required_fields_2 = ["key1", "key2", "key3", "key4", "key5"]
keywords_2 = ["word2", "word5"]
assert parse_json(json_str_2, required_fields_2, keywords_2) == {'key1': 7, 'key2': 1, 'key3': 1, 'key4': 2}

json_str_3 = '{"monday": "Physics Physics History Geometry ", '\
             '"tuesday": "Geometry Algebra Literature Chemistry", '\
             '"wednesday": "Physics Literature Literature", '\
             '"thursday": "History History Chemistry",'\
             '"friday": "PhEducation Geography Biolodgy Physics"}'
required_fields_3 = ["monday", "wednesday", "friday"]
keywords_3 = ["Physics", "History"]
assert parse_json(json_str_3, required_fields_3, keywords_3) == {'monday': 3, 'wednesday': 1, 'friday': 1}

json_str_4 = '{"family1": "MTS BEELINE TELE2 TELE2 ", '\
              '"family2": "BEELINE MTS TELE2", '\
              '"family3": "MTS MTS MTS"}'
required_fields_4 = ["family1", "family2", "family3"]
keywords_4 = ["MTS"]
assert parse_json(json_str_4, required_fields_4, keywords_4) == {'family1': 1, 'family2': 1, 'family3': 3}

json_str_5 = '{"words1": "stain color stainless blame ", '\
              '"words2": "point doubtless state", '\
              '"words3": "doubt fault stainless"}'
required_fields_5 = ["words1", "words2", "words3"]
keywords_5 = ["stain", "doubt"]
assert parse_json(json_str_5, required_fields_5, keywords_5) == {'words1': 1, 'words2' : 0, 'words3': 1}
