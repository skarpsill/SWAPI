---
title: "Get Sheet Metal Folder Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sheet_Metal_Folder_Feature_Example_VBNET.htm"
---

# Get Sheet Metal Folder Feature Example (VB.NET)

This example shows how to get the sheet metal folder and its contents.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a multibody sheet metal part that has a folder
 ' of sheet metal features.
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
     Dim sheetMetalFolder As SheetMetalFolder
     Dim featArray As Object
     Dim i As  Integer

     Sub main()

         myModel = swApp.ActiveDoc
         featureMgr = myModel.FeatureManager

         sheetMetalFolder = featureMgr.GetSheetMetalFolder
         feat = sheetMetalFolder.GetFeature
         Debug.Print("Sheet metal folder name: " & feat.Name)
         Debug.Print("  Number of sheet metal features in the folder: " & sheetMetalFolder.GetSheetMetalCount)
         featArray = sheetMetalFolder.GetSheetMetals
         For i = LBound(featArray) To UBound(featArray)
             feat = featArray(i)
             Debug.Print("    " & feat.Name)
         Next i

     End Sub

     Public swApp As SldWorks

 End  Class
```
