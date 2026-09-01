project_name = "Enterprise GenAI Lab"
day_number = 1
is_learning = True
print(project_name)
print(day_number)
print(is_learning)
print(type(project_name))
print(type(day_number))
print(type(is_learning))
next_day = day_number + 1
print(next_day)
temperature = 0.7
print(temperature)
print(type(temperature))
models = ["GPT", "Claude", "Gemini"]
print(models)
print(models[0])
print(models[2])
models.append("Llama")
print(models)
model_count = len(models)
print(model_count)
for model in models:
    print("Available model:", model)
model_config = {
    "model": "GPT",
    "temperature": 0.7,
    "enabled": True  
}
print(model_config)
print(model_config["model"])
print(model_config["temperature"])
model_config["provider"] = "OpenAI"
print(model_config)
print(type(model_config))
if model_config["enabled"]:
    print("The model is enabled.")
else:
    print("The model is disabled.")
def show_model_status(model_name):
    print("checking model:", model_name)
show_model_status("GPT") 
show_model_status("Claude")
show_model_status("Gemini")
def create_model_label(model_name):
    label= "Model: " + model_name
    return label
model_label = create_model_label("GPT")
print(model_label)