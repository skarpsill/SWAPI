---
title: "Get Whether Linear Edge Is Foreshortened Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Whether_Linear_Dimension_Is_Foreshortened_Example_VB.htm"
---

# Get Whether Linear Edge Is Foreshortened Example (VBA)

## Get Whether Linear Dimension Is Foreshortened Example (VBA)

This example shows how to get whether a linear dimension is foreshortened.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\chair.slddrw.
' 2. Click Tools > Options > Document Properties > Dimensions > Linear.
' 3. Click ANSI in Base linear dimension standard.
' 4. Verify that the following check box and option are selected in
'    Foreshortened:
'    * Automatic
'    * Zigzag
' 5. Click OK.
' 6. Dimension an outside linear edge.
'
' Postconditions:
' 1. Gets whether the dimension is foreshortened.
' 2. Examine the Immediate window and drawing.
'
' NOTES:
' * Foreshortened dimensions are only valid for
'   linear dimensions and only when the detailing standard
'   is ANSI.
' * Because the part and drawing are used elsewhere, do not
'   save changes.
'-------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swDisplayDimension As SldWorks.DisplayDimension
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelectionMgr = swModel.SelectionManager
    Set swDisplayDimension = swSelectionMgr.GetSelectedObject6(1, -1)
    Debug.Print "Foreshortened dimension? " & swDisplayDimension.Foreshortened
```

```
    swModel.ClearSelection2 True
```

```
End Sub
```
