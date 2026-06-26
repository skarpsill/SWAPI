---
title: "Merge and Unmerge Bend Tags Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Merge_and_Unmerge_Bend_Tags_Example_VBNET.htm"
---

# Merge and Unmerge Bend Tags Example (VB.NET)

This example shows how to merge and unmerge bend tags in a drawing.

```
'---------------------------------------------------------------
' Preconditions:
' 1. The specified drawing document exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. The specified drawing document opens.
' 2. Press F5 repeatedly after examining the changes
'    in the bend tags and the output in the Immediate window.
'---------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelectionMgr As SelectionMgr
        Dim swNote As Note
        Dim swView As View
        Dim swDrawingDoc As DrawingDoc
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer, warnings As Integer
        Dim noteList(1) As Note

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\2012-sm.slddrw"
        swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModel = swApp.ActiveDoc
        swSelectionMgr = swModel.SelectionManager
        swModelDocExt = swModel.Extension

        Stop
        ' Locate the bend tags (A, B, C, and D)
        ' in the drawing
        ' Press F5 to continue

        ' Select a bend tag to merge
        status = swModelDocExt.SelectByID2("DetailItem37@Drawing View1", "NOTE", 0.0902750427561398, 0.24484926035503, 0, False, 0, Nothing, 0)
        swNote = swSelectionMgr.GetSelectedObject6(1, 0)
        noteList(0) = swNote
        Debug.Print("Is a bendline note? " & swNote.IsBendLineNote)
        swModel.ClearSelection2(True)

        ' Select another bend tag with which to merge
        ' the previously selected bend tag
        status = swModelDocExt.SelectByID2("DetailItem38@Drawing View1", "NOTE", 0.0978933563656073, 0.244401124260355, 0, True, 0, Nothing, 0)
        swNote = swSelectionMgr.GetSelectedObject6(1, 0)
        noteList(1) = swNote
        Debug.Print("Is a bendline note? " & swNote.IsBendLineNote)
        swModel.ClearSelection2(True)

        ' Select the drawing view in which to
        ' merge bend tags
        status = swModelDocExt.SelectByID2("Drawing View1", "DRAWINGVIEW", 0.0765893917313017, 0.16302919597189, 0, False, 0, Nothing, 0)
        swView = swSelectionMgr.GetSelectedObject6(1, 0)
        swModel.ClearSelection2(True)

        'Merge the selected bend tags
        status = swView.MergeBendTags(True, noteList)

        swModel.EditRebuild3()

        Stop
        ' Verify that bend tag A and B merged into
        ' bend tag A, bend tag C was renamed to B,
        ' and bend tag D was renamed to C
        ' Press F5 to continue

        ' Select the merged bend tag
        swDrawingDoc = swModel
        status = swDrawingDoc.ActivateView("Drawing View1")
        status = swModelDocExt.SelectByID2("DetailItem38@Drawing View1", "NOTE", 0.098037379978424, 0.245097849056604, 0, False, 0, Nothing, 0)
        swNote = swSelectionMgr.GetSelectedObject6(1, 0)
        noteList(0) = swNote

        ' Unmerge the merged bend tag
        swView.MergeBendTags(False, noteList)

        Stop
        ' Verify that bend tag A and B unmerged,
        ' bend tag B was renamed back to C, and bend tag C
        ' was renamed back to D
        ' Press F5 to finish

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
