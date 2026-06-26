---
title: "Change Radial to Diametric Style Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Radial_to_Diametric_Style_Example_VB.htm"
---

# Change Radial to Diametric Style Example (VBA)

This example shows how to change radial style to diametric style.

```
'-------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\block.sldprt.
' 2. Right-click Annotations and click Show Feature Dimensions.
'
' Postconditions:
' 1. Selects a radial dimension.
' 2. Changes the selected radial dimension to a diametric
'    dimension.
' 3. Examine the graphics area.
'
' NOTE: Because the part is used elsewhere, do not save
' changes.
'--------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swDispDim As SldWorks.DisplayDimension
    Dim boolstatus As Boolean
    Dim longstatus As Long
    Dim longwarnigs As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
    boolstatus = swModelDocExt.SelectByID2("D1@Sketch2@block.SLDPRT", "DIMENSION", 1.69848055113666E-02, -0.028515153676096, -3.13572600146445E-04, False, 0, Nothing, 0)
    Set swDispDim = swSelMgr.GetSelectedObject6(1, -1)
```

```
    ' Toggle between radial and diametric styles
    If swDispDim.Diametric Then
        swDispDim.Diametric = False
    Else
        swDispDim.Diametric = True
    End If
```

```
    ' Redraw to see changes
    swModel.GraphicsRedraw2
```

```
End Sub
```
