import re

class bpe_tokenizer:
    def __init__(self):
        self.s2i = vocab
        self.i2s = {index:token for token,index in vocab.items()}
    def bpe_breaker(self, st=''):
        subsets = []
        for i in range(len(st)):
            for j in range(len(st),0,-1):
                if st[i:j]:
                    subsets.append(st[i:j])
        return subsets
    def encode(self, input_text):
        ids = []
        input_text+="<|EOT|>"
        inp = re.split(r'([,.;?_!"()\']|--|\s)',input_text)
        inp = [i.strip() for i in inp]
        for word in inp:
            while word != "":
                print(word)
                try:
                    if self.s2i[word]:
                        ids.append(self.s2i[word])
                        break
                except:
                    for part in self.bpe_breaker(word):
                        try:
                            if self.s2i[part]:
                                ids.append(self.s2i[part])
                                word = word[:word.index(part)]+word[word.index(part)+len(part):]
                                break
                        except Exception as e:
                            print(f" -- ERROR --> {e} ")
                            pass
        return ids
    def decode(self, ids):
        if type(ids) == int:
            num = ids
            ids = []
            ids.append(num)
        for i in ids:
            text = " ".join([self.i2s[i] for i in ids])
            text = re.sub(r'\s+([,.?!"()\'])', r'\1', text).replace("' ","'")
        return text



with open ('./text.txt','r',encoding='utf-8') as file:
    text = file.read()
all_words = re.split(r'([,.;?_!"()\']|--|\s)',text)
all_words = [i.strip() for i in all_words]
all_words.extend(['<|EOT|>'])
all_words = list(set(all_words))

def bpe_breaker(st):
    subsets = []
    for i in range(len(st)):
        for j in range(len(st),0,-1):
            if st[i:j]:
                subsets.append(st[i:j])
    return subsets

all_word_combos = []
for word in all_words:
    all_word_combos.extend(bpe_breaker(word))
all_word_combos = set(sorted(all_word_combos))

vocab = {token:index for index,token in enumerate(all_word_combos) if token}
bpe = bpe_tokenizer()
string_ = "His confident eyes grew dim, and his cheeks paled a little under their h."
encoded_tokens = bpe.encode(string_)
decoded_ids = bpe.decode(encoded_tokens)

print(len(encoded_tokens))
print(string_)
print(decoded_ids)

