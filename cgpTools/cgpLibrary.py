#Import libraries
import os, sys
import maya.cmds as cmds
import maya.OpenMayaUI as apiUI
 
#Import custom libraries
import cgpTools.booksTool as cgp
reload(cgp)
 
#Import Pyside Modules
try:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    from PySide2.QtUiTools import *
    from shiboken2 import wrapInstance
except ImportError:
    from PySide.QtCore import *
    from PySide.QtGui import *
    from PySide.QtWidgets import *
    from PySide.QtUiTools import *
    from shiboken2 import wrapInstance
 
randomHeights = True

#Get variables
SCRIPT_LOC = os.path.split(__file__)[0]+"/"
UI_NAME = "library" #Nombre de archivo de QT
 
#UI command for loading .ui files
def loadUiWidget(uifilename, parent=None):
    """Properly Loads and returns UI files - by BarryPye on stackOverflow"""
    loader = QUiLoader()
    uifile = QFile(uifilename)
    uifile.open(QFile.ReadOnly)
    ui = loader.load(uifile, parent)
    uifile.close()
    return ui
 
class cgpGenerateLibrary(QMainWindow):

    """Class of creating Library"""
    def __init__(self):
        #Initialize UI Items
        super(cgpGenerateLibrary, self).__init__()
 
        #Set a assigned copy of a window for maya
        MayaMain = wrapInstance(long(apiUI.MQtUtil.mainWindow()), QWidget)
 
        #Set up the window inside of maya
        self.MainWindowUI = loadUiWidget(SCRIPT_LOC+UI_NAME+".ui", MayaMain)
 
        #Set up the Window inside of Maya
        self.MainWindowUI.setAttribute(Qt.WA_DeleteOnClose, True)
 
        #add signals and slots
        self.MainWindowUI.LibraryCreatorButton.clicked.connect(lambda: self.createAllLibrary())
        self.MainWindowUI.activateRandomHeightsCheckBox.stateChanged.connect(self.activateRandomHeights)
        self.MainWindowUI.cancelButton.clicked.connect(self.cancel)
 
        #Show UI
        self.MainWindowUI.show()

    def cancel(self):
        """
        Method for closing the UI
        """
        cmds.deleteUI("MainWindow")

 
    def createAllLibrary(self):
        """
        Method for creating the library system
        """
        #Grab all data
        getHeight = self.MainWindowUI.HeightSpinBox.value()
        getWidth = self.MainWindowUI.WidthSpinBox.value()
        getDepth= self.MainWindowUI.DepthSpinBox.value()
        getLevels= self.MainWindowUI.LevelsSpinBox.value()
        getMinBooks= self.MainWindowUI.MinBooksSpinBox.value()
        getMaxBooks= self.MainWindowUI.MaxBooksSpinBox.value()
        getShelfHeight= self.MainWindowUI.ShelfHeightSpinBox.value()
        getFixedBookHeight= self.MainWindowUI.FixedHeightsSpinBox.value()

        #Run library function
        cgp.createBookcase(getHeight, getWidth, getDepth, getLevels, getMinBooks, getMaxBooks,getShelfHeight, randomHeights, getFixedBookHeight)
    
    def activateRandomHeights(self):
        '''
        Method for enable and disable the fixed books height group
        '''
        global randomHeights
        if self.MainWindowUI.activateRandomHeightsCheckBox.isChecked():            
            randomHeights = True
            self.MainWindowUI.fixedHeightGroupBox.setEnabled(False)
        else:
            randomHeights = False
            self.MainWindowUI.fixedHeightGroupBox.setEnabled(True)
        


 
def runUI():
    """
    Function to show a clean UI everytime
    """
    if not (cmds.window("MainWindow",exists=True)):
        ui=cgpGenerateLibrary()
    else:
        cmds.confirmDialog( title='Confirm', message="Tool is already open", button=['Ok'])
        #sys.stderr.write("Tool is already open")
