---
title: "Get Text Items in GTol Frame Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Text_Items_in_GTol_Frame_Example_VBNET.htm"
---

# Get Text Items in GTol Frame Example (VB.NET)

This example shows how to get text items, values, and symbols in a GTol frame.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Open a document with a GTol frame and select that GTol
'    frame.
' 2. Open an Immediate window.
'
' Postconditions:
' 1. Gets the text items, values, and symbols in the
'    selected GTol frame.
' 2. Examine the Immediate window.
'-------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Diagnostics
Imports System

Partial Public Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelMgr As SelectionMgr
        Dim swGtol As Gtol

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        swSelMgr = swModel.SelectionManager
        swGtol = swSelMgr.GetSelectedObject6(1, -1)

        Debug.Print("GetTextCount = " & swGtol.GetTextCount().ToString())

        For idx As Integer = 0 To swGtol.GetTextCount() - 1
            Debug.Print(("GetTextAtIndex(" & idx.ToString() & ") = ") + swGtol.GetTextAtIndex(idx))
        Next

        Debug.Print("GetFrameCount = " & (swGtol.GetFrameCount().ToString()) - 1)

        For idx As Integer = 1 To swGtol.GetFrameCount() - 1
            Dim myParams As Object
            Dim arrSymbols As Object
            myParams = swGtol.GetFrameValues(idx)
            If myParams IsNot Nothing Then
                Debug.Print(((((("GetFrameValues(" & idx.ToString() & ") = ") & myParams.GetValue(0) & ",") & myParams.GetValue(1) & ",") & myParams.GetValue(2) & ",") & myParams.GetValue(3) & ",") & myParams.GetValue(4))
                arrSymbols = swGtol.GetFrameSymbols3(idx)
                Debug.Print(((((((("  GetFrameSymbols3(" & idx.ToString() & ") = ") & arrSymbols(0) & ", " & arrSymbols(1) & ", " & arrSymbols(2) & ", " & arrSymbols(3) & ", " & arrSymbols(4) & ", " & arrSymbols(5) & ")")))))))
            End If
        Next

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
     Public swApp As SldWorks

End Class
```
