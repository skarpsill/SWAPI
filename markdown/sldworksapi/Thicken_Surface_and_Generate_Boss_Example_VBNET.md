---
title: "Thicken Surface and Generate Boss Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Thicken_Surface_and_Generate_Boss_Example_VBNET.htm"
---

# Thicken Surface and Generate Boss Example (VB.NET)

This example shows how to thicken a surface and then generate a boss..

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a model document and select a boundary surface.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a thicken feature.
 ' 2. Inspect the Immediate window.
  '----------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swFeatMgr As FeatureManager
         Dim swFeat As Feature
         Dim swThicken As ThickenFeatureData
         Dim bRet As Boolean

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swFeatMgr = swModel.FeatureManager

         bRet = swSelMgr.SetSelectedObjectMark(1, 1, swSelectionMarkAction_e.swSelectionMarkSet)

         swFeat = swFeatMgr.FeatureBossThicken(0.001, swThickenThicknessType_e.swThickenSideOne, 0, False, True, True, True)
         swThicken = swFeat.GetDefinition

         Debug.Print("Feature: " & swFeat.Name)
         Debug.Print("  Automatically select all bodies? " & swThicken.AutoSelect)
         Debug.Print("  True if thicken feature affects specified bodies, false if it affects all bodies: " & swThicken.FeatureScope)
         Debug.Print("  Is a boss feature? " & swThicken.IsBossFeature)
         Debug.Print("  Merge the results if a multibody part?  " & swThicken.Merge)
         Debug.Print("  Fill a volume?  " & swThicken.FillVolume)
         Debug.Print("  Thickness:  " & swThicken.Thickness * 1000.0# & " mm")
         Debug.Print("  Thickness type as defined in swThickenThicknessType_e:  " & swThicken.ThicknessSide)

     End Sub

     Public swApp As SldWorks

 End Class
```
