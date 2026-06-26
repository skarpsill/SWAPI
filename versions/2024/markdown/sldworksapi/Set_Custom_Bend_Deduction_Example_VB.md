---
title: "Set Custom Bend Deduction Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Custom_Bend_Deduction_Example_VB.htm"
---

# Set Custom Bend Deduction Example (VBA)

This example shows how to set a custom bend deduction for a miter flange feature.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Open a sheet metal part that contains a miter flange
'    feature with bends.
' 2. Select the miter flange feature.
'
' Postconditions: Sets the selected miter flange's custom
' bend deduction to 1 mm.
'-------------------------------------------------------------
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim boolstatus As Boolean
 Dim FeatureData As SldWorks.MiterFlangeFeatureData
 Dim Feature As SldWorks.Feature
 Dim Component As SldWorks.Component
 Dim bData As SldWorks.CustomBendAllowance
 Dim nam As String
Sub main()
    Set swApp = CreateObject("SldWorks.Application")
     Set Part = swApp.ActiveDoc

    ' Get the selected feature
     Set Feature = Part.SelectionManager.GetSelectedObject6(1, -1)

    ' Get the name of the selected feature
     nam = Feature.GetTypeName

    ' Get the feature definition
     Set FeatureData = Feature.GetDefinition

    ' Get whether to use default bend allowance to determine the current state
     Dim useCustom As Boolean
     useCustom = FeatureData.UseDefaultBendAllowance

    ' Get the custom bend allowance object
     Set bData = FeatureData.GetCustomBendAllowance

    Dim bType As Long
     bType = bData.Type
     ' Set the bend allowance type to deduction
     bData.Type = swBendAllowanceDeduction

    ' Set the value of the bend deduction
     bData.BendDeduction = 0.001

    FeatureData.UseDefaultBendAllowance = False
    ' Set the value of the custom bend deduction
     Call FeatureData.SetCustomBendAllowance(bData)

    ' Modify the feature definition
     boolstatus = Feature.ModifyDefinition(FeatureData, Part, Component)
End Sub
```
