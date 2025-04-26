import requests
from time import sleep
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

json_words = 'words.json'
json_counters = 'words_counters_embedded.json'

host = "http://10.41.186.9:8000"
post_url = f"{host}/submit-word"
get_url = f"{host}/get-word"
status_url = f"{host}/status"
NUM_ROUNDS = 10

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
    if word == '':
        return
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
    # print(f"Beaten by list: {beaten_by_list}, system word: {word}")
    # print(f"Beaten by: {beaten_by}, system word: {word}, similarity: {maximum_similarity:.4f}")

    best_beating_word = None
    min_cost = float('inf')

    for beating_word in beaten_by_list:
        if beating_word in word_costs:
            cost = word_costs[beating_word]
            if cost < min_cost:
                min_cost = cost
                best_beating_word = beating_word

    if best_beating_word:
        # print(f"Cuvantul cu cel mai mic cost care bate '{word}': {best_beating_word} (cost: {min_cost})")
        index = list(word_costs.keys()).index(best_beating_word) + 1
        return index
    else:
        # print(f"Cuvantul cu cel mai mic cost care bate {word} : {beaten_by}")
        index = list(word_costs.keys()).index(beaten_by) + 1
        # print(f"{beaten_by} -> {index}")
        return index

def play_game(player_id):
    global sys_word
    for round_id in range(1, NUM_ROUNDS + 1):
        round_num = -1

        while round_num != round_id:
            response = requests.get(get_url)
            print(response.json())
            sys_word = response.json()['word']
            round_num = response.json()['round']
            # print(what_beats(sys_word), sys_word)
            sleep(1)

        if round_id > 1:
            status = requests.get(status_url)
            print(status.json())

        chosen_word = what_beats(sys_word)
        data = {"player_id": player_id, "word_id": chosen_word, "round_id": round_id}
        response = requests.post(post_url, json=data)
        # print(response)
        print(response.json())

def register(player_id):
    register_url = f"{host}/register"
    data = {"player_id": player_id}
    response = requests.post(register_url, json=data)

    return response.json()

register("kPgkmt47")
play_game('kPgkmt47')
