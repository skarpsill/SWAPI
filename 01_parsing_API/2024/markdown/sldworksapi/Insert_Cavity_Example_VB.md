---
title: "Insert Cavity Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Cavity_Example_VB.htm"
---

# Insert Cavity Example (VBA)

This example shows how to insert a cavity in a mold base.

```
'------------------------------------------------------------------------------------
' Preconditions:
' 1. Create a new folder and copy public_documents\samples\tutorial\molds\telephone.sldprt
'    to that folder.
' 2. Click File > New > Part > OK to create a new part document.
'    a. Insert a sketch of a rectangle with a length of 240 mm and width of 350 mm.
'    b. Using the sketch, create a boss extrude feature with a depth of 160 mm.
'    c. Save the part as telephoneMoldBase.sldprt in the folder created in step 1.
' 3. Click File > New > Assembly > OK to create a new assembly document.
'    a. Click telephoneMoldBase in Part/Assembly to Insert in the PropertyManager page.
'    b. Click OK.
'    c. Click Insert Components on the Assembly toolbar, click Browse in
'       Part/Assembly to Insert, click telephone.sldprt located in the folder
'       created in step 1, and click Open.
'    d. Drop telephone.sldprt in the graphics area.
'    e. Click View > Display > Hidden Lines Visible.
'    f. In the FeatureManager design tree, click telephone<1> and click Move Component
'       in the Assembly toolbar.
'    g. Move telephone<1> into the center of telephoneMoldBase<1> and click OK.
'       TIP: Change the view orientation to Top and Front to help center telephone<1>.
'    h. Click File > Save All > Rebuild and save the document (recommended),
'       navigate to the folder created in step 1, type AssemInterim.sldasm in
'       File name, and click Save.
' 4. Click telephoneMoldBase<1> in the FeatureManager design tree.
' 5. Ctrl+click telephone<1> in the FeatureManager design tree.
'
' Postconditions:
' 1. Creates Cavity1 in telphoneMoldBase<1>.
' 2. Expand telephoneMoldBase<1> to verify step 1.
'-----------------------------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swMoldBaseComp As SldWorks.Component2
    Dim swCoreComp1 As SldWorks.Component2
    Dim nRetval As Long
    Dim nInfo as Long
    Dim bRet  As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel

    Set swSelMgr = swModel.SelectionManager
    Set swMoldBaseComp = swSelMgr.GetSelectedObjectsComponent2(1)
    Set swCoreComp1 = swSelMgr.GetSelectedObjectsComponent2(2)
```

```
    swModel.ClearSelection2 True
```

```
    bRet = swMoldBaseComp.Select2(False, 0)
    nRetval = swAssy.EditPart2(True, True, nInfo)
    bRet = swCoreComp1.Select2(True, 0)
    swAssy.InsertCavity4 0#, 0, 0#, True, swAboutCentroid, 0
    swAssy.EditAssembly
```

```
End Sub
```
