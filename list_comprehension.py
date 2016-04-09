all_data = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
            ['Susie', 'Casey', 'Jill', 'Ana', 'Eva', 'Jennifer', 'Stephanie']]

# how long is each name?
name_length = [len(name) for gender in all_data for name in gender]

# print all names in one list
single_list = [name for gender in all_data for name in gender]

# dict
dict_comprehension = {name[0]: [name for name in single_list]}


# Do some testing
seq1 = ['foo', 'bar', 'baz', 'baz']
seq2 = ['bar', 'dud', 'shit', 'piss']

seqed = zip(seq1, seq2)
dict_zipped = dict(seqed)
