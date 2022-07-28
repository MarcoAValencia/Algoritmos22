## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import struct, sys, time, random
from NaiveBubbleSort import *
from ImprovedBubbleSort import *
from InsertionSort import *
from randomGen import *


## -------------------------------------------------------------------------
def IsSorted( S ):
  f = True
  for i in range( len( S ) - 1 ):
    f = f and not( S[ i + 1 ] < S[ i ] )
  # end for
  return f
# end def

## -------------------------------------------------------------------------
def DoExperiment( S, f ):
  r = 5
  t = 0
  s = True
  for i in range( r ):
    C = S.copy( )
    start = time.time( )
    f( C )
    end = time.time( )
    s = s and IsSorted( C )
    t += float( end - start )
  # end for
  return [ s, t / float( r ) ]
# end def

## -------------------------------------------------------------------------
# Inputs
if (int( sys.argv[ 1 ] )==0) : 
 input_file = open( sys.argv[ 2 ], 'rb' )
 input_buffer = input_file.read( )
 input_file.close( )
 b = int( sys.argv[ 3 ] )#desde
 e = int( sys.argv[ 4 ] )#hasta
 s = int( sys.argv[ 5 ] )#salto

 # Data type configuration
 element_type = int
 element_size = 4
 element_id = 'i'
 N = len( input_buffer ) // element_size

 # Read sequence as numbers
 input_sequence = []
 for i in range( N ):
   input_sequence += [ struct.unpack( element_id, input_buffer[ element_size * i : element_size * ( i + 1 ) ] )[ 0 ] ]
 # end for

 # Perform experiments
 for n in range( b, e + 1, s ):
   nbr = DoExperiment( input_sequence[ 0 : n ], NaiveBubbleSort )
   ibr = DoExperiment( input_sequence[ 0 : n ], ImprovedBubbleSort )
   inr = DoExperiment( input_sequence[ 0 : n ], InsertionSort )
   if not( nbr[ 0 ] and ibr[ 0 ] and inr[ 0 ] ):
     print( "ERROR: Input sequence was not ordered" )
     sys.exit( 1 )
   # end if
   print( n, nbr[ 1 ], ibr[ 1 ], inr[ 1 ] )#>datos.csv en la terminal para exportar los datos 
 # end for
# eof first if
##------------------------------------------------------------------------------------------------------------------------
#Numeros Aleatorios
if (int( sys.argv[ 1 ] )==1) :
 b = int( sys.argv[ 2 ] )#desde
 e = int( sys.argv[ 3 ] )#hasta
 s = int( sys.argv[ 4 ] )#salto  
 # Perform experiments
 for n in range( b, e + 1, s ):
   nbr = DoExperiment( randomGen(n), NaiveBubbleSort )
   ibr = DoExperiment( randomGen(n), ImprovedBubbleSort )
   inr = DoExperiment( randomGen(n), InsertionSort )
   if not( nbr[ 0 ] and ibr[ 0 ] and inr[ 0 ] ):
     print( "ERROR: Input sequence was not ordered" )
     sys.exit( 1 )
   # end if
   print( n, nbr[ 1 ], ibr[ 1 ], inr[ 1 ] )
 # end for
# end second if
##------------------------------------------------------------------------------------------------------------------------
#Numeros Aleatorios Ordenados 
if (int( sys.argv[ 1 ] )==2) :
 b = int( sys.argv[ 2 ] )#desde
 e = int( sys.argv[ 3 ] )#hasta
 s = int( sys.argv[ 4 ] )#salto  
 # Perform experiments
 for n in range( b, e + 1, s ):
   nbr = DoExperiment( randomSort(n), NaiveBubbleSort )
   ibr = DoExperiment( randomSort(n), ImprovedBubbleSort )
   inr = DoExperiment( randomSort(n), InsertionSort )
   if not( nbr[ 0 ] and ibr[ 0 ] and inr[ 0 ] ):
     print( "ERROR: Input sequence was not ordered" )
     sys.exit( 1 )
   # end if
   print( n, nbr[ 1 ], ibr[ 1 ], inr[ 1 ] )
 # end for
# end third if
##------------------------------------------------------------------------------------------------------------------------
#Numeros Aleatorios Orden invertido
if (int( sys.argv[ 1 ] )==3) :
 b = int( sys.argv[ 2 ] )#desde
 e = int( sys.argv[ 3 ] )#hasta
 s = int( sys.argv[ 4 ] )#salto  
 # Perform experiments
 for n in range( b, e + 1, s ):
   nbr = DoExperiment( randomInvertSort(n), NaiveBubbleSort )
   ibr = DoExperiment( randomInvertSort(n), ImprovedBubbleSort )
   inr = DoExperiment( randomInvertSort(n), InsertionSort )
   if not( nbr[ 0 ] and ibr[ 0 ] and inr[ 0 ] ):
     print( "ERROR: Input sequence was not ordered" )
     sys.exit( 1 )
   # end if
   print( n, nbr[ 1 ], ibr[ 1 ], inr[ 1 ] )
 # end for
# end fourth if
## eof - run_experiment.py



## ordenar datos con el algortimo de pyton y repetir(Lo mismo con arreglos ordenados invertidos). Verificar si son cuadraticos(Regresion lineal), mostrar graficas de los codigos.



