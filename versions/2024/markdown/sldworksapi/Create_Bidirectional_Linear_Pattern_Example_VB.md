---
title: "Create Bidirectional Linear Pattern Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Bidirectional_Linear_Pattern_Example_VB.htm"
---

# Create Bidirectional Linear Pattern Example (VBA)

This example shows how to create a bidirectional linear pattern.

```
'----------------------------------------------------
' Preconditions: Verify that the part exists.
'
' Postconditions:
' 1. Opens the part.
' 2. Selects the feature to pattern.
' 3. Selects the edges for Direction 1 and
'    Direction 2 for the bidirectional linear
'    pattern.
' 4. Creates a bidirectional linear pattern.
' 5. Examine the FeatureManager design tree and
'    graphics area.
'
' NOTE: Because the part is used elsewhere, do not save
' changes.
'------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeatureManager As SldWorks.FeatureManager
Dim swFeature As SldWorks.Feature
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim fileName As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\box.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
    Set swFeatureManager = swModel.FeatureManager
```

```
    'Select feature to pattern
    status = swModelDocExt.SelectByID2("CBORE for #6 Binding Head Machine Screw1", "BODYFEATURE", 0, 0, 0, False, 4, Nothing, 0)

    'Select edges for Direction 1 and Direction 2
    status = swModelDocExt.SelectByID2("", "EDGE", -3.41223962029176E-02, 3.00321434688158E-02, 4.60303188361877E-02, True, 1, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "EDGE", 4.36465176948104E-02, 3.01916139486593E-02, 1.14344277122314E-02, True, 2, Nothing, 0)
```

```
    'Create linear pattern
    Set swFeature = swFeatureManager.FeatureLinearPattern5(3, 0.01, 3, 0.01, False, False, "NULL", "NULL", True, False, False, False, False, False, True, True, False, False, 0, 0, False, False)
```

```
End Sub
```
