import requests
from bs4 import BeautifulSoup
import json
from collections import Counter
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_word_frequencies(url):
    # Fetch HTML content from the URL
    response = requests.get(url)
    html_content = response.text

    # Parse HTML and extract text
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()

    # Split the text into words
    words = text.split()

    # Count the frequency of each word
    word_frequencies = dict(Counter(words))

    return word_frequencies

@app.route('/analyze', methods=['POST'])
def analyze():
    url = request.json['url']

    # Get word frequencies
    word_frequencies = get_word_frequencies(url)

    # Return the result as JSON
    return jsonify(word_frequencies)

if __name__ == '__main__':
    app.run()
