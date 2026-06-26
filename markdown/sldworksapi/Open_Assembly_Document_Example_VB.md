---
title: "Open Assembly Document Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Assembly_Document_Example_VB.htm"
---

# Open Assembly Document Example (VBA)

This example shows how to specify how to open an assembly document.

```
'------------------------------------------------------
' Preconditions: Verify that the specified assembly document
' to open exists.
'
' Postconditions:
' 1. If the Large Design Review dialog is displayed, click OK
'    to close it.
' 2. Opens the specified assembly document and loads
'    and displays the specified component.
' 3. Examine the graphics area.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDocSpecification As SldWorks.DocumentSpecification
Dim componentsArray(0) As String
Dim components As Variant
Dim name As String
Dim errors As Long
Dim warnings As Long

Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Set the specifications
    Set swDocSpecification = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\bowl and chute.sldasm")
    componentsArray(0) = "food bowl-1@bowl and chute"
    components = componentsArray
    swDocSpecification.ComponentList = components
    swDocSpecification.Selective = True
    name = swDocSpecification.FileName
    swDocSpecification.DocumentType = swDocASSEMBLY
    swDocSpecification.DisplayState = "Default_Display State-1"
    swDocSpecification.UseLightWeightDefault = False
    swDocSpecification.LightWeight = True
    swDocSpecification.Silent = True
    swDocSpecification.IgnoreHiddenComponents = True
```

```
    'Open the assembly document as per the specifications
    Set swModel = swApp.OpenDoc7(swDocSpecification)
    errors = swDocSpecification.error
    warnings = swDocSpecification.Warning

End Sub
```
