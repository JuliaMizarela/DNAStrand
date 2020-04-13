#!/usr/bin/env python
##
#
#   DNAStrand
#
#   This file implements the class DNAStrand, simulating
#   parts of a DNA's bases sequence, with the main purpose
#   of checking matches between two different strands.
#
#   @author Júlia Mizarela (based on Professor Paulo Roma's work)
#   @since 16/03/2020
#
#
#   \mainpage DNAStrand.py: AD1 Programação com Interfaces Gráficas 2020.1
#
#   \section intro_sec Introduction
#
#   DNAStrand.py: AD1 Programação com Interfaces Gráficas 2020.1
#   Professor: Paulo Roma
#   Student: Júlia Mizarela de Oliveira Silva
#   Stundent's ID #: 19113050516
#
#   \section stwr Software
#
#   The following were used: PyCharm (IDE), TexWorks (LaTeX), unittest (testing),
#   and Doxygen (documentation)
#
#   \section ref References
#
#   The following were consulted:
#
#   https://docs.python.org/3/library/unittest.html
#
#   https://www.maths.tcd.ie/~dwilkins/LaTeXPrimer/
#
#   https://texfaq.org/FAQ-man-latex
#
#   https://pymotw.com/2/unittest/
#
#   http://opencdss.state.co.us/statemod/latest/doc-dev/project-init/doc-doxygen/
#
#   http://alesnosek.com/blog/2015/06/14/technical-documentation-with-doxygen/
#
#   http://www.doxygen.nl/manual/
#
#
#



import sys


