import json 
model_config = {
    "model": "GPT",
    "temperature": 0.7,
    "enabled": True
}
print(model_config)
print(type(model_config))
json_text = json.dumps(model_config) 
print(json_text)
print(type(json_text))
parsed_config = json.loads(json_text)
print(parsed_config)
print(type(parsed_config))
print(parsed_config["model"])
bad_json = '{"model": "GPT", "enabled": true}'
parsed_bad_json = json.loads(bad_json) 
print(parsed_bad_json)
print(type(parsed_bad_json))
with open("model_config.json", "w") as file:
    json.dump(model_config, file) 
with open("model_config.json", "r") as file:
    loaded_config = json.load(file)
print(loaded_config)
print(type(loaded_config)) 
request_data = {
    "model": "GPT",
    "prompt": "Explain retrieval augmented generation.",
    "max_tokens": 100
}
print(request_data) 
request_json = json.dumps(request_data)
print(request_json)
print(type(request_json)) 