---
title: "Get Material Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Material_Example_VB.htm"
---

# Get Material Example (VBA)

This example shows how to get the material for a part.

```
'------------------------------------------------------
' Preconditions:
' 1. Open a part with a configuration named Default.
' 2. Apply a material to the part.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the name of the material applied to the part.
' 2. Examine the Immediate window.
'------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swPart As SldWorks.PartDoc
    Dim sMatName As String
    Dim sMatDB As String
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
```

```
    sMatName = swPart.GetMaterialPropertyName2("Default", sMatDB)
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Material = " & sMatName & " (" & sMatDB & ")"
```

```
End Sub
```
