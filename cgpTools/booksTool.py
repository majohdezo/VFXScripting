import maya.cmds as cmds
import random

#This counter helps to have a control of the bookcases created
cont = 0

#This list contains the colors combination for the different materials 
Colors = []


def placeShelf(Shelves,name, Xscale, Yscale, Zscale, Xtranslate = 0, Ytranslate =0 ):
    shelf=cmds.polyCube(n=name)
    cmds.setAttr( shelf[0]+".scaleX", Xscale)
    cmds.setAttr( shelf[0]+".scaleY", Yscale )
    cmds.setAttr( shelf[0]+".scaleZ", Zscale )
    cmds.setAttr( shelf[0]+".translateX", Xtranslate )
    cmds.setAttr( shelf[0]+".translateY", Ytranslate )
    Shelves.append(shelf[0])

def createBookcase(_height, _width, _depth, _levels, _minBooks, _maxBooks , _shelfH, randomHeights, _fixedBookHeight):
    
    #Assign Values from Ui to the script variables 
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

    #Get the average size of the height and width to set the percentage that the height shelf can have
    average  = ((bookcaseHeight + bookcaseWidth) * 0.5) / levels
    averagePercentage = average * 0.5
    

    #Validate shelf height
    if shelfHeight > (averagePercentage):
        cmds.confirmDialog( title='Confirm', message='Shelf height must be smaller, please enter a valid size', button=['Ok'])
        return

    #Get the space between shelves where the book will be placed
    spaceBtwShelfs=(bookcaseHeight / levels) 

    #Validate that tha fixed book height is smaller than the space between shelves
    if fixedBookHeight > (spaceBtwShelfs - shelfHeight) * 0.9 and not randomHeights:
        cmds.confirmDialog( title='Confirm', message='Book fixed height must be smaller to fit on the bookcase, please enter a valid size', button=['Ok'])
        return

    #Every time we click on the crate button, we increment the counter of the bookcases created
    global cont
    cont = cont + 1
      
    #Deletes objects if selected 
    selected = cmds.ls( selection = True)
    if len(selected) >= 1:
        cmds.delete()
  
    #Lists that will store each tipe of asset respectively and assigned its name to each group
    Shelves = []
    shelvesName = "shelfs"+str(cont)
    Books = []
    booksName = "books"+str(cont) 
    bookcaseName = "Bookcase"+str(cont)

    #Create and place correctly bottom and top shelf
    placeShelf(Shelves,'shelfBottom',bookcaseWidth, shelfHeight, bookcaseDepth, 0 , (shelfHeight / 2)  )
    placeShelf(Shelves,'shelfTop',bookcaseWidth, shelfHeight, bookcaseDepth, 0 , bookcaseHeight - (shelfHeight / 2) )
        
    #Create and place correctly inner shelves
    for i in range (1, levels):
        placeShelf(Shelves,'shelf',bookcaseWidth, shelfHeight, bookcaseDepth, 0 , spaceBtwShelfs * i  )
    
    #Create and place correctly side shelves  
    placeShelf(Shelves,'shelfRight',shelfHeight, bookcaseHeight, bookcaseDepth, (bookcaseWidth - shelfHeight) / 2 , (bookcaseHeight - shelfHeight) / 2 + (shelfHeight * 0.5))
    placeShelf(Shelves,'shelfLeft',shelfHeight, bookcaseHeight, bookcaseDepth,-(bookcaseWidth - shelfHeight) / 2 , (bookcaseHeight - shelfHeight) / 2 + (shelfHeight * 0.5))

    cmds.group( Shelves, n=shelvesName)
    
    '''Create Books'''
    #Set maximum and minimum heigths of the books for the random option
    minHeight=spaceBtwShelfs * 0.3
    maxHeight=(spaceBtwShelfs - shelfHeight) * 0.8
   
    
    #Set the whole space where the books will be placed
    booksSpace = bookcaseWidth - (2 * shelfHeight)


    '''Create random colors only once at the beggining'''
    global Colors
    if cont == 1:       
        for x in range (0, numberOfColors):
            color1, color2, color3 = random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)
            myLambert = cmds.shadingNode( 'lambert', asShader=True, name='M_book'+str(x))
            cmds.setAttr ( (myLambert + '.color'), color1,color2,color3, type = 'double3' )
            Colors.append(myLambert)

    '''Create the books of each level'''
    for i in range (0, levels): 
        #We set the random books each level will have according to the minimum and maximum values given by the user
        booksNumber = random.randint(minBooksNumber, maxBooksNumber)

        #We get the width of each book according to the number of books and the space we have to place them
        if booksNumber > 0:
            bookWidth = booksSpace / booksNumber
        #We avoid to have division by cero if we have no books
        else:
            bookWidth=0

        '''
        Create books per level
        '''
        for j in range(1, booksNumber + 1):
            bookHeight = fixedBookHeight
            
            #If the user selected the random option, we create different heights for each book
            if(randomHeights):
                bookHeight=random.uniform(minHeight, maxHeight) 

            #We place the books properly based on the shelfHeight of the bookcase or the
            #shelfs, it depend on the case
            if i > 0:
                booksVSeparation=(i * spaceBtwShelfs) + shelfHeight * 0.5                
            else:
                booksVSeparation=(i * spaceBtwShelfs) + shelfHeight   
            
            #Create and properly place each book
            book=cmds.polyCube( n = 'book')
            cmds.setAttr( book[0]+".scaleY", bookHeight)
            cmds.setAttr( book[0]+".scaleZ", bookDepth)
            cmds.setAttr( book[0]+".scaleX", bookWidth)               
            cmds.setAttr( book[0]+".translateX", - (booksSpace / 2) + (bookWidth * j) - (bookWidth / 2))  
            cmds.setAttr( book[0]+".translateY", (bookHeight / 2 + booksVSeparation) )     

            #Select a random color for ach book
            randomColor=random.randint(0,numberOfColors-1)
            cmds.select(book[0])
            cmds.hyperShade( assign=Colors[randomColor] )
            
            Books.append(book[0])
   
    #Add the shelves and books to the bookcase group. If there are no books, we only add the shelves
    if len(Books) > 0:
        cmds.group( Books, n=booksName)
        cmds.group( shelvesName, booksName , n =bookcaseName )
    #If books lenght is equal to cero, it means we don't have books on the bookcase
    else:
        cmds.group( shelvesName, n =bookcaseName)


 

    


          
