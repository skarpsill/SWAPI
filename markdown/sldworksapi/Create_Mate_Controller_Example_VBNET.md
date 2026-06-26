---
title: "Create a Mate Controller Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Mate_Controller_Example_VBNET.htm"
---

# Create a Mate Controller Example (VB.NET)

This example shows how to create a Mate Controller in an assembly.

'======================================================================================

' Preconditions: Open an
assembly document that contains a mechanical slot feature

' with a slot mate that has one
of these constraints:

' - Distance Along Slot

' - Percent Along Slot

'

' Postconditions:

' 1. Mate Controller (Position
3) is added to the FeatureManager design tree.

' 2. Inspect the graphics area.

'
' NOTE: Because the model is used elsewhere, do not save changes.
'---------------------------------------------------------------------------

ImportsSolidWorks.Interop.sldworks

ImportsSolidWorks.Interop.swconst

ImportsSystem.Runtime.InteropServices

ImportsSystem

PartialClassSolidWorksMacro

DimPartAsModelDoc2

DimAssemAsAssemblyDoc

DimfeatMgrAsFeatureManager

DimboolstatusAsBoolean

DimmyModelViewAsObject

DimvarAsObject

DimmateControllerObjAsMateControllerFeatureData

DimmcObj2AsMateControllerFeatureData

DimmateContFeatAsFeature

Dimposition2ValArr(0)AsDouble

Dimposition3ValArr(0)AsDouble

Dimvar1AsObject

Dimposition2ValArr2(0)AsDouble

Dimposition3ValArr2(0)AsDouble

FunctionObjectArrayToDispatchWrapperArray(ByValObjectsAsObject())AsDispatchWrapper()

DimArraySizeAsInteger

ArraySize = Objects.GetUpperBound(0)

Dimd(ArraySize)AsDispatchWrapper

DimArrayIndexAsInteger

ForArrayIndex = 0ToArraySize

d(ArrayIndex) =NewDispatchWrapper(Objects(ArrayIndex))

Next

Returnd

EndFunction

Submain()

Part = swApp.ActiveDoc

Assem = Part

myModelView = Part.ActiveView

myModelView.FrameState = swWindowState_e.swWindowMaximized

Part.ClearSelection2(True)

boolstatus = Assem. IsSupportedMatesAvailable

var = Assem. CollectAllSupportiveMates

featMgr = Part.FeatureManager

mateControllerObj = featMgr. CreateDefinition (swFeatureNameID_e.swFmMateController)

DimdArray()AsDispatchWrapper

dArray = ObjectArrayToDispatchWrapperArray(var)

CallmateControllerObj. Initialize (dArray)

mateControllerObj. AddNewPosition ("Position1")

mateControllerObj. AddNewPosition ("Position2")

mateControllerObj. AddNewPosition ("Position3")

position2ValArr(0) = 0.0375

CallmateControllerObj. SetValues ("Position2",
position2ValArr)

position3ValArr(0) = 0.0625

CallmateControllerObj. SetValues ("Position3",
position3ValArr)

mateContFeat = featMgr. CreateFeature (mateControllerObj)

mcObj2 = mateContFeat. GetDefinition ()

var1 = mcObj2. Mates

position2ValArr2(0) = 0.015

CallmcObj2. SetValues ("Position2",
position2ValArr2)

position3ValArr2(0) = 0.085

CallmcObj2. SetValues ("Position3",
position3ValArr2)

mateContFeat. ModifyDefinition (mcObj2, Part,Nothing)

EndSub

'''<summary>

'''The SldWorks swApp variable is
pre-assigned for you.

'''</summary>

PublicswAppAsSldWorks

EndClass
