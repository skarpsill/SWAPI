---
title: "Create Bidirectional Circular Pattern Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Bidirectional_Circular_Pattern_Feature_Example_VB.htm"
---

# Create Bidirectional Circular Pattern Feature Example (VBA)

This example shows how to create a bidirectional circular pattern feature.

```vb
'-------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the part exists.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the part.
 ' 2. Selects a feature.
 ' 3. Selects an edge for Direction 1.
 ' 4. Creates a bidirectional circular pattern.
 ' 5. Examine the FeatureManager design tree,
 '    graphics area, and Immediate window.
 '
 ' NOTE: Because the part is used elsewhere, do not
 ' save changes.
 '--------------------------------------------------------
 Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swFeatureManager As SldWorks.FeatureManager
 Dim swFeature As SldWorks.Feature
 Dim swCircularPatternFeatureData As SldWorks.CircularPatternFeatureData
 Dim status As Boolean
 Dim errors As Long
 Dim warnings As Long
 Dim fileName As String
Sub main()
     Set swApp = Application.SldWorks
     fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\featurecircularpattern.sldprt"
     Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
     Set swModelDocExt = swModel.Extension
     Set swFeatureManager = swModel.FeatureManager
     status = swModelDocExt.SelectByID2("Boss-Extrude2", "BODYFEATURE", -5.68552547690615E-05, 3.36059294503599E-02, 6.99999999999932E-02, False, 4, Nothing, 0)
     status = swModelDocExt.SelectByRay(2.89184346104037E-02, 2.05122863998071E-02, 5.98787397922251E-02, 0.342497149434059, -0.159204982974168, -0.925931679998983, 9.12809005339891E-04, 1, True, 1, 0)

    Set swCircularPatternFeatureData = swFeatureManager.CreateDefinition(swFmCirPattern)
     Set swFeature = swFeatureManager.CreateFeature(swCircularPatternFeatureData)

     Set swCircularPatternFeatureData = swFeature.GetDefinition
     Debug.Print "Direction 1:"
     Debug.Print "  Equal spacing: " & swCircularPatternFeatureData.EqualSpacing
     Debug.Print "  Spacing: " & swCircularPatternFeatureData.Spacing
     Debug.Print "  Total instances: " & swCircularPatternFeatureData.TotalInstances
     If swCircularPatternFeatureData.Direction2 Then
         Debug.Print "Direction 2:"
         Debug.Print "  Symmetric: " & swCircularPatternFeatureData.Symmetric
         Debug.Print "  Equal spacing: " & swCircularPatternFeatureData.EqualSpacing2
         Debug.Print "  Spacing: " & swCircularPatternFeatureData.Spacing2
         Debug.Print "  Total instances: " & swCircularPatternFeatureData.TotalInstances2
     End If
End Sub
```
