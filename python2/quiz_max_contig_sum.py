def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE

    
    #wikipedia
    max_ending_here = max_so_far = 0
    for x in L:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

    '''
    in the list [3, 4, -1, 5, -4], the maximum sum is 3+4-1+5 = 11
    in the list [3, 4, -8, 15, -1, 2], the maximum sum is 15-1+2 = 16
    '''
    #brute force sum
    '''def partitions(set_):
        if not set_:
            yield []
            return
        for i in range(2**len(set_)//2):
            parts = [set(), set()]
            for item in set_:
                parts[i&1].add(item)
                i >>= 1
            for b in partitions(parts[1]):
                yield [parts[0]]+b
                '''


# This is a helper function that will fetch all of the available 
# partitions for you to use for your brute force algorithm.
    '''def get_partitions(set_):
        for partition in partitions(set_):
            yield [list(elt) for elt in partition]'''
    '''
    def get_partitions(set_):
        yield 

    max_sum=0
    for item in (get_partitions(L)):
         print(item)
         for x in item:
             #print(x)
             if sum(x) >= max_sum:
                 max_sum=sum(x)
    return max_sum
'''
    

print(max_contig_sum([3, 4, -1, 5, -4]))
print(max_contig_sum([3, 4, -8, 15, -1, 2]))    
