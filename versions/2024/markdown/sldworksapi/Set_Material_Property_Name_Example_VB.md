---
title: "Set Material Property Name Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Material_Property_Name_Example_VB.htm"
---

# Set Material Property Name Example (VBA)

This example shows how to set a part's material property name.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Changes the model's and part's material property name
'    Alloy Steel.
' 2. Examine the Immediate window.
'------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Old model material   = " & swModel.MaterialIdName
    Debug.Print "  Old part  material   = " & swPart.MaterialIdName
```

```
    swPart.SetMaterialPropertyName "SOLIDWORKS Materials.sldmat", "Alloy Steel"
```

```
    Debug.Print "  New model material   = " & swModel.MaterialIdName
    Debug.Print "  New part  material   = " & swPart.MaterialIdName
```

```
End Sub
```
