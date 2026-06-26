---
title: "Get and Set Center Mark Set Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Center_Marks_Set_Example_VBNET.htm"
---

# Get and Set Center Mark Set Example (VB.NET)

This example shows how to get and set properties of a center mark set.

```
'------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\introtosw\pressure_plate.sldprt.
' 2. Click File > Make Drawing from Part > OK.
' 3. Drag Bottom from the View Palette to Sheet1 and click OK.
' 4. Click a center mark and press Delete.
' 5. Open the Immediate window.
'
' Postconditions:
' 1. Activates Drawing View1.
' 2. Selects a center mark in Drawing View1.
' 3. Gets and sets properties of the center mark set.
' 4. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'-----------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swDrawingDoc As DrawingDoc
        Dim swCenterMark As CenterMark
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelectionMgr As SelectionMgr
        Dim status As Boolean
        Dim nbrInGroup As Integer
        Dim i As Integer
        Dim cmCoordinates(2) As Double

        swDrawingDoc = swApp.ActiveDoc

        'Get drawing view
        swDrawingDoc.ActivateView("Drawing View1")
        swModel = swDrawingDoc
        swModelDocExt = swModel.Extension

        'Select a center mark
        status = swModelDocExt.SelectByID2("DetailItem217@Drawing View1", "CENTERMARKSYM", 0.434357613710555, 0.467612346028292, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swCenterMark = swSelectionMgr.GetSelectedObject6(1, -1)

        'Get and set properties of center mark set
        Debug.Print("Center mark set")
        Debug.Print(" Style (4 = swCenterMark_CircularGroup): " & swCenterMark.Style)
        Debug.Print(" Is grouped? " & swCenterMark.IsGrouped)
        nbrInGroup = swCenterMark.GroupCount
        Debug.Print(" Number in set: " & nbrInGroup - 1)
        Debug.Print(" Any detached? " & swCenterMark.HasDetachCenterMark)
        For i = 0 To nbrInGroup - 1
            Debug.Print("   Center mark: " & i)
            Debug.Print("      Detached: " & swCenterMark.IsDetached(i))
            cmCoordinates = swCenterMark.GetPosition(i)
            Debug.Print("      x, y, z coordinates: " & cmCoordinates(0) & ", " & cmCoordinates(1) & ", " & cmCoordinates(2))
            Debug.Print("      Original extended length: " & swCenterMark.GetExtendedLength(i, swCenterMarkHandle_e.swCenterMarkHandle_Right))
            status = swCenterMark.SetExtendedLength(i, swCenterMarkHandle_e.swCenterMarkHandle_Right, 0.005)
            Debug.Print("      Modified extended length: " & swCenterMark.GetExtendedLength(i, swCenterMarkHandle_e.swCenterMarkHandle_Right))
            Debug.Print("      Is deleted? " & swCenterMark.IsDeleted(i))
        Next i
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
