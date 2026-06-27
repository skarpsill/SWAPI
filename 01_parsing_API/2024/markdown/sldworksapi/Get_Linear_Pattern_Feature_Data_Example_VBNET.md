---
title: "Get Linear Pattern Feature Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Linear_Pattern_Feature_Data_Example_VBNET.htm"
---

# Get Linear Pattern Feature Data Example (VB.NET)

This example shows how to get data for a linear pattern feature.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a part document with a LPattern1 feature.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets, sets, and prints linear pattern feature data to
'    the Immediate window.
' 2. Examine the FeatureManager design tree, graphics area, and Immediate window.
'----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swFeature As Feature
        Dim swSelectionMgr As SelectionMgr
        Dim swLinearPatternFeatureData As LinearPatternFeatureData
        Dim status As Boolean

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension

        'Get the linear pattern feature data
        status = swModelDocExt.SelectByID2("LPattern1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swLinearPatternFeatureData = swFeature.GetDefinition
        swLinearPatternFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("Number of features in pattern: " & swLinearPatternFeatureData.GetPatternFeatureCount)
        Debug.Print("Total number of instances: ")
        Debug.Print(" Direction 1: " & swLinearPatternFeatureData.D1TotalInstances)
        Debug.Print(" Direction 2: " & swLinearPatternFeatureData.D2TotalInstances)
        'Change Direction 2 spacing
        Debug.Print("Direction 2 spacing: ")
        Debug.Print(" Original: " & swLinearPatternFeatureData.D2Spacing)
        swLinearPatternFeatureData.D2Spacing = 0.04
        Debug.Print(" Updated: " & swLinearPatternFeatureData.D2Spacing)
        swFeature.ModifyDefinition(swLinearPatternFeatureData, swModel, Nothing)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
