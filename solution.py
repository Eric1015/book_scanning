import numpy as np
import csv

fileName = "a_example.csv"
A = np.array(list(csv.reader(open(fileName) )))
A1 = np.loadtxt(A[(0,)], delimiter=' ')
A2 = np.loadtxt(A[(1,)], delimiter=' ')

info = A1
# first line
numTotalBooks = info[0].astype(int)
numLibraries = info[1].astype(int)
totalDays = info[2].astype(int)

# second line
bookList = A2.astype(int)

# read libraries from here
index = 2
while ((libInfo = np.loadtxt(A[(index,)], delimiter=' ')) != null)
    numBooks = libInfo[0].astype(int)
    daysToSignUp = libInfo[1].astype(int)
    shipCapacity = libInfo[2].astype(int)
    books = np.loadtxt(A[(index,)], delimiter=' ').astype(int)


for lib in libraries:
    

# given the books of the library and its information, return the total maximum possible score
def get_poss_score_of_lib(library):
    total_bks = library.shipCapacity * (D - library.daysToSignUp)
    sub_books = library.books[0:min(len(library.books), total_bks)]
    return np.sum(sub_books)


class Library:
    def __init__(self, numBooks, daysToSignUp, shipCapacity, books, booksIdx):
        self.numBooks = numBooks #int
        self.daysToSignUp = daysToSignUp #int
        self.shipCapacity = shipCapacity #int
        self.books = books # list of int
        self.booksIdx = booksIdx
        self.isSignedUp = False


def calculateScores(libraries):
    scores = []
    daysEllapsedForSignUp = 0
    libraryNumCount = 0
    library = libraries[libraryNumCount]
    for day in range(D):
        daysEllapsedForSignUp+=1
        if (library.daysToSignUp == daysEllapsedForSignUp):
            library.isSignedUp = True
            daysEllapsedForSignUp = 0
            library = library
        
        
    # for library in libraries:
    #     score = 0
    #     if (library.isSignedUp)
    #         for i in range(library.shipCapacity):
    