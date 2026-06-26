---
title: "Offset Edges to Create 3D Sketch Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Offset_Edges_to_Create_3D_Sketch_on_Surface_Example_VBNET.htm"
---

# Offset Edges to Create 3D Sketch Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchManager As SketchManager
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\lesson1\tutor1a.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        'Select the edges
        status = swModelDocExt.SelectByID2("", "EDGE", 0.06, 0.12, 0.03, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0, 0.12, 0.015, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.06, 0.12, 0, True, 0, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.12, 0.12, 0.015, True, 0, Nothing, 0)
        swModel.ClearSelection2(True)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.06, 0.12, 0.03, True, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0, 0.12, 0.015, True, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.06, 0.12, 0, True, 1, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "EDGE", 0.12, 0.12, 0.015, True, 1, Nothing, 0)

        'Create a 3D sketch
        status = swModelDocExt.SketchOffsetOnSurface(0.01, False, True, False)

        swModel.ClearSelection2(True)

        'Close the sketch
        swSketchManager = swModel.SketchManager
        swSketchManager.InsertSketch(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
