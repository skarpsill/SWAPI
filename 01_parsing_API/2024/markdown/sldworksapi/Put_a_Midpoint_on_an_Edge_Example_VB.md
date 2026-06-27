---
title: "Select the Midpoint of an Edge Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Put_a_Midpoint_on_an_Edge_Example_VB.htm"
---

# Select the Midpoint of an Edge Example (VBA)

This example shows how to select the midpoint of an edge.

```
'-------------------------------------------------------
' Preconditions:
' 1. Open a part document.
' 2. Select an edge.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Puts a midpoint on the selected edge.
' 2. Place the cursor on the selected edge to see the
'    midpoint.
' 3. Examine the Immediate window.
'------------------------------------------------------
Option Explicit
```

```
Const swSelEDGES As Long = 1
Const swSelREFERENCECURVES As Long = 26
Const swSelPOINTREFS As Long = 41
Const swSelREFEDGES As Long = 51
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim nSelType As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
    Set swSelMgr = swModel.SelectionManager
```

```
    nSelType = swSelMgr.GetSelectedObjectType3(1, -1)
    Debug.Print "SelType (before) = " + Str(nSelType)
```

```
    swModel.SelectMidpoint
```

```
    nSelType = swSelMgr.GetSelectedObjectType3(1, -1)
    Debug.Print "SelType (after ) = " + Str(nSelType)
```

```
End Sub
```
