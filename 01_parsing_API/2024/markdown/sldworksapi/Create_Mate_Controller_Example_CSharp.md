---
title: "Create a Mate Controller Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Mate_Controller_Example_CSharp.htm"
---

# Create a Mate Controller Example (C#)

This example shows how to create a Mate Controller in an assembly.

//
======================================================================================

// Preconditions: Open an assembly document that contains
a mechanical slot feature

// with a slot mate that has one of these constraints:

// - Distance Along Slot

// - Percent Along Slot

//

// Postconditions:

// 1. Mate Controller (Position 3) is added to the
FeatureManager design tree.

// 2. Inspect the graphics area.

//

//
=====================================================================================

usingSystem;

usingSystem.Collections.Generic;

usingSystem.Linq;

usingSystem.Text;

usingSystem.Threading.Tasks;

usingSystem.Windows;

usingSystem.Windows.Forms;

usingSolidWorks.Interop.sldworks;

usingSolidWorks.Interop.swconst;

usingSystem.Runtime.InteropServices;

namespaceSlotMate_CSharp

{

publicpartialclassSolidWorksMacro

{

privateModelDoc2 Part;

privateAssemblyDoc Assem;

privateFeatureManager featMgr;

privateboolboolstatus;

privateobjectmyModelView;

privateobject[]
var;

privateMateControllerFeatureData mateControllerObj;

privateMateControllerFeatureData mcObj2;

privateFeature mateContFeat;

privatedouble[]
position2ValArr =newdouble[1];

privatedouble[]
position3ValArr =newdouble[1];

privateobjectvar1;

privatedouble[]
position2ValArr2 =newdouble[1];

privatedouble[]
position3ValArr2 =newdouble[1];

publicDispatchWrapper[]
ObjectArrayToDispatchWrapperArray(object[] Objects)

{

intArraySize;

ArraySize = Objects.GetUpperBound(0);

DispatchWrapper[] d =newDispatchWrapper[ArraySize + 1];

intArrayIndex;

for(ArrayIndex = 0; ArrayIndex <=
ArraySize; ArrayIndex++)

d[ArrayIndex] =newDispatchWrapper(Objects[ArrayIndex]);

returnd;

}

publicvoidMain()

{

Part = (ModelDoc2)swApp.ActiveDoc;

Assem = (AssemblyDoc)Part;

myModelView = Part.ActiveView;

Part.ClearSelection2(true);

boolstatus = Assem. IsSupportedMatesAvailable ;

var = (object[])Assem. CollectAllSupportiveMates ();

featMgr = Part.FeatureManager;

mateControllerObj = (MateControllerFeatureData)featMgr. CreateDefinition ((int)swFeatureNameID_e.swFmMateController);

DispatchWrapper[] dArray;

dArray = ObjectArrayToDispatchWrapperArray(var);

mateControllerObj. Initialize (dArray);

mateControllerObj. AddNewPosition ("Position1");

mateControllerObj. AddNewPosition ("Position2");

mateControllerObj. AddNewPosition ("Position3");

position2ValArr[0] = 0.0375;

mateControllerObj. SetValues ("Position2",
position2ValArr);

position3ValArr[0] = 0.0625;

mateControllerObj. SetValues ("Position3",
position3ValArr);

mateContFeat = featMgr. CreateFeature (mateControllerObj);

mcObj2 = (MateControllerFeatureData)mateContFeat. GetDefinition ();

var1 = mcObj2. Mates ;

position2ValArr2[0] = 0.015;

mcObj2. SetValues ("Position2",
position2ValArr2);

position3ValArr2[0] = 0.085;

mcObj2. SetValues ("Position3",
position3ValArr2);

mateContFeat. ModifyDefinition (mcObj2, Part,null);

}

// The SldWorks swApp variable
is pre-assigned for you.

publicSldWorks swApp;

}

}
