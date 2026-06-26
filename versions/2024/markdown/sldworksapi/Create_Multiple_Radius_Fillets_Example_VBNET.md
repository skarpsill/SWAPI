---
title: "Create Multiple-Radius Fillets Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Multiple_Radius_Fillets_Example_VBNET.htm"
---

# Create Multiple-Radius Fillets Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swModelDocExt As ModelDocExtension
     Dim swFeatMgr As FeatureManager
     Dim VarRadArray8 As Object
     Dim radArray8(2) As Double
     Dim FilletOptions As Long

     Sub main()

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension
         swFeatMgr = swModel.FeatureManager

         'Multiple Radii
         radArray8(0) = 0.01
         radArray8(1) = 0.015
         radArray8(2) = 0.02
         VarRadArray8 = radArray8

         'Fillet options
         FilletOptions = swFeatureFilletOptions_e.swFeatureFilletPropagate + swFeatureFilletOptions_e.swFeatureFilletAttachEdges + swFeatureFilletOptions_e.swFeatureFilletKeepFeatures

         'Create multiple-radius fillets along selected edges
         swFeatMgr.FeatureFillet(FilletOptions, 0.01, swFeatureFilletType_e.swFeatureFilletType_Simple, swFilletOverFlowType_e.swFilletOverFlowType_Default, (VarRadArray8), 0, 0)

     End Sub

     Public swApp As SldWorks

 End Class
```
