---
title: "Recalculate Bounding Box Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Recalculate_Bounding_Box_Example_VB.htm"
---

# Recalculate Bounding Box Example (VBA)

This example shows how to recalculate the bounding box of an assembly.

```
'-----------------------------------------
' Preconditions:
' 1. Specified assembly document exists.
' 2. Open the Immediate window.
' 3. Run the macro.
'
' Postconditions:
' 1. Opens assembly document.
' 2. Gets the bounding box for the assembly.
' 3. Prints the lower- and upper-diagonal corner points
'    of the bounding box to the Immediate window.
' 4. Modifies a dimension in a component in the assembly.
' 5. Updates the bounding box.
' 6. Prints the lower- and upper-diagonal corner points
'    of the bounding box to the Immediate window.
' 7. Examine the values printed to the Immediate window
'    to verify that the bounding box was updated.
'
' NOTE: Because this assembly is used elsewhere,
' do not save any changes when closing it.
'-------------------------------------------
Option Explicit
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swDimension As SldWorks.Dimension
    Dim fileName As String
    Dim errors As Long
    Dim warnings As Long
    Dim status As Boolean
```

```
Sub ProcessAssyBox(swApp As SldWorks.SldWorks, swAssy As SldWorks.AssemblyDoc)
    Dim vBox As Variant
    vBox = swAssy.GetBox(0)
    Debug.Print "  Min = (" & vBox(0) * 1000# & ", " & vBox(1) * 1000# & ", " & vBox(2) * 1000# & ") mm"
    Debug.Print "  Max = (" & vBox(3) * 1000# & ", " & vBox(4) * 1000# & ", " & vBox(5) * 1000# & ") mm"
End Sub
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\key pad_1.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swAssy = swModel
    Set swModelDocExt = swModel.Extension
```

```
    ' Print the two diagonal corner points
    ' of the bounding box before modifying the
    ' assembly
    Debug.Print "Before:"
```

```
    ProcessAssyBox swApp, swAssy
```

```
    ' Change a dimension of one of the assembly components
    status = swModelDocExt.SelectByID2("Sketch1@Pad_1-1@key pad_1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    swModel.EditSketch
    swModel.ClearSelection2 True
    status = swModelDocExt.SelectByID2("D1@Sketch1@Pad_1-1@key pad_1", "DIMENSION", 3.06153201295202E-03, 3.73842545521677E-02, -3.23079625553351E-02, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
    Set swDimension = swModel.Parameter("D1@Sketch1@pad_1.Part")
    errors = swDimension.SetSystemValue3(0.04, swSetValueInConfiguration_e.swSetValue_InThisConfiguration, Nothing)
    swModel.ClearSelection2 True
```

```
    ' Update the bounding box
    swAssy.UpdateBox
```

```
    ' Print the two diagonal corner points of the
    ' bounding box after modifying the assembly
    Debug.Print "After:"
    ProcessAssyBox swApp, swAssy
```

```
End Sub
```
