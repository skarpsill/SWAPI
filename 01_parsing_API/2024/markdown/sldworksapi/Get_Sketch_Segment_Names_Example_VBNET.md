---
title: "Get Sketch Segment Names Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Segment_Names_Example_VBNET.htm"
---

# Get Sketch Segment Names Example (VB.NET)

This example shows how to get the names of selected sketch segments.

```
'----------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Inserts a sketch of a rectangle.
' 3. Selects two sketch segments and prints their names
'    to the Immediate window.
' 4. Examine the Immediate window.
'----------------------------------------------------
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
        Dim swSketchManager As SketchManager
        Dim sketchLines As Object
        Dim swSketchSegHoriz As SketchSegment
        Dim swSketchSegVert As SketchSegment
        Dim ret As Boolean

        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2016\templates\Part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension

        ret = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
        ret = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
        swSketchManager = swModel.SketchManager
        sketchLines = swSketchManager.CreateCornerRectangle(0, 0, 0, 0.110951010058045, -0.066328380491143, 0)
        ret = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0.00443505736694483, -0.012832795562811, 0.00637809258389225, False, 0, Nothing, 0)
        ret = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0.095835993249203, -0.0306185999393385, -0.0297695225643872, True, 0, Nothing, 0)
        swSelMgr = swModel.SelectionManager
        swSketchSegHoriz = swSelMgr.GetSelectedObject6(1, -1)
        Debug.Print("Name of selected horizontal sketch segment = " & swSketchSegHoriz.GetName)
        swSketchSegVert = swSelMgr.GetSelectedObject6(2, -1)
        Debug.Print("Name of selected vertical sketch segment = " & swSketchSegVert.GetName)

        swSketchManager.InsertSketch(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
