---
title: "Create Bidirectional Circular Pattern Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Bidirectional_Circular_Pattern_Feature_Example_VBNET.htm"
---

# Create Bidirectional Circular Pattern Feature Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub main()

         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim swFeatureManager As FeatureManager
         Dim swFeature As Feature
         Dim swCircularPatternFeatureData As CircularPatternFeatureData
         Dim status As Boolean
         Dim errors As Integer
         Dim warnings As Integer
         Dim fileName As String

         fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\featurecircularpattern.sldprt"
         swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         swModelDocExt = swModel.Extension
         swFeatureManager = swModel.FeatureManager
         status = swModelDocExt.SelectByID2("Boss-Extrude2", "BODYFEATURE", -0.0000568552547690615, 0.0336059294503599, 0.0699999999999932, False, 4, Nothing, 0)
         status = swModelDocExt.SelectByRay(0.0289184346104037, 0.0205122863998071, 0.0598787397922251, 0.342497149434059, -0.159204982974168, -0.925931679998983, 0.000912809005339891, 1, True, 1, 0)
         swCircularPatternFeatureData = swFeatureManager.CreateDefinition(swFeatureNameID_e.swFmCirPattern)
     swFeature = swFeatureManager.CreateFeature(swCircularPatternFeatureData)

         swCircularPatternFeatureData = swFeature.GetDefinition
         Debug.Print("Direction 1:")
         Debug.Print("  Equal spacing: " & swCircularPatternFeatureData.EqualSpacing)
         Debug.Print("  Spacing: " & swCircularPatternFeatureData.Spacing)
         Debug.Print("  Total instances: " & swCircularPatternFeatureData.TotalInstances)
         If swCircularPatternFeatureData.Direction2 Then
             Debug.Print("Direction 2:")
             Debug.Print("  Symmetric: " & swCircularPatternFeatureData.Symmetric)
             Debug.Print("  Equal spacing: " & swCircularPatternFeatureData.EqualSpacing2)
             Debug.Print("  Spacing: " & swCircularPatternFeatureData.Spacing2)
             Debug.Print("  Total instances: " & swCircularPatternFeatureData.TotalInstances2)
         End If

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
