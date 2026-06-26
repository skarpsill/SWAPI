---
title: "Get Flat-Pattern Folder Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Flat_Pattern_Folder_Feature_Example_VB.htm"
---

# Get Flat-Pattern Folder Feature Example (VBA)

This example shows how to get the flat-pattern folder and its contents.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a multibody sheet metal part that has a folder
 ' of flat-patterns.
 '
 ' Postconditions: Inspect the Immediate window.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim myModel As SldWorks.ModelDoc2
 Dim featureMgr As SldWorks.FeatureManager
 Dim feat As SldWorks.Feature
 Dim featArray As Variant
 Dim i As Long
 Option Explicit
Sub main()

    Set swApp = Application.SldWorks
     Set myModel = swApp.ActiveDoc
     Set featureMgr = myModel.FeatureManager
     Dim flatPatternFolder As SldWorks.flatPatternFolder
     Set flatPatternFolder = featureMgr.GetFlatPatternFolder
     Set feat = flatPatternFolder.GetFeature
     Debug.Print "Flat-pattern folder name: " & feat.Name
     Debug.Print "  Number of flat-pattern features in the folder: " & flatPatternFolder.GetFlatPatternCount
     featArray = flatPatternFolder.GetFlatPatterns
     For i = LBound(featArray) To UBound(featArray)
         Set feat = featArray(i)
         Debug.Print "    " & feat.Name
     Next i

End Sub
```
