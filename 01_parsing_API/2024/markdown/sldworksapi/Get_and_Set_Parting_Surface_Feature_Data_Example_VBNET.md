---
title: "Get and Set Parting Surface Feature Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Parting_Surface_Feature_Data_Example_VBNET.htm"
---

# Get and Set Parting Surface Feature Data Example (VB.NET)

This example shows how to get and set parting surface feature data.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a model document that contains a parting surface feature.
' 2. Select the parting surface feature in the FeatureManager design tree.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets and sets parting surface feature data.
' 2. Examine the Immediate window.
'----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swSelectionMgr As SelectionMgr
        Dim swFeature As Feature
        Dim swPartingSurfaceFeatureData As PartingSurfaceFeatureData
        Dim state As Boolean

        swModel = swApp.ActiveDoc

        'Get parting surface feature
        swSelectionMgr = swModel.SelectionManager
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swPartingSurfaceFeatureData = swFeature.GetDefinition

        'Roll back to get and set parting surface feature data
        state = swPartingSurfaceFeatureData.AccessSelections(swModel, Nothing)
        Debug.Print("File = " & swModel.GetPathName)
        Debug.Print(" Feature name: " & swFeature.Name)
        Debug.Print("    Number of parting lines: " & swPartingSurfaceFeatureData.GetPartingLinesCount)
        Debug.Print("    Parting line type (0 = parting line feature, 1 = edge): " & swPartingSurfaceFeatureData.GetPartingLinesType)
        Debug.Print("    Parting surface type as defined by swPartingSurfaceMoldParmType_e: " & swPartingSurfaceFeatureData.PartingType)
        If swPartingSurfaceFeatureData.PartingType = swPartingSurfaceMoldParmType_e.swPartingSurfaceMoldParmPerpendicular Then
            Debug.Print("    Offset angle not available for this parting surface type.")
        Else
            Debug.Print("    Offset angle: " & swPartingSurfaceFeatureData.OffsetAngle)
        End If
        Debug.Print("    Knit all surfaces: " & swPartingSurfaceFeatureData.Knit)
        Debug.Print("    Distance this parting surface feature extends: " & swPartingSurfaceFeatureData.OffsetDistance)
        Debug.Print("    Transition between adjacent edges as defined by swPartingSurfaceSmoothingType_e: " & swPartingSurfaceFeatureData.TransitionType)
        'Reverse alignment
        If (swPartingSurfaceFeatureData.ReverseAlignment = True) Then
            swPartingSurfaceFeatureData.ReverseAlignment = False
        Else
            swPartingSurfaceFeatureData.ReverseAlignment = True
        End If
        Debug.Print("    Reversed alignment: " & swPartingSurfaceFeatureData.ReverseAlignment)
```

```
        'Modify and roll forward parting surface feature
        swFeature.ModifyDefinition(swPartingSurfaceFeatureData, swModel, Nothing)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
