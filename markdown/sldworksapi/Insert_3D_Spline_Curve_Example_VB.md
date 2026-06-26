---
title: "Insert 3D-Spline Curve Example VB"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_3D_Spline_Curve_Example_VB.htm"
---

# Insert 3D-Spline Curve Example VB

## Insert a 3D-Spline Curve Example (VBA)

This example shows how to insert an open 3D-spline curve.

```
'-----------------------------------------------
' Preconditions:
' 1. Open a new part document.
' 2. Open a sketch and insert sketch points for
'    the spline.
' 3. Close the sketch.
' 4. Select the sketch points.
' 5. Open the Immediate window.
'
' Postconditions:
' 1. Creates a 3D-spline curve.
' 2. Examine the graphics area and Immediate window.
'-----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim nSelCount As Long
    Dim i As Long
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
```

```
    nSelCount = swSelMgr.GetSelectedObjectCount
    Debug.Print "SelCount (before) = " + Str(nSelCount)
    For i = 1 To nSelCount
        Debug.Print "   SelType(" + Str(i) + ") = " + Str(swSelMgr.GetSelectedObjectType(i))
    Next i
```

```
    swModel.Insert3DSplineCurve False
```

```
    nSelCount = swSelMgr.GetSelectedObjectCount
    Debug.Print "SelCount (after ) = " + Str(nSelCount)
    For i = 1 To nSelCount
        Debug.Print "   SelType(" + Str(i) + ") = " + Str(swSelMgr.GetSelectedObjectType(i))
    Next i
```

```
End Sub
```
