import sys
import timeit

from superSearch import SuperSearch

if len(sys.argv) != 2:
    print("Please provide text file name to use as a source of keywords.")

searchObject = SuperSearch(sys.argv[1])

start_time = timeit.default_timer()
searchObject.loadKeywords()
elapsed = timeit.default_timer() - start_time
print(elapsed)

h = input("Enter the word to search: ")
while h:
    start_time = timeit.default_timer()
    print(h + " " + searchObject.search(h))
    elapsed = timeit.default_timer() - start_time
    print(elapsed)

    h = input("Enter the word to search: ")
