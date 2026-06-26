---
title: "Get and Fill Gaps in Body Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Fill_Gaps_in_Body_Example_VB.htm"
---

# Get and Fill Gaps in Body Example (VBA)

This example shows how to get and fill the gaps in a body.

```
'---------------------------------------------------------------
' Preconditions:
' 1. Open a model document that contains at least one body
'    with one or more gaps.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Identifies the number of gaps in each
'    body and fills each gap with a fill-surface
'    feature.
' 2. Examine the Immediate window and the FeatureManager
'    design tree.
'---------------------------------------------------------------
```

```
Option Explicit
```

```
Sub ProcessBody(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swBody As SldWorks.Body2)
```

```
    Dim nRetval1 As Long
    Dim nRetval2 As Long
    Dim swDiagnose As SldWorks.DiagnoseResult
    Dim vCoEdgeArr As Variant
    Dim vCoEdge As Variant
    Dim swCoEdge As SldWorks.CoEdge
    Dim swEdge As SldWorks.Edge
    Dim swEnt As SldWorks.Entity
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swSelData As SldWorks.SelectData
    Dim swFeatMgr As SldWorks.FeatureManager
    Dim swFeat As SldWorks.Feature
    Dim swFaultEnt as SldWorks.FaultEntity
    Dim nNumGap As Long
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swSelMgr = swModel.SelectionManager
    Set swSelData = swSelMgr.CreateSelectData
    Set swFeatMgr = swModel.FeatureManager
    Set swDiagnose = swBody.Diagnose
    Set swFaultEnt = swBody.Check3
    nRetval1 = swFaultEnt.Count
    Set swFaultEnt = swBody.Check3
    nRetval2 = swFaultEnt.Count
    swSelData.Mark = 257
    nNumGap = swDiagnose.GetGapsCount
```

```
    Debug.Print "    Body check1                        = " & nRetval1
    Debug.Print "      Body check2 (Number of faults)   = " & nRetval2
    Debug.Print "    Number of gaps                     = " & nNumGap
```

```
    For i = 1 To nNumGap
        swModel.ClearSelection2 True
        vCoEdgeArr = swDiagnose.GetCoEdgesAtGap(i - 1)
        For Each vCoEdge In vCoEdgeArr
            Set swCoEdge = vCoEdge
            Set swEdge = swCoEdge.GetEdge
            Set swEnt = swEdge
            bRet = swEnt.Select4(True, swSelData)
        Next vCoEdge
        Set swFeat = swFeatMgr.InsertFillSurface2(3, swOptimizeSurface, swSelData, swContact, Nothing, Nothing)
    Next i
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim vBodyArr As Variant
    Dim vBody As Variant
    Dim swBody As SldWorks.Body2
    Dim i As Long

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
    Debug.Print "File = " & swModel.GetPathName
    For i = 0 To 5
        vBodyArr = swPart.GetBodies2(i, False)
        If Not IsEmpty(vBodyArr) Then
            Debug.Print "  NumBody[" & i & "] = " & UBound(vBodyArr) + 1
            For Each vBody In vBodyArr
                Set swBody = vBody
                ProcessBody swApp, swModel, swBody
            Next vBody
        End If
    Next i
```

```
End Sub
```
