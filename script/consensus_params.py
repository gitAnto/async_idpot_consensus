#!/usr/bin/env python

# Adjacency Matrix
G = [[0, 1, 0],[1, 0, 1],[0, 1, 0]]

# Consensus Functions

def max_consensus(x):
	out = max(x)

def logical_consensus(x):
	out = any(x)

funcdict = {
  'max': max_consensus,
  'bool': logical_consensus,
}