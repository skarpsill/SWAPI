---
title: "Get Angle of Hole Not Normal to a Face Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Angle_of_Hole_Not_Normal_to_a_Face_Example_VB.htm"
---

# Get Angle of Hole Not Normal to a Face Example (VBA)

This example shows how to get the angle of a hole not normal to a face.

```
'-----------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\cover_datum.sldprt.
' 2. Select the edge of a hole that enters the part on a flat face.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Click Continue at each Debug.Assert statement.
' 2. Gets an angle in the first quadrant, which should be
'    the angle measured between the hole axis and face
'    normal.
' 3. Examine the Immediate window.
'-----------------------------------------------------------
Option Explicit
```

```
Const PI As Double = 3.14159265358979
```

```
Function Arccos(X As Double) As Double
    If Abs(1# - X) < 0.00000001 Then Arccos = PI / 2#: Exit Function
    Arccos = Atn(-X / Sqr(-X * X + 1)) + 2 * Atn(1)
End Function
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swMathUtil As SldWorks.MathUtility
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swEdge As SldWorks.Edge
    Dim vFace As Variant
    Dim swFace(1) As SldWorks.Face2
    Dim swSurf(1) As SldWorks.Surface
    Dim swCylSurf As SldWorks.Surface
    Dim swFlatSurf  As SldWorks.Surface
    Dim vCylinder As Variant
    Dim vPlane As Variant
    Dim nVector(2) As Double
    Dim vVector As Variant
    Dim i As Long
    Dim swCylAxis As SldWorks.MathVector
    Dim swFlatNorm As SldWorks.MathVector
    Dim nDotProd As Double
    Dim nAngle As Double
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swMathUtil = swApp.GetMathUtility
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swEdge = swSelMgr.GetSelectedObject6(1, -1)
```

```
    vFace = swEdge.GetTwoAdjacentFaces2
    Set swFace(0) = vFace(0)
    Set swFace(1) = vFace(1)
    Set swSurf(0) = swFace(0).GetSurface
    Set swSurf(1) = swFace(1).GetSurface
```

```
    If swSurf(0).IsCylinder Then
        Set swCylSurf = swSurf(0)
        Set swFlatSurf = swSurf(1)
    Else
        Debug.Assert swSurf(0).IsPlane
        Debug.Assert swSurf(1).IsCylinder
        Set swCylSurf = swSurf(1)
        Set swFlatSurf = swSurf(0)
    End If
```

```
    vCylinder = swCylSurf.CylinderParams
    vPlane = swFlatSurf.PlaneParams
```

```
    nVector(0) = vCylinder(3):  nVector(1) = vCylinder(4):  nVector(2) = vCylinder(5)
    vVector = nVector
    Set swCylAxis = swMathUtil.CreateVector((vVector))
    nVector(0) = vPlane(0):     nVector(1) = vPlane(1):     nVector(2) = vPlane(2)
    vVector = nVector
    Set swFlatNorm = swMathUtil.CreateVector((vVector))
    nDotProd = swCylAxis.Dot(swFlatNorm)
```

```
    ' Ensure angle is in first quadrant
    nAngle = Arccos(Abs(nDotProd)) * 180# / PI
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  cylinder origin = (" & vCylinder(0) * 1000# & ", " & vCylinder(1) * 1000# & ", " & vCylinder(2) * 1000# & ") mm"
    Debug.Print "  cylinder axis   = (" & vCylinder(3) & ", " & vCylinder(4) & ", " & vCylinder(5) & ")"
    Debug.Print "  cylinder radius = " & vCylinder(6) * 1000# & " mm"
    Debug.Print "  flat normal     = (" & vPlane(0) & ", " & vPlane(1) & ", " & vPlane(2) & ")"
    Debug.Print "  flat root       = (" & vPlane(3) * 1000# & ", " & vPlane(4) * 1000# & ", " & vPlane(5) * 1000# & ") mm"
    Debug.Print "  angle           = " & nAngle & " deg"
```

```
End Sub
```
