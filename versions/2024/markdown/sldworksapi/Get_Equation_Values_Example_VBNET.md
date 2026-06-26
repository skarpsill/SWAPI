---
title: "Get Equation Values Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Equation_Values_Example_VBNET.htm"
---

# Get Equation Values Example (VB.NET)

This example shows how to get the values of equations.

```
'-----------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\partequations.sldprt.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets each equation's value and index and whether the
'    equation is a global variable.
' 2. Examine the Immediate window.
'------------------------------------------
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
        Dim nCount As Integer

        swModel = swApp.ActiveDoc
        swEqnMgr = swModel.GetEquationMgr
        Debug.Print("File = " & swModel.GetPathName)
        nCount = swEqnMgr.GetCount
        For i = 0 To nCount - 1
            Debug.Print("  Equation(" & i & ")  = " & swEqnMgr.Equation(i))
            Debug.Print("    Value = " & swEqnMgr.Value(i))
            Debug.Print("    Index = " & swEqnMgr.Status)
            Debug.Print("    Global variable? " & swEqnMgr.GlobalVariable(i))
        Next i

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
