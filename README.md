# pmhsc - Poor Man's Homophonic Substitution Cipher

This is a Python implementation of a [homophonic substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher#Homophonic_substitution). Upon generating a `mapping.p` file, pmhsc takes 7 random, non-repeating letters and space (for confusion) and gathers all the permutations with repetitions (cartesian product) of those letters (8^8 or 16,777,216 unique strings). These permutations are then shuffled, and dispersed equally 27 ways (26 letters of the alphabet and space). This gives each letter 621,378 unique mappings. When a message is encrypted one of these 621,378 strings belonging to each letter are selected at random to represent each character. During decryption strings are searched for and remapped to their original letters.

Seeing as we still cannot break some homophonic substitution ciphers from the eighteen hundreds that were comprised of 50,000 symbols or less, I'm fairly certain that this cipher can be used to very safely share short, important, nerdy messages. Swap `mapping.p` files with your homies face-to-face, and then send each other all the secret messages. <3

## Usage
```
$ python pmhsc.py
usage: pmhsc.py [-h] [-g] [-e] [-d] [-m MAPPING] [-i INPUT] [-o OUTPUT]

poor mans homophonic substitution cipher

optional arguments:
  -h, --help            show this help message and exit
  -g, --genmaps         generate mapping file
  -e, --encrypt         encrypt a file
  -d, --decrypt         decrypt a file
  -m MAPPING, --mapping MAPPING
                        specify a mapping file to use (default: mapping.p)
  -i INPUT, --input INPUT
                        input file
  -o OUTPUT, --output OUTPUT
                        output file

$ python pmhsc.py --genmaps
Mapping completed in 85.75 seconds.

$ du -sh mapping.p
358M	mapping.p

$ python pmhsc.py --encrypt -i example/example.txt -o example/example.enc
Encryption completed in 41.94 seconds.

$ python pmhsc.py --decrypt -i example/example.enc -o example/example.dec
Decryption completed in 161.18 seconds.
```

## Results

```
$ cat example.txt
Perhaps it had something to do with living in a dark cupboard, but
Harry had always been small and skinny for his age. He looked even
smaller and skinnier than he really was because all he had to wear were
old clothes of Dudley's, and Dudley was about four times bigger than he
...

$ cat example.enc
b kbkk rrkdknrkvrqkbvd bdnkq nr nqrvbvrbbvkvknbqb nbd nvvd  dkrqvrvvqrddqrvrdd
rqnqnvvnbdk rbvvkdqdb bvvnrqbvr vkqrvrbvqvq dbndknqndq rrvdbrqdb vkrkkrvvqdvdkb
n bkqkrk kqkkq qvqqvbdd q rqd bdv vv r rqvvd qdndrd k vbnkdk vqkkqkvqndnnnbnbrkr
drbrkv kbbr dqndqnbnnqr kdqbvqqbvdkdnd dkdr  kkrnnkbqdnbv kkk qkbn  qddrdnbnqb
...

$ cat example.dec
perhaps it had something to do with living in a dark cupboard but
harry had always been small and skinny for his age he looked even
smaller and skinnier than he really was because all he had to wear were 
old clothes of dudleys and dudley was about four times bigger than he
...
```
