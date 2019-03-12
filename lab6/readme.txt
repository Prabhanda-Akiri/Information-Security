Implement RSA Blind Signature Attack that should consider input of any size and of type
alphanumeric/integer during runtime of the program. Implemented program should produce the
corresponding signature as output of the program. Display all intermediate results as well as final output
on terminal and also store all obtained results including intermediate results into a file with a name
“Program6-Output-BlindSignature.txt”. Note that output should be in human readable form not in
binary/hex-decimal.
Steps:
1. Read the input, divide into blocks and apply RSA Blind Signature Attack for each of the blocks
independently. Concatenate output of all the blocks as final output.
2. For each input character use the corresponding 8-bit ASCII value. Consider the space between
two words/characters as one input character and its ASCII value for further computation.
Sample Text Case
Plaintext : NITK575025
Public key : N=143, e=3
