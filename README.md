# pmhsc - Poor Man's Homophonic Substitution Cipher

This is a Python implementation of a [homophonic substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher#Homophonic_substitution). Upon generating a `mapping.p` file, pmhsc takes 10 random, non-repeating letters and gathers all the permutations of those letters (10! or 3,628,800 unique strings). These permutations are then shuffled, and dispersed equally between the 26 letters of the alphabet. This gives each letter of the alphabet 139,569 mappings. When a message is encrypted one of these 139,569 strings belonging to each letter are selected at random to represent each character. During decryption strings are searched for and remapped to their original letters.

Seeing as we still cannot break some homophonic substitution ciphers from the eighteen hundreds that were comprised of 50,000 symbols or less, I'm fairly certain that this cipher can be used to safely talk about nerdy, unimportant things. Swap `mapping.p` files with your homies face-to-face, and then send each other all the secret messages. <3

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
Mapping completed in 5.55 seconds.

$ du -sh mapping.p
70M	mapping.p

$ python pmhsc.py --encrypt -i example/example.txt -o example/example.enc
Encryption completed in 0.33 seconds.

$ python pmhsc.py --decrypt -i example/example.enc -o example/example.dec
Decryption completed in 25.95 seconds
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
qntviodxwgwtvqdnxoginvowdxgqtiviwonqxgdtitwxgnoqdvxvqoiwtgndtwdqionxvg nxiqtvodgwdgqotnwvxi wgdxiotqnvgodxtwnvqigtoqxinwdv
dtviowngxqtdiqxgvnowqgtvwxndiotoqwgxnvdiixnotwdvqgwxtgndvioqndxvqowtgiqgwxodnvtitgdnoqivwx gxwtvoidnqgiqtvonwdx
qxvnitodgwxgoqdntwiv igvdnxtowqnxvqotdgwidgwxvnitqodqvontixwg nqtigvxodwovwngiqxtdvdtoiwgqxngvtxqwodniqgwvdnxitotgdqixwonv
xwtdonqvgixodqngviwt oxigvtqdwn qntdoxivgwiogqdvxtwnqgxdnvtiwondwqvgtoix
...

$ cat example.dec
perhaps it had something to do with living in a dark cupboard but
harry had always been small and skinny for his age he looked even
smaller and skinnier than he really was because all he had to wear were 
old clothes of dudleys and dudley was about four times bigger than he
...
```
