---
title: "Get Equation Values Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Equation_Values_Example_VB.htm"
---

# Get Equation Values Example (VBA)

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
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swEqnMgr As SldWorks.EquationMgr
    Dim i As Long
    Dim nCount As Long

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swEqnMgr = swModel.GetEquationMgr
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    nCount = swEqnMgr.GetCount
    For i = 0 To nCount - 1
        Debug.Print "  Equation(" & i & ")  = " & swEqnMgr.Equation(i)
        Debug.Print "    Value = " & swEqnMgr.Value(i)
        Debug.Print "    Index = " & swEqnMgr.Status
        Debug.Print "    Global variable? " & swEqnMgr.GlobalVariable(i)
    Next i
```

```
End Sub
```
