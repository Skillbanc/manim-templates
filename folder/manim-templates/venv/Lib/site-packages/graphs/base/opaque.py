from __future__ import absolute_import
import copy
import numpy as np
import scipy.sparse as ss
import warnings
from collections import namedtuple, defaultdict

from .base import Graph

_UnweightedAdj = namedtuple('_UnweightedAdj', ('idx'))
_WeightedAdj = namedtuple('_WeightedAdj', ('idx', 'weight'))


class AdjacencyListGraph(Graph):

  def num_vertices(self):
    return len(self._adj_list)

  def num_edges(self):
    return sum(len(nbrs) for nbrs in self._adj_list)

  def copy(self):
    return self.__class__(copy.deepcopy(self._adj_list))

  def subgraph(self, mask):
    sub_v = np.arange(self.num_vertices())[mask]
    return self.__class__([self._adj_list[i] for i in sub_v])

  def adj_list(self):
    for nbrs in self._adj_list:
      yield [n.idx for n in nbrs]

  def pairs(self, copy=False, directed=True):
    pairs = []
    for i, nbrs in enumerate(self._adj_list):
      for n in nbrs:
        if directed or i <= n.idx:
          pairs.append((i, n.idx))
    return np.array(pairs, dtype=int)

  def matrix(self, *formats, **kwargs):
    kwargs.pop('copy', False)
    if kwargs:
      raise ValueError('Unexpected kwargs for matrix(): %s' % kwargs)
    adj = self._to_csr()
    if not formats or 'csr' in formats:
      return adj
    for fmt in formats:
      if fmt != 'dense':
        return adj.asformat(fmt)
    if 'dense' in formats:
      return adj.toarray()
    raise NotImplementedError('Unknown matrix format(s): %s' % (formats,))

  subgraph.__doc__ = Graph.subgraph.__doc__
  adj_list.__doc__ = Graph.adj_list.__doc__
  pairs.__doc__ = Graph.pairs.__doc__
  matrix.__doc__ = Graph.matrix.__doc__

  def symmetrize(self, method='sum', copy=False):
    '''Symmetrizes with the given method. {sum,max,avg}
    Returns a copy if copy=True.'''
    raise NotImplementedError()

  def remove_edges(self, from_idx, to_idx, symmetric=False, copy=False):
    '''Removes all from->to edges, without making sure they already exist.
    If symmetric=True, also removes to->from edges.'''
    raise NotImplementedError()


class UnweightedAdjacencyListGraph(Graph):

  def __init__(self, adj_list):
    '''adj_list: list of lists of integers representing edge connections'''
    self._adj_list = [list(map(_UnweightedAdj, nbrs)) for nbrs in adj_list]

  def is_weighted(self):
    return False

  def degree(self, kind='out', weighted=True):
    d = np.zeros(self.num_vertices(), dtype=int)
    if kind == 'out':
      for i, nbrs in enumerate(self._adj_list):
        d[i] = len(nbrs)
    else:
      for nbrs in self._adj_list:
        for n in nbrs:
          d[n.idx] += 1
    return d

  def add_edges(self, from_idx, to_idx, weight=None, symmetric=False,
                copy=False):
    if weight is not None:
      warnings.warn('Cannot supply weights for unweighted graph; '
                    'ignoring weight argument')
    to_add = defaultdict(set)
    if hasattr(from_idx, '__len__'):
      for i, j in zip(from_idx, to_idx):
        to_add[i].add(j)
        if symmetric:
          to_add[j].add(i)
    else:
      to_add[from_idx].add(to_idx)
      if symmetric:
        to_add[to_idx].add(from_idx)

    res = self.copy() if copy else self
    for i in to_add:
      nbrs = res._adj_list[i]
      edges = to_add[i]
      edges.update(n.idx for n in nbrs)
      nbrs[:] = list(map(_UnweightedAdj, sorted(edges)))
    return res

  def _to_csr(self):
    indices, indptr = [], [0]
    for i, nbrs in enumerate(self.adj_list):
      indptr.append(len(nbrs) + indptr[-1])
      indices.extend(n.idx for n in nbrs)
    return ss.csr_matrix((np.ones(len(indices)), indices, indptr))

  is_weighted.__doc__ = Graph.is_weighted.__doc__
  degree.__doc__ = Graph.degree.__doc__
  add_edges.__doc__ = Graph.add_edges.__doc__


class WeightedAdjacencyListGraph(Graph):

  def __init__(self, weighted_adj_list):
    '''adj_list: list of lists of (edge,weight) tuples'''
    self._adj_list = [[_WeightedAdj(v,w) for v,w in nbrs]
                      for nbrs in weighted_adj_list]

  def is_weighted(self):
    return True

  def edge_weights(self, copy=False, directed=True):
    weights = []
    for i, nbrs in enumerate(self._adj_list):
      for n in nbrs:
        if directed or i <= n.idx:
          weights.append(n.weight)
    return np.array(weights, dtype=float)

  def degree(self, kind='out', weighted=True):
    if not weighted:
      return UnweightedAdjacencyListGraph.degree(self, kind=kind)
    d = np.zeros(self.num_vertices())
    if kind == 'out':
      for i, nbrs in enumerate(self._adj_list):
        d[i] = sum(n.weight for n in nbrs)
    else:
      for nbrs in self._adj_list:
        for n in nbrs:
          d[n.idx] += n.weight
    return d

  def add_edges(self, from_idx, to_idx, weight=1, symmetric=False, copy=False):
    from_idx, to_idx = np.atleast_1d(from_idx, to_idx)
    weight = 1 if weight is None else weight
    from_idx, to_idx, weight = np.broadcast_arrays(from_idx, to_idx, weight)

    res = self.copy() if copy else self
    for s, t, w in zip(from_idx, to_idx, weight):
      nbrs = res._adj_list[s]
      # TODO
    return res

  def _to_csr(self):
    data, indices, indptr = [], [0]
    for i, nbrs in enumerate(self.adj_list):
      indptr.append(len(nbrs) + indptr[-1])
      for n in nbrs:
        indices.append(n.idx)
        data.append(n.weight)
    return ss.csr_matrix((data, indices, indptr))

  def _update_edges(self, weights, copy=False):
    res = self.copy() if copy else self
    widx = 0
    for nbrs in res._adj_list:
      for i, n in enumerate(nbrs):
        nbrs[i] = _WeightedAdj(n.idx, weights[widx])
        widx += 1
    return res

  is_weighted.__doc__ = Graph.is_weighted.__doc__
  edge_weights.__doc__ = Graph.edge_weights.__doc__
  degree.__doc__ = Graph.degree.__doc__
  add_edges.__doc__ = Graph.add_edges.__doc__
