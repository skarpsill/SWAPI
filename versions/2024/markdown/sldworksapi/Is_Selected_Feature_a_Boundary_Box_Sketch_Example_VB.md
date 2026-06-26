---
title: "Is Selected Feature a Boundary Box Sketch (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Is_Selected_Feature_a_Boundary_Box_Sketch_Example_VB.htm"
---

# Is Selected Feature a Boundary Box Sketch (VBA)

This example shows how to determine if a sketch is a boundary box sketch.

```
'----------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\2012-sm.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Unsuppresses the Flat-Pattern1 feature.
' 2. Selects the Flat-Pattern1's boundary box sketch feature.
' 3. Gets whether the selected sketch is a boundary box sketch.
' 4. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim swSketch As SldWorks.Sketch
Dim status As Boolean
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
```

```
' Open a sheet metal part
Set swModel = swApp.ActiveDoc
```

```
' Select the flat-pattern feature
Set swModelDocExt = swModel.Extension
status = swModelDocExt.SelectByID2("Flat-Pattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
```

```
' Unsuppress the flat-pattern feature
status = swModel.EditUnsuppress2
swModel.ClearSelection2 True
```

```
' Select the flat-pattern feature's boundary box feature
status = swModelDocExt.SelectByID2("Bounding-Box1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
Set swSelMgr = swModel.SelectionManager
Set swFeature = swSelMgr.GetSelectedObject6(1, -1)
Set swSketch = swFeature.GetSpecificFeature2
```

```
' Print to the Immediate window if the just-selected feature is a boundary box
Debug.Print "Selected feature a boundary box sketch? " & swSketch.IsBoundaryBoxSketch
```

```
End Sub
```
