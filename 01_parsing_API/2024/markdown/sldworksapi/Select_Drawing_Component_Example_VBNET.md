---
title: "Select Drawing Component Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Drawing_Component_Example_VBNET.htm"
---

# Select Drawing Component Example (VB.NET)

This example shows how to select an assembly component in a drawing.

```
'--------------------------------------------
' Preconditions:
' 1. Open a drawing of an assembly.
' 2. Select an assembly component in the drawing.
'
' Postconditions: Displays a message box
' containing the name of the selected assembly
' component.
'---------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Dim swModelDoc As ModelDoc2
    Dim swSelMgr As SelectionMgr
    Dim swComponent As Component2
    Dim swDrawingComponent As DrawingComponent

    Sub main()

        swModelDoc = swApp.ActiveDoc
        If swModelDoc Is Nothing Then
            Exit Sub
        End If
        swSelMgr = swModelDoc.SelectionManager

        If swSelMgr.GetSelectedObjectCount2(0) = 0 Then
            MsgBox("No selections detected.")
            Exit Sub
        End If

        If swSelMgr.GetSelectedObjectType3(1, 0) = swSelectType_e.swSelCOMPONENTS Then
            swDrawingComponent = swSelMgr.GetSelectedObjectsComponent4(1, 0) 'works
            If swDrawingComponent Is Nothing Then
                MsgBox("The component is empty.")
                Exit Sub
            Else
                swComponent = swDrawingComponent.Component
                MsgBox(swComponent.Name2)
            End If
        Else
            MsgBox("The selection is not an assembly component.")
            Exit Sub
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
