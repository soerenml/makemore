words = open('names.txt', 'r').read().splitlines()

words[:10]

b = {}
for w in words:
  # Adding start- and ending character
  chs = ['<S>'] + list(w) + ['<E>']

  for ch1, ch2 in zip(chs, chs[1:]):
    bigram = (ch1, ch2)
    # If the bigram is not existend -> 0 othewise -> +1
    b[bigram] = b.get(bigram, 0) + 1

# Logic of the previos commands.
#test = ['horsti']
#for w in test:
#    e = list(w)
#    for a,b in zip(e, e[1:]):
#        bigram=(a,b)
#        print(bigram)

sorted(b.items(), key=lambda kv: kv[1], reverse=True)
import torch

N = torch.zeros((28,28), dtype=torch.int32)
print(N)

N.dtype