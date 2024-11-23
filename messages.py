from fuzzywuzzy import process

def correct_city_name(user_input, cities):
    city_names = list(cities.keys())
    best_match, score = process.extractOne(user_input, city_names)
    return best_match if score >= 30 else None

def ask_question(vk, user_id, question):
    vk.messages.send(user_id=user_id, message=question, random_id=0)
