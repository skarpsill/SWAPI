---
title: "Thicken Surface and Generate Boss Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Thicken_Surface_and_Generate_Boss_Example_VB.htm"
---

# Thicken Surface and Generate Boss Example (VBA)

This example shows how to thicken a surface and then generate a boss.

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
Option Explicit
Sub main()
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swSelMgr                    As SldWorks.SelectionMgr
    Dim swFeatMgr                   As SldWorks.FeatureManager
    Dim swFeat                      As SldWorks.Feature
    Dim swThicken                   As SldWorks.ThickenFeatureData
    Dim bRet                        As Boolean

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swFeatMgr = swModel.FeatureManager

    bRet = swSelMgr.SetSelectedObjectMark(1, 1, swSelectionMarkSet)

    Set swFeat = swFeatMgr.FeatureBossThicken(0.001, swThickenSideOne, 0, False, True, True, True)
    Set swThicken = swFeat.GetDefinition
    Debug.Print "Feature: " & swFeat.Name
    Debug.Print "  Automatically select all bodies? " & swThicken.AutoSelect
    Debug.Print "  True if thicken feature affects specified bodies, false if it affects all bodies: " & swThicken.FeatureScope
    Debug.Print "  Is a boss feature? " & swThicken.IsBossFeature
    Debug.Print "  Merge the results if a multibody part?  " & swThicken.Merge
    Debug.Print "  Fill a volume?  " & swThicken.FillVolume
    Debug.Print "  Thickness:  " & swThicken.Thickness * 1000# & " mm"
    Debug.Print "  Thickness type as defined in swThickenThicknessType_e:  " & swThicken.ThicknessSide
End Sub
```
