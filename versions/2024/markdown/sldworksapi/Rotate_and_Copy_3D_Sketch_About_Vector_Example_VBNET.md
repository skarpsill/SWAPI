---
title: "Rotate and Copy 3D Sketch About Vector Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_and_Copy_3D_Sketch_About_Vector_Example_VBNET.htm"
---

# Rotate and Copy 3D Sketch About Vector Example (VB.NET)

This example shows how to rotate and copy 3D sketches about a vector.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a part that contains two 3D sketches,
'    3DSketch1 and 3DSketch2.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Copies and rotates the 3DSketch2 sketch around
'    the center point of the 3DSketch1 sketch's arc.
' 2. Rotates the 3DSketch1 sketch around the center
'    point of its arc.
' 3. Examine the Immediate window.
'---------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSelMgr As SelectionMgr
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSelData As SelectData
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSketchMgr As SketchManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSketch As Sketch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolStatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim varSketchSegments As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Integer

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' If SOLIDWORKS isn't running,
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' then exit
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If swApp Is Nothing Then Exit Sub

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Document with two 3D sketches, named 3DSketch2 and
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' 3DSketch1, is open and active
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If swModel Is Nothing Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MsgBox("Failed to open document.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSelData = swSelMgr.CreateSelectData
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchMgr = swModel.SketchManager

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Select 3DSketch2 sketch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolStatus = swModelDocExt.SelectByID2("3DSketch2", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If boolStatus = False Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MsgBox("Failed to select sketch 3DSketch2.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Open 3DSketch2 sketch in edit mode
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.EditSketch()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketch = swSketchMgr.ActiveSketch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If swSketch Is Nothing Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MsgBox("Failed to get pointer to 3DSketch2 sketch.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Select all sketch segments in 3DSketch2 sketch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}varSketchSegments = swSketch.GetSketchSegments()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = 0 To UBound(varSketchSegments)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolStatus = varSketchSegments(i).select4(True, swSelData)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If boolStatus = False Then MsgBox("Failed to select sketch segment instance." & i & ".")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next i

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Copy and rotate 3DSketch2 sketch about center
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' point of 3DSketch1 sketch's arc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Rotating and copying 3DSketch2 sketch about the center point of 3DSketch1's arc? " & swSketchMgr.RotateOrCopy3DAboutVector(True, 1, True, -0.09925811702374, 0.004131001848179, 0, 1, 0, 0, 1.5707963267949))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ClearSelection2(True)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Exit 3DSketch2 sketch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchMgr.InsertSketch(True)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Select 3DSketch1 sketch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolStatus = swModelDocExt.SelectByID2("3DSketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If boolStatus = False Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MsgBox("Failed to select sketch 3DSketch1.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Edit 3DSketch1 sketch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.EditSketch()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketch = swModel.GetActiveSketch2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If swSketch Is Nothing Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MsgBox("Failed to get pointer to sketch 3DSketch1.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Select all sketch segments in 3DSketch1 sketch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}varSketchSegments = swSketch.GetSketchSegments()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = 0 To UBound(varSketchSegments)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolStatus = varSketchSegments(i).select4(True, swSelData)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If boolStatus = False Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}MsgBox("Failed to select sketch segment instance." & i & ".")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next i

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Rotate 3DSketch1 sketch about the
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' center point of its arc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Rotating 3DSketch1 sketch about the center point of its arc? " & swSketchMgr.RotateOrCopy3DAboutVector(True, 1, True, -0.09925811702374, 0.004131001848179, 0, 1, 0, 0, 1.5707963267949))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ClearSelection2(True)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Exit 3DSketch1 sketch
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSketchMgr.InsertSketch(True)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
