---
title: "Add and Get Property Extensions Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Get_Property_Extension_Example_VB.htm"
---

# Add and Get Property Extensions Example (VBA)

This example shows how to add and get a property extension on a part.

```
'--------------------------------------------------------
' Preconditions:
' 1. Open a part.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Adds three property extensions to the part.
' 2. Gets the three property extensions added to the part.
' 3. Examine the Immediate window.
'--------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swPart As SldWorks.PartDoc
    Dim retVal As Long
    Dim objAdded As Variant
    Dim objAdded2 As Variant
    Dim objAdded3 As Variant
    Dim objRetrieved As Variant
```

```
    Set swApp = Application.SldWorks
    Set swPart = swApp.ActiveDoc
```

```
    Debug.Print "Property extensions added:"

    objAdded = "12345PID"
    retVal = swPart.AddPropertyExtension(objAdded)
    Debug.Print " First property extension: " & objAdded
```

```
    objAdded2 = "6789PID"
    retVal = swPart.AddPropertyExtension(objAdded2)
    Debug.Print " Second property extension: " & objAdded2
```

```
    objAdded3 = "00000PID"
    retVal = swPart.AddPropertyExtension(objAdded3)
    Debug.Print " Third property extension: " & objAdded3
```

```
    Debug.Print "Property extensions retrieved:"

    objRetrieved = swPart.GetPropertyExtension(retVal - 3)
    Debug.Print " First property extension: " & objRetrieved
```

```
    objRetrieved = swPart.GetPropertyExtension(retVal - 2)
    Debug.Print " Second property extension: " & objRetrieved
```

```
    objRetrieved = swPart.GetPropertyExtension(retVal - 1)
    Debug.Print " Third property extension: " & objRetrieved
```

```
End Sub
```
