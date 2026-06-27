---
title: "Create Infinite Plane Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Infinite_Plane_Example_VB.htm"
---

# Create Infinite Plane Example (VBA)

This example shows how to create an infinite plane.

```
'-------------------------------------------
' Preconditions:
' 1. Open a model document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates an infinite plane.
' 2. Examine the Immediate window.
'--------------------------------------------
Option Explicit
```

```
' Define two types
Type DoubleRec
    dValue As Double
End Type
```

```
Type Long2Rec
    iLower As Long
    iUpper As Long
End Type
```

```
' Extract two integer values from a single double value
' by assigning a DoubleRec to the double value and
' copying the value to a Long2Rec and
' extracting the integer values
Function ExtractFields(ByVal dValue As Double, iLower As Integer, iUpper As Integer)
Dim dr As DoubleRec
    Dim i2r As Long2Rec
    ' Set the double value
    dr.dValue = dValue
    ' Copy the values
    LSet i2r = dr
    ' Extract the values
    iLower = i2r.iLower
    iUpper = i2r.iUpper
End Function
```

```
Sub ProcessSurface(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swSurf As SldWorks.Surface)
    Dim vSurfParam As Variant
    Dim uBboundType(2) As Integer
    Dim vBboundType(2) As Integer
    Dim Num_uProp As Integer
    Dim Num_vProp As Integer
    Dim uProp(4) As Integer
    Dim vProp(4) As Integer
    Dim i As Integer
```

```
    vSurfParam = swSurf.Parameterization
    ExtractFields vSurfParam(4), uBboundType(1), uBboundType(2)
    ExtractFields vSurfParam(5), vBboundType(1), vBboundType(2)
    ExtractFields vSurfParam(10), Num_uProp, Num_vProp
    ExtractFields vSurfParam(6), uProp(1), uProp(2)
    ExtractFields vSurfParam(7), uProp(3), uProp(4)
    ExtractFields vSurfParam(8), vProp(1), vProp(2)
    ExtractFields vSurfParam(9), vProp(3), vProp(4)
```

```
    Debug.Print "  uRange       = [" & vSurfParam(0) & " , " & vSurfParam(1) & "]"
    Debug.Print "  uBoundType   = [" & uBboundType(1) & " , " & uBboundType(2) & "]"
    Debug.Print "  Num_uProp    = " & Num_uProp
```

```
    For i = 1 To Num_uProp
        Debug.Print "    uProp[" & i & "]   = " & uProp(i)
    Next i
```

```
    Debug.Print ""
```

```
    Debug.Print "  vRange       = [" & vSurfParam(2) & " , " & vSurfParam(3) & "]"
    Debug.Print "  vBoundType   = [" & vBboundType(1) & " , " & vBboundType(2) & "]"
    Debug.Print "  Num_vProp    = " & Num_vProp
```

```
    For i = 1 To Num_vProp
        Debug.Print "    vProp[" & i & "]   = " & vProp(i)
    Next i
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModeller As SldWorks.Modeler
    Dim swSurf As SldWorks.Surface
    Dim BasePt(2) As Double
    Dim Normal(2) As Double
    Dim Xvect(2) As Double
    Dim vBasePt As Variant
    Dim vNormal As Variant
    Dim vXvect As Variant
    Dim vPlane As Variant
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModeller = swApp.GetModeler
```

```
    BasePt(0) = 0#:     BasePt(1) = 0#:     BasePt(2) = 0#
    vBasePt = BasePt
```

```
    Normal(0) = 0#:     Normal(1) = 0#:     Normal(2) = 1#
    vNormal = Normal
```

```
    Xvect(0) = 1#:      Xvect(1) = 0#:      Xvect(2) = 0#
    vXvect = Xvect
```

```
    Set swSurf = swModeller.CreatePlanarSurface2((vBasePt), (vNormal), (vXvect))
```

```
    Debug.Assert Not swSurf Is Nothing
    Debug.Assert swSurf.IsPlane
```

```
    vPlane = swSurf.PlaneParams
    Debug.Print "SW Version = " & swApp.RevisionNumber
    Debug.Print "  normal       = (" & vPlane(0) & ", " & vPlane(1) & ", " & vPlane(2) & ")"
    Debug.Print "  root         = (" & vPlane(3) * 1000# & ", " & vPlane(4) * 1000# & ", " & vPlane(5) * 1000# & ") mm"
```

```
    Debug.Print ""
```

```
    ProcessSurface swApp, Nothing, swSurf
```

```
End Sub
```
