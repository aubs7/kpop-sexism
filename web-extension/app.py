from flask import Flask, request, jsonify
from flask_cors import CORS
import praw
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import preprocessing

# Load model and tokenizer
model = tf.keras.models.load_model('kpop-sexism-model2.h5')
with open('tokenizer.pickle', 'rb') as f:
    tokenizer = pickle.load(f)

MAXLEN = 100
app = Flask(__name__)
CORS(app)

# Reddit API setup (use your own credentials)
reddit = praw.Reddit(
    client_id='XkjI8iUH-LEhPbVHk2BUGg',
    client_secret='32QJCRmY17QOeInoVLdEU5Eg9NvI_w',
    user_agent='"desktop:myapp:v1.0 (by u/Illustrious-Bake4821)'
)

def classify_text(text):
    cleaned = preprocessing.preprocess_text(text)
    seq = tokenizer.texts_to_sequences([cleaned])
    padded = pad_sequences(seq, maxlen=MAXLEN, padding='post')
    prob = model.predict(padded)[0][0]
    label = 'Sexist' if prob >= 0.5 else 'Non-Sexist'
    return label, float(prob)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data['url']
    try:
        submission = reddit.submission(url=url)
    except Exception as e:
        return jsonify({'error': f'Failed to fetch Reddit post: {str(e)}'}), 400

    texts = [submission.title + " " + submission.selftext]
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        texts.append(comment.body)

    results = []
    for t in texts[:20]:  # Limit to 20 items for speed
        label, prob = classify_text(t)
        results.append({'text': t, 'label': label, 'probability': round(prob, 4)})

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)