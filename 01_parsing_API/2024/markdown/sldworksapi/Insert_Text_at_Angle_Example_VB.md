---
title: "Insert Text at Angle Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Text_at_Angle_Example_VB.htm"
---

# Insert Text at Angle Example (VBA)

This example shows how to insert a sketch of text at an angle.

```
'---------------------------------------------------------
' Preconditions: Verify that the specified document to open
' exists.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Inserts the string Part2.SLDPRT as Sketch2
'    at the origin and at an angle.
' 3. Examine the graphics area and FeatureManager design tree.
'
' NOTE: Because the model is used elsewhere, do not
' save any changes.
'----------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Const sSketchText As String = "<r65>Part2.SLDPRT</r>"
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSketchText As SldWorks.SketchText
    Dim errors As Long
    Dim warnings As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt", 1, 0, "", errors, warnings)
    Set swSketchText = swModel.InsertSketchText(0#, 0#, 0#, sSketchText, 0, 0, 0, 100, 100)
    swModel.InsertSketch2 True
```

```
End Sub
```
