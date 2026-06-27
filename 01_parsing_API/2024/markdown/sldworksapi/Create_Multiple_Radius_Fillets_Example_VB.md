---
title: "Create Multiple-Radius Fillets Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Multiple_Radius_Fillets_Example_VB.htm"
---

# Create Multiple-Radius Fillets Example (VBA)

This example shows how to create multiple-radius fillets.

```vb
 '--------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\box.sldprt.
 ' 2. Select three intersecting edges on the inside of the part.
 '
 ' Postconditions:
 ' 1. Fillets the three selected edges using three
 '    different radii.
 ' 2. Examine the graphics area and FeatureManager design tree.
 '
 ' Note: Because the model is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swFeatMgr As SldWorks.FeatureManager
 Dim VarRadArray8 As Variant
 Dim radArray8(2) As Double
 Dim FilletOptions As Long
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension
     Set swFeatMgr = swModel.FeatureManager
    'Multiple Radii
     radArray8(0) = 0.01
     radArray8(1) = 0.015
     radArray8(2) = 0.02
     VarRadArray8 = radArray8
    'Fillet options
     FilletOptions = swFeatureFilletPropagate + swFeatureFilletAttachEdges + swFeatureFilletKeepFeatures
    'Create multiple-radius fillets along selected edges
     swFeatMgr.FeatureFillet FilletOptions, 0.01, swFeatureFilletType_Simple, swFilletOverFlowType_Default, (VarRadArray8), 0, 0
End Sub
```
