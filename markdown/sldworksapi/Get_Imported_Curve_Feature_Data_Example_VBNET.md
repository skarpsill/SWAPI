---
title: "Get Imported Curve Feature Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Imported_Curve_Feature_Data_Example_VBNET.htm"
---

# Get Imported Curve Feature Data Example (VB.NET)

This example shows how to get the number of curves in an imported curve feature.

```
'-----------------------------------------------------------------
' Preconditions:
' 1. Open a part document that has an ImportedCurve1 feature.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Selects the ImportedCurve1 feature.
' 2. Gets the number of curves in ImportedCurve1.
' 3. Examine the Immediate window.
'-----------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelectionMgr As SelectionMgr
        Dim swFeature As Feature
        Dim swImportedCurveFeatureData As ImportedCurveFeatureData
        Dim status As Boolean

        swModel = swApp.ActiveDoc
        swModelDocExt = swModel.Extension
        swSelectionMgr = swModel.SelectionManager

        'Select ImportedCurve1 and get the number of curves in the feature
        status = swModelDocExt.SelectByID2("ImportedCurve1", "REFERENCECURVES", 0, 0, 0, False, 0, Nothing, 0)
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swImportedCurveFeatureData = swFeature.GetDefinition
        Debug.Print("Number of curves: " & swImportedCurveFeatureData.GetCurveCount)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
