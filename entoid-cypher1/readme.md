```
  ____|   \  |   ___|   _ \ \ \   /   _ \ __ __|  _ \ _ _|  __ \  
  __|      \ |  |      |   | \   /   |   |   |   |   |  |   |   |
  |      |\  |  |      __ <     |    ___/    |   |   |  |   |   | // Name : entoid-cypher1
 _____| _| \_| \____| _| \_\   _|   _|      _|  \___/ ___| ____/  // Type : Cypher Shuffle
```

***

### // Diagram
``` 
 encoded password     Using the encoded password            Using the array locations iterate                 After iterating though all values
 using SHA256         generate a unique location array      through the arrays and move each character        we have the encrypted message
 
┌─────────────┐       [[2,5],[6,10],[142,175],[2,35],       First iteration [0,4]                             ['h','f','d','b','i','g','a','c','e']      
│ a x w e f 3 │        [3,67],[9,0],[18,432],[2,158],         ┌───>──┴────────┐
│ f % 3 ( ! t │        [1,2],[532,15],[7,15],[4,175],       ['a','b','c','d','e','f','g','h','i']
│ " g ) ? / 3 │  ===>  [3,67],[9,0],[18,432],[2,158],  ===>                                           ===>
│ 2 # g G Y H │        [2,5],[6,10],[142,175],[2,35],       Seconds iteration [7,2]
│ e F e G t m │        [1,2],[532,15],[7,15],[4,175],                 ┌──────<───┴────────┐
└─────────────┘        [3,67],[9,0],[18,432],[2,158]]       ['e','b','c','d','a','f','g','h','i']
```


### // Pseudocode
```Pseudo
// This creates a location for each bite of data within the cypher array

function shiftLocationGenerator (key, lengthOfCypher):
    SET shiftValue to []
    foreach i in range of lengthOfCypher:
        foreach x in key:
            SET RANDOM.SEED to x + i + lengthOfCypher
            APPEND [ RANDOM.RANDINT( 0, round( lengthOfCypher - 1 ) ), RANDOM.RANDINT( 0, round( lengthOfCypher - 1 ) ) ] to shiftValue
     RETURN shiftValue
```
```Pseudo
// Generates a 256 character key to use for generating the shift locations

function keyGenerator (key):
    SET RANDOM.SEED to key
    RETURN SHA256( SHA256( key.ENCODE ) + SHA256( RANDOM.BYTES(10).ENCODE ).ENCODE )
            
```
```Pseudo
// Generates a specific amount of random filler to add to the cypher

function fillerGenerator (content):
    SET fillerAmount to round( ( ( LENGTH of content ) / 2 ) * 10 )
    SET filler to []
    foreach i in range of fillerAmount:
        APPEND RANDOM.RANDBYTES(1) to filler
    RETURN filler
            
```
```Pseudo
// Encrypts the content using the cypher shuffle

function Encypt (key, content):
    SET fillerAmount to round( ( ( LENGTH of content ) / 2 ) * 10 )
    SET cypherSize to ( LENGTH of STRING( ( LENGHT of content ) + fillerAmount ) ) + ( LENGTH of content ) + fillerAmount
    SET key to keyGenerator (key)
    
    SET cyperShift to shiftLocationGenerator(key, cypherSize)
    SET cypherContent to [ i.ENCODE foreach i in content ]
    SET cypherFiller to fillerGenerator (content)
    
    SET preShift to [ i foreach i in STRING( cypherCOntent ) ] + cypherContent + cypherFiller
    
    foreach i in cypherShift:
        SET x = preShift[i[0]]
        SET y = preShift[i[1]]
        
        SET preShift[i[0]] = y
        SET preShift[i[1]] = x
       
     RETURN preShift
            
```

```
```Pseudo
// Decrypt the content using the reverse cypher shuffle

function Encypt (key, content):
    SET cypherSize to ( LENGTH of content )
    SET cyperShift to shiftLocationGenerator(key, cypherSize)
    SET key to keyGenerator (key)
    
    cypherShift.REVERSE_ORDER
    SET preShift to content
    
    foreach i in cypherShift:
        SET x = preShift[i[0]]
        SET y = preShift[i[1]]
        
        SET preShift[i[0]] = y
        SET preShift[i[1]] = x
     
     SET messageLength
     
     foreach i in range( ( LENGTH of preShift ) ):
        IF ( TYPE of preShift[i] ) != ( TYPE of BYTES ):
            SET messageLength to STRING( messageLength ) + STRING( preSHift[i] )
        ELSE:
            BREAK forloop
      
      SET message
      
      foreach i in range( INTEGER( messageLength + 3 ) ):
          SET message = STRING( message ) + STRING( preSHift[i].ENCODE )
     
     RETURN message
```
