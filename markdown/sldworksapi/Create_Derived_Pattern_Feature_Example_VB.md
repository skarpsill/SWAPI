---
title: "Create Derived Pattern Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Derived_Pattern_Feature_Example_VB.htm"
---

# Create Derived Pattern Feature Example (VBA)

This example shows how to create a derived pattern feature.

```
'--------------------------------------------------------------------
' Preconditions:
' 1. Verify that the assembly to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the assembly.
' 2. Creates a derived pattern feature.
' 3. Gets the type and name of the pattern feature used for
'    the derived pattern feature.
' 4. Changes the position of the pattern instance used as the seed
'    feature in the derived pattern feature.
' 5. Examine the FeatureManager design tree, Immediate window, and
'    graphics area.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'--------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExtension As SldWorks.ModelDocExtension
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim swDerivedPatternFeatureData As SldWorks.DerivedPatternFeatureData
Dim fileName As String
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim patternObj As SldWorks.Feature
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\assem2.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExtension = swModel.Extension
    Set swFeatureManager = swModel.FeatureManager
```

```
    swModel.ClearSelection2 True
```

```
    ' Create derived pattern feature
    status = swModelDocExtension.SelectByID2("Part2^assem2-7@assem2", "COMPONENT", 0, 0, 0, False, 1, Nothing, 0)
    status = swModelDocExtension.SelectByID2("LPattern1@Part3^assem2-1@assem2", "BODYFEATURE", 0, 0, 0, True, 2, Nothing, 0)
```

```vb
Set swDerivedPatternFeatureData = swFeatureManager.CreateDefinition(swFmDerivedLPattern)
 Set swFeature = swFeatureManager.CreateFeature(swDerivedPatternFeatureData)
```

```
     ' Get derived pattern feature name and type
     If Not swFeature Is Nothing Then
       Debug.Print "Derived pattern feature name = " & swFeature.Name
       Debug.Print "  Type of feature: " & swFeature.GetTypeName2
       Set swDerivedPatternFeatureData = swFeature.GetDefinition()
       If Not swDerivedPatternFeatureData Is Nothing Then
          swDerivedPatternFeatureData.AccessSelections swModel, Nothing
          ' Get type of pattern feature used for derived pattern feature
          Set patternObj = swDerivedPatternFeatureData.PatternFeature
          Debug.Print "    Type of pattern feature used for derived pattern feature: " & patternObj.GetTypeName2
          ' Get pattern feature name
          Debug.Print "    Name of pattern feature used for the derived pattern feature: " & patternObj.Name
          Dim swLinearPatternFeatureData As SldWorks.LinearPatternFeatureData
          ' Get the pattern feature used for the derived pattern feature
          Set swLinearPatternFeatureData = patternObj.GetDefinition
          Dim nbrPatternInstances As Long
          nbrPatternInstances = (swLinearPatternFeatureData.D1TotalInstances * swLinearPatternFeatureData.D2TotalInstances)
          Debug.Print "    Total number of pattern instances in pattern feature used for the derived pattern feature: " & nbrPatternInstances
          ' Get position of the pattern instance used as the seed feature in the derived pattern feature
          Debug.Print "      Position of the pattern instance used as the seed feature in the derived pattern feature: " & swDerivedPatternFeatureData.SeedPosition
          ' Change position of the pattern instance to use as the seed feature in the derived pattern feature
          swDerivedPatternFeatureData.SeedPosition = nbrPatternInstances - 1
          Debug.Print "      Modified position of the pattern instance to use as the seed feature in the derived pattern feature: " & swDerivedPatternFeatureData.SeedPosition
          swFeature.ModifyDefinition swDerivedPatternFeatureData, swModel, Nothing
       End If
    End If
```

```
    swModel.ClearSelection2 True
```

```
End Sub
```
