---
title: "Set Custom Stock Body in Machined Part Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swcostingapi/Set_Custom_Stock_Body_in_Machined_Part_Example_VBNET.htm"
---

# Set Custom Stock Body in Machined Part Example (VB.NET)

This example shows how to set a custom stock body in a machined part.

```
'-----------------------------------------------
' Preconditions:
' 1. Verify that the specified:
'    * part documents to open and reference exist.
'    * Costing template exists by clicking
'      Tools > Options > System Options > File Locations
'      and selecting Costing templates in Show folders for
'      in SOLIDWORKS. Click Cancel to close the dialog.
' 2. Add a reference to SolidWorks.Interop.sldcostingapi.dll.
' 3. Open the Immediate window.
' 4. Run the macro.
'
' Postconditions:
' 1. Opens the specified part document.
' 2. Creates common and machining Costing analyses, which can
'    take one or more minutes to complete.
' 3. Sets and gets custom stock body Costing information and
'    updates the estimated cost to manufacture the part,
'    which can take one or more minutes to complete.
' 4. Examine the Immediate window
'
' NOTE: Because the part is used elsewhere, do not
' save any changes when closing it.
'------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System.Diagnostics
Imports SolidWorks.Interop.sldcostingapi

Imports System

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swCosting As CostManager
        Dim swCostingPart As CostPart
        Dim swCostingBody As CostBody
        Dim swCostingModel As Object
        Dim swCostingAnalysis As CostAnalysis
        Dim swCostingMachining As CostAnalysisMachining
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer
        Dim nbrCostingBodies As Integer
        Dim costingBodies As Object
        Dim costingBodyName As String
        Dim i As Integer
        Dim isBody As Boolean

        ' Open part specified document
	fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\clamp1.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        ' Get CostingManager
        swCosting = swModelDocExt.GetCostingManager
        swCosting.WaitForUIUpdate()

        ' Get Costing part
        swCostingModel = swCosting.CostingModel
        swCostingPart = swCostingModel

        ' Create common Costing analysis
        swCostingAnalysis = swCostingPart.CreateCostAnalysis("C:\Program Files\SolidWorks Corp\SolidWorks\lang\english\costing templates\multibodytemplate_default(englishstandard).sldctc")

        ' Get common Costing analysis data
        Debug.Print("Common Costing analysis data:")
        Debug.Print("    Template name:  " & swCostingAnalysis.CostingTemplateName)
        Debug.Print("    Currency code: " & swCostingAnalysis.CurrencyCode)
        Debug.Print("    Currency name: " & swCostingAnalysis.CurrencyName)
        Debug.Print("    Currency separator: " & swCostingAnalysis.CurrencySeparator)
        Debug.Print("    Total manufacturing cost: " & swCostingAnalysis.GetManufacturingCost)
        Debug.Print("    Material costs: " & swCostingAnalysis.GetMaterialCost)
        Debug.Print("    Setup cost: " & swCostingAnalysis.GetSetupCost)
        Debug.Print("    Total cost to charge: " & swCostingAnalysis.GetTotalCostToCharge)
        Debug.Print("    Total cost to manufacture: " & swCostingAnalysis.GetTotalCostToManufacture)
        Debug.Print("    Lot size: " & swCostingAnalysis.LotSize)
        Debug.Print("    Total quantity: " & swCostingAnalysis.TotalQuantity)
        Debug.Print("")

        ' Get Costing bodies
        nbrCostingBodies = swCostingPart.GetBodyCount
        isBody = False
        If (nbrCostingBodies > 0) Then
            Debug.Print("Costing bodies:")
            Debug.Print("    Number of Costing bodies: " & nbrCostingBodies)
            costingBodies = swCostingPart.GetBodies
            For i = 0 To (nbrCostingBodies - 1)
                swCostingBody = costingBodies(i)
                costingBodyName = swCostingBody.GetName
                Debug.Print("    Name of Costing body: " & costingBodyName)
                ' Make sure body is machining body
                If (swCostingBody.GetBodyType = swcBodyType_e.swcBodyType_Machined) Then
                    isBody = True
                    ' Determine analysis status of Costing body
                    Select Case swCostingBody.BodyStatus
                        Case swcBodyStatus_e.swcBodyStatus_NotAnalysed
                            ' Create Costing analysis
                            swCostingAnalysis = swCostingBody.CreateCostAnalysis("C:\Program Files\SolidWorks Corp\SolidWorks\lang\english\costing templates\machiningtemplate_default(englishstandard).sldcts")
                            Debug.Print("    Creating machining Costing analysis for: " & swCostingBody.GetName)
                        Case swcBodyStatus_e.swcBodyStatus_Analysed
                            ' Get Costing analysis
                            swCostingAnalysis = swCostingBody.GetCostAnalysis
                            Debug.Print("    Getting machining Costing analysis for: " & swCostingBody.GetName)
                        Case swcBodyStatus_e.swcBodyStatus_Excluded
                            ' Body excluded from Costing analysis
                            Debug.Print("    Excluded from machining Costing analysis: " & swCostingBody.GetName)
                        Case swcBodyStatus_e.swcBodyStatus_AssignedCustomCost
                            ' Body has an assigned custom cost
                            Debug.Print("    Custom cost assigned: " & swCostingBody.GetName)
                    End Select
                    Debug.Print("")
                End If
            Next i
        End If

        If Not isBody Then
            Debug.Print("")
            Debug.Print("No bodies in part! Exiting macro.")
            Exit Sub
        End If

        ' Get machining Costing analysis data
        swCostingMachining = swCostingAnalysis.GetSpecificAnalysis
        Debug.Print("Machining Costing analysis: ")
        Debug.Print("    Current material: " & swCostingMachining.CurrentMaterial)
        Debug.Print("    Current material class: " & swCostingMachining.CurrentMaterialClass)
        Debug.Print("    Current plate thickness: " & swCostingMachining.CurrentPlateThickness)
        Debug.Print("")

        ' Set and get custom stock body Costing information
        swCostingMachining.CurrentStockType = swcStockType_e.swcStockType_Custom
        Debug.Print("Custom stock body Costing information:")
        swCostingMachining.CustomStockBodyName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\clamp2.sldprt"
        Debug.Print("    Body: " & swCostingMachining.CustomStockBodyName)
        swCostingMachining.CustomStockCostInfoType = swcCustomStockCostInfoType_e.swcCustomStockCostType_CustomCost
        Debug.Print("    Information type: " & swCostingMachining.CustomStockCostInfoType)
        swCostingMachining.CustomStockCustomCost = 3.53
        Debug.Print("    Cost: " & swCostingMachining.CustomStockCustomCost)
        swCostingMachining.CustomStockImportType = swcCustomStockImportType_e.swcCustomStockImportType_ReferencePart
        Debug.Print("    Import type: " & swCostingMachining.CustomStockImportType)
        Debug.Print ("")

        ' Updated estimated total cost to manufacture the part
        Debug.Print ("Updated estimated total cost to manufacture: " & swCostingAnalysis.GetTotalCostToManufacture)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
