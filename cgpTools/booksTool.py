import maya.cmds as cmds
import random  
cont = 0
Colors = []

def createBookcase(_height, _width, _depth, _levels, _minBooks, _maxBooks , _shelfH, randomHeights, _fixedBookHeight):
    
    #Assign Values from Ui to the variables
    bookcaseHeight = _height
    bookcaseDepth = _depth
    bookcaseWidth = _width
    
    shelfHeight = _shelfH
    levels = _levels
    
    minBooksNumber = _minBooks
    maxBooksNumber = _maxBooks
    bookDepth = bookcaseDepth * .8
    fixedBookHeight = _fixedBookHeight

    numberOfColors=20

    #Get the avarage size of the height and width
    avarage = (bookcaseHeight + bookcaseWidth) * 0.5

    #Validate shelf height
    if shelfHeight > avarage * 0.05:
        cmds.confirmDialog( title='Confirm', message='Shelf height must be smaller, please enter a valid size', button=['Ok'])
        return

    spaceBtwShelfs=(bookcaseHeight / levels) 

    if fixedBookHeight > (spaceBtwShelfs - shelfHeight) * 0.9:
        cmds.confirmDialog( title='Confirm', message='Book fixed height must be smaller to fit on the bookcase, please enter a valid size', button=['Ok'])
        return


    global cont
    cont = cont + 1
      
    #Deletes objects if selected 
    selected = cmds.ls( selection = True)
    if len(selected) >= 1:
        cmds.delete()
  

    

    Shelfs = []
    shelfsName = "shelfs"+str(cont)

    Books = []
    booksName = "books"+str(cont)

    bookcaseName = "Bookcase"+str(cont)

    #creamos repisa inferior
    shelfBottom=cmds.polyCube(n='shelfBottom')
    cmds.setAttr( shelfBottom[0]+".scaleX", bookcaseWidth)
    cmds.setAttr( shelfBottom[0]+".scaleY", shelfHeight )
    cmds.setAttr( shelfBottom[0]+".scaleZ",bookcaseDepth )
    cmds.setAttr( shelfBottom[0]+".translateY", (shelfHeight / 2) )
    Shelfs.append(shelfBottom[0])

    #creamos repisa superior
    shelfTop=cmds.polyCube(n='shelfTop')
    cmds.setAttr( shelfTop[0]+".scaleX", bookcaseWidth)
    cmds.setAttr( shelfTop[0]+".scaleY", shelfHeight )
    cmds.setAttr( shelfTop[0]+".scaleZ",bookcaseDepth )
    cmds.setAttr( shelfTop[0]+".translateY", bookcaseHeight - (shelfHeight / 2) )
    Shelfs.append(shelfTop[0])
  
        
    #Creamos repisas intermedias
    for i in range (1, levels):
        shelf=cmds.polyCube(n='shelf')
        cmds.setAttr( shelf[0]+".scaleX", bookcaseWidth)
        cmds.setAttr( shelf[0]+".scaleY", shelfHeight)
        cmds.setAttr( shelf[0]+".scaleZ", bookcaseDepth)
        cmds.setAttr( shelf[0]+".translateY", spaceBtwShelfs * i )
        Shelfs.append(shelf[0])

    
    #Creamos costados del librero    
    shelfRight=cmds.polyCube(n='shelfRight')
    cmds.setAttr( shelfRight[0]+".scaleX", shelfHeight)
    cmds.setAttr( shelfRight[0]+".scaleY", bookcaseHeight )
    cmds.setAttr( shelfRight[0]+".scaleZ",bookcaseDepth )
    cmds.setAttr( shelfRight[0]+".translateX", (bookcaseWidth - shelfHeight) / 2 )
    cmds.setAttr( shelfRight[0]+".translateY", (bookcaseHeight - shelfHeight) / 2 + (shelfHeight * 0.5))
    Shelfs.append(shelfRight[0])
    
    shelfLeft=cmds.polyCube(n='shelfLeft')
    cmds.setAttr( shelfLeft[0]+".scaleX", shelfHeight)
    cmds.setAttr( shelfLeft[0]+".scaleY", bookcaseHeight )
    cmds.setAttr( shelfLeft[0]+".scaleZ",bookcaseDepth )
    cmds.setAttr( shelfLeft[0]+".translateX", - (bookcaseWidth - shelfHeight) / 2 )
    cmds.setAttr( shelfLeft[0]+".translateY", (bookcaseHeight - shelfHeight) / 2 + (shelfHeight * 0.5))
    Shelfs.append(shelfLeft[0])

    cmds.group( Shelfs, n=shelfsName)
    
    '''Create Books'''
    #Set maximum and minimum heigths of the books
    minHeight=spaceBtwShelfs * 0.3
    maxHeight=(spaceBtwShelfs - shelfHeight) * 0.8
   
    
    #Set the whole space where the books will be placed
    booksSpace = bookcaseWidth - (2 * shelfHeight)
    #Set the width of each book
    
    '''Create random colors only once at the beggining'''
    global Colors
    if cont == 1:       
        for x in range (0, numberOfColors):
            color1, color2, color3 = random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)
            myLambert = cmds.shadingNode( 'lambert', asShader=True)
            cmds.setAttr ( (myLambert + '.color'), color1,color2,color3, type = 'double3' )
            Colors.append(myLambert)


    for i in range (0, levels): 

        booksNumber = random.randint(minBooksNumber, maxBooksNumber)
        if booksNumber > 0:
            bookWidth = booksSpace / booksNumber
        else:
            bookWidth=0
        
        for j in range(1, booksNumber + 1):
            bookHeight = fixedBookHeight
            
            if(randomHeights):
                bookHeight=random.uniform(minHeight, maxHeight) 

            #We place the books properly on the shelfHeight of the bookcase or the
            #shelfs, it depend on the case
            if i > 0:
                booksVSeparation=(i * spaceBtwShelfs) + shelfHeight * 0.5                
            else:
                booksVSeparation=(i * spaceBtwShelfs) + shelfHeight   
            
            book=cmds.polyCube( n = 'book')
            cmds.setAttr( book[0]+".scaleY", bookHeight)
            cmds.setAttr( book[0]+".scaleZ", bookDepth)
            cmds.setAttr( book[0]+".scaleX", bookWidth)               
            cmds.setAttr( book[0]+".translateX", - (booksSpace / 2) + (bookWidth * j) - (bookWidth / 2))  
            cmds.setAttr( book[0]+".translateY", (bookHeight / 2 + booksVSeparation) )     

            color1, color2, color3 = random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)
            randomColor=random.randint(0,numberOfColors-1)
            cmds.select(book[0])
            cmds.hyperShade( assign=Colors[randomColor] )
            
            Books.append(book[0])
   

    if len(Books) > 0:
        cmds.group( Books, n=booksName)
        cmds.group( shelfsName, booksName , n =bookcaseName )
    else:
        cmds.group( shelfsName, n =bookcaseName)
 

    


          
