import re
class bpe_tokenizer_class:
  def __init__(self):
    self.vocab_ = self.vocab()
    self.s2i = self.vocab_
    self.i2s = {index:token for token,index in self.vocab_.items()}
  def vocab(self):
    with open("text.txt",'r') as file:
      preprocessed_text = file.read()
    all_tokens = re.split(r'([,.:;?_!"()\']|--|\s)',preprocessed_text)
    all_tokens = [token.strip() for token in all_tokens]
    all_token_parts = []
    for token in all_tokens:
      all_token_parts.extend(self.bpe_word_breaker(token))
    all_token_parts = list(set(all_token_parts))
    all_token_parts.extend("<|EndOfText|>")
    vocab = {token:index for index,token in enumerate(all_token_parts) if token}
    return vocab
  def bpe_word_breaker(self, input_text):
    subsets = []
    for i in range(len(input_text)):
      for j in range(len(input_text),0,-1):
        if input_text[i:j]:
          subsets.append(input_text[i:j])
    return subsets
  def encode(self, input_text):
    ids = []
    all_tokens = re.split(r'([,.:;?_!"()\']|--|\s)', input_text)
    all_tokens = [token.strip() for token in all_tokens]
    for token in all_tokens:
      try:
        if self.s2i[token] != -1:
          ids.append(self.s2i[token])
      except:
        while token != "":
          for part in self.bpe_word_breaker(token):
            try:
              if self.s2i[part] != -1:
                ids.append(self.s2i[part])
                token = token[:token.index(part)]+token[token.index(part)+len(part):]
                break
            except Exception as e:
              pass
    return ids
  def decode(self, ids):
    if type(ids) == int:
      return self.i2s(ids)
    output_string_ = []
    for id in ids:
      output_string_.append(self.i2s[id])
    output_string = " ".join(output_string_).replace(" <|Space|> ", " ")
    output_string = re.sub(r'\s+([,.?!"()\'])', r'\1', output_string).replace("' ","'")
    return output_string