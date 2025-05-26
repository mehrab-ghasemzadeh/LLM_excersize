from bpe_ import bpe_tokenizer_class

bpe = bpe_tokenizer_class()

text = "I HAD always thought Jack Gisburn rather a cheap genius--though a good fellow enough--so it was no"
ids = bpe.encode(text)
print(ids)
print(bpe.decode(ids))
