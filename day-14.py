import math

from collections import namedtuple
Ingredient = namedtuple('Ingredient', 'id amount')

my_input = ['8 LHFV => 3 PMVMQ', '2 ZXNM, 1 PSVLS, 4 GRDNT, 26 GLZH, 3 VHJX, 16 BGPF, 1 LHVTN => 4 BTQL', '10 NKHSG, 20 FCPC, 11 GRDNT => 5 HDJB', '6 WPZN, 1 LHFV => 7 BGPF', '1 WDXT, 1 PLCNZ => 3 QHFKR', '12 LCHZ => 1 TPXCK', '11 LSNG => 4 XFGH', '195 ORE => 4 GRNC', '8 XFGQ => 1 GRDNT', '1 FBRG => 5 LCHZ', '7 XZBJ, 8 RSZF, 9 SVDX => 9 LWDP', '20 WDXT => 5 RQFRT', '1 LXQWG, 1 GLZH => 6 SDLJ', '4 XFGH => 1 GCZLZ', '1 WPZN => 1 FBRG', '19 XZBJ => 5 WXGV', '1 GDXC => 6 WDXT', '1 WXGV, 1 NKHSG, 2 LWDP => 5 FCNPB', '4 LWDP, 5 BGPF => 9 KLRB', '1 GMRN => 4 GLZH', '1 RQFRT => 5 SVDX', '2 HWKG => 7 LHFV', '2 LCHZ, 13 JTJT, 10 TPXCK => 3 RSZF', '29 MZTVH => 6 TSGR', '9 NRFLK, 1 SVDX => 5 NKHSG', '123 ORE => 9 GDXC', '1 PZPBV, 21 PMVMQ, 1 GCZLZ => 8 SKZGB', '3 GRNC, 5 GDXC => 8 QZVM', '6 VTDQ, 13 TCQW, 3 FCNPB, 48 PSVLS, 3 RLNF, 73 BTQL, 5 MHRVG, 26 BGPF, 26 HDJB, 5 XFGQ, 6 HTFL => 1 FUEL', '5 QZVM, 2 JTJT => 1 PXKHG', '3 LSNG, 1 PMVMQ => 8 VTDQ', '31 XFGH => 1 FCPC', '9 PSVLS => 8 FWGTF', '1 GRNC => 3 WPZN', '16 JBXDX, 4 GRNC => 6 HWKG', '1 SKZGB, 5 RSZF => 4 XZBJ', '134 ORE => 9 CTDRZ', '1 SVDX, 2 TPXCK => 7 JTJT', '6 RQFRT, 4 KBCW => 3 BGNLR', '12 KLRB, 12 LHFV => 4 HTFL', '2 GMRN => 6 XFGQ', '16 WNSW, 12 SKZGB => 8 LXQWG', '2 NRFLK, 2 CTDRZ => 9 JBXDX', '1 PZPBV => 8 RLNF', '2 JTJT, 5 GCZLZ => 3 WNSW', '5 WXGV, 2 LCHZ => 2 SCDS', '1 QHFKR => 3 GMRN', '10 JTJT, 2 HRCG => 8 KBCW', '7 HWKG => 4 PSVLS', '7 WNSW, 1 PXKHG, 3 BGNLR => 9 MZTVH', '15 TPXCK, 11 LHFV => 5 HRCG', '1 LSNG, 1 HWKG => 3 PZPBV', '7 BGPF => 9 PLCNZ', '1 ZGWT => 6 ZXNM', '26 NKHSG, 1 LHFV, 2 JTJT, 26 WXGV, 6 SDLJ, 1 KLRB, 1 TSGR => 8 TCQW', '154 ORE => 4 NRFLK', '1 GMRN => 3 VHJX', '5 QZVM, 3 GDXC => 7 LSNG', '5 WNSW => 5 ZGWT', '6 QHFKR, 8 PZPBV, 10 FBRG, 13 FWGTF, 1 LHVTN, 4 SCDS, 8 VHJX, 7 TSGR => 6 MHRVG', '12 GLZH => 5 LHVTN']
ex1 = ['10 ORE => 10 A', '1 ORE => 1 B', '7 A, 1 B => 1 C', '7 A, 1 C => 1 D', '7 A, 1 D => 1 E', '7 A, 1 E => 1 FUEL']
ex1_ = ['10 ORE => 10 A', '1 ORE => 1 B', '7 A, 1 B => 2 C', '7 A, 1 C => 3 D', '7 A, 1 D => 1 E', '7 A, 1 E => 1 FUEL']
ex2 = ['9 ORE => 2 A', '8 ORE => 3 B', '7 ORE => 5 C', '3 A, 4 B => 1 AB', '5 B, 7 C => 1 BC', '4 C, 1 A => 1 CA', '2 AB, 3 BC, 4 CA => 1 FUEL']
ex3 = ['157 ORE => 5 NZVS', '165 ORE => 6 DCFZ', '44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL', '12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ', '179 ORE => 7 PSHF', '177 ORE => 5 HKGWZ', '7 DCFZ, 7 PSHF => 2 XJWVT', '165 ORE => 2 GPVTF', '3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT']

ORE = 'ORE'

class Node:

  def __init__( self, this ):
    (amount, id) = this.split()
    self.id = id
    self.amount = int(amount)
    self.ingredients = {}

  def __repr__( self ):
    i = []
    for k,v in self.ingredients.items():
      i.append( str('%d %s' % (v, k)) )
    result = ', '.join(i)
    result += str( ' => %s %s' % (self.amount, self.id) )
    return result

  def getId( self ):
    return self.id

  def addIngredients( self, newIngredients ):
    for i in newIngredients:
      (amount, id) = i.split()
      self.ingredients[id] = int(amount)

  def getOreRatio( self ):
    oreAmount = None
    if ORE in self.ingredients:
      oreAmount = self.ingredients[ORE]
    return( self.amount, oreAmount )

  def getLeaves( self ):
    if len(self.ingredients.keys()) == 0:
      print( 'foo' )
      exit()

    elif len(self.ingredients.keys()) == 1 and ORE in self.ingredients:
      return None

    totals = {}
    for ik, iv in self.ingredients.items():
      required = g_reactions[ik].getLeaves()
      if required is None:
        if ik in totals:
          totals[ik] += iv
        else:
          totals[ik] = iv
      else:
        for rk,rv in required.items():
          if rk in totals:
            totals[rk] += (rv * iv)
          else:
            totals[rk] = (rv * iv)

    return totals

# ---

g_reactions = {}

def getOre( id ):
  leaf_totals = g_reactions[id].getLeaves()
  print( 'leaf_totals:', leaf_totals )

  ore_total = 0
  for id, total in leaf_totals.items():
    ratio = g_reactions[id].getOreRatio()
    need = total / ratio[0]
    ore_needed = ratio[1] * math.ceil(need)
    ore_total += ore_needed

  return ore_total

      

def part_one( data ):

  for line in data:
    (lhs, rhs) = line.split('=>')
    reaction = Node( rhs )
    reaction.addIngredients( lhs.split(',') )
    g_reactions[reaction.getId()] = reaction

  print( g_reactions )
  #print( g_reactions['FUEL'] )
  #print( g_reactions['D'] )

  print( '---')
  ore_needed = getOre('FUEL')
  print( ore_needed )

# ---

part_one( ex2 )
