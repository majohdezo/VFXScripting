# Bookcase tool

This tool allows the user to create customized bookcases in `Autodesk Maya`. The user will be able to choose the  height, width, depth, and levels of the asset. He will also be able to select the amount of books he wants on each level of the bookcase.

The tool works through an UI that the user can customize in order to create his owns models.

![image](readme_rsc/gif1.gif)


## Instructions:

`Language: Python 3.8.2`

### Libraries used
```
PySide2: pip install PySide2
Shiboken2: pip install shiboken2
```
The UI was created on QTDesigner. If you want to edit the UI or create your own interface, yo need to [install QTDesigner](https://build-system.fman.io/qt-designer-download) on your computer


### Usage

To run this project you need to follow these steps:

1. Clone or download this repo
2. Add the `cgpTools` folder inside the path Documents/Maya/scripts/
3. Open Maya Script Editor
4. Type the following lines to run:

```
import cgpTools.cgpLibrary as library
reload(library)
library.runUI()
```

5. Run the code
6. Then, it will open a UI window where you can customize your own bookcase



### Features

#### Bookcase data

You can insert height, width, and depth you want for the model. You can also add the height you want for the shelves. 

The program validates that you introduce a small value so the bookcase can look good. This value is calculated using the proportion of the average between the height and width of the asset, divided by the number of levels. Then this value is multiplied by 0.5. This way, we always get a proportional value that works properly with the current dimensions inserted for the bookcase. Also, this way we validate that the shelfs' height is smaller than the whole bookcase height.

You can also customize the number of levels.

#### Books data

It is possible to randomize the number of books per levels. You just need to insert a minimum and maximum value of the books you want.

You can also choose if you want random height values for each book, or if you prefer a fixed height value for all of them. The Randomize Heights option is checked by default. If you want to set a fixed value, you just need to uncheck this option, and insert th value you want. You can not insert values bigger than the space between each shelf.

![image](readme_rsc/gif2.gif)

Finally, click on Create to have you bookcase placed on scene.
Each bookcase is grouped by shelfs and books. This way the user can manipulate the whole elements that conform the model easily.


#### Delete models

You can create different bookcases and have all of them placed on the scene. However, if you want to delete a model created, you just need to select it, and when you click on `Create`, it will delete avything selected.

![image](readme_rsc/gif3.gif)










