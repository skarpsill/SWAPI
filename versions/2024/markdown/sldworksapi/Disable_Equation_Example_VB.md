---
title: "Disable Equation Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Disable_Equation_Example_VB.htm"
---

# Disable Equation Example (VBA)

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
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swEqnMgr  As SldWorks.EquationMgr
    Dim i As Long
    Dim count As Long
    Dim disabledCount As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swEqnMgr = swModel.GetEquationMgr
    count = swEqnMgr.GetCount
    Debug.Print "Number of equations in part = " & count
    For i = 0 To count - 1
        Debug.Print "  Eqn(" & i & ")  = " & swEqnMgr.Equation(i)
    Next i
```

```
    Debug.Print ""
```

```
    disabledCount = swEqnMgr.GetDisabledEquationCount
    Debug.Print "Number of disabled equations in part before running macro = " & disabledCount
```

```
    swEqnMgr.Disabled(count - 1) = True
    Debug.Print "Eqn(" & (count - 1) & ") disabled? " & swEqnMgr.Disabled(count - 1)
```

```
    disabledCount = swEqnMgr.GetDisabledEquationCount
    Debug.Print "Number of disabled equations in part after running macro = " & disabledCount
```

```
    Debug.Print ""
```

```
    count = swEqnMgr.GetCount
    Debug.Print "Number of equations in part = " & count
    For i = 0 To count - 1
        Debug.Print "  Eqn(" & i & ")  = " & swEqnMgr.Equation(i)
    Next i
```

```
End Sub
```
