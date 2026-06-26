---
title: "Get Arcs in Sketch Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Arcs_in_Sketch_Example_VB.htm"
---

# Get Arcs in Sketch Example (VBA)

This example shows how to get the arcs in a sketch.

```
'-------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\cstick.sldprt.
' 2. Expand Revolve1 in the FeatureManager design tree
'    and select Sketch1.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets all of the arcs in the sketch and their
'    information.
' 2. Examine the Immediate window.
'--------------------------------------------------
Option Explicit
```

```
Public Enum swLineTypes_e
    swLF_VISIBLE = 0
    swLF_HIDDEN = 1
    swLF_SKETCH = 2
    swLF_DETAIL = 3
    swLF_SECTION = 4
    swLF_DIMENSION = 5
    swLF_CENTER = 6
    swLF_HATCH = 7
    swLF_TANGENT = 8
End Enum
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swSketch As SldWorks.Sketch
    Dim NumArcs As Long
    Dim vArcs As Variant
    Dim i As Variant
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    Set swSketch = swFeat.GetSpecificFeature
    NumArcs = swSketch.GetArcCount
    Debug.Print "Feature = " & swFeat.GetTypeName
    Debug.Print "  NumArcs = " & NumArcs
    Debug.Print ""
```

```
    vArcs = swSketch.GetArcs2
    If IsEmpty(vArcs) Then Exit Sub
```

```
    Debug.Assert UBound(vArcs) + 1 = 16 * NumArcs
    For i = 0 To NumArcs - 1
        Debug.Print "    Arc(" & i & ")"
        Debug.Print "      colour         = " & vArcs(16 * i + 0)
        Debug.Print "      type           = " & vArcs(16 * i + 1)
        Debug.Print "      font           = " & vArcs(16 * i + 2)
        Debug.Print "      width          = " & vArcs(16 * i + 3)
        Debug.Print "      layerID        = " & vArcs(16 * i + 4)
        Debug.Print "      layer override = " & vArcs(16 * i + 5)
        Debug.Print "      start          = (" & vArcs(16 * i + 6) * 1000# & ", " & vArcs(16 * i + 7) * 1000# & ", " & vArcs(16 * i + 8) * 1000# & ") mm"
        Debug.Print "      end            = (" & vArcs(16 * i + 9) * 1000# & ", " & vArcs(16 * i + 10) * 1000# & ", " & vArcs(16 * i + 11) * 1000# & ") mm"
        Debug.Print "      ctr            = (" & vArcs(16 * i + 12) * 1000# & ", " & vArcs(16 * i + 13) * 1000# & ", " & vArcs(16 * i + 14) * 1000# & ") mm"
        Debug.Print "      RotDir         = " & vArcs(16 * i + 15)
```

```
    Next i
```

```
End Sub
```
