---
title: "Get and Fill Gaps in Body Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Fill_Gaps_in_Body_Example_VBNET.htm"
---

# Get and Fill Gaps in Body Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swPart As PartDoc
        Dim vBodyArr As Object
        Dim vBody As Object
        Dim swBody As Body2
        Dim i As Integer

        swModel = swApp.ActiveDoc
        swPart = swModel
        Debug.Print("File = " & swModel.GetPathName)
        For i = 0 To 5
            vBodyArr = swPart.GetBodies2(i, False)
            If Not vBodyArr Is Nothing Then
                Debug.Print("  NumBody[" & i & "] = " & UBound(vBodyArr) + 1)
                For Each vBody In vBodyArr
                    swBody = vBody
                    ProcessBody(swApp, swModel, swBody)
                Next vBody
            End If
        Next i

    End Sub

    Sub ProcessBody(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal swBody As Body2)
        Dim nRetval1 As Integer
        Dim nRetval2 As Integer
        Dim swDiagnose As DiagnoseResult
        Dim vCoEdgeArr As Object
        Dim vCoEdge As Object
        Dim swCoEdge As CoEdge
        Dim swEdge As Edge
        Dim swEnt As Entity
        Dim swSelMgr As SelectionMgr
        Dim swSelData As SelectData
        Dim swFeatMgr As FeatureManager
        Dim swFaultEnt As FaultEntity
        Dim swFeat As Feature
        Dim nNumGap As Integer
        Dim i As Integer
        Dim bRet As Boolean

        swSelMgr = swModel.SelectionManager
        swSelData = swSelMgr.CreateSelectData
        swFeatMgr = swModel.FeatureManager
        swDiagnose = swBody.Diagnose
        swFaultEnt = swBody.Check3
        nRetval1 = swFaultEnt.Count
        swFaultEnt = swBody.Check3
        nRetval2 = swFaultEnt.Count
        swSelData.Mark = 257
        nNumGap = swDiagnose.GetGapsCount

        Debug.Print("    Body check1                        = " & nRetval1)
        Debug.Print("      Body check2 (Number of faults)   = " & nRetval2)
        Debug.Print("    Number of gaps                     = " & nNumGap)

        For i = 1 To nNumGap
            swModel.ClearSelection2(True)
            vCoEdgeArr = swDiagnose.GetCoEdgesAtGap(i - 1)
            For Each vCoEdge In vCoEdgeArr
                swCoEdge = vCoEdge
                swEdge = swCoEdge.GetEdge
                swEnt = swEdge
                bRet = swEnt.Select4(True, swSelData)
            Next vCoEdge
            swFeat = swFeatMgr.InsertFillSurface2(3, swFeatureFillSurfaceOptions_e.swOptimizeSurface, swSelData, swContactType_e.swContact, Nothing, Nothing)
        Next i

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
