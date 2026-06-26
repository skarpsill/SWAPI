---
title: "Insert Gusset Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Gusset_Feature_Example_VB.htm"
---

# Insert Gusset Feature Example (VBA)

This example shows how to create a weldment gusset feature.

```
'----------------------------------------------------------------------------
' Preconditions: Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
'
' Postconditions:
' 1. Creates Gusset5.
' 2. Expand CutList(32) in the FeatureManager design tree and
'    scroll to the bottom of the list.
' 3. Examine the graphics area.
'
' NOTE: Because the model is used elsewhere, do not save changes.
'---------------------------------------------------------------------------
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim myFeature As SldWorks.Feature
 Dim boolstatus As Boolean

 Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.ActiveDoc

    boolstatus = Part.Extension.SelectByID2("", "FACE", 0.600909534718824, 0.15614125327869, -0.985000000000127, True, 1, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("", "FACE", 0.597259667129663, 1.49999999998727E-02, -0.944257845206607, True, 1, Nothing, 0)

    Set myFeature = Part.FeatureManager.InsertGussetFeature3(0.005, swGussetThicknessType_e.swGussetThicknessBothSides, swGussetProfileLocationType_e.swGussetProfileLocationCenter, False, 0.025, 0.025, 0.015, 0.78539816339745, 0.015, False, 0.005, 0, False, False, False, 0.0125, 0.0125, 0.785398163397452, True, False)

End Sub
```
