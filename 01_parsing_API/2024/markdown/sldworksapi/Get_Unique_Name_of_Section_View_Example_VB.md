---
title: "Get Unique Name of Section View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Unique_Name_of_Section_View_Example_VB.htm"
---

# Get Unique Name of Section View Example (VBA)

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
Option Explicit
```

```vb
Sub main()
    Dim swApp                   As SldWorks.SldWorks
     Dim swModel                 As SldWorks.ModelDoc2
     Dim swDraw                  As SldWorks.DrawingDoc
     Dim swSheet                 As SldWorks.Sheet
     Dim swView                  As SldWorks.view
     Dim boolstat                As Boolean
     Dim selMgr                  As SldWorks.SelectionMgr
     Dim view                    As SldWorks.view
    Set swApp = CreateObject("SldWorks.Application")
     Set swModel = swApp.ActiveDoc
     Set selMgr = swModel.SelectionManager
     Set swDraw = swModel
     Set swSheet = swDraw.GetCurrentSheet

    ' Get the section views
     Set swView = swDraw.GetFirstView
     While (Not swView Is Nothing)
         If (swView.Type = swDrawingSectionView) Then

            ' Print the section view's display name
             Debug.Print "Display name: " & swView.GetName2

            swModel.ClearSelection2 True

            boolstat = swModel.Extension.SelectByID2(swView.GetUniqueName, "DRAWINGVIEW", 0, 0, 0, False, 0, Nothing, 0)
             Set view = selMgr.GetSelectedObject6(1, -1)

            ' Print the section view's unique name
             Debug.Print "Unique name: " & view.GetUniqueName
            swModel.ClearSelection2 True
             Debug.Print ""
         End If

        Set swView = swView.GetNextView
     Wend

End Sub
```
