---
title: "Traverse Annotations Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_Annotations_Example_VB.htm"
---

# Traverse Annotations Example (VBA)

This example shows how to get display dimension annotations.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified part document and selects
'    a sketch containing multiple dimensions.
' 2. Iterates the display dimensions and gets
'    each display dimension annotation and its position.
' 3. Moves each display dimension annotation 100mm to
'    the right.
' 4. Examine the graphics area and Immediate window.
'
' NOTE: Because the part document is used elsewhere, do not
' save changes.
'------------------------------------------------------------
Option Explicit
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swAnnotation As SldWorks.Annotation
    Dim annotationPosition As Variant
    Dim swFeature As SldWorks.Feature
    Dim swDispDim As SldWorks.DisplayDimension
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
    Dim status As Boolean
```

```
Sub main()
```

```
    Set swApp = CreateObject("SldWorks.Application")
```

```
    'Open part document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\tolanalyst\offset\top_plate.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Get and edit sketch with dimensions
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
    Set swFeature = swSelMgr.GetSelectedObject6(1, -1)
    swModel.EditSketch
```

```
    'Get the first display dimension
    Set swDispDim = swFeature.GetFirstDisplayDimension
```

```
    'Iterate through all of the display dimension
    'annotations in the sketch
    Do While Not swDispDim Is Nothing
        Debug.Print "Display dimension annotation name:"
        'Get the display dimension annotation
        Set swAnnotation = swDispDim.GetAnnotation
        Debug.Print "  " & swAnnotation.GetName
        'Get the position of the display dimension annotation
        annotationPosition = swAnnotation.GetPosition
        If Not IsNull(annotationPosition) Then
            'Move the display dimension annotation 100mm to the right
            swAnnotation.SetPosition2 annotationPosition(0) + 0.1, annotationPosition(1), annotationPosition(2)
        End If
        'Get the next display dimension
        Set swDispDim = swFeature.GetNextDisplayDimension(swDispDim)
    Loop
```

```
End Sub
```
