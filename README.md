# pmhsc - Poor Man's Homophonic Substitution Cipher

This is a Python command-line tool for an implementation of a [homophonic substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher#Homophonic_substitution). Upon generating a `mapping.p` file, pmhsc takes 8 random, non-repeating letters and gathers all the permutations with repetitions (Cartesian product) of those letters (8^8 or 16,777,216 unique strings). These permutations are then shuffled, and dispersed equally 27 ways (26 letters of the alphabet and space). This gives each letter 621,378 unique representations (or mappings). When a message is encrypted one of these 621,378 strings belonging to each letter are selected at random to represent each character. During decryption strings are searched for and remapped to their original letters.

Seeing as we still cannot break some homophonic substitution ciphers from the eighteen hundreds that were comprised of 50,000 symbols or less, I'm fairly certain that this cipher can be used to very safely share relatively short, important, nerdy messages. Swap `mapping.p` files with your homies face-to-face, and then send each other all the secret messages. <3

A little while after making pmhsc I came back and created **Rich Man's Homophonic Substitution Cipher** which can encrypt any file type (not just ASCII) with a homophonic cipher similar to pmhsc. It's notably less strong, but this is mostly just for fun anyhow (read: just use OTP). It uses an 8-letter [isogram](https://en.wikipedia.org/wiki/Isogram) (`espinoza` in this case) and takes the Cartesian product of that string to produce 8^8 unique strings. It then takes every possible value of 8-bits (2^8 or 256 states) and disperses the 8^8 unique strings to these 256 states. This gives each 8-bit state 65,536 unique representations. Encryption and decryption occurs the same as pmhsc.

See below for the usage and results of both of these tools.

## Usage (pmhsc)
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

# Usage (rmhsc)
```
$ python rmhsc.py --help
usage: rmhsc.py [-h] [-g] [-e] [-d] [-i INPUT] [-o OUTPUT]

rich man's homophonic substitution cipher

optional arguments:
  -h, --help            show this help message and exit
  -g, --genmaps         generate mapping file
  -e, --encrypt         encrypt a file
  -d, --decrypt         decrypt a file
  -i INPUT, --input INPUT
                        input file
  -o OUTPUT, --output OUTPUT
                        output file

$ python rmhsc.py -g
Generating mapping file...
Completed genmaps in 32.41 seconds.

$ du -sh mapping.p
289M	mapping.p

$ python rmhsc.py --encrypt -i example/1x1.png -o example/1x1.enc
Encrypting file...
Completed encryption in 1.90 seconds.

$ python rmhsc.py --decrypt -i example/1x1.enc -o example/1x1.dec
Decrypting file...
Completed decryption in 40.88 seconds.

$ md5sum example/1x1.*
71a50dbba44c78128b221b7df7bb51f1  example/1x1.dec
e26386ee59797c96ba40d38c91aab23f  example/1x1.enc
71a50dbba44c78128b221b7df7bb51f1  example/1x1.png
```

## Results

pmhsc:
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

rmhsc:
```
$ xxd 1x1.png
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 0001 0000 0001 0103 0000 0025 db56  .............%.V
00000020: ca00 0000 0350 4c54 4500 0000 a77a 3dda  .....PLTE....z=.
00000030: 0000 0001 7452 4e53 0040 e6d8 6600 0000  ....tRNS.@..f...
00000040: 0a49 4441 5408 d763 6000 0000 0200 01e2  .IDAT..c`.......
00000050: 21bc 3300 0000 0049 454e 44ae 4260 82    !.3....IEND.B`.

$ cat 1x1.enc
nposaznsonipzppeeoppzponpniiopiepizapniiaaznipppsosanpznnaninoiiioaoapinpazansa
ozszsaaieaiiossanionpaisnianaepioapsszzassapoopionieoazszaszszenizzsoaippsanoap
panipznooziepezzsnzononazosoonpezinaispiipznoipaapenoioapananpaoaaiipsniiasnnzo
noapnzaoezeaepeniaaipozzzeeeepasepsspaapspzeansoaepiaeoeiospponiioeaazpoazaipop
...
```
