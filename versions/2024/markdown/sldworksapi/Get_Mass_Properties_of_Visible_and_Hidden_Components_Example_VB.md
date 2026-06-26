---
title: "Get Mass Properties of Visible and Hidden Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mass_Properties_of_Visible_and_Hidden_Components_Example_VB.htm"
---

# Get Mass Properties of Visible and Hidden Components Example (VBA)

This example shows how to get the mass properties for:

- visible and hidden components in an assembly.
- only the visible components in an assembly.

```
'----------------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\routing-pipes\ball valve with flanges.sldasm.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the mass properties of all components.
' 2. Hides the slip on weld flange<1> component.
' 3. Gets the mass properties of the visible components only.
' 4. Examine the Immediate window.
'
' NOTE: Because this assembly is used elsewhere, do not save changes.
'---------------------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim massStatus As Long
Dim vMassProp As Variant
Dim boolstatus As Boolean

Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    Debug.Print "-------------------------------"
```

```
    Debug.Print "Mass properties of all visible and hidden components:"
    vMassProp = swModelDocExt.GetMassProperties(1, massStatus)
        If Not IsEmpty(vMassProp) Then
            Debug.Print "  CenterOfMassX = " & vMassProp(0)
            Debug.Print "  CenterOfMassY = " & vMassProp(1)
            Debug.Print "  CenterOfMassZ = " & vMassProp(2)
            Debug.Print "  Volume = " & vMassProp(3)
            Debug.Print "  Area = " & vMassProp(4)
            Debug.Print "  Mass = " & vMassProp(5)
            Debug.Print "  MomXX = " & vMassProp(6)
            Debug.Print "  MomYY = " & vMassProp(7)
            Debug.Print "  MomZZ = " & vMassProp(8)
            Debug.Print "  MomXY = " & vMassProp(9)
            Debug.Print "  MomZX = " & vMassProp(10)
            Debug.Print "  MomYZ = " & vMassProp(11)
        End If
```

```
        Debug.Print "-------------------------------"
```

```
   ' Now hide a component
   boolstatus = swModelDocExt.SelectByID2("slip on weld flange-1@ball valve with flanges", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
   swModel.HideComponent2
```

```
    Debug.Print "Mass properties of visible components only:"
    swModelDocExt.IncludeMassPropertiesOfHiddenBodies = False
    vMassProp = swModelDocExt.GetMassProperties(1, massStatus)
        If Not IsEmpty(vMassProp) Then
            Debug.Print "  CenterOfMassX = " & vMassProp(0)
            Debug.Print "  CenterOfMassY = " & vMassProp(1)
            Debug.Print "  CenterOfMassZ = " & vMassProp(2)
            Debug.Print "  Volume = " & vMassProp(3)
            Debug.Print "  Area = " & vMassProp(4)
            Debug.Print "  Mass = " & vMassProp(5)
            Debug.Print "  MomXX = " & vMassProp(6)
            Debug.Print "  MomYY = " & vMassProp(7)
            Debug.Print "  MomZZ = " & vMassProp(8)
            Debug.Print "  MomXY = " & vMassProp(9)
            Debug.Print "  MomZX = " & vMassProp(10)
            Debug.Print "  MomYZ = " & vMassProp(11)
        End If
```

```
        Debug.Print "-------------------------------"
```

```
End Sub
```
