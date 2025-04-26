import requests
import json
from time import sleep
import os

host = "http://10.41.186.9:8000/"
get_url = f"{host}/get-word"

OUTPUT_FILE = "new_words.txt"  # You can change this to "new_words.json" for JSON output
PROCESSED_WORDS_FILE = "processed_words.txt"

def load_processed_words():
    """Loads the set of already processed words from a file."""
    processed_words = set()
    if os.path.exists(PROCESSED_WORDS_FILE):
        with open(PROCESSED_WORDS_FILE, "r") as f:
            for line in f:
                processed_words.add(line.strip())
    return processed_words

def save_processed_words(processed_words):
    """Saves the set of processed words to a file."""
    with open(PROCESSED_WORDS_FILE, "w") as f:
        for word in processed_words:
            f.write(f"{word}\n")

def save_new_words_to_txt(new_words):
    """Appends new words to a text file."""
    with open(OUTPUT_FILE, "a") as f:
        for word in new_words:
            f.write(f"{word}\n")

def save_new_words_to_json(new_words):
    """Appends new words to a JSON file."""
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r") as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    updated_data = existing_data + new_words
    with open(OUTPUT_FILE, "w") as f:
        json.dump(updated_data, f, indent=4)

def check_for_new_words():
    """Fetches a word from the server and saves it if it's new."""
    processed_words = load_processed_words()
    newly_found_words = []

    try:
        response = requests.get(get_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        if 'word' in data:
            current_word = data['word']
            if current_word not in processed_words:
                newly_found_words.append(current_word)
                processed_words.add(current_word)
                print(f"New word found: {current_word}")
                if OUTPUT_FILE.endswith(".txt"):
                    save_new_words_to_txt(newly_found_words)
                elif OUTPUT_FILE.endswith(".json"):
                    save_new_words_to_json(newly_found_words)
                else:
                    print("Unsupported output file format.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching word: {e}")
    except json.JSONDecodeError:
        print("Error decoding JSON response.")
    finally:
        save_processed_words(processed_words)

if __name__ == "__main__":
    print("Running the script to check for new words every second...")
    while True:
        check_for_new_words()
        sleep(1)