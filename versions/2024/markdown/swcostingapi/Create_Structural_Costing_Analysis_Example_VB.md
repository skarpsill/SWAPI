---
title: "Create Structural Costing Analysis Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swcostingapi/Create_Structural_Costing_Analysis_Example_VB.htm"
---

# Create Structural Costing Analysis Example (VBA)

This example shows how to create a structural Costing analysis of a weldment part.

```
'------------------------------------------------
' Preconditions:
' 1. Specified part template exists.
' 2. Add a reference to SldCostingAPI nnnn Type Library.
' 3. Open the Immediate window.
' 4. Run the macro.
'
' Postconditions:
' 1. Creates a weldment part.
' 2. Gets the CostingManager.
' 3. Gets the Costing part.
' 4. Sets the Costing manufacturing method
'    to structural and gets the Costing body.
' 5. Gets the common Costing analysis and the
'    structural Costing analysis.
' 6. Gets the material classes from the Costing template
'    and sets the material class.
' 7. Gets the material names from the Costing template
'    and sets the material for the material class.
' 8. Sets and gets structural Costing analysis
'    parameters.
' 9. Gets the total manufacturing cost.
'10. Examine the Immediate window to see the
'    results of steps 6 through 9.
'-------------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchMgr As SldWorks.SketchManager
Dim swFeatMgr As SldWorks.FeatureManager
Dim swSelMgr As SldWorks.SelectionMgr
Dim swcCostMgr As SldCostingAPI.CostManager
Dim swcCostPart As SldCostingAPI.CostPart
Dim swcCostBody As SldCostingAPI.CostBody
Dim swcCostAnalysis As SldCostingAPI.CostAnalysis
Dim swcStructuralAnalysis As SldCostingAPI.CostAnalysisStructural
Dim swFeat As Object
Dim sketchLines As Variant
Dim groups As Variant
Dim groupArray() As Object
Dim group1 As Object
Dim segment1 As Variant
Dim segmentArray1() As Object
Dim segment As SldWorks.SketchLine
Dim status As Boolean
Dim totalCost As Double
Dim templateName As String
Dim materialClassCount As Long
Dim materialClasses As Variant
Dim materialCount As Long
Dim materials As Variant
Dim i As Long
Dim costMethod As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Open new part
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)

    'Sketch a rectangle
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
    status = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
    Set swSketchMgr = swModel.SketchManager
    sketchLines = swSketchMgr.CreateCornerRectangle(0, 0, 0, 7.12674458144988E-02, -4.41036883594848E-02, 0)
    swModel.ClearSelection2 True
    swSketchMgr.InsertSketch True
```

```
    'Create a weldment feature
    Set swFeatMgr = swModel.FeatureManager
    Set swFeat = swFeatMgr.InsertWeldmentFeature()
```

```
    'Create a structural member
    status = swModelDocExt.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", 0, -8.30721773633059E-03, 0, True, 0, Nothing, 0)
    ReDim groupArray(0 To 0) As Object
    Set group1 = swFeatMgr.CreateStructuralMemberGroup()
    ReDim segmentArray1(0 To 0) As Object
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("Line2@Sketch1", "EXTSKETCHSEGMENT", 0, 0.334864850338306, 0.393154025912395, True, 0, Nothing, 0)
    Set swSelMgr = swModel.SelectionManager
    Set segment = swSelMgr.GetSelectedObject6(1, 0)
    Set segmentArray1(0) = segment
    segment1 = segmentArray1
    group1.Segments = (segment1)
    group1.ApplyCornerTreatment = True
    group1.CornerTreatmentType = 1
    group1.GapWithinGroup = 0
    group1.GapForOtherGroups = 0
    group1.Angle = 0
    Set groupArray(0) = group1
    groups = groupArray
    Set swFeat = swFeatMgr.InsertStructuralWeldment4("c:\program files\solidworks corp\solidworks\lang\english\weldment profiles\ansi inch\rectangular tube\3 x 2 x 0.25.sldlfp", 1, True, (groups))
    swModel.ClearSelection2 True
```

```
    'Get CostingManager
    Set swcCostMgr = swModelDocExt.GetCostingManager
    If swcCostMgr Is Nothing Then
        Debug.Print "CostingManager is nothing."
        Exit Sub
    End If
```

```
    'Get Costing part
    Set swcCostPart = swcCostMgr.CostingModel
    If swcCostPart Is Nothing Then
        Debug.Print "Costing part is nothing."
        Exit Sub
    End If
```

```
    'Set the Costing manufacturing method
    'to structural and get the Costing body
    Set swcCostBody = swcCostPart.SetCostingMethod("", swcMethodType_e.swcMethodType_Structural)
    If swcCostBody Is Nothing Then
        Debug.Print "Costing body is nothing."
        Exit Sub
    End If
```

```
    'Get the common Costing analysis
    Set swcCostAnalysis = swcCostBody.GetCostAnalysis
    If swcCostAnalysis Is Nothing Then
        Debug.Print "Failed to activate Costing analysis."
        Exit Sub
    End If
```

```
    'Get the structural Costing analysis
    Set swcStructuralAnalysis = swcCostAnalysis.GetSpecificAnalysis
    If swcStructuralAnalysis Is Nothing Then
        Debug.Print "Structural Costing analysis is nothing."
        Exit Sub
    End If
```

```
    'Get the material classes from the Costing template
    materialClassCount = swcStructuralAnalysis.GetMaterialClassesCount
    If materialClassCount = 0 Then
        Debug.Print ("No material classes for this structural Costing analysis.")
        Exit Sub
    End If
```

```
    Debug.Print "Structural Costing Analysis"
```

```
    materialClasses = swcStructuralAnalysis.GetMaterialClasses
    Debug.Print ("  Valid material classes for this structural Costing Analysis: ")
    For i = 0 To materialClassCount - 1
        Debug.Print ("    " & materialClasses(i))
    Next i
```

```
    'Set the material class
    swcStructuralAnalysis.CurrentMaterialClass = materialClasses(0)
    Debug.Print ("  Name of the material class for this structural Costing analysis: " & materialClasses(0))
```

```
    'Get the material names from the Costing template
    templateName = swcCostAnalysis.CostingTemplateName
    Debug.Print ("  Costing template path and file name: " & templateName)
    materialCount = swcStructuralAnalysis.GetMaterialCount(materialClasses(0))
    If materialCount = 0 Then
        Debug.Print "No materials for this structural Costing Analysis."
        Exit Sub
    End If
    Debug.Print "  Number of materials: " & materialCount
    materials = swcStructuralAnalysis.GetMaterials(materialClasses(0))
    Debug.Print ("  Valid materials for this structural Costing Analysis: ")
    For i = 0 To materialCount - 1
        Debug.Print ("    " & materials(i))
    Next i
```

```
    swcStructuralAnalysis.CurrentMaterial = materials(0)
    Debug.Print ("  Name of material for " & materialClasses(0) & " for this structural Costing analysis: " & materials(0))
```

```
    'Set and get structural Costing analysis parameters
    'Get current profile
    Debug.Print "  Current profile:"
    Debug.Print "    Standard: " & swcStructuralAnalysis.CurrentProfileStandard
    Debug.Print "    Type:     " & swcStructuralAnalysis.CurrentProfileType
    Debug.Print "    Size:     " & swcStructuralAnalysis.CurrentProfileSize
```

```
    'Get current cost method
    costMethod = swcStructuralAnalysis.CurrentCostMethodType
    Select Case costMethod
        Case 0
            Debug.Print "  Current cost method: Unknown"
            Debug.Print "  Exiting. Check the template."
            Exit Sub
        Case 1
            Debug.Print "  Current cost method: Per length"
        Case 2
            Debug.Print "  Current cost method: Per unit length"
    End Select
```

```
   'Reset the shop rate to the default
    swcStructuralAnalysis.ShopRateApplied = True
    swcStructuralAnalysis.shoprate = 27.55
    Debug.Print ("  Shop rate applied: " & swcStructuralAnalysis.ShopRateApplied)
    Debug.Print ("  Shop rate: $" & swcStructuralAnalysis.shoprate)

    totalCost = swcCostAnalysis.GetTotalCostToManufacture
    Debug.Print ("Total structural cost to manufacture: $" & totalCost)
```

```
End Sub
```
