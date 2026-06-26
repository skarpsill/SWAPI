---
title: "Insert Grid System Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Grid_System_Feature_Example_VB.htm"
---

# Insert Grid System Feature Example (VBA)

This example shows how to insert a Grid System feature into a model.

```
'-----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Creates a sketch of a circle.
' 3. Inserts GridSystem1, which contains Surface-Extrude1, Level1, Level2,
'    and two derived sketches, in the FeatureManager design tree.
' 4. Sets the height of each level of the surface extrude to 50.0 mm.
' 5. Examine the Immediate window and graphics area.
' 6. Expand GridSystem1 in FeatureManager design tree.
'------------------------------------------------------------------------------

Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim GridFeature As SldWorks.Feature
 Dim Part As SldWorks.ModelDoc2
 Dim myModelView As SldWorks.ModelView
 Dim skSegment As SldWorks.SketchSegment
 Dim boolstatus As Boolean
 Dim longstatus As Long
Sub main()
    Set swApp = Application.SldWorks
     swApp.ResetUntitledCount 0, 0, 0
     Set Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2011\templates\Part.prtdot", 0, 0, 0)
     swApp.ActivateDoc2 "Part1", False, longstatus
     Set Part = swApp.ActiveDoc

    Set myModelView = Part.ActiveView
     myModelView.FrameLeft = 0
     myModelView.FrameTop = 0
     myModelView.FrameState = swWindowState_e.swWindowMaximized
     Part.ShowNamedView2 "*Isometric", 7

    Set skSegment = Part.SketchManager.CreateCircle(-0.019633, 0.076084, 0#, -0.001997, 0.081475, 0#)
     Part.SketchManager.InsertSketch True

    boolstatus = Part.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)

    Dim offsetArray As Variant
     Dim heightsArray() As Double
     ReDim heightsArray(0 To 1) As Double
     heightsArray(0) = 0.05
     heightsArray(1) = 0.05
     offsetArray = heightsArray

    Set GridFeature = Part.FeatureManager.InsertGridFeature((offsetArray))
     Debug.Print GridFeature.Name & " was created."

     Part.ViewZoomtofit
End Sub
```
