import requests
from time import sleep
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

json_words = 'words.json'
json_counters = 'words_counters_embedded.json'

host = ""
post_url = f"{host}/submit-word"
get_url = f"{host}/get-word"
status_url = f"{host}/status"
NUM_ROUNDS = 5

word_costs = None
word_counters = None

try:
    with open(json_words, 'r') as f:
        word_costs = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading {json_words}: {e}")

try:
    with open(json_counters, 'r') as f:
        word_counters = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading {json_counters}: {e}")

model_sentence = SentenceTransformer('all-mpnet-base-v2')

def get_sentence_embedding(text):
    return model_sentence.encode(text)

def what_beats(word):
    if word.lower() == "pillar":
        return 7
    elif word.lower() == "tornado":
        return 52
    elif word.lower() == "picture":
        return 4
    elif word.lower() == "shoes":
        return 9
    elif word.lower() == "solar panel":
        return 7
    elif word.lower() == "battery":
        return 9
    elif word.lower() == "computer":
        return 11
    elif word.lower() == "wind":
        return 25
    elif word.lower() == "table":
        return 7
    elif word.lower() == "bitcoin":
        return 45
    elif word.lower() == "spider":
        return 9
    elif word.lower() == "vampire":
        return 19
    elif word.lower() == "darkness":
        return 19
    elif word.lower() == "acorn":
        return 5
    elif word.lower() == "apple":
        return 4
    elif word.lower() == "rose":
        return 9

    word_embedding = get_sentence_embedding(word)
    beaten_by = None
    maximum_similarity = 0.0
    beaten_by_list = []

    for counter_word, embedded_list in word_counters.items():
        for item in embedded_list:
            emb = np.array(item["embedding"])
            similarity = cosine_similarity([word_embedding], [emb])[0, 0]
            if similarity > 0.7:
                beaten_by_list.append(counter_word)
            if similarity > maximum_similarity:
                maximum_similarity = similarity
                beaten_by = counter_word


    best_beating_word = None
    min_cost = float('inf')

    for beating_word in beaten_by_list:
        if beating_word in word_costs:
            cost = word_costs[beating_word]
            if cost < min_cost:
                min_cost = cost
                best_beating_word = beating_word

    if best_beating_word:
        index = list(word_costs.keys()).index(best_beating_word) + 1
        return index
    else:
        index = list(word_costs.keys()).index(beaten_by) + 1
        return index


def register(player_id):
    register_url = f"{host}/register"
    data = {"player_id": player_id}
    response = requests.post(register_url, json=data)

    return response.json()


def play_game(player_id):

    def get_round():
        response = requests.get(get_url)
        print(response.json())
        sys_word = response.json()['word']
        round_num = response.json()['round']
        return (sys_word, round_num)

    submitted_rounds = []
    round_num = 0

    while round_num != NUM_ROUNDS :
        print(submitted_rounds)
        sys_word, round_num = get_round()
        while round_num == 0 or round_num in submitted_rounds:
            sys_word, round_num = get_round()
            sleep(0.5)

        if round_num > 1:
            status = requests.post(status_url, json={"player_id": player_id}, timeout=2)
            print(status.json())

        chosen_word = what_beats(sys_word)
        data = {"player_id": player_id, "word_id": chosen_word, "round_id": round_num}
        response = requests.post(post_url, json=data, timeout=5)
        submitted_rounds.append(round_num)
        print("POST: !!!!!!!!!!!!!!!!")
        print(response.json())


# register("")
# play_game("")
