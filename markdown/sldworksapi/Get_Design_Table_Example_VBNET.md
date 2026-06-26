---
title: "Get Design Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Design_Table_Example_VBNET.htm"
---

# Get Design Table Example (VB.NET)

This example shows how to get a design table and its contents.

```
'---------------------------------------
' Preconditions:
' 1. Open a part or assembly document that
'    contains a design table.
' 2. Verify that a design table exists by
'    expanding Tables in the ConfigurationManager.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Prints the design table contents to the
'    Immediate window.
' 2. Examine the Immediate window.
'----------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swDesTable As DesignTable
        Dim nTotRow As Integer
        Dim nTotCol As Integer
        Dim sRowStr As String
        Dim i As Integer
        Dim j As Integer
        Dim bRet As Boolean

        swModel = swApp.ActiveDoc

        swDesTable = swModel.GetDesignTable
        bRet = swDesTable.Attach

        nTotRow = swDesTable.GetTotalRowCount
        nTotCol = swDesTable.GetTotalColumnCount
        Debug.Print("File = " & swModel.GetPathName)
        Debug.Print("  Title        = " & swDesTable.GetTitle)
        Debug.Print("  Row          = " & swDesTable.GetRowCount)
        Debug.Print("  Col          = " & swDesTable.GetColumnCount)
        Debug.Print("  TotRow       = " & nTotRow)
        Debug.Print("  TotCol       = " & nTotCol)
        Debug.Print("  VisRow       = " & swDesTable.GetVisibleRowCount)
        Debug.Print("  VisCol       = " & swDesTable.GetVisibleColumnCount)
        Debug.Print("")

        For i = 0 To nTotRow
            sRowStr = "  |"
            For j = 0 To nTotCol
                sRowStr = sRowStr + swDesTable.GetEntryText(i, j) + "|"
            Next j
            Debug.Print(sRowStr)
        Next i
        swDesTable.Detach()
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
