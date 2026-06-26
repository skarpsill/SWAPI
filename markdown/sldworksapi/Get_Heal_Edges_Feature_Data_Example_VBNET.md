---
title: "Get Heal Edges Feature Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Heal_Edges_Feature_Data_Example_VBNET.htm"
---

# Get Heal Edges Feature Data Example (VB.NET)

This example shows how to get some data of a heal edges feature.

```
'---------------------------------------------------
' Preconditions:
' 1. Open a part document that contains a HealEdge1 feature.
' 2. Select the HealEdge1 feature.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets HealEdge1 feature data.
' 2. Examine the Immediate window.
'----------------------------------------------------

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swSelMgr As SelectionMgr
        Dim swHealEdgesFeature As HealEdgesFeatureData
        Dim swFeature As Feature
        Dim before As Integer
        Dim after As Integer

        swModel = swApp.ActiveDoc

        'Get and print HealEdge1 feature data
        swSelMgr = swModel.SelectionManager
        swFeature = swSelMgr.GetSelectedObject6(1, 0)
        swHealEdgesFeature = swFeature.GetDefinition
        swModel.ClearSelection2(True)
        swHealEdgesFeature.AccessSelections(swModel, Nothing)
        Debug.Print("Number of faces in this heal edges feature: " & swHealEdgesFeature.GetFacesCount)
        Debug.Print("Number of edges before and after healing: ")
        swHealEdgesFeature.GetEdgeInformation(before, after)
        Debug.Print("  Before: " & before)
        Debug.Print("  After : " & after)
        Debug.Print(" Maximum angle betweeen the merged edges: " & swHealEdgesFeature.AngularTolerance)
        Debug.Print(" Maximum length of the merged edges: " & swHealEdgesFeature.EdgeLengthTolerance)
        swHealEdgesFeature.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
