---
title: "Set Custom Bend Deduction Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Custom_Bend_Deduction_Example_VBNET.htm"
---

# Set Custom Bend Deduction Example (VB.NET)

This example shows how to set a custom bend deduction for a miter flange feature.

```vb
 '---------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a sheet metal part that contains a miter flange
 '    feature with bends.
 ' 2. Select the miter flange feature.
 '
 ' Postconditions: Sets the selected miter flange's custom
 ' bend deduction to 1 mm.
 '---------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim boolstatus As Boolean
     Dim FeatureData As MiterFlangeFeatureData
     Dim Feature As Feature
     Dim Component As Component
     Dim bData As CustomBendAllowance
     Dim nam As  String

     Sub main()

         Part = swApp.ActiveDoc

         ' Get the selected feature
         Feature = Part.SelectionManager.GetSelectedObject6(1, -1)

         ' Get the name of the selected feature
         nam = Feature.GetTypeName

         ' Get the feature definition
         FeatureData = Feature.GetDefinition

         ' Get whether to use default bend allowance to determine the current state
         Dim useCustom As Boolean
         useCustom = FeatureData.UseDefaultBendAllowance

         ' Get the custom bend allowance object
         bData = FeatureData.GetCustomBendAllowance

         Dim bType As Long
         bType = bData.Type
         ' Set the bend allowance type to deduction
         bData.Type = swBendAllowanceTypes_e.swBendAllowanceDeduction

         ' Set the value of the bend deduction
         bData.BendDeduction = 0.001

         FeatureData.UseDefaultBendAllowance =  False

         ' Set the value of the custom bend deduction
         Call FeatureData.SetCustomBendAllowance(bData)

         ' Modify the feature definition
         boolstatus = Feature.ModifyDefinition(FeatureData, Part, Component)

     End Sub

     Public swApp As SldWorks

 End  Class
```
