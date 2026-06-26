---
title: "Create 3D Printing Costing Analysis Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swcostingapi/Create_3D_Printing_Costing_Analysis_Example_VBNET.htm"
---

# Create 3D Printing Costing Analysis Example (VB.NET)

This example shows how to create a 3D printing Costing analysis for a part.

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
'    to 3D printing and gets the Costing body.
' 5. Gets the common Costing analysis and
'    the 3D printing Costing analysis.
' 6. Gets the material classes from the Costing template
'    and sets the material class.
' 7. Gets the material names from the Costing template
'    and sets the material for the material class.
' 8. Sets and gets 3D printing Costing analysis
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
    Dim swc3DPrintAnalysis As CostAnalysis3dPrinting
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
        'to 3D printing and get the Costing body
        swcCostBody = swcCostPart.SetCostingMethod("", swcMethodType_e.swcMethodType_3dPrinting)
        If swcCostBody Is Nothing Then
            Debug.Print("Costing body is nothing.")
            Exit Sub
        End If

        Debug.Print("3D printing Costing analysis")
        'Get the common Costing analysis
        swcCostAnalysis = swcCostBody.GetCostAnalysis
        If swcCostAnalysis Is Nothing Then
            Debug.Print("Failed to activate Costing analysis.")
            Exit Sub
        End If

        'Get the 3D printing Costing analysis
        swc3DPrintAnalysis = swcCostAnalysis.GetSpecificAnalysis
        If swc3DPrintAnalysis Is Nothing Then
            Debug.Print("3D printing Costing analysis is nothing.")
            Exit Sub
        End If

        'Get the material classes from the Costing template
        materialClassCount = swc3DPrintAnalysis.GetMaterialClassesCount
        If materialClassCount = 0 Then
            Debug.Print("No material classes for this 3D printing Costing analysis.")
            Exit Sub
        End If

        materialClasses = swc3DPrintAnalysis.GetMaterialClasses
        For i = 0 To materialClassCount - 1
            Debug.Print("  Valid material classes for this 3D printing Costing Analysis: ")
            Debug.Print("    " & materialClasses(i))
        Next i

        'Set the material class
        swc3DPrintAnalysis.CurrentMaterialClass = materialClasses(0)
        Debug.Print("  Name of the material class for this 3D printing Costing analysis: " & materialClasses(0))
        'Get the material names from the Costing template
        templateName = swcCostAnalysis.CostingTemplateName
        Debug.Print("  Costing template path and file name: " & templateName)
        materialCount = swc3DPrintAnalysis.GetMaterialCount(materialClasses(0))
        If materialCount = 0 Then
            Debug.Print("No materials for this 3D printing Costing Analysis.")
            Exit Sub
        End If
        Debug.Print("  Number of materials: " & materialCount)
        materials = swc3DPrintAnalysis.GetMaterials(materialClasses(0))
        For i = 0 To materialCount - 1
            Debug.Print("  Valid materials for this 3D printing Costing Analysis: ")
            Debug.Print("    " & materials(i))
        Next i

        'Set the material
        swc3DPrintAnalysis.CurrentMaterial = materials(0)
        Debug.Print("  Name of material for " & materialClasses(0) & " for this 3D printing Costing analysis: " & materials(0))

        'Set and get 3D printing Costing analysis parameters
        swc3DPrintAnalysis.OrientationPlane = swcPlane_e.swcPlane_XZ
        swc3DPrintAnalysis.PercentInfill = 80
        swc3DPrintAnalysis.WallThickness = swc3DPrintAnalysis.WallThickness * 2
        Debug.Print("  3D printing Costing analysis parameters:")
        Debug.Print("    Orientation plane: " & swc3DPrintAnalysis.OrientationPlane)
        Debug.Print("    Infill percentage: " & swc3DPrintAnalysis.PercentInfill & "%")
        Debug.Print("    Wall thickness: " & swc3DPrintAnalysis.WallThickness & " meters")
        Debug.Print("    Structural material cost: $" & swc3DPrintAnalysis.StructuralMaterialCost)
        'Reset the shop rate to the default
        swc3DPrintAnalysis.ResetShopRate()
        swc3DPrintAnalysis.ShopRateApplied = True
        Debug.Print("    Default shop rate applied: " & swc3DPrintAnalysis.ShopRateApplied)
        Debug.Print("    Default shop rate: $" & swc3DPrintAnalysis.ShopRate)
        totalCost = swcCostAnalysis.GetTotalCostToManufacture
        Debug.Print("Total 3D printing cost to manufacture: $" & totalCost)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
