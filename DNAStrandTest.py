#!/usr/bin/env python
#
## @package DNAStrandTest
#
#   Class for testing the DNA strand matching.
#
#   AD1 Programação com Interfaces Gráficas 2020.1
#   Professor: Paulo Roma
#
#   @author Júlia Mizarela (based on Professor Paulo Roma's work)
#   @since 16/03/2020
#


from DNAStrand import DNAStrand
import unittest, sys


    ## DNAStrandClass Unittest
    # Class for testing all the methods of DNAStrand class.
    #
class DNAStrandClass(unittest.TestCase):

    ##
    # Prepares four strings for the subsequent tests
    #
    def setUp(self):
        # First couple of strands for the tests
        #
        self.f = DNAStrand("GAG")
        # First strand
        self.m = DNAStrand("act")
        # Other strand
        self.a1 = DNAStrand("TcAt")
        # Alternative strand 1
        self.a2 = DNAStrand("AGAGCAT")
        # Alternative strand 2

        # Two possible left shifts for m or f
        #
        self.ls0 = 0
        self.ls1 = 1
        self.ls2 = 2

        # Two possible right shifts for m or f
        #
        self.rs0 = 0
        self.rs1 = 1
        self.rs2 = 2

        # Possible left shifts with a1 fixed and a2 moving
        #
        self.a2ls0 = 0
        self.a2ls1 = 1
        self.a2ls2 = 2
        self.a2ls3 = 3
        self.a2ls4 = 4
        self.a2ls5 = 5
        self.a2ls6 = 6

        # Possible right shifts with a1 fixed and a2 moving
        #
        self.a2rs0 = 0
        self.a2rs1 = 1
        self.a2rs2 = 2
        self.a2rs3 = 3

        # Possible right shifts with a2 fixed and a1 moving
        #
        self.a1rs0 = 0
        self.a1rs1 = 1
        self.a1rs2 = 2
        self.a1rs3 = 3
        self.a1rs4 = 4
        self.a1rs5 = 5
        self.a1rs6 = 6

        # Possible left shifts with a1 fixed and a2 moving
        #
        self.a1ls0 = 0
        self.a1ls1 = 1
        self.a1ls2 = 2
        self.a1ls3 = 3


    ##
    # Testing of isValid
    #
    def test_isValid(self):
        mT = "isValid method should return TRUE"
        self.assertTrue(self.f.isValid(), mT + "for " + str(self.f) + "\n")
        self.assertTrue(self.m.isValid(), mT + "for " + str(self.m) + "\n")
        self.assertTrue(self.a1.isValid(), mT + "for " + str(self.a1) + "\n")
        self.assertTrue(self.a2.isValid(), mT + "for " + str(self.a2) + "\n")
        mE = "isValid method should return adequate boolean for"
        self.assertEqual(self.f.isValid(), True, mE + str(self.f)+"\n")
        self.assertEqual(self.m.isValid(), True, mE + str(self.m) + "\n")
        self.assertEqual(self.a1.isValid(), True, mE + str(self.m) + "\n")
        self.assertEqual(self.a2.isValid(), True, mE + str(self.m) + "\n")


    ##
    # Testing of createComplement
    #
    def test_createComplement(self):
        mE = "createComplement method should return "
        self.assertEqual(str(self.f.createComplement()), 'CTC', mE + "CTC" + " for " + str(self.f)+"\n")
        self.assertEqual(str(self.m.createComplement()), 'TGA', mE + "TGA" + " for " + str(self.m)+"\n")
        self.assertEqual(str(self.a1.createComplement()), 'AGTA', mE + "AGTA" + " for " + str(self.a1)+"\n")
        self.assertEqual(str(self.a2.createComplement()), 'TCTCGTA', mE + "TCTCGTA" + " for " + str(self.a2)+"\n")


    ##
    # Testing of countMatchesWithLeftShift
    #
    def test_countMatchesWithLeftShift(self):
        mT = "countMatchesWithLeftShift method should return "
        self.assertEqual(int(self.f.countMatchesWithLeftShift(self.m, self.ls0)), 0, mT + "0 matches" + " for " + "left shift = " + str(self.ls0) + "\n")
        self.assertEqual(int(self.f.countMatchesWithLeftShift(self.m, self.ls1)), 2, mT + "2 matches" + " for " + "left shift = " + str(self.ls1) + "\n")
        self.assertEqual(int(self.f.countMatchesWithLeftShift(self.m, self.ls2)), 0, mT + "0 matches" + " for " + "left shift = " + str(self.ls2) + "\n")
        self.assertEqual(int(self.m.countMatchesWithLeftShift(self.f, self.ls0)), 0, mT + "0 matches" + " for " + "left shift = " + str(self.ls0) + "\n")
        self.assertEqual(int(self.m.countMatchesWithLeftShift(self.f, self.ls1)), 1, mT + "1 matches" + " for " + "left shift = " + str(self.ls1) + "\n")
        self.assertEqual(int(self.m.countMatchesWithLeftShift(self.f, self.ls2)), 0, mT + "0 matches" + " for " + "left shift = " + str(self.ls2) + "\n")
    # Further testing
        self.assertEqual(int(self.a1.countMatchesWithLeftShift(self.a2, self.a2ls0)), 2, mT + "2 matches" + " for " + "left shift = " + str(self.a2ls0) + "\n")
        self.assertEqual(int(self.a1.countMatchesWithLeftShift(self.a2, self.a2ls1)), 0, mT + "0 matches" + " for " + "left shift = " + str(self.a2ls1) + "\n")
        self.assertEqual(int(self.a1.countMatchesWithLeftShift(self.a2, self.a2ls2)), 3, mT + "3 matches" + " for " + "left shift = " + str(self.a2ls2) + "\n")
        self.assertEqual(int(self.a1.countMatchesWithLeftShift(self.a2, self.a2ls3)), 0, mT + "0 matches" + " for " + "left shift = " + str(self.a2ls3) + "\n")
        self.assertEqual(int(self.a1.countMatchesWithLeftShift(self.a2, self.a2ls4)), 1, mT + "1 matches" + " for " + "left shift = " + str(self.a2ls4) + "\n")
        self.assertEqual(int(self.a1.countMatchesWithLeftShift(self.a2, self.a2ls5)), 1, mT + "1 matches" + " for " + "left shift = " + str(self.a2ls5) + "\n")
        self.assertEqual(int(self.a1.countMatchesWithLeftShift(self.a2, self.a2ls6)), 0, mT + "0 matches" + " for " + "left shift = " + str(self.a2ls6) + "\n")
        self.assertEqual(int(self.a2.countMatchesWithLeftShift(self.a1, self.a1ls0)), 2, mT + "2 matches" + " for " + "left shift = " + str(self.a1ls0) + "\n")
        self.assertEqual(int(self.a2.countMatchesWithLeftShift(self.a1, self.a1ls1)), 1, mT + "1 matches" + " for " + "left shift = " + str(self.a1ls1) + "\n")
        self.assertEqual(int(self.a2.countMatchesWithLeftShift(self.a1, self.a1ls2)), 0, mT + "0 matches" + " for " + "left shift = " + str(self.a1ls2) + "\n")
        self.assertEqual(int(self.a2.countMatchesWithLeftShift(self.a1, self.a1ls3)), 1, mT + "1 matches" + " for " + "left shift = " + str(self.a1ls3) + "\n")


    ##
    # Testing of findMatchesWithLeftShift
    #
    def test_findMatchesWithLeftShift(self):
        mT = "findMatchesWithLeftShift method should return "
        self.assertEqual(str(self.f.findMatchesWithLeftShift(self.m, self.ls0)), "gag", mT + "gag" + " for " + "left shift = " + str(self.ls0) + "\n")
        self.assertEqual(str(self.f.findMatchesWithLeftShift(self.m, self.ls1)), "GAg", mT + "GAg" + " for " + "left shift = " + str(self.ls1) + "\n")
        self.assertEqual(str(self.f.findMatchesWithLeftShift(self.m, self.ls2)), "gag", mT + "gag" + " for " + "left shift = " + str(self.ls2) + "\n")
        self.assertEqual(str(self.m.findMatchesWithLeftShift(self.f, self.ls0)), "act", mT + "act" + " for " + "left shift = " + str(self.ls0) + "\n")
        self.assertEqual(str(self.m.findMatchesWithLeftShift(self.f, self.ls1)), "aCt", mT + "aCt" + " for " + "left shift = " + str(self.ls1) + "\n")
        self.assertEqual(str(self.m.findMatchesWithLeftShift(self.f, self.ls2)), "act", mT + "act" + " for " + "left shift = " + str(self.ls2) + "\n")
    # Further testing
        self.assertEqual(str(self.a1.findMatchesWithLeftShift(self.a2, self.a2ls0)), "TCat", mT + "TCat" + " for " + "left shift = " + str(self.a2ls0) + "\n")
        self.assertEqual(str(self.a1.findMatchesWithLeftShift(self.a2, self.a2ls1)), "tcat", mT + "tcat" + " for " + "left shift = " + str(self.a2ls1) + "\n")
        self.assertEqual(str(self.a1.findMatchesWithLeftShift(self.a2, self.a2ls2)), "TCaT", mT + "TCaT" + " for " + "left shift = " + str(self.a2ls2) + "\n")
        self.assertEqual(str(self.a1.findMatchesWithLeftShift(self.a2, self.a2ls3)), "tcat", mT + "tcat" + " for " + "left shift = " + str(self.a2ls3) + "\n")
        self.assertEqual(str(self.a1.findMatchesWithLeftShift(self.a2, self.a2ls4)), "tcAt", mT + "tcAt" + " for " + "left shift = " + str(self.a2ls4) + "\n")
        self.assertEqual(str(self.a1.findMatchesWithLeftShift(self.a2, self.a2ls5)), "Tcat", mT + "Tcat" + " for " + "left shift = " + str(self.a2ls5) + "\n")
        self.assertEqual(str(self.a1.findMatchesWithLeftShift(self.a2, self.a2ls6)), "tcat", mT + "tcat" + " for " + "left shift = " + str(self.a2ls6) + "\n")
        self.assertEqual(str(self.a2.findMatchesWithLeftShift(self.a1, self.a1ls0)), "AGagcat", mT + "AGagcat" + " for " + "left shift = " + str(self.a1ls0) + "\n")
        self.assertEqual(str(self.a2.findMatchesWithLeftShift(self.a1, self.a1ls1)), "agAgcat", mT + "agAgcat" + " for " + "left shift = " + str(self.a1ls1) + "\n")
        self.assertEqual(str(self.a2.findMatchesWithLeftShift(self.a1, self.a1ls2)), "agagcat", mT + "agagcat" + " for " + "left shift = " + str(self.a1ls2) + "\n")
        self.assertEqual(str(self.a2.findMatchesWithLeftShift(self.a1, self.a1ls3)), "Agagcat", mT + "Agagcat" + " for " + "left shift = " + str(self.a1ls3) + "\n")


    ##
    # Testing of countMatchesWithRightShift
    #
    def test_countMatchesWithRightShift(self):
        mT = "countMatchesWithRightShift method should return "
        self.assertEqual(int(self.f.countMatchesWithRightShift(self.m, self.rs0)), 0, mT + "0 matches" + " for " + "right shift = " + str(self.rs0) + "\n")
        self.assertEqual(int(self.f.countMatchesWithRightShift(self.m, self.rs1)), 1, mT + "1 matches" + " for " + "right shift = " + str(self.rs1) + "\n")
        self.assertEqual(int(self.f.countMatchesWithRightShift(self.m, self.rs2)), 0, mT + "0 matches" + " for " + "right shift = " + str(self.rs2) + "\n")
        self.assertEqual(int(self.m.countMatchesWithRightShift(self.f, self.rs0)), 0, mT + "0 matches" + " for " + "right shift = " + str(self.rs0) + "\n")
        self.assertEqual(int(self.m.countMatchesWithRightShift(self.f, self.rs1)), 2, mT + "2 matches" + " for " + "right shift = " + str(self.rs1) + "\n")
        self.assertEqual(int(self.m.countMatchesWithRightShift(self.f, self.rs2)), 0, mT + "0 matches" + " for " + "right shift = " + str(self.rs2) + "\n")
    # Further testing
        self.assertEqual(int(self.a1.countMatchesWithRightShift(self.a2, self.a2rs0)), 2, mT + "2 matches" + " for " + "right shift = " + str(self.a2rs0) + "\n")
        self.assertEqual(int(self.a1.countMatchesWithRightShift(self.a2, self.a2rs1)), 1, mT + "1 matches" + " for " + "right shift = " + str(self.a2rs1) + "\n")
        self.assertEqual(int(self.a1.countMatchesWithRightShift(self.a2, self.a2rs2)), 0, mT + "0 matches" + " for " + "right shift = " + str(self.a2rs2) + "\n")
        self.assertEqual(int(self.a1.countMatchesWithRightShift(self.a2, self.a2rs3)), 1, mT + "1 matches" + " for " + "right shift = " + str(self.a2rs3) + "\n")
        self.assertEqual(int(self.a2.countMatchesWithRightShift(self.a1, self.a1rs0)), 2, mT + "2 matches" + " for " + "right shift = " + str(self.a1rs0) + "\n")
        self.assertEqual(int(self.a2.countMatchesWithRightShift(self.a1, self.a1rs1)), 0, mT + "0 matches" + " for " + "right shift = " + str(self.a1rs1) + "\n")
        self.assertEqual(int(self.a2.countMatchesWithRightShift(self.a1, self.a1rs2)), 3, mT + "3 matches" + " for " + "right shift = " + str(self.a1rs2) + "\n")
        self.assertEqual(int(self.a2.countMatchesWithRightShift(self.a1, self.a1rs3)), 0, mT + "0 matches" + " for " + "right shift = " + str(self.a1rs3) + "\n")
        self.assertEqual(int(self.a2.countMatchesWithRightShift(self.a1, self.a1rs4)), 1, mT + "1 matches" + " for " + "right shift = " + str(self.a1rs4) + "\n")
        self.assertEqual(int(self.a2.countMatchesWithRightShift(self.a1, self.a1rs5)), 1, mT + "1 matches" + " for " + "right shift = " + str(self.a1rs5) + "\n")
        self.assertEqual(int(self.a2.countMatchesWithRightShift(self.a1, self.a1rs6)), 0, mT + "0 matches" + " for " + "right shift = " + str(self.a1rs6) + "\n")


    ##
    # Testing of findMatchesWithRightShift
    #
    def test_findMatchesWithRightShift(self):
        mT = "findMatchesWithRightShift method should return "
        self.assertEqual(str(self.f.findMatchesWithRightShift(self.m, self.rs0)), "gag", mT + "gag" + " for " + "right shift = " + str(self.rs0) + "\n")
        self.assertEqual(str(self.f.findMatchesWithRightShift(self.m, self.rs1)), "gaG", mT + "gaG" + " for " + "right shift = " + str(self.rs1) + "\n")
        self.assertEqual(str(self.f.findMatchesWithRightShift(self.m, self.rs2)), "gag", mT + "gag" + " for " + "right shift = " + str(self.rs2) + "\n")
        self.assertEqual(str(self.m.findMatchesWithRightShift(self.f, self.rs0)), "act", mT + "act" + " for " + "right shift = " + str(self.rs0) + "\n")
        self.assertEqual(str(self.m.findMatchesWithRightShift(self.f, self.rs1)), "aCT", mT + "aCT" + " for " + "right shift = " + str(self.rs1) + "\n")
        self.assertEqual(str(self.m.findMatchesWithRightShift(self.f, self.rs2)), "act", mT + "act" + " for " + "right shift = " + str(self.rs2) + "\n")
    # Further testing
        self.assertEqual(str(self.a1.findMatchesWithRightShift(self.a2, self.a2rs0)), "TCat", mT + "TCat" + " for " + "right shift = " + str(self.a2rs0) + "\n")
        self.assertEqual(str(self.a1.findMatchesWithRightShift(self.a2, self.a2rs1)), "tcaT", mT + "tcaT" + " for " + "right shift = " + str(self.a2rs1) + "\n")
        self.assertEqual(str(self.a1.findMatchesWithRightShift(self.a2, self.a2rs2)), "tcat", mT + "tcat" + " for " + "right shift = " + str(self.a2rs2) + "\n")
        self.assertEqual(str(self.a1.findMatchesWithRightShift(self.a2, self.a2rs3)), "tcaT", mT + "tcaT" + " for " + "right shift = " + str(self.a2rs3) + "\n")
        self.assertEqual(str(self.a2.findMatchesWithRightShift(self.a1, self.a1rs0)), "AGagcat", mT + "AGagcat" + " for " + "right shift = " + str(self.a1rs0) + "\n")
        self.assertEqual(str(self.a2.findMatchesWithRightShift(self.a1, self.a1rs1)), "agagcat", mT + "agagcat" + " for " + "right shift = " + str(self.a1rs1) + "\n")
        self.assertEqual(str(self.a2.findMatchesWithRightShift(self.a1, self.a1rs2)), "agAGcAt", mT + "agAGcAt" + " for " + "right shift = " + str(self.a1rs2) + "\n")
        self.assertEqual(str(self.a2.findMatchesWithRightShift(self.a1, self.a1rs3)), "agagcat", mT + "agagcat" + " for " + "right shift = " + str(self.a1rs3) + "\n")
        self.assertEqual(str(self.a2.findMatchesWithRightShift(self.a1, self.a1rs4)), "agagcaT", mT + "agagcaT" + " for " + "right shift = " + str(self.a1rs4) + "\n")
        self.assertEqual(str(self.a2.findMatchesWithRightShift(self.a1, self.a1rs5)), "agagcAt", mT + "agagcAt" + " for " + "right shift = " + str(self.a1rs5) + "\n")
        self.assertEqual(str(self.a2.findMatchesWithRightShift(self.a1, self.a1rs6)), "agagcat", mT + "agagcat" + " for " + "right shift = " + str(self.a1rs6) + "\n")


    ## Testing of findMaxPossibleMatches
    #
    def test_findMaxPossibleMatches(self):
        mT = "findMaxPossibleMatches should return "
        self.assertEqual(int(self.f.findMaxPossibleMatches(self.m)), 2, mT + "2 matches between " + str(self.f) + " and " + str(self.m) + "\n")
        self.assertEqual(int(self.f.findMaxPossibleMatches(self.a1)), 2, mT + "2 matches between " + str(self.f) + " and " + str(self.a1) + "\n")
        self.assertEqual(int(self.f.findMaxPossibleMatches(self.a2)), 1, mT + "1 match between " + str(self.f) + " and " + str(self.a2) + "\n")
        self.assertEqual(int(self.m.findMaxPossibleMatches(self.f)), 2, mT + "2 matches between " + str(self.m) + " and " + str(self.f) + "\n")
        self.assertEqual(int(self.m.findMaxPossibleMatches(self.a1)), 2, mT + "2 matches between " + str(self.m) + " and " + str(self.a1) + "\n")
        self.assertEqual(int(self.m.findMaxPossibleMatches(self.a2)), 2, mT + "2 matches between " + str(self.m) + " and " + str(self.a2) + "\n")
        self.assertEqual(int(self.a1.findMaxPossibleMatches(self.a2)), 3, mT + "2 matches between " + str(self.a1) + " and " + str(self.a2) + "\n")
        self.assertEqual(int(self.a2.findMaxPossibleMatches(self.a1)), 3, mT + "2 matches between " + str(self.a2) + " and " + str(self.a1) + "\n")



    ## Testing of letterCount
    #
    def test_letterCount(self):
        mt = "letterCount should return "
        self.assertEqual(int(self.f.letterCount("A")), 1, mt + "for letter A in " + str(self.f) + "\n")
        self.assertEqual(int(self.f.letterCount("C")), 0, mt + "for letter C in " + str(self.f) + "\n")
        self.assertEqual(int(self.f.letterCount("G")), 2, mt + "for letter G in " + str(self.f) + "\n")
        self.assertEqual(int(self.f.letterCount("T")), 0, mt + "for letter T in " + str(self.f) + "\n")
        self.assertEqual(int(self.m.letterCount("A")), 1, mt + "for letter A in " + str(self.m) + "\n")
        self.assertEqual(int(self.m.letterCount("C")), 1, mt + "for letter C in " + str(self.m) + "\n")
        self.assertEqual(int(self.m.letterCount("G")), 0, mt + "for letter G in " + str(self.m) + "\n")
        self.assertEqual(int(self.m.letterCount("T")), 1, mt + "for letter T in " + str(self.m) + "\n")
        self.assertEqual(int(self.a1.letterCount("A")), 1, mt + "for letter A in " + str(self.a1) + "\n")
        self.assertEqual(int(self.a1.letterCount("C")), 1, mt + "for letter C in " + str(self.a1) + "\n")
        self.assertEqual(int(self.a1.letterCount("G")), 0, mt + "for letter G in " + str(self.a1) + "\n")
        self.assertEqual(int(self.a1.letterCount("T")), 2, mt + "for letter T in " + str(self.a1) + "\n")
        self.assertEqual(int(self.a2.letterCount("A")), 3, mt + "for letter A in " + str(self.a2) + "\n")
        self.assertEqual(int(self.a2.letterCount("C")), 1, mt + "for letter C in " + str(self.a2) + "\n")
        self.assertEqual(int(self.a2.letterCount("G")), 2, mt + "for letter G in " + str(self.a2) + "\n")
        self.assertEqual(int(self.a2.letterCount("T")), 1, mt + "for letter T in " + str(self.a2) + "\n")


    ## Testing of matches
    #
    def test_matches(self):
        mT = "matches should return "
        self.assertEqual(self.f.matches("A", "T"), True, mT + "True for " + "A and T" + "\n")
        self.assertEqual(self.f.matches("T", "A"), True, mT + "True for " + "T and A" + "\n")
        self.assertEqual(self.f.matches("C", "G"), True, mT + "True for " + "C and G" + "\n")
        self.assertEqual(self.f.matches("G", "C"), True, mT + "True for " + "G and C" + "\n")
        self.assertEqual(self.f.matches("A", "A"), False, mT + "False for " + "A and A" + "\n")
        self.assertEqual(self.f.matches("A", "C"), False, mT + "False for " + "A and C" + "\n")
        self.assertEqual(self.f.matches("A", "G"), False, mT + "False for " + "A and G" + "\n")
        self.assertEqual(self.f.matches("C", "A"), False, mT + "False for " + "C and A" + "\n")
        self.assertEqual(self.f.matches("C", "C"), False, mT + "False for " + "C and C" + "\n")
        self.assertEqual(self.f.matches("C", "T"), False, mT + "False for " + "C and T" + "\n")
        self.assertEqual(self.f.matches("G", "A"), False, mT + "False for " + "G and A" + "\n")
        self.assertEqual(self.f.matches("G", "G"), False, mT + "False for " + "G and C" + "\n")
        self.assertEqual(self.f.matches("G", "T"), False, mT + "False for " + "G and T" + "\n")
        self.assertEqual(self.f.matches("T", "C"), False, mT + "False for " + "T and C" + "\n")
        self.assertEqual(self.f.matches("T", "G"), False, mT + "False for " + "T and G" + "\n")
        self.assertEqual(self.f.matches("T", "T"), False, mT + "False for " + "T and T" + "\n")
        self.assertEqual(self.f.matches("A", ""), False, mT + "False for " + "A and Empty" + "\n")
        self.assertEqual(self.f.matches("C", ""), False, mT + "False for " + "C and Empty" + "\n")
        self.assertEqual(self.f.matches("G", ""), False, mT + "False for " + "G and Empty" + "\n")
        self.assertEqual(self.f.matches("T", ""), False, mT + "False for " + "T and Empty" + "\n")





## Main program for testing.
 #
 # @param args two DNA strands.
 #
def main (args = None):
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

if __name__ == '__main__':
    unittest.main()

if __name__ == "__main__":
   sys.exit(main())