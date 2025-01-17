from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize  
from nltk.tokenize import RegexpTokenizer
import nltk
import re 
import os

def setup():
    nltk.download('stopwords')
    nltk.download('punkt')

    tokenizer = RegexpTokenizer(r'\w+')
    stop_words = set(stopwords.words('english'))

    !git clone https://github.com/areebbeigh/profanityfilter.git
    return 

def tokenise(corpus):
  filtered_sentence = [] 
  corpus = str(corpus)
  encoded_string = corpus.encode("ascii", "ignore")
  decode_string = encoded_string.decode()
  word_tokens = tokenizer.tokenize(corpus) 
  # corpus = corpus.lower()
  # filtered_sentence = [w for w in word_tokens if not w in stop_words]  
  return word_tokens

def map_book(tokens):
    hash_map = {}

    if tokens is not None:
        for element in tokens:          
            if element in hash_map:
                hash_map[element] = hash_map[element] + 1
            else:
                hash_map[element] = 1

        return hash_map
    else:
        return None
def initialize(path):
      filename = (path)
      f = open(filename)
      wordlist = f.readlines()
      wordlist = [w.strip() for w in wordlist if w]
      return wordlist

def load_corpus(path):
    tot = ""
    filename = (path)
    f = open(filename)
    wordlist = f.readlines()
    tot += str(wordlist)
    return tot


def generate_rating(corpus):
  word_list = initialize(os.curdir + '/profanityfilter/profanityfilter/data/badwords.txt')
  words = tokenise(corpus)

  map = map_book(words)
  explicit_count = 0
  explicit_word = {}
  for word in word_list:
      try:
            explicit_count +=map[word]
            # print('Word: [' + word + '] Frequency: ' + str(map[word]))
            print("Explicit Count: "+ str(explicit_count))
            explicit_word[word] = map[word]
      except:
            continue
  print(explicit_word)
  tot = sum(map.values())


  exp_tot = sum(explicit_word.values())

  return (tot, exp_tot)

setup()
df = pd.read_csv(os.curdir + '/Song_data_prep-L.csv')
rating = []
for i in tqdm(df['Lyrics']):
  # corpus = load_corpus()

  (tot, exp_tot) = generate_rating(i)
  rating.append(round((exp_tot/tot * 400 )) if  (exp_tot/tot * 400 < 100) else 100)

df['Explicit Rating'] = rating

df.to_csv('With_Explicit_Rating.csv', index= False)

