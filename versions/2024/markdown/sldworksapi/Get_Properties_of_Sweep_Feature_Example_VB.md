---
title: "Get Properties of Sweep Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Properties_of_Sweep_Feature_Example_VB.htm"
---

# Get Properties of Sweep Feature Example (VBA)

This example shows how to get the properties of a sweep feature.

```
'------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\cstick.sldprt.
' 2. Select Sweep1.
'
' Postconditions: Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not
' save changes.
'------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swSweep As SldWorks.SweepFeatureData
    Dim swProfFeat As SldWorks.Feature
    Dim swProfSketch As SldWorks.Sketch
    Dim swPathFeat As SldWorks.Feature
    Dim swPathSketch As SldWorks.Sketch
    Dim vGuideCurvesTypeArr As Variant
    Dim vGuideCurvesType As Variant
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject5(1)
    Set swSweep = swFeat.GetDefinition
    Set swProfFeat = swSweep.Profile
    Set swProfSketch = swProfFeat.GetSpecificFeature

    bRet = swSweep.AccessSelections(swModel, Nothing)
    Set swPathFeat = swSweep.Path
    Set swPathSketch = swPathFeat.GetSpecificFeature
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  " & swFeat.Name
    Debug.Print "    Sweep path = " & swPathFeat.Name
    Debug.Print "    Sweep path type = " & swSweep.GetPathType
    Debug.Print "    Profile = " & swProfFeat.Name
    Debug.Print "    Profile type as defined in swSelectType_e = " & swSweep.GetProfileType
    Debug.Print "    Profile orientation/twist type as defined in swTwistControlType_e = " & swSweep.TwistControlType
    Debug.Print "    Path alignment type as defined in swTangencyType_e = " & swSweep.PathAlignmentType
    Debug.Print "    Align sweep with end faces? " & swSweep.AlignWithEndFaces
    Debug.Print "    Automatically select all bodies in a multibody part? " & swSweep.AutoSelect
    Debug.Print "    Type of tangency at the sweep's end as defined in swTangencyType_e = " & swSweep.EndTangencyType
    Debug.Print "    Type of tangency at the sweep's start as defined in swTangencyType_e = " & swSweep.StartTangencyType

    Debug.Print "    Is a boss sweep? " & swSweep.IsBossFeature
    Debug.Print "    Is a thin-walled sweep feature?  " & swSweep.IsThinFeature
    Debug.Print "    Thin-walled type (0=1D, 1=1DReverse, 2=MidPlane, 3=2D) = " & swSweep.ThinWallType
    Debug.Print "    Wall thickness in Direction 1 = " & swSweep.GetWallThickness(True) * 1000# & " mm"
    Debug.Print "    Wall thickness in Direction 2 = " & swSweep.GetWallThickness(False) * 1000# & " mm"
    Debug.Print "    Merge tangent faces?  " & swSweep.MaintainTangency
    Debug.Print "    Merge results for a multibody part?  " & swSweep.Merge
    Debug.Print "    Merge smooth faces if using guide curves? " & swSweep.MergeSmoothFaces

    vGuideCurvesTypeArr = swSweep.GetGuideCurvesType

    If Not IsEmpty(vGuideCurvesTypeArr) Then
        Debug.Print "    Number of guide curves  = " & UBound(vGuideCurvesTypeArr) + 1
        For Each vGuideCurvesType In vGuideCurvesTypeArr
            Debug.Print "      Type as defined in swSelectType_e  = " & vGuideCurvesType
        Next vGuideCurvesType
    End If

    swSweep.ReleaseSelectionAccess
```

```
End Sub
```
