---
title: "Get Flat-Pattern Folder Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Flat_Pattern_Folder_Feature_Example_VBNET.htm"
---

# Get Flat-Pattern Folder Feature Example (VB.NET)

This example shows how to get the flat-pattern folder and its contents.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a multibody sheet metal part that has a folder
 ' of flat-patterns.
 '
 ' Postconditions: Inspect the Immediate window.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim myModel As ModelDoc2
     Dim featureMgr As FeatureManager
     Dim feat As Feature
     Dim featArray() As Object
     Dim i As  Integer

     Sub main()

         myModel = swApp.ActiveDoc
         featureMgr = myModel.FeatureManager
         Dim flatPatternFolder As FlatPatternFolder
         flatPatternFolder = featureMgr.GetFlatPatternFolder
         feat = flatPatternFolder.GetFeature
         Debug.Print("Flat-pattern folder name: " & feat.Name)
         Debug.Print("  Number of flat-pattern features in the folder: " & flatPatternFolder.GetFlatPatternCount)
         featArray = flatPatternFolder.GetFlatPatterns
         For i = featArray.GetLowerBound(0) To featArray.GetUpperBound(0)
             feat = featArray(i)
             Debug.Print("    " & feat.Name)
         Next i

     End Sub

     Public swApp As SldWorks

 End  Class
```
