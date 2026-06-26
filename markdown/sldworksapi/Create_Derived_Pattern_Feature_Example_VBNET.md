---
title: "Create Derived Pattern Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Derived_Pattern_Feature_Example_VBNET.htm"
---

# Create Derived Pattern Feature Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExtension As ModelDocExtension
        Dim swFeatureManager As FeatureManager
        Dim swFeature As Feature
        Dim swDerivedPatternFeatureData As DerivedPatternFeatureData
        Dim fileName As String
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim patternObj As Feature

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\assem2.sldasm"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExtension = swModel.Extension
        swFeatureManager = swModel.FeatureManager

        swModel.ClearSelection2(True)

        ' Create derived pattern feature
        status = swModelDocExtension.SelectByID2("Part2^assem2-7@assem2", "COMPONENT", 0, 0, 0, False, 1, Nothing, 0)
        status = swModelDocExtension.SelectByID2("LPattern1@Part3^assem2-1@assem2", "BODYFEATURE", 0, 0, 0, True, 2, Nothing, 0)
```

```vb
        swDerivedPatternFeatureData = swFeatureManager.CreateDefinition(swFeatureNameID_e.swFmDerivedLPattern)
         swFeature = swFeatureManager.CreateFeature(swDerivedPatternFeatureData)
```

```
        ' Get derived pattern feature name and type
        If Not swFeature Is Nothing Then
            Debug.Print("Derived pattern feature name = " & swFeature.Name)
            Debug.Print("  Type of feature: " & swFeature.GetTypeName2)
            swDerivedPatternFeatureData = swFeature.GetDefinition()
            If Not swDerivedPatternFeatureData Is Nothing Then
                swDerivedPatternFeatureData.AccessSelections(swModel, Nothing)
                ' Get type of pattern feature used for derived pattern feature
                patternObj = swDerivedPatternFeatureData.PatternFeature
                Debug.Print("    Type of pattern feature used for derived pattern feature: " & patternObj.GetTypeName2)
		' Get pattern feature name
		Debug.Print("    Name of pattern feature used for the derived pattern feature: " & patternObj.Name)
		Dim swLinearPatternFeatureData As LinearPatternFeatureData
		' Get the pattern feature used for the derived pattern feature
		swLinearPatternFeatureData = patternObj.GetDefinition
		Dim nbrPatternInstances As Integer
		nbrPatternInstances = (swLinearPatternFeatureData.D1TotalInstances * swLinearPatternFeatureData.D2TotalInstances)
		Debug.Print("    Total number of pattern instances in pattern feature used for the derived pattern feature: " & nbrPatternInstances)
		' Get position of the pattern instance used as the seed feature in the derived pattern feature
		Debug.Print("      Position of the pattern instance used as the seed feature in the derived pattern feature: " & swDerivedPatternFeatureData.SeedPosition)
		' Change position of the pattern instance to use as the seed feature in the derived pattern feature
		swDerivedPatternFeatureData.SeedPosition = nbrPatternInstances - 1
		Debug.Print("      Modified position of the pattern instance to use as the seed feature in the derived pattern feature: " & swDerivedPatternFeatureData.SeedPosition)
		swFeature.ModifyDefinition(swDerivedPatternFeatureData, swModel, Nothing)
            End If
        End If

        swModel.ClearSelection2(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
