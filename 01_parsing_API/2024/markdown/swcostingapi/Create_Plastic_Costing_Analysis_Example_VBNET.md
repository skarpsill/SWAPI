---
title: "Create Plastic Costing Analysis Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swcostingapi/Create_Plastic_Costing_Analysis_Example_VBNET.htm"
---

# Create Plastic Costing Analysis Example (VB.NET)

This example shows how to create a plastic Costing analysis of a part.

```
'-----------------------------------------------
' Preconditions:
' 1. Specified part to open exists.
' 2. Add a reference to SolidWorks.Interop.sldcostingapi.dll.
' 3. Open the Immediate window.
' 4. Run the macro.
'
' Postconditions:
' 1. Opens the specified part.
' 2. Gets the CostingManager.
' 3. Gets the Costing part.
' 4. Sets the Costing manufacturing method
'    to plastic and gets the Costing body.
' 5. Gets the common Costing analysis and
'    the plastic Costing analysis.
' 6. Gets the material classes from the Costing template
'    and sets the material class.
' 7. Gets the material names from the Costing template
'    and sets the material for the material class.
' 8. Sets and gets plastic Costing analysis
'    parameters.
' 9. Gets the total manufacturing cost.
'10. Examine the Immediate window to see the
'    results of steps 6 through 9.
'
' NOTE: Because the part is used elsewhere, do
' not save changes when closing it.
'-------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.sldcostingapi
Imports System.Runtime.InteropServices
Imports System.Diagnostics
Imports System

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swModelDocExt As ModelDocExtension
    Dim swcCostMgr As CostManager
    Dim swcCostPart As CostPart
    Dim swcCostBody As CostBody
    Dim swcCostAnalysis As CostAnalysis
    Dim swcPlasticAnalysis As CostAnalysisPlastic
    Dim fileName As String
    Dim errors As Integer
    Dim warnings As Integer
    Dim totalCost As Double
    Dim templateName As String
    Dim materialClassCount As Integer
    Dim materialClasses As Object
    Dim materialCount As Integer
    Dim materials As Object
    Dim i As Integer

    Public Sub Main()

        'Open the specified part
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\clamp1.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        'Get CostingManager
        swcCostMgr = swModelDocExt.GetCostingManager
        If swcCostMgr Is Nothing Then
            Debug.Print("CostingManager is nothing.")
            Exit Sub
        End If

        'Get Costing part
        swcCostPart = swcCostMgr.CostingModel
        If swcCostPart Is Nothing Then
            Debug.Print("Costing part is nothing.")
            Exit Sub
        End If

        'Set the Costing manufacturing method
        'to plastic and get the Costing body
        swcCostBody = swcCostPart.SetCostingMethod("", swcMethodType_e.swcMethodType_Plastic)
        If swcCostBody Is Nothing Then
            Debug.Print("Costing body is nothing.")
            Exit Sub
        End If

        Debug.Print("Plastic Costing analysis")
        'Get the common Costing analysis
        swcCostAnalysis = swcCostBody.GetCostAnalysis
        If swcCostAnalysis Is Nothing Then
            Debug.Print("Failed to activate Costing analysis.")
            Exit Sub
        End If

        'Get the plastic Costing analysis
        swcPlasticAnalysis = swcCostAnalysis.GetSpecificAnalysis
        If swcPlasticAnalysis Is Nothing Then
            Debug.Print("Plastic Costing analysis is nothing.")
            Exit Sub
        End If

        'Get the material classes from the Costing template
        materialClassCount = swcPlasticAnalysis.GetMaterialClassesCount
        If materialClassCount = 0 Then
            Debug.Print("No material classes for this plastic Costing analysis.")
            Exit Sub
        End If

        materialClasses = swcPlasticAnalysis.GetMaterialClasses
        Debug.Print("  Valid material classes for this plastic Costing Analysis: ")
        For i = 0 To materialClassCount - 1
            Debug.Print("    " & materialClasses(i))
        Next i

        'Set the material class
        swcPlasticAnalysis.CurrentMaterialClass = materialClasses(0)
        Debug.Print("  Name of the material class for this plastic Costing analysis: " & materialClasses(0))
        'Get the material names from the Costing template
        templateName = swcCostAnalysis.CostingTemplateName
        Debug.Print("  Costing template path and file name: " & templateName)
        materialCount = swcPlasticAnalysis.GetMaterialCount(materialClasses(0))
        If materialCount = 0 Then
            Debug.Print("No materials for this plastic Costing Analysis.")
            Exit Sub
        End If
        Debug.Print("  Number of materials: " & materialCount)
        materials = swcPlasticAnalysis.GetMaterials(materialClasses(0))
        Debug.Print("  Valid materials for this plastic Costing Analysis: ")
        For i = 0 To materialCount - 1
            Debug.Print("    " & materials(i))
        Next i

        'Set the material
        swcPlasticAnalysis.CurrentMaterial = materials(0)
        Debug.Print("  Name of material for " & materialClasses(0) & " for this plastic Costing analysis: " & materials(0))

        'Set and get plastic Costing analysis parameters
        swcPlasticAnalysis.PercentWasteMaterial = 10
        swcPlasticAnalysis.MoldCost = swcPlasticAnalysis.MoldCost / 100
        swcPlasticAnalysis.CalculationMethod = swcMoldCalculationMethod_e.swcMoldCalculationMethod_WallThickness
        swcPlasticAnalysis.MaxWallThickness = 0.005
        swcPlasticAnalysis.RunnerSystem = swcRunnerSystem_e.swcRunnerSystem_ColdRunner
        Debug.Print("  Plastic Costing analysis parameters:")
        Debug.Print("    Waste percentage: " & swcPlasticAnalysis.PercentWasteMaterial & "%")
        Debug.Print("    Mold cost: $" & swcPlasticAnalysis.MoldCost)
        Debug.Print("    Calculation method: " & swcPlasticAnalysis.CalculationMethod)
        Debug.Print("    Maximum wall thickness: " & swcPlasticAnalysis.MaxWallThickness & " meters")
        'Reset the shop rate to the default
        swcPlasticAnalysis.ResetShopRate()
        swcPlasticAnalysis.ShopRateApplied = True
        Debug.Print("    Default shop rate applied: " & swcPlasticAnalysis.ShopRateApplied)
        Debug.Print("    Default shop rate: $" & swcPlasticAnalysis.ShopRate)
        totalCost = swcCostAnalysis.GetTotalCostToManufacture
        Debug.Print("Total plastic cost to manufacture: $" & totalCost)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
