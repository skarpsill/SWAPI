---
title: "Move Copy Sketch Entities Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_Copy_Sketch_Entities_Example_VBNET.htm"
---

# Move Copy Sketch Entities Example (VB.NET)

This example shows how to move, copy, and move and copy sketch entities.

```
'----------------------------------------------------------------------
' Preconditions: Verify that the specified part template exists.
'
' Postconditions:
' 1. Insert a breakpoint at the following lines of code:
'
'    swFeature = swPart.FeatureByName("Sketch1")
'
'    swModel.EditUndo2(1)
'
' 2. Run the macro.
' 3. Examine the sketch at each breakpoint, then press F5.
'     1.  Opens a new part document.
'     2.  Opens a sketch and sketches a line and a circle.
'     3.  Selects the line and circle.
'     4.  Moves the line and circle.
'     5.  Moves and copies the line and circle once.
'     6.  Moves and copies the line and circle twice.
' 4. Close the part document without saving it.
'----------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swPart As PartDoc
        Dim swFeature As Feature
        Dim swSketchMgr As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim lIdx As Integer
        Dim bCopy As Boolean
        Dim lNumCopies As Integer
        Dim aBasePoint(2) As Double
        Dim aMoveVector(2) As Double
        Dim errors As Integer
        Dim status As Boolean

        ' Open a new part document and sketch a line and a circle
        swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2013\templates\Part.prtdot", 0, 0, 0)
        swApp.ActivateDoc3("Part1", True, False, errors)
        swModel = swApp.ActiveDoc
        swPart = swModel
        swModelDocExt = swModel.Extension
        swSketchMgr = swModel.SketchManager
        swSketchMgr.InsertSketch(True)
        swSketchSegment = swSketchMgr.CreateLine(-0.096389, 0.032667, 0.0#, -0.062943, 0.019437, 0.0#)
        swSketchSegment = swSketchMgr.CreateCircle(-0.084504, 0.013823, 0.0#, -0.087932, 0.006083, 0.0#)
        swFeature = swPart.FeatureByName("Sketch1")
        status = swFeature.Select2(False, 0)
        swModel.EditSketch()
        aBasePoint(0) = 0.0#
        aBasePoint(1) = 0.0#
        aBasePoint(2) = 0.0#
        aMoveVector(0) = 0.1
        aMoveVector(1) = 0.0#
        aMoveVector(2) = 0.0#

        For lIdx = 0 To 2
            swModel.ClearSelection2(True)
            status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", -0.0752087432116777, 0.0368667656031986, 0.0146398923143701, True, 0, Nothing, 0)
            status = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", -0.0802420935887737, 0.0333695230163339, 0.019671897706856, True, 0, Nothing, 0)
            Select Case (lIdx)
                Case 0
                    ' Move
                    bCopy = False
                    lNumCopies = 0
                Case 1
                    ' Move and copy once
                    bCopy = True
                    lNumCopies = 1
                Case 2
                    ' Move and copy twice
                    bCopy = True
                    lNumCopies = 2
            End Select
            If (Not bCopy) Then
                lNumCopies = 0
            End If
            swModelDocExt.MoveOrCopy(bCopy, lNumCopies, True, aBasePoint(0), aBasePoint(1), 0.0#, aBasePoint(0) + aMoveVector(0), aBasePoint(1) + aMoveVector(1), aBasePoint(2) + aMoveVector(2))
            swModel.ClearSelection2(True)
            ' Undo so that you can do it again, but differently
            swModel.EditUndo2(1)
        Next lIdx
        swSketchMgr.InsertSketch(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
