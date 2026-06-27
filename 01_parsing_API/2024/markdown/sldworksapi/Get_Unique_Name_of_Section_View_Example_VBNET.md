---
title: "Get Unique Name of Section View Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Unique_Name_of_Section_View_Example_VBNET.htm"
---

# Get Unique Name of Section View Example (VB.NET)

This example shows how to get the unique name of a section view.

```
'----------------------------------------------------------------------
' Preconditions:
' 1. Open a drawing document with three views,
'    two of which are section views with the
'    same display name.
' 2. Open the Immediate window.
'
' Postconditions: Inspect the Immediate window
' for the display names and internal unique names
' of the section views.
'---------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swDraw As DrawingDoc
        Dim swSheet As Sheet
        Dim swView As View
        Dim boolstat As Boolean
        Dim selMgr As SelectionMgr
        Dim sectionView As View

        swModel = swApp.ActiveDoc
        selMgr = swModel.SelectionManager
        swDraw = swModel
        swSheet = swDraw.GetCurrentSheet

        ' Get the section views
        swView = swDraw.GetFirstView
        While (Not swView Is Nothing)
            If (swView.Type = swDrawingViewTypes_e.swDrawingSectionView) Then

                ' Print the section view's display name
                Debug.Print("Display name: " & swView.GetName2)

                swModel.ClearSelection2(True)

                boolstat = swModel.Extension.SelectByID2(swView.GetUniqueName, "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
                sectionView = selMgr.GetSelectedObject6(1, -1)

                ' Print the section view's unique name
                Debug.Print("Unique name: " & sectionView.GetUniqueName)

                swModel.ClearSelection2(True)
                Debug.Print("")
            End If

            swView = swView.GetNextView
        End While

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
