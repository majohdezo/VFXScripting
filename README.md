# Bookcase tool

This tool allows the user to create customized bookcases. The user will be able to choose the  height, width depth, and levels of the asset. He will also be able to select the amount of books he wants on each level of the bookcase.

The tool works through a UI that th user can customize in order to create his owns models.

![image](reamde_rsc/Obj.gif)


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

1. Open a terminal and go to the root directory where you added the folder.
2. Type to run

```
python fluid.py
```

3. Then, the program will ask you to introduce the name of the file that has all the settings of the fluids. The default txt added to the folder is called `settings.txt`, so you can introduce this file or create a new one. It is important to add the extension of the file, which is `.txt`

Now, depending on the number of frames you've defined, will be the time the simulation will take. Once it is finished it will save a video on the same folder called [movie.mp4](movie.mp4)


### Input

This program needs a txt file. This is the correct format to create it:

At the first line, you will write the `Number of frames` you want in the simulation (30 frames equals one second). Then, on the second line, you will introduce the `Number of emitters` you want to have. Starting from the third line, you will introduce the emitter's settings. Each emitter settings should be on a different line. Values required for each one: 
- [Behavior](#behaviors) (string)
- X position (int)
- Y position (int)
- Density (int)
- X velocity (int)
- Y velocity (int)
- Emitter size (int)
- Factor movement (float)

The factor movement changes the period of the movement. The bigger your factor is, the faster the fluid will move.

After adding the emitters you will introduce the number of objects you want in the scene. As you did with the emitters you will first need to write on a single line the `Number of objects` you want on the scene.Afte this line,  you will introduce the object's settings. Each object settings should be on a different line. Values required for each one: 
- X position (int)
- Y position (int)
- Size (int)

Once you've finished adding the configuration of the emitters and the objects, you will finally add the `Color Scheme`. Each color is identified with a number. This must be a value between 1 and 15. These are the colors available to choose.

![image](reamde_rsc/color.png)


The correct format to give its configuration is the following one: 

```
<frames>
<n-emitters>
<behavior_name> <X position> <Y position> <density> <X velocity> <Y velocity> <emitter size> <factor movement>
.
.
.
<behavior_name> <X position> <Y position> <density> <X velocity> <Y velocity> <emitter size> <factor movement>
<n-objects>
<X object position> <Y object position> <object size>
.
.
.
<X object position> <Y object position> <object size>
<color>
```

Remember that the number of emitters added on the second line should match with the number of lines of each emitter configuration. For example, if you added 3 emitters, there must be 3 lines below the second line that corresponds to each emitter. This is the same logic for the objects, the number of lines below the number of objects must match with the objects added.

[Example](settings.txt)



## Behaviors:

It is possible to have different fluid behaviors. You can choose between 4 different behaviors; "Horizontal Curly", "Vertical Curly", "Swirl" and "Constant". 

To change the behavior you have to add one of the following key-words:

```
- horizontalCurly
- verticalCurly
- swirl
- constant
```

Depending on the X and Y velocities that you add, each emitter will move faster or slower. The velocities also affects the direction of the fluid.

This is how each one of them looks:

`Horizontal Curly`


![image](reamde_rsc/horizontal.gif)

`Vertical Curly`

![image](reamde_rsc/vertical.gif)

`Swirl`

![image](reamde_rsc/swirl.gif)

`Constant`

![image](reamde_rsc/constant.gif)



