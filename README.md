# Multilabel
" Premature optimization is the root of all evil. " - Donald Knuth

A project to see whether it is reasonable to encode/decode masks as a "2.5D" label image, specifically by factorizing primes. This was inspired by investigating novel tools in bioimaging (such as the Segment Anything Model) and chatting on the image.sc forums.

Each unique mask is given a sequential prime number >1. Create an empty label image of 1s. Multiply each mask together. At the end, you'll still have a 2D label image, except a subset label-values could be prime-factored into a set of distinct and unique primes ("square-free integers").

Benefits: 
- Possibly space-efficient in images with few overlaps.
- Theoretically able to represent any list of overlapping 2D masks in 2-dimensions.
- Would be easy and fast to cycle/visualize masks by dividing each pixel by each prime number and taking the modulus.
Drawbacks:
- 32-bit integer images would be easily surpassed by images with many colliding masks. Pah!

Maybe this project works, or maybe it will be bioimaging meets cryptography.

Ideas for if an array exceeds the bit-limit...
- In the label_image encoder/decoder, create a mapping such that each unique label can be transformed to a unique 32-bit integer and back again.

## Draft implementation

### Label image encoding
1) Get a list of all masks representing an image
2) Represent each mask using a sequential prime number >=2, or 1 for background 
3) Multiply each mask together element-wise.

### Label image decoding
1) To view any particular mask, divide the label image by a prime number `n`. 
2) All masks will be either be prime or a square-free integer `P`. `P` mod `n` will be 0 iff the `n` is a prime factor of `P`.
3) In the case `n` == `P`, then `P` is prime and therefore the mask has no overlaps.
4) Therefore, we can use `P mod n` to generate the binary mask for label `n`.
5) We can iterate this for all prime numbers up to the number of different masks in the image.

## Current status
1) It works for images with limited overlaps. You can save overlapping masks as a 2D label image and decode it as masks later.
