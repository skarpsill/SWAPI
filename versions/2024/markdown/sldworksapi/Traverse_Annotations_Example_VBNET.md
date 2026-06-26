---
title: "Traverse Annotations Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_Annotations_Example_VBNET.htm"
---

# Traverse Annotations Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelMgr As SelectionMgr
        Dim swAnnotation As Annotation
        Dim annotationPosition() As Double
        Dim swFeature As Feature
        Dim swDispDim As DisplayDimension
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer
        Dim status As Boolean

        'Open part document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\tolanalyst\offset\top_plate.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Get and edit sketch with dimensions
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        swSelMgr = swModel.SelectionManager
        swFeature = swSelMgr.GetSelectedObject6(1, -1)
        swModel.EditSketch()

        'Get the first display dimension
        swDispDim = swFeature.GetFirstDisplayDimension

        'Iterate through all of the display dimension
        'annotations in the sketch
        Do While Not swDispDim Is Nothing
            Debug.Print("Display dimension annotation name:")
            'Get the display dimension annotation
            swAnnotation = swDispDim.GetAnnotation
            Debug.Print("  " & swAnnotation.GetName)
            'Get the position of the display dimension annotation
            annotationPosition = swAnnotation.GetPosition
            If Not annotationPosition Is Nothing Then
                'Move the display dimension annotation 100mm to the right
                swAnnotation.SetPosition2(annotationPosition(0) + 0.1, annotationPosition(1), annotationPosition(2))
            End If
            'Get the next display dimension
            swDispDim = swFeature.GetNextDisplayDimension(swDispDim)
        Loop

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
