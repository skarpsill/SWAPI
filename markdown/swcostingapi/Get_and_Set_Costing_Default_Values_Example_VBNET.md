---
title: "Get and Set Costing Default Values Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swcostingapi/Get_and_Set_Costing_Default_Values_Example_VBNET.htm"
---

# Get and Set Costing Default Values Example (VB.NET)

This example shows how to get and set Costing default values.

```
'-----------------------------------------------
' Preconditions:
' 1. Specified sheet metal part to open exists.
' 3. Add a reference to SolidWorks.Interop.sldcostingapi.dll.
' 4. Open the Immediate window.
' 5. Open the Notepad text editor.
' 6. Run the macro.
'
' Postconditions:
' 1. Opens the specified sheet metal part.
' 2. Prints to the Immediate window the current
'    Costing default values.
' 3. Copy and paste the contents of the
'    Immediate window into Notepad.
' 4. Press F5 to continue.
' 5. Sets some new Costing default values.
' 6. Pops up a message box.
' 7. After reading the instructions in the message box,
'    click OK to close the message box, and perform the
'    instructions.
'
' NOTE: Running this macro changes the specified
' Costing default values in your computer's registry.
'------------------------------------------------

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.sldcostingapi
Imports System.Runtime.InteropServices
Imports System.Diagnostics
Imports System

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swcCostingMgr As CostManager
        Dim swcCostingPart As CostPart
        Dim swcCostingBody As CostBody
        Dim swcCostingDefaults As CostingDefaults
        Dim fileName As String
        Dim errors As Integer
        Dim warnings As Integer

        'Open the specified part
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\costing\sheet_metal_part.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        'Get CostingManager
        swcCostingMgr = swModelDocExt.GetCostingManager
        If swcCostingMgr Is Nothing Then
            Debug.Print("CostingManager is nothing.")
            Exit Sub
        End If

        'Get Costing part
        swcCostingPart = swcCostingMgr.CostingModel
        If swcCostingPart Is Nothing Then
            Debug.Print("Costing part is nothing.")
            Exit Sub
        End If

        'Set the Costing manufacturing method
        'to sheet metal and get the Costing body
        swcCostingBody = swcCostingPart.SetCostingMethod("", swcMethodType_e.swcMethodType_Sheetmetal)
        If swcCostingBody Is Nothing Then
            Debug.Print("Costing body is nothing.")
            Exit Sub
        End If

        'Get Costing defaults object
        swcCostingDefaults = swcCostingMgr.CostingDefaults
        If swcCostingDefaults Is Nothing Then
            Debug.Print("Costing defaults is nothing.")
            Exit Sub
        End If

        'Get Costing defaults registry values
        Debug.Print("Costing costing defaults values:")
        Debug.Print("    Template name:  " & swcCostingDefaults.GetTemplateName(swcCostingType_e.swcCostingType_SheetMetal))
        Debug.Print("    Manufacturing method: " & swcCostingDefaults.GetManufacturingMethod(swcBodyType_e.swcBodyType_SheetMetal))
        Debug.Print("    Material class: " & swcCostingDefaults.GetMaterialClass(swcMethodType_e.swcMethodType_Sheetmetal))
        Debug.Print("    Material name: " & swcCostingDefaults.GetMaterialName(swcMethodType_e.swcMethodType_Sheetmetal))
        Debug.Print("    Lot size for single-body mode: " & swcCostingDefaults.LotSizeForSingleBody)
        Debug.Print("    Sheet metal blank size type: " & swcCostingDefaults.SheetmetalBlankSizeType)
        Debug.Print("    Total number of parts for single body: " & swcCostingDefaults.TotalNumberOfPartsForSingleBody)
        Debug.Print("")

        Stop

        'Examine the Immediate window
        'Copy and paste the contents of the
        'Immediate window into Notepad if
        'running the macro for the first time
        'Press F5 to continue

        'Set some new Costing default registry values
        swcCostingDefaults.SetMaterialClass(swcMethodType_e.swcMethodType_Sheetmetal, "Copper Alloys")
        swcCostingDefaults.SetMaterialName(swcMethodType_e.swcMethodType_Sheetmetal, "Brass Alloy")
        swcCostingDefaults.LotSizeForSingleBody = 150
        swcCostingDefaults.TotalNumberOfPartsForSingleBody = 150

        'Pop up message box
        MsgBox("1. Save and exit the macro." & System.Environment.NewLine & "2. Close the part without saving any changes." & System.Environment.NewLine & "3. Exit SOLIDWORKS." & System.Environment.NewLine & "4. Start up SOLIDWORKS and run the macro again." & System.Environment.NewLine & "5. Examine the Immediate window and Notepad to verify that new default values were set in the registry, where applicable.")

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
