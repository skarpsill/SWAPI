---
title: "Create and Modify Distance Chain Pattern Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Modify_Distance_Chain_Pattern_Feature_Example_VBNET.htm"
---

# Create and Modify Distance Chain Pattern Feature Example (VB.NET)

This example shows how to create and modify a distance chain pattern feature.

```vb
'--------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the assembly to open exists.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the specified assembly.
 ' 2. Selects entities to create a distance chain pattern feature.
 ' 3. Creates the distance chain pattern feature.
 ' 4. After examining the graphics area and FeatureManager design
 '    tree, press F5.
 ' 5. Modifies the distance chain pattern feature.
 ' 6. Examine the graphics area to verify step 5.
 ' 7. Examine the Immediate window.
 '
 ' NOTE: Because the assembly is used elsewhere, do not save
 ' changes.
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
         Dim swChainPatternFeatureData As ChainPatternFeatureData
         Dim status As Boolean
         Dim errors As Integer
         Dim warnings As Integer
         Dim fileName As String

         fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\distance linkage.sldasm"
         swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

         'Select entities to create distance chain pattern feature
         swModelDocExt = swModel.Extension
         status = swModelDocExt.SelectByID2("Belt Drive Path", "SKETCH", 0, 0, 0, True, 0, Nothing, 0)
         status = swModelDocExt.SelectByID2("Mount Base-1@distance linkage", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
         swModel.ViewZoomTo2(1.03935160466665, -0.0995602294424154, 0.846177052265487, 1.16810340243326, -0.261325308687639, 0.846177052265488)
         status = swModelDocExt.SelectByID2("", "FACE", 0.187298652259415, -0.193039676915248, 0.113419833821467, True, 0, Nothing, 0)
         status = swModelDocExt.SelectByID2("Right Plane@Mount Base-1@distance linkage", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
         swModel.ClearSelection2(True)
         status = swModelDocExt.SelectByID2("Belt Drive Path", "SKETCH", 0, 0, 0, False, 2, Nothing, 0)
         status = swModelDocExt.SelectByID2("Mount Base-1@distance linkage", "COMPONENT", 0, 0, 0, True, 1, Nothing, 0)
         status = swModelDocExt.SelectByID2("", "FACE", 0.187298652259415, -0.193039676915248, 0.113419833821467, True, 256, Nothing, 0)
         status = swModelDocExt.SelectByID2("Right Plane@Mount Base-1@distance linkage", "PLANE", 0, 0, 0, True, 16384, Nothing, 0)

         'Create distance chain pattern feature
         swFeatureManager = swModel.FeatureManager
         swChainPatternFeatureData = swFeatureManager.CreateDefinition(swFeatureNameID_e.swFmLocalChainPattern)
     swFeature = swFeatureManager.CreateFeature(swChainPatternFeatureData)
         swModel.ClearSelection2(True)
         swModel.ViewZoomtofit2()

         Stop
         'Examine the graphics area and FeatureManager design tree
         'Press F5

         'Modify distance chain pattern feature
         swChainPatternFeatureData = swFeature.GetDefinition
         status = swChainPatternFeatureData.AccessSelections(swModel, Nothing)
         swChainPatternFeatureData.Spacing = 0.078
         swChainPatternFeatureData.FillPath = True
         Debug.Print("Number of instances calculated by SOLIDWORKS to fill the path: " & swChainPatternFeatureData.InstanceCount)
         swFeature.ModifyDefinition(swChainPatternFeatureData, swModel, Nothing)

         'Examine the graphics area

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
