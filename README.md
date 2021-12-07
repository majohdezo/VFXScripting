# Bookcase tool

This tool allows the user to create customized bookcases in `Autodesk Maya`. The user will be able to choose the  height, width depth, and levels of the asset. He will also be able to select the amount of books he wants on each level of the bookcase.

The tool works through a UI that th user can customize in order to create his owns models.

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

To run this project you need to follow the next steps:

1. Clone or download this repo
2. Add the `cgpTools` folder inside the path Documents/Maya/scripts/
3. Open Maya Script Editor
4. Type to run

```
import cgpTools.cgpLibrary as library
reload(library)
library.runUI()
```

5. Then, it will open a UI window where you can customise your own bookcase



### Features





