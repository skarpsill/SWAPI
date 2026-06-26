---
title: "Evaluate Points on Surface Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Evaluate_Points_on_Surface_Example_VB.htm"
---

# Evaluate Points on Surface Example (VBA)

This example shows how to evaluate points on a surface.

```
'---------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Select a face.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Evaluates the selection point on the
'    selected face.
' 2. Examine the Immediate window.
'----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFace As SldWorks.Face2
    Dim swSurf As SldWorks.Surface
    Dim vSelPt As Variant
    Dim vClosePt As Variant
    Dim vEval As Variant
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFace = swSelMgr.GetSelectedObject5(1)
    Set swSurf = swFace.GetSurface
    vSelPt = swSelMgr.GetSelectionPoint(1)
    vClosePt = swSurf.GetClosestPointOn(vSelPt(0), vSelPt(1), vSelPt(2))
    vEval = swSurf.EvaluateAtPoint(vClosePt(0), vClosePt(1), vClosePt(2))
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Sel Pt       = (" & vSelPt(0) * 1000 & ", " & vSelPt(1) * 1000 & ", " & vSelPt(2) * 1000 & ") mm"
    Debug.Print "  Close Pt     = (" & vClosePt(0) * 1000 & ", " & vClosePt(1) * 1000 & ", " & vClosePt(2) * 1000 & ") mm"
    Debug.Print "    Close U-V  = [" & vClosePt(3) & ", " & vClosePt(4) & "]"
    Debug.Print "  Normal       = (" & vEval(0) & ", " & vEval(1) & ", " & vEval(2) & ")"
    Debug.Print "  Dirn 1       = (" & vEval(3) & ", " & vEval(4) & ", " & vEval(5) & ")"
    Debug.Print "  Dirn 2       = (" & vEval(6) & ", " & vEval(7) & ", " & vEval(8) & ")"
    Debug.Print "  Curvat 1     = " & vEval(9)
    Debug.Print "  Curvat 2     = " & vEval(10)
```

```
End Sub
```
