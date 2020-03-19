import csv
from collections import Counter
from collections import defaultdict


# a member is an object with a string "name" and a list of strings "interests"
class Member:
    def __init__(self, name):
        self.name = name
        self.interests = []


interest_words= []
members= []

# this part creates a list of members
with open('test.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    reader.next()
    for row in reader:
        del row[17] #delete photo link string
        del row[7:11] #delete looking for, siblings, match gender, self gender
        del row[4:6] #delete affiliation and grade
        del row[:2] #delete timestamp and email address
        new_member = Member(row[0])
        del row[0]
        # print new_member.name
        for cell in row:
            interest_words = cell.split(" ")
            for i in interest_words:
                new_member.interests.append(i)
        set(new_member.interests)
        members.append(new_member)

# this part adds all of the strings in everyone's interests to a giant list to sort out popular ones
for member in members:
    for interest in member.interests:
        interest_words.append(interest)
words_counted = []
for i in interest_words:
    x = interest_words.count(i)
    words_counted.append((x,i))
words_counted = sorted(set(words_counted), reverse=True)
# some more needs to be done here to actually narrow down interests:
# remove case-sensitivity, punctuation, articles, pronouns, conjunctions, prepositions, whatever else
# (or we could just pick some out by looking ourselves lol)

# this writes the list to a csv file
with open('output.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(words_counted)

# now put the members in a dictionary so you can look up names based on the interests
# totally copied from here https://stackoverflow.com/questions/6091549/efficient-data-structure-of-objects-in-python-for-lookup-based-on-any-object-mem
# >>> from collections import defaultdict
# >>> collection = [(1, 200, 9),
# ...               (2, 300, 8),
# ...               (3, 400, 7)]
# >>> keyed_dict = defaultdict(list)
# >>> for tup in collection:
# ...     for i, e in enumerate(tup):
# ...         keyed_dict[(i, e)].append(tup)