#!/usr/bin/env python

# Adjacency Matrix
G = [[0, 1, 0],[1, 0, 1],[0, 1, 0]]

# Consensus Functions

def max_consensus(x):
#        print 'you have chosen max consensus'
	out = max(x)
        return out

def logical_consensus(x):
	out = any(x)
        return out


consensus_dict = {
  'max': max_consensus,
  'bool': logical_consensus,
}
