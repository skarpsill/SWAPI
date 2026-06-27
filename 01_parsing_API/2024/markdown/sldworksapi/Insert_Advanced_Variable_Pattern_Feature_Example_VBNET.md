---
title: "Insert Variable Pattern Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Advanced_Variable_Pattern_Feature_Example_VBNET.htm"
---

# Insert Variable Pattern Feature Example (VB.NET)

This example shows how to insert a variable pattern feature.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part to open exists.
' 2. Verify that c:\temp exists.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Inserts a variable pattern feature.
' 2. Exports the table to a Microsoft Excel file.
' 3. Examine the graphics area, Immediate window, and c:\temp.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub Main()

         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim swFeatureManager As FeatureManager
         Dim swFeature As Feature
         Dim swDimensionDrivenTablePatternFeat As DimPatternFeatureData
         Dim fileName As String
         Dim status As Boolean
         Dim errors As Integer, warnings As Integer
         Dim nbr As Integer
         Dim dimNbr As Integer
         Dim i As Integer
 Dim j As Integer
 Dim controllingDimNames() As String
 Dim controllingDimName As String
 Dim instanceName As String
 Dim instanceNames() As String
 Dim patternName As String

         fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\cstick.sldprt"
         swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         swModelDocExt = swModel.Extension

         'Select feature to pattern
         status = swModelDocExt.SelectByID2("Sweep1", "BODYFEATURE", 0, 0, 0, False, 4, Nothing, 0)

         'Select reference geometry to drive seed feature
         status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, True, 1048576, Nothing, 0)

         'Populate table
         swFeatureManager = swModel.FeatureManager
         status = swFeatureManager.InsertVaryInstanceOverride("D1@Sketch2@cstick.SLDPRT", 256, 1, 0, 1, 0, 0.085)
         status = swFeatureManager.InsertVaryInstanceOverride("D3@Sketch2@cstick.SLDPRT", 256, 1, 0, 1, 0, 0.04)
         status = swFeatureManager.InsertVaryInstanceOverride("D4@Sketch2@cstick.SLDPRT", 256, 1, 0, 1, 0, 0.03)
         status = swFeatureManager.InsertVaryInstanceOverride("D1@Sketch2@cstick.SLDPRT", 256, 1, 0, 2, 0, 0.105)
         status = swFeatureManager.InsertVaryInstanceOverride("D3@Sketch2@cstick.SLDPRT", 256, 1, 0, 2, 0, 0.06)
         status = swFeatureManager.InsertVaryInstanceOverride("D4@Sketch2@cstick.SLDPRT", 256, 1, 0, 2, 0, 0.05)

         'Insert the variable pattern feature
         'and access its feature data
         swDimensionDrivenTablePatternFeat = swFeatureManager.CreateDefinition(swFeatureNameID_e.swFmDimPattern)
         swFeature = swFeatureManager.CreateFeature(swDimensionDrivenTablePatternFeat)
         swDimensionDrivenTablePatternFeat = swFeature.GetDefinition
         status = swDimensionDrivenTablePatternFeat.AccessSelections(swModel, Nothing)

         nbr = swDimensionDrivenTablePatternFeat.GetInstanceCount
         Debug.Print("Number of pattern instances: " & nbr)
```

```
        dimNbr = swDimensionDrivenTablePatternFeat.GetControllingDimensionCount
        Debug.Print("Number of controlling dimensions: " & dimNbr)
        Debug.Print("  Controlling dimension names: ")
        ReDim controllingDimNames(dimNbr)
        For i = 0 To dimNbr - 1
            controllingDimNames(i) = swDimensionDrivenTablePatternFeat.GetControllingDimensionName(i)
            controllingDimName = controllingDimNames(i)
            Debug.Print("     " & controllingDimName)
        Next i

        Debug.Print("Names of pattern instances:")
        ReDim instanceNames(nbr - 1)
        j = 0
        For i = 1 To nbr
            instanceName = swDimensionDrivenTablePatternFeat.GetInstanceNameByIndex(i)
            Debug.Print("  " & instanceName)
            instanceNames(j) = instanceName
            j = j + 1
        Next i

        Debug.Print("Table row indices of pattern instances:")
        For i = 0 To nbr - 1
            Debug.Print("  " & swDimensionDrivenTablePatternFeat.GetTableRowIndex(instanceNames(i)) & ": " & instanceNames(i))
        Next i

        Debug.Print("Pattern dimension names: ")
        For i = 0 To nbr - 1
            For j = 0 To dimNbr - 1
               patternName = swDimensionDrivenTablePatternFeat.GetInstanceDimensionName(instanceNames(i), controllingDimNames(j))
               Debug.Print("  " & patternName & ": " & instanceNames(i) & ": Controlling dimension name: " & swDimensionDrivenTablePatternFeat.GetControllingDimensionName(j))
            Next j
        Next i

        Debug.Print("Pattern instance suppression state:")
        For i = 0 To nbr - 1
            Debug.Print("  " & swDimensionDrivenTablePatternFeat.GetInstanceSuppressStateByIndex(swDimensionDrivenTablePatternFeat.GetTableRowIndex(instanceNames(i))) & ": " & instanceNames(i))
        Next i

        ' Export table to Microsoft Excel file
        errors = swDimensionDrivenTablePatternFeat.ExportToExcel("c:\temp\cstickVarPattern.xls", True)
        Debug.Print "Table exported to Microsoft Excel file (0 = Succeeded)? " & errors

        swDimensionDrivenTablePatternFeat.ReleaseSelectionAccess()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
