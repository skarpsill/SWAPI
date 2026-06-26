---
title: "Get Sheet Metal Folder Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sheet_Metal_Folder_Feature_Example_VB.htm"
---

# Get Sheet Metal Folder Feature Example (VBA)

This example shows how to get the sheet metal folder and its contents.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a multibody sheet metal part that has a folder
 ' of sheet metal features.
 '
 ' Postconditions: Inspect the Immediate window.
 ' ---------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
 Dim myModel As SldWorks.ModelDoc2
 Dim featureMgr As SldWorks.FeatureManager
 Dim feat As SldWorks.Feature
 Dim sheetMetalFolder As SldWorks.sheetMetalFolder
 Dim featArray As Variant
 Dim i As Long
 Option Explicit
Sub main()
    Set swApp = Application.SldWorks
     Set myModel = swApp.ActiveDoc
     Set featureMgr = myModel.FeatureManager

    Set sheetMetalFolder = featureMgr.GetSheetMetalFolder
     Set feat = sheetMetalFolder.GetFeature
     Debug.Print "Sheet metal folder name: " & feat.Name
     Debug.Print "  Number of sheet metal features in the folder: " & sheetMetalFolder.GetSheetMetalCount
     featArray = sheetMetalFolder.GetSheetMetals
     For i = LBound(featArray) To UBound(featArray)
         Set feat = featArray(i)
         Debug.Print "    " & feat.Name
     Next i
End Sub
```
