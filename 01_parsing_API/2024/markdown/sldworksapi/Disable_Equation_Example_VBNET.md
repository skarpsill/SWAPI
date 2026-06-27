---
title: "Disable Equation Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Disable_Equation_Example_VBNET.htm"
---

# Disable Equation Example (VB.NET)

This example shows how to disable an equation.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\partequations.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Disables an equation.
' 2. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swEqnMgr As EquationMgr
        Dim i As Integer
        Dim count As Integer
        Dim disabledCount As Integer

        swModel = swApp.ActiveDoc
        swEqnMgr = swModel.GetEquationMgr
        count = swEqnMgr.GetCount
        Debug.Print("Number of equations in part = " & count)
        For i = 0 To count - 1
            Debug.Print("  Eqn(" & i & ")  = " & swEqnMgr.Equation(i))
        Next i

        Debug.Print("")

        disabledCount = swEqnMgr.GetDisabledEquationCount
        Debug.Print("Number of disabled equations in part before running macro = " & disabledCount)

        swEqnMgr.Disabled(count - 1) = True
        Debug.Print("Eqn(" & (count - 1) & ") disabled? " & swEqnMgr.Disabled(count - 1))

        disabledCount = swEqnMgr.GetDisabledEquationCount
        Debug.Print("Number of disabled equations in part after running macro = " & disabledCount)

        Debug.Print("")

        count = swEqnMgr.GetCount
        Debug.Print("Number of equations in part = " & count)
        For i = 0 To count - 1
            Debug.Print("  Eqn(" & i & ")  = " & swEqnMgr.Equation(i))
        Next i

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
