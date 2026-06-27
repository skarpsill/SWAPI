---
title: "Offset Edges to Create 3D Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Offset_Edges_to_Create_3D_Sketch_on_Surface_Example_VB.htm"
---

# Offset Edges to Create 3D Sketch Example (VBA)

This example shows how to offset edges to create a 3D sketch on a face.

```
'--------------------------------------------------------------
' Preconditions: Verify that the part to open exists.
'
' Postconditions:
' 1. Opens the part.
' 2. Selects the edges to offset.
' 3. Creates a 3D sketch on the face whose edges were selected.
' 4. Examine the graphics area.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\lesson1\tutor1a.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    'Select the edges
    status = swModelDocExt.SelectByID2("", "EDGE", 0.06, 0.12, 0.03, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 0, 0.12, 0.015, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 0.06, 0.12, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 0.12, 0.12, 0.015, True, 0, Nothing, 0)
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("", "EDGE", 0.06, 0.12, 0.03, True, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 0, 0.12, 0.015, True, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 0.06, 0.12, 0, True, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 0.12, 0.12, 0.015, True, 1, Nothing, 0)
```

```
    'Create a 3D sketch
    status = swModelDocExt.SketchOffsetOnSurface(0.01, False, True, False)
```

```
    swModel.ClearSelection2 True
```

```
    'Close the sketch
    Set swSketchManager = swModel.SketchManager
    swSketchManager.InsertSketch True
```

```
End Sub
```
