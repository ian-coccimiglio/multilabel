#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 14:46:33 2024

@author: ian
"""


# Cases #
# Image A
# Image B


# Iterate over all labels in image A
# If a label in A does not overlap with any label in B
## Assign it an even number (2, 4...)

# For the remaining labels, assign a prime number

## Prime assignment
# In an ideal situation, we're trying to achieve two goals
## square-free semiprimes
## small (enough) numbers

# Plausible worst case scenarios (n=2 images)
# 3000 objects per image, all of which are overlapping.
# 8821*8819
# However, we can probably imagine that most of the numbers are between 4 and 10
# print(f"{8821*8819:,}")


def primes_sieve2(limit):
    a = [True] * limit  # Initialize the primality list
    a[0] = a[1] = False

    for i, isprime in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):  # Mark factors non-prime
                a[n] = False


im1 = [a for a in primes_sieve2(1000) if a > 2]
im2 = [b for b in primes_sieve2(2000) if b > 1000]

max(im1) * max(im2)

# %%


class PrimeImageCombiner:
    def __init__(self):
        self.combined = self.combine_images()

    def background_offset():
        """
        Offsets the background from 0 to 1
        """
        pass

    def convert_to_primes():
        """
        Converts a list of labels to prime numbers
        """
        pass

    def combine_images(self, im1, im2):
        """
        Combines two appropriately formatted images to an overlapped label image
        """
        prime_im1 = self.convert_to_primes(self.background_offset(im1))
        prime_im2 = self.convert_to_primes(self.background_offset(im1))

        return prime_im1 * prime_im2

    def decompose_image(self):
        """ """
        pass
