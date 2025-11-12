import re
import regex
import pandas as pd
import contractions
import inflect

def remove_URL(text):
    url = re.compile(r'(https?://\S+|www\.\S+)')
    return url.sub(r'', text)

def remove_html(text):
    html = re.compile(r'<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    return re.sub(html, '', text)

def remove_non_ascii(text):
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    return text

def remove_bracket(text):
    bracket = r"[]"
    text = re.sub(f"[{re.escape(bracket)}]", " ", text)
    return text

def remove_mentions(text, placeholder="[USER]"):

    # Replace mentions in the middle of the text
    text = re.sub(r'@\w+', placeholder, text)

    # Reduce multiple placeholders to a single one
    text = re.sub(r'(\[USER\] ){2,}', f"{placeholder} ", text)

    return text

# Function to split CamelCase hashtags
def camel_case_split(identifier):
    matches = regex.finditer(r'.+?(?:(?<=\p{Ll})(?=\p{Lu})|(?<=\p{Lu})(?=\p{Lu}\p{Ll})|[0-9]+|$)', identifier)
    return ' '.join([m.group(0) for m in matches])

# Function to expand hashtags in a sentence
def expand_hashtags(text):
    """
    Replaces hashtags with meaningful words by splitting CamelCase.
    """
    return regex.sub(r'#(\w+)', lambda match: camel_case_split(match.group(1)), text)

# Function to remove hashtags
def remove_hashtag(text):
    """
    Removes the # symbol but keeps the word.
    """
    return re.sub(r'#([^\s]+)', r'\1', text)

def expand_contractions(text):

    return contractions.fix(text)

def remove_punct(text):
    punct_to_remove = r"""!#%$&'()*+,-."/:;<=>?@\^_`—{|}~"""

    # Use regex to remove punctuation while keeping [USER]
    text = re.sub(f"[{re.escape(punct_to_remove)}]", " ", text)

    return text

def split_hashtags(text):
    words = text.split()
    processed_words = []

    for word in words:
        if re.match(r"\[.*?\]", word):
            processed_words.append(word) 
        else:
            processed_words.extend(wordninja.split(word)) 

    return " ".join(processed_words)

p = inflect.engine()

def convert_numbers_to_words(text):
    return " ".join([p.number_to_words(word) if word.isdigit() else word for word in text.split()])

def normalize_numbers(text):
    text = re.sub(r'(\d+)K', lambda m: str(int(m.group(1)) * 1000), text)
    text = re.sub(r'(\d+)k', lambda m: str(int(m.group(1)) * 1000), text)

    text = re.sub(r'(\d+)(st|nd|rd|th)\b', lambda m: p.number_to_words(int(m.group(1))), text)

    text = re.sub(r'\b(\d{2,4})s\b', r'\1s', text)  

    return text

def remove_elongation(text):
    return re.sub(r'(\w)\1{2,}', r'\1\1', text) 

def remove_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip()

def expand_slang(text):
    # Escape '/' in keys for regex safety
    pattern = re.compile(r'\b(' + '|'.join(map(re.escape, slang_dict.keys())) + r')\b', re.IGNORECASE)
    return pattern.sub(lambda m: slang_dict[m.group(0).lower()], text)

def lowercase(text):
  text = text.lower()
  return text

def preprocess_text(text):
    if not isinstance(text, str):  # Avoid errors on NaN or non-string values
        return ""
    text = remove_URL(text)
    text = remove_html(text)
    text = remove_bracket(text)
    text = remove_mentions(text)
    text = expand_contractions(text)
    text = remove_punct(text)
    text = normalize_numbers(text)
    text = convert_numbers_to_words(text)
    text = camel_case_split(text)
    text = expand_hashtags(text)
    text = remove_hashtag(text)
    text = remove_elongation(text)
    text = expand_slang(text)
    text = remove_non_ascii(text)
    text = lowercase(text)

    # text = camel_case_remove(text)
    return text

slang_dict = {
    "y/o": "year old",
    "fm": "from",
    "istg": "I swear to God",
    "tmrw": "tomorrow",
    "idk": "I don't know",
    "brb": "be right back",
    "omw": "on my way",
    "tho": "though",
    "gonna": "going to",
    "wanna": "want to",
    "rn": "right now",
    "fr": "for real",
    "lmk": "let me know",
    "smth": "something",
    "acc": "actually",
    "prolly": "probably",
    "qt": "cute",
    "fck": "fuck",
    "btch": "bitch",
    "sht": "shit",
    "outta": "out of",
    "2day": "today",
    "2nite": "tonight",
    "4u": "for you",
    "4ward": "forward",
    "a3": "anyplace anywhere anytime",
    "a/n": "author note",
    "a/w": "anyway",
    "a/s/l": "age, sex, location",
    "adn": "any day now",
    "afaic": "as far as I am concerned",
    "afaik": "as far as I know",
    "afk": "away from keyboard",
    "aggro": "aggressive",
    "aight": "alright",
    "airhead": "stupid",
    "aka": "as known as",
    "alol": "actually laughing out loud",
    "amigo": "friend",
    "amz": "amazing",
    "app": "application",
    "armpit": "undesirable",
    "asap": "as soon as possible",
    "atm": "at the moment",
    "atw": "all the way",
    "b/c": "because",
    "b-day": "birthday",
    "b4": "before",
    "b4n": "bye for now",
    "bae": "before anyone else",
    "bak": "back at the keyboard",
    "bbl": "bee back later",
    "bday": "birthday",
    "becuz": "because",
    "bc": "because",
    "bent": "angry",
    "bestie": "best friend",
    "besty": "best friend",
    "bf": "boyfriend",
    "bff": "best friends forever",
    "bffe": "best friends forever",
    "bfn": "bye for now",
    "bg": "big grin",
    "bmfe": "best mates forever",
    "bmfl": "best mates life",
    "bozo": "idiot",
    "brah": "friend",
    "bravo": "well done",
    "brb": "be right back",
    "bro": "brother",
    "bta": "but then again",
    "btdt": "been there, done that",
    "btr": "better",
    "btw": "by the way",
    "buddy": "friend",
    "c'mon": "came on",
    "cid": "crying in disgrace",
    "congrats": "congratulations",
    "copacetic": "excellent",
    "coz": "because",
    "cu": "see you",
    "cuddy": "friends",
    "cul": "see you later",
    "cul8r": "see you later",
    "cutie": "cute",
    "cuz": "because",
    "cya": "bye",
    "cyo": "see you online",
    "dbau": "doing business as usual",
    "deets": "details",
    "dmn": "damn",
    "dobe": "idiot",
    "dope": "stupid",
    "dork": "strange",
    "dunno": "don't know",
    "dwi": "deal with it",
    "dyd": "don't you dare",
    "ermahgerd": "oh my gosh",
    "eu": "europe",
    "ez": "easy",
    "f9": "fine",
    "fav": "favorite",
    "far-out": "great",
    "fb": "facebook",
    "flick": "movie",
    "fml": "fuck my life",
    "foxy": "sexy",
    "friggin": "freaking",
    "fttn": "for the time being",
    "ftw": "for the win",
    "fud": "fear, uncertainty, and doubt",
    "fwiw": "for what it's worth",
    "fyi": "for your information",
    "g": "grin",
    "g2g": "got to go",
    "ga": "go ahead",
    "gal": "get a life",
    "getcha": "understand",
    "gf": "girlfriend",
    "gfn": "gone for now",
    "gg": "good game",
    "gj": "good job",
    "gky": "go kill yourself",
    "gl": "good luck",
    "glhf": "good luck have fun",
    "gmab": "give me a break",
    "gmbo": "giggling my butt off",
    "gmta": "great minds think alike",
    "goof": "idiot",
    "goofy": "idiot",
    "gr8": "great",
    "gtg": "got to go",
    "gud": "good",
    "h8": "hate",
    "hagn": "have a good night",
    "hdop": "help delete online predators",
    "hf": "have fun",
    "hml": "hate my life",
    "hoas": "hold on a second",
    "hhis": "hanging head in shame",
    "hmu": "hit me up",
    "hru": "how are you",
    "twt": "hope this helps",
    "hw": "homework",
    "i'ma": "i am going to",
    "iac": "in any case",
    "ic": "I see",
    "icymi": "in case you missed it",
    "idk": "I don't know",
    "iggy": "ignore",
    "iht": "i hate this",
    "ikr": "i know right",
    "ilt": "i like that",
    "ily": "i love you",
    "ima": "i am going to",
    "imao": "in my arrogant opinion",
    "imnsho": "in my not so humble opinion",
    "imo": "in my opinion",
    "imy": "i miss you",
    "iou": "i owe you",
    "iow": "in other words",
    "ipn": "I am posting naked",
    "irl": "in real life",
    "j/k": "just kidding",
    "jdi": "just do it",
    "jk": "just kidding",
    "jkn": "joking",
    "jyeah": "yeah",
    "kinda": "kind of",
    "l8": "late",
    "l8r": "later",
    "lbh": "let's be honest",
    "ld": "later dude",
    "ldi": "let's do it",
    "ldr": "long distance relationship",
    "lees": "beautiful",
    "lfm": "looking for more",
    "lil": "little",
    "llta": "lots and lots of thunderous applause",
    "lmao": "laugh my ass off",
    "lmirl": "let us meet in real life",
    "lol": "laugh out loud",
    "lolz": "laugh out loud",
    "lotta": "lot of",
    "lsr": "loser",
    "ltr": "longterm relationship",
    "lua": "love you always",
    "lub": "love",
    "lubb": "love",
    "lulab": "love you like a brother",
    "lulas": "love you like a sister",
    "lul": "laugh",
    "luls": "laugh",
    "lulz": "laugh",
    "lumu": "love you miss you",
    "luv": "love",
    "lux": "luxury",
    "lwm": "laugh with me",
    "lwp": "laugh with passion",
    "lvl": "level",
    "m/f": "male or female",
    "m2": "me too",
    "m8": "mate",
    "me2": "me too",
    "milf": "mother I would like to fuck",
    "mma": "meet me at",
    "mmb": "message me back",
    "mvp": "most valuable player",
    "msg": "message",
    "mtf": "more to follow",
    "myob": "mind your own business",
    "nah": "no",
    "nc": "no comment",
    "nk": "not kidding",
    "ngl": "not gonna lie",
    "nlt": "no later than",
    "nm": "not much",
    "no1": "no one",
    "np": "no problem",
    "nsfw": "not safe for work",
    "nuh": "no",
    "nvm": "nevermind",
    "obo": "or best offer",
    "oic": "oh, i see",
    "oll": "online love",
    "omg": "oh my god",
    "omw": "on my way",
    "osm": "awesome",
    "otoh": "on the other hand",
    "perv": "pervert",
    "pervy": "pervert",
    "phat": "pretty hot and tempting",
    "pir": "parent in room",
    "pls": "please",
    "plz": "please",
    "ppl": "people",
    "pro": "professional",
    "pwnd": "owned",
    "qq": "crying",
    "r": "are",
    "rly": "really",
    "rofl": "roll on the floor laughing",
    "rolf": "roll on the floor laughing",
    "rpg": "role playing games",
    "ru": "are you",
    "s2u": "shame to you",
    "scrub": "loser",
    "sec": "second",
    "shid": "slaps head in disgust",
    "shoulda": "should have",
    "sff": "so funny",
    "smexy": "smart and sexy",
    "smh": "shaking my head",
    "somy": "sick of me yet",
    "sot": "short of time",
    "sry": "sorry",
    "str8": "straight",
    "sux": "sucks",
    "swag": "style",
    "taze": "irritate",
    "tba": "to be announced",
    "tbfu": "too bad for you",
    "tbc": "to be continued",
    "tbd": "to be determined",
    "tbr": "to be rude",
    "tc": "take care",
    "tho": "though",
    "thx": "thanks",
    "thanx": "thanks",
    "tfw": "that feeling when",
    "til": "today i learned",
    "ttyl": "talk to you later",
    "ty": "thank you",
    "tyvm": "thank you very much",
    "u": "you",
    "uber": "the best",
    "ugh": "disgusted",
    "ur": "you are",
    "uw": "you are welcome",
    "vs": "versus",
    "w2f": "way too funny",
    "w8": "wait",
    "wak": "weird",
    "wanna": "want to",
    "wb": "welcome back",
    "whiz": "talented",
    "whoa": "surprise",
    "whoah": "surprise",
    "wfm": "works for me",
    "wibni": "would not it be nice if",
    "wmd": "weapon of mass destruction",
    "wot": "what",
    "wtf": "what the fuck",
    "wtg": "way to go",
    "wtgp": "want to go private",
    "wu": "what is up",
    "wuh": "what?",
    "wuv": "love",
    "ym": "young man",
    "yawn": "boring",
    "yum": "good",
    "x": "kiss",
    "xxx": "kiss",
    "xdd": "laughing",
    "y": "why",
    "yolo": "you only live once",
    "yuge": "huge",
    "yw": "you are welcome",
    "ywa": "you are welcome anyway",
    "zomg": "oh my god",
    "zzz": "sleeping",
    "af": "as fuck",
    "bs": "bullshit",
    "fml": "fuck my life",
    "stfu": "shut the fuck up",
    "lmfao": "laughing my fucking ass off",
    "omfg": "oh my fucking god",
    "ffs": "for fucks sake",
    "mf": "motherfucker",
    "gtfo": "get the fuck out",
    "pos": "piece of shit",
    "mofo": "motherfucker",
    "pos": "piece of shit",
    "p*ssy": "pussy",
    "dck": "dick",
    "d*ck": "dick",
    "cock": "cock",
    "asshole": "asshole",
    "shit": "shit",
    "damn": "damn",
    "hell": "hell",
    "f***": "fuck",
    "b****": "bitch",
    "a**": "ass",
    "s***": "shit",
    "d***": "damn",
    "h***": "hell",
    "stfu": "shut the fuck up",
    "em": "them",
    "fw": "fuck with",
    "f": "fuck",
    "sibs": "siblings",
    "n": "and",
    "y/o": "year old",
    "yr": "year",
    "etc": "et cetera",
    "mgtow": "Men Going Their Own Way"
}