class DNAStrand:
    ## Valid DNA symbols.
    symbols = 'ATCG'


    ## DNAStrand class constructor
    #
    # Constructs a DNAStrand with the given string of data,
    # normally consisting of multiple characters 'A', 'C', 'G', and 'T'.
    #
    # Raises a ValueError exception in case of an invalid givenData strand.
    #
    # @param givenData string of characters for this DNAStrand.
    #
    def __init__(self, givenData):
        ## Strand of this DNA, in upper case.
        self.strand = givenData.upper()
        if not self.isValid():
            raise ValueError("Invalid characters in Strand")


    ## Returns a string representing the strand data of this DNAStrand.
    def __str__(self):
        return self.strand


    ##
    # Returns a new DNAStrand that is the complement of this one,
    # that is, 'A' is replaced with 'T' and so on.
    #
    # @return complement of this DNA.
    #
    def createComplement(self):
        complementConversionTable = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        complement = ""
        i = 0
        while i < len(self.strand):
            complement += (complementConversionTable.get(self.strand[i]))
            i += 1
        return DNAStrand(complement)

    ##
    # Returns a string showing which characters in this strand are matched
    # with 'other', when shifted left by the given amount.
    # Simulates the movement of a second DNA strand relative to a fixed one,
    # comparing base (char) by base
    #
    # @param other given DNAStrand, that's is going to be "shifting".
    # @param shift number of positions to shift other strand to the left.
    # @return a copy of this strand, where matched characters remain upper
    # case and unmatched become lower case.
    #
    def findMatchesWithLeftShift(self, other, shift):
        matches = ""
        i = shift
        j = 0
        k = i
        l = len(self.strand)
        m = len(other.strand)
        while j < l:
            char1 = self.strand[j]
            if k < m:
                char2 = other.strand[k]
            else:
                char2 = ""
            if self.matches(char1, char2):
                matches += char1.upper()
            else:
                matches += char1.lower()
            k += 1
            j += 1
        return matches


    ##
    # Returns a string showing which characters in this strand are matched
    # with 'other', when shifted right by the given amount.
    # Simulates the movement of a second DNA strand relative to a fixed one,
    # comparing base (char) by base
    #
    # @param other given DNAStrand.
    # @param shift number of positions to shift other to the right.
    # @return a copy of this strand, where matched characters are upper case
    #         and unmatched, lower case.
    #
    def findMatchesWithRightShift(self, other, shift):
        matches = ""
        i = shift
        j = 0
        k = 0
        l = len(self.strand)
        m = len(other.strand)
        while j < l:
            char1 = self.strand[j]
            if i > j or k == m:
                char2 = ""
            else:
                char2 = other.strand[k]
                k +=1
            if self.matches(char1, char2):
                matches += char1
            else:
                matches += char1.lower()
            j += 1
        return matches


    ##
    # Returns the maximum possible number of matching base pairs,
    # when the given sequence is shifted left or right by any amount.
    #
    # @param other given DNAStrand to be matched with this one.
    # @return maximum number of matching pairs.
    #
    def findMaxPossibleMatches(self, other):
        maxPossibleLS = len(other.strand)
        maxPossibleRS = len(self.strand)
        maxMatchesL = 0
        maxMatchesR = 0
        ls = 0
        rs = 0
        while ls < maxPossibleLS:
            currenteLSMatches = self.countMatchesWithLeftShift(other, ls)
            maxMatchesL = max(currenteLSMatches, maxMatchesL)
            ls += 1
        while rs < maxPossibleRS:
            currenteRSMatches = self.countMatchesWithRightShift(other, rs)
            maxMatchesR = max(currenteRSMatches, maxMatchesR)
            rs += 1
        COUNT = 0
        side = "No matches found with either shifts"
        if maxMatchesL > maxMatchesR:
            side = "Max matches found with left shifts:"
            COUNT = maxMatchesL
        elif maxMatchesR > maxMatchesL:
            side = "Max matches found with right shifts:"
            COUNT = maxMatchesR
        elif maxMatchesR or maxMatchesL > 0:
            side = "Max matches (found on both shifted sides): "
            COUNT = maxMatchesL
        return COUNT

    ##
    # Returns the number of matching pairs,
    # when 'other' is shifted to the left by 'shift' positions.
    #
    # @param other given DNAStrand to match with this strand.
    # @param shift number of positions to shift other to the left.
    # @return number of matching pairs.
    #
    def countMatchesWithLeftShift(self, other, shift):
        COUNT = 0
        i = shift
        j = 0
        k = i
        l = len(self.strand)
        m = len(other.strand)
        while j < l:
            char1 = self.strand[j]
            if k < m:
                char2 = other.strand[k]
            else:
                char2 = ""
            if self.matches(char1, char2):
                COUNT += 1
            k += 1
            j += 1
        return COUNT


    ##
    # Returns the number of matching pairs,
    # when 'other' is shifted to the right by 'shift' positions.
    #
    # @param other given DNAStrand to be matched with this one.
    # @param shift number of positions to shift other to the right.
    # @return number of matching pairs.
    #
    def countMatchesWithRightShift(self, other, shift):
        COUNT = 0
        i = shift
        j = 0
        k = 0
        l = len(self.strand)
        m = len(other.strand)
        while j < l:
            char1 = self.strand[j]
            if i > j or k == m:
                char2 = ""
            else:
                char2 = other.strand[k]
                k +=1
            if self.matches(char1, char2):
                COUNT += 1
            j += 1
        return COUNT

    ##
    # Determines whether all characters in this strand
    # are valid ('A', 'G', 'C', or 'T').
    #
    # @return True if valid, and False otherwise.
    #
    def isValid(self):
        valid = True
        i = 0
        while i < len(self.strand):
            ch = self.strand[i]
            if ch not in DNAStrand.symbols:
                valid = False
            i += 1
        return valid

    ##
    # Counts the number of occurrences of the given character in this strand.
    #
    # @param ch given character.
    # @return number of occurrences of ch.
    #
    def letterCount(self, ch):
        count = 0
        for i in self.strand:
            if ch == i:
                count += 1
        return count

    ##
    # Returns True if the two characters form a base pair
    # ('A' with 'T' or 'C' with 'G').
    #
    # @param c1 first character.
    # @param c2 second character.
    # @return True if they form a base pair, and False otherwise.
    #
    def matches(self, c1, c2):
        match = False
        complementTable = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        if complementTable.get(c1) == c2:
            match = True
        return match


## Main program for testing.
 #
 # @param args two DNA strands.
 #
def main (args=None):

    if args is None:
       args = sys.argv

    if len(args) == 5:
       d = DNAStrand(args[1])
       d2 = DNAStrand(args[2])
       ls = int(args[3])
       rs = int(args[4])
    else:
       d = DNAStrand ("AGAGCAT")
       d2 = DNAStrand ("TCAT")
       ls = 2
       rs = 3

    print("Complement: %s" % d.createComplement())
    print("Count A in %s: %d" % (d, d.letterCount('A')))
    print("%s isValid: %r" % (d, d.isValid()))
    print("Strand: %s" % d2)
    print("RightShift: %s, %d = %s" % (d, rs, d2.findMatchesWithRightShift(d,rs)))
    print("Left Shift: %s, %d = %s" % (d, ls, d2.findMatchesWithLeftShift(d,ls)))
    print("Maximum Matches: %d" % d.findMaxPossibleMatches(d2))
    print("Number of matches left shift: %s, %d = %s" % (d2, ls+rs, d.countMatchesWithLeftShift(d2,ls+rs)))

if __name__ == "__main__":
   sys.exit(main())