from meta_ai_api import MetaAI

ai = MetaAI()
response = ai.prompt(message="Whats the weather in San Francisco today? And what is the date?")
print(response)