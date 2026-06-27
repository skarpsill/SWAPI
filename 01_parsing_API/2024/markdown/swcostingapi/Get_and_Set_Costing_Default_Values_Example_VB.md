---
title: "Get and Set Costing Default Values Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swcostingapi/Get_and_Set_Costing_Default_Values_Example_VB.htm"
---

# Get and Set Costing Default Values Example (VBA)

This example shows how to get and set Costing default values.

```
'-----------------------------------------------
' Preconditions:
' 1. Specified sheet metal part to open exists.
' 3. Add a reference to sldcostingapi.tlb.
' 4. Open the Immediate window.
' 5. Open the Notepad text editor.
' 6. Run the macro.
'
' Postconditions:
' 1. Opens the specified sheet metal part.
' 2. Prints to the Immediate window the current
'    Costing default values.
' 3. Copy and paste the contents of the
'    Immediate window to Notepad.
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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swcCostingMgr As SldCostingAPI.CostManager
Dim swcCostingPart As SldCostingAPI.CostPart
Dim swcCostingBody As SldCostingAPI.CostBody
Dim swcCostingDefaults As SldCostingAPI.CostingDefaults
Dim fileName As String
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
```

```
'Open the specified part
fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\costing\sheet_metal_part.sldprt"
Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
Set swModelDocExt = swModel.Extension
```

```
'Get CostingManager
Set swcCostingMgr = swModelDocExt.GetCostingManager
If swcCostingMgr Is Nothing Then
   Debug.Print "CostingManager is nothing."
   Exit Sub
End If
```

```
'Get Costing part
Set swcCostingPart = swcCostingMgr.CostingModel
If swcCostingPart Is Nothing Then
   Debug.Print "Costing part is nothing."
   Exit Sub
End If
```

```
'Set the Costing manufacturing method
'to sheet metal and get the Costing body
Set swcCostingBody = swcCostingPart.SetCostingMethod("", swcMethodType_e.swcMethodType_Sheetmetal)
If swcCostingBody Is Nothing Then
   Debug.Print "Costing body is nothing."
   Exit Sub
End If
```

```
'Get Costing defaults object
Set swcCostingDefaults = swcCostingMgr.CostingDefaults
If swcCostingDefaults Is Nothing Then
   Debug.Print "Costing defaults is nothing."
   Exit Sub
End If
```

```
'Get Costing defaults registry values
Debug.Print ("Costing costing defaults values:")
Debug.Print ("    Template name:  " & swcCostingDefaults.GetTemplateName(swcCostingType_e.swcCostingType_SheetMetal))
Debug.Print ("    Manufacturing method: " & swcCostingDefaults.GetManufacturingMethod(swcBodyType_e.swcBodyType_SheetMetal))
Debug.Print ("    Material class: " & swcCostingDefaults.GetMaterialClass(swcMethodType_e.swcMethodType_Sheetmetal))
Debug.Print ("    Material name: " & swcCostingDefaults.GetMaterialName(swcMethodType_e.swcMethodType_Sheetmetal))
Debug.Print ("    Lot size for single-body mode: " & swcCostingDefaults.LotSizeForSingleBody)
Debug.Print ("    Sheet metal blank size type: " & swcCostingDefaults.SheetmetalBlankSizeType)
Debug.Print ("    Total number of parts for single body: " & swcCostingDefaults.TotalNumberOfPartsForSingleBody)
Debug.Print ""
```

```
Stop
'Examine the Immediate window
'Copy and paste the contents of the
'Immediate window into Notepad if
'running the macro for the first time
'Press F5 to continue
```

```
'Set some Costing default registry values
swcCostingDefaults.SetMaterialClass swcMethodType_e.swcMethodType_Sheetmetal, "Alluminum Alloys"
swcCostingDefaults.SetMaterialName swcMethodType_e.swcMethodType_Sheetmetal, "6061 Alloy"
swcCostingDefaults.LotSizeForSingleBody = 200
swcCostingDefaults.TotalNumberOfPartsForSingleBody = 200
```

```
'Pop up message box
 MsgBox "1. Save and exit the macro." & vbCrLf & "2. Close the part without saving any changes." & vbCrLf & "3. Exit SOLIDWORKS." & vbCrLf & "4. Start up SOLIDWORKS and run the macro again." & vbCrLf & "5. Examine the Immediate window and Notepad to verify that new default values were set in the registry, where applicable."
```

```
End Sub
```
