from bpe import bpe_tokenizer

bpe = bpe_tokenizer()
en = bpe.encode('shotorgavpalang')
print(en)
de = bpe.decode(en)
print(de)