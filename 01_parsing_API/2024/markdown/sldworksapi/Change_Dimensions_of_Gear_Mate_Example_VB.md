---
title: "Change Dimensions of Gear Mate Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Dimensions_of_Gear_Mate_Example_VB.htm"
---

# Change Dimensions of Gear Mate Example (VBA)

This example shows how to change the dimensions of a gear mate.

```
'---------------------------------------------------------------------
' Preconditions:
' 1. Verify that the assembly to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the assembly.
' 2. Selects a face on middle-gear<1> and a face on shaft gear<1>.
' 3. Adds a mate called GearMate1.
' 4. Gets and sets the dimensions of GearMate1.
' 5. Expand MateGroup1 and edit GearMate1.
' 6. Examine the Immediate window to verify that the values shown
'    there match the ratios shown in the GearMate1 PropertyManager page.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'---------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swAssembly As SldWorks.AssemblyDoc
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swMate As SldWorks.Mate2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim swDispDim_1 As SldWorks.DisplayDimension
Dim swDispDim_2 As SldWorks.DisplayDimension
Dim swDim_1 As SldWorks.Dimension
Dim swDim_2 As SldWorks.Dimension
Dim dimValue_1 As Variant
Dim dimValue_2 As Variant
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim mateSelectionMark As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swAssembly = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\98food processor.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModel = swAssembly
    Set swModelDocExt = swModel.Extension
```

```
    ' Add a gear mate
    mateSelectionMark = 1
    swModel.ViewZoomTo2 0.032214794364982, -2.13641280653619E-03, 2.43727437299652E-02, 7.14815689826596E-02, -2.90907241966369E-02, 2.43727437299654E-02
    status = swModelDocExt.SelectByID2("", "FACE", 5.94157516983955E-02, 1.47722422245806E-02, 1.01883978994124E-02, True, mateSelectionMark, Nothing, swSelectOption_e.swSelectOptionDefault)
    status = swModelDocExt.SelectByID2("", "FACE", 0.10202121114628, 0.037565135718296, 1.20206517165684E-02, True, mateSelectionMark, Nothing, swSelectOption_e.swSelectOptionDefault)
    Set swMate = swAssembly.AddMate5(swMateType_e.swMateGEAR, swMateAlign_e.swMateAlignALIGNED, True, 4.79944356756808E-02, 0.001, 0.001, 0.0618, 0.0752, 0.5235987755983, 0.5235987755983, 0.5235987755983, False, False, 0, errors)
    swModel.ClearSelection2 True
    swModel.EditRebuild3
```

```
    Set swSelMgr = swModel.SelectionManager
    swModel.ShowFeatureDimensions
```

```
    ' Select the gear mate
    status = swModelDocExt.SelectByID2("GearMate1", "MATE", 0, 0, 0, False, 0, Nothing, swSelectOption_e.swSelectOptionDefault)
    Set swFeature = swSelMgr.GetSelectedObject6(1, -1)
```

```
    Set swMate = swFeature.GetSpecificFeature2
```

```
    ' IMate2::DisplayDimension2 is a property
    ' that requires an index argument
    ' For a gear mate, there are two display dimensions
    ' Thus, IMate2::DisplayDimension2(0) and
    ' IMate2::DisplayDimension2(1) give two display dimensions
```

```
    ' Get the gear mates' display dimensions
    Set swDispDim_1 = swMate.DisplayDimension2(0)
    Set swDispDim_2 = swMate.DisplayDimension2(1)
```

```
    ' Get the dimensions
    Set swDim_1 = swDispDim_1.GetDimension
    Set swDim_2 = swDispDim_2.GetDimension
```

```
    ' Get the value of dimensions
    dimValue_1 = swDim_1.GetSystemValue3(swInConfigurationOpts_e.swThisConfiguration, Empty)
    dimValue_2 = swDim_2.GetSystemValue3(swInConfigurationOpts_e.swThisConfiguration, Empty)
    Debug.Print "Original gear dimensions: " & dimValue_2(0) * 1000 & "mm, " & dimValue_1(0) * 1000 & "mm"
```

```
    ' Half the values of dimensions
    dimValue_1(0) = dimValue_1(0) / 2
    dimValue_2(0) = dimValue_2(0) / 2
    errors = swDim_1.SetSystemValue3(dimValue_1(0), swSetValueInConfiguration_e.swSetValue_InThisConfiguration, Empty)
    errors = swDim_2.SetSystemValue3(dimValue_2(0), swSetValueInConfiguration_e.swSetValue_InThisConfiguration, Empty)
    Debug.Print "Updated gear dimensions: " & dimValue_2(0) * 1000 & "mm, " & dimValue_1(0) * 1000 & "mm"
```

```
    swModel.EditRebuild3
```

```
End Sub
```
