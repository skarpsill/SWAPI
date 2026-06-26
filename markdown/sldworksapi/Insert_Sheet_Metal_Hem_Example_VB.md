---
title: "Insert Sheet Metal Hem Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Sheet_Metal_Hem_Example_VB.htm"
---

# Insert Sheet Metal Hem Example (VBA)

This example shows how to insert a hem into a sheet metal part.

```
'-------------------------------------------------------------------
' Preconditions:
' 1. Open a sheet metal part.
' 2. Select the edge to which you can add a hem.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Adds an open hem with a custom relief of type Obround and
'    a relief ratio of 1.0.
' 2. Gets the hem type.
' 3. Examine the Immediate window and graphics area.
' -----------------------------------------------------------------
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim CBAObject As SldWorks.CustomBendAllowance
 Dim myFeature As SldWorks.Feature
 Dim myHem As SldWorks.HemFeatureData

Option Explicit
 Sub main()
     Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc
    Set CBAObject = Part.FeatureManager.CreateCustomBendAllowance()
     CBAObject.Type = 2
     CBAObject.KFactor = 0.5

    ' Insert an open hem of custom relief type Obround and relief ratio 1.0
     Set myFeature = Part.FeatureManager.InsertSheetMetalHem2(swHemTypes_e.swHemTypeOpen, swHemPositionTypes_e.swHemPositionTypeOutside, False, 0.01, 0.01, 0, 0.005, 0.0011, CBAObject, False, swSheetMetalReliefTypes_e.swSheetMetalReliefObround, 0, True, 1#, 0, 0)
     Part.ClearSelection2 True

    Set myHem = myFeature.GetDefinition
     Debug.Print "Hem type as defined in swHemTypes_e: " & myHem.Type
 End Sub
```
