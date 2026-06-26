---
title: "Get Chamfer Dimension Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Chamfer_Dimension_Example_VB.htm"
---

# Get Chamfer Dimension Example (VBA)

This example shows how to the values of a chamfer dimension.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open a drawing that contains a chamfered part.
' 2. Click Tools > Dimension > Chamfer.
' 3. Select a chamfered edge, select one of the lead-in edges, and click
'    the drawing to display and select the chamfer dimension.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Gets the chamfer dimensions.
' 2. Examine the Immediate window.
'---------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swDisplayDimension As SldWorks.DisplayDimension
    Dim swDimension As SldWorks.Dimension
    Dim status As Boolean
    Dim length As Double
    Dim angle As Double
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
    Set swSelMgr = swModel.SelectionManager
```

```
    'Get chamfer dimensions
    Set swDisplayDimension = swSelMgr.GetSelectedObject6(1, -1)
    Set swDimension = swDisplayDimension.GetDimension
    status = swDimension.GetSystemChamferValues(length, angle)
    Debug.Print "Is selected dimension a chamfer dimension? " & status
    '1 radian = 180º/p = 57.295779513º or approximately 57.3º
    Debug.Print "Angle = " & (angle * 57.3) & " degrees"
    Debug.Print "Length = " & length
```

```
End Sub
```
