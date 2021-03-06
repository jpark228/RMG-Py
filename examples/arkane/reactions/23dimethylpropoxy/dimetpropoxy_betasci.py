#!/usr/bin/env python                                                                                                                          
# encoding: utf-8

bonds = {}

externalSymmetry = 1

spinMultiplicity = 2

opticalIsomers = 2

energy = {
    'm08so/mg3s*': Log('dimetpropoxy_betasci.out'),
}

geometry = Log('dimetpropoxy_betasci.out')
frequencies = Log('dimetpropoxy_betasci.out')

"""pivot are the two atoms that are attached to the rotor                                                                                      
top contains the atoms that are being rotated including one of the atoms from pivots                                                           
symmetry is the symmetry number of the scan                                                                                                    
fit is fit of the scan data. It defaults to 'best', but can also be assigned as 'cosine' or 'fourier' 
rotors = [
    HinderedRotor(scanLog=Log('c5h11o1scan2.out'), pivots=[1,3], top=[3,4,5,6], symmetry=3, fit='best'),
    HinderedRotor(scanLog=Log('c5h11o1scan3.out'), pivots=[1,7], top=[7,8,9,10], symmetry=3, fit='best'),
]

"""
