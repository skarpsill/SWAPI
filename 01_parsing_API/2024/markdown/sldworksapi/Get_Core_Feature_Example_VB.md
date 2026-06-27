---
title: "Get Core Feature Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Core_Feature_Example_VB.htm"
---

# Get Core Feature Data Example (VBA)

This example shows how to get the data for a core feature.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Open a model document that contains a core feature.
' 2. Open the Immediate window.
' 3. Select the core feature in the FeatureManager design tree.
'
' Postconditions:
' 1. Prints the core feature data to the Immediate window.
' 2. Examine the Immediate window.
'--------------------------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat As Feature
Dim swCoreFeat As SldWorks.CoreFeatureData
Dim b As Boolean
Dim nam As String
Dim cap As Boolean
Dim d1 As Double
Dim d2 As Double
Dim ang As Double
Dim useDr As Boolean
Dim Drout As Boolean
Dim rev As Boolean
Dim typ1 As Long
Dim typ2 As Long
Dim dir1 As Object
Dim dir2 As Object
Dim e1 As Long
Dim e2 As Long
Dim ct As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set swCoreFeat = swFeat.GetDefinition
```

```
    'Roll back to the feature before the core feature
    b = swCoreFeat.AccessSelections(swModel, Nothing)
```

```
    'Get the bounding sketch of the core feature
    Set swFeat = swCoreFeat.BoundingSketch
    nam = swFeat.Name
    Debug.Print "Name of bounding sketch = " & nam
    cap = swCoreFeat.CapEnds
    Debug.Print "Are ends capped? " & cap
    d1 = swCoreFeat.Depth(0)
    Debug.Print "Depth along extraction direction = " & d1
    d2 = swCoreFeat.Depth(1)
    Debug.Print "Depth away from extraction direction = " & d2
    useDr = swCoreFeat.UseDraft
    Debug.Print "Drafted? " & useDr
    If useDr Then
        ang = swCoreFeat.DraftAngle
        Debug.Print "Angle of draft = " & ang
        Drout = swCoreFeat.DraftOutward
        Debug.Print "Drafted outward? = " & Drout
    End If
    e1 = swCoreFeat.EndCondition(0)
    Debug.Print "End condition along extraction = " & e1
    e2 = swCoreFeat.EndCondition(1)
    Debug.Print "End condition away from extraction = " & e2
    rev = swCoreFeat.ReverseDirection
    Debug.Print "Direction of extraction reversed? " & rev
    ct = swCoreFeat.GetExtractionDirection(typ1, dir1, typ2, dir2)
    Debug.Print "Number of entities that define extraction = " & ct
```

```
    'Roll forward
    swCoreFeat.ReleaseSelectionAccess
```

```
End Sub
```
