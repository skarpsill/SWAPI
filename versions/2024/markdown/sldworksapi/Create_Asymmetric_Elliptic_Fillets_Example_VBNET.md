---
title: "Create Variable Radius Asymmetric Elliptical Fillet Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Asymmetric_Elliptic_Fillets_Example_VBNET.htm"
---

# Create Variable Radius Asymmetric Elliptical Fillet Example (VB.NET)

This example shows how to create a variable radius asymmetric elliptical fillet and get its data.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\block.sldprt.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a variable radius asymmetric elliptical fillet, VarFillet1,
 '    in the FeatureManager design tree.
 ' 2. Inspect the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swSelMgr As SelectionMgr
     Dim myFeature As Feature
     Dim swedge As Edge
     Dim ver1 As Vertex
     Dim ver2 As Vertex
     Dim swFeatData As VariableFilletFeatureData2
     Dim Fillet_ProfileTyp As Integer
     Dim dists26(1) As Double
     Dim AsyRadius1 As Double
     Dim AsyRadius2 As Double
     Dim AsyRadius3 As Double
     Dim AsyRadius4 As Double
     Dim boolstatus As Boolean
     Dim radiis(1) As Double
     Dim radiiArray0 As Object
     Dim conicRhosArray0 As Object
     Dim setBackArray0 As Object
     Dim pointArray0 As Object
     Dim pointRhoArray0 As Object
     Dim dist2Array0 As Object
     Dim pointDist2Array0 As Object

     Sub main()

         swModel = SwApp.ActiveDoc
         swSelMgr = swModel.SelectionManager

         radiis(0) = 0.008
         radiis(1) = 0.009
         radiiArray0 = radiis
         dists26(0) = 0.006
         dists26(1) = 0.007
         dist2Array0 = dists26

         conicRhosArray0 = 0
         setBackArray0 = 0
         pointArray0 = 0
         pointRhoArray0 = 0
         pointDist2Array0 = 0
```

```vb
        boolstatus = swModel.Extension.SelectByID2("", "EDGE", 0.0166068305868521, -0.00000440742070395572, -0.0149970056632469,  True, 1, Nothing, 0)
```

```vb
         If boolstatus = False Then ErrorMsg(SwApp, "Failed to select edge")

         myFeature = swModel.FeatureManager.FeatureFillet3(swFeatureFilletOptions_e.swFeatureFilletAsymmetric + swFeatureFilletOptions_e.swFeatureFilletKeepFeatures + swFeatureFilletOptions_e.swFeatureFilletAttachEdges + swFeatureFilletOptions_e.swFeatureFilletUniformRadius + swFeatureFilletOptions_e.swFeatureFilletPropagate, 0, 0, 0, swFeatureFilletType_e.swFeatureFilletType_VariableRadius, swFilletOverFlowType_e.swFilletOverFlowType_Default, swFeatureFilletProfileType_e.swFeatureFilletCircular, (radiiArray0), (dist2Array0), (conicRhosArray0), (setBackArray0), (pointArray0), (pointDist2Array0), (pointRhoArray0))
         If myFeature Is Nothing Then ErrorMsg(SwApp, "Failed to create fillet")

         swFeatData = myFeature.GetDefinition()
         If swFeatData Is Nothing Then ErrorMsg(SwApp, "Failed to get definition for fillet feature")

         boolstatus = swFeatData.AccessSelections(swModel,  Nothing)
         If boolstatus = False Then ErrorMsg(SwApp, "Failed to access selections for fillet feature")

         boolstatus = swFeatData.AsymmetricFillet
         If boolstatus = False Then ErrorMsg(SwApp, "Fillet is not asymmetric")
         Debug.Print("Variable size fillet is asymmetric? " & boolstatus)

         swedge = swFeatData.GetFilletEdgeAtIndex(0)
         If swedge Is Nothing Then ErrorMsg(SwApp, "Failed to get edge")

         ver1 = swedge.GetStartVertex
         If ver1 Is Nothing Then ErrorMsg(SwApp, "Failed to get start vertex of edge")

         ver2 = swedge.GetEndVertex
         If ver2 Is Nothing Then ErrorMsg(SwApp, "Failed to get end vertex of edge")

         AsyRadius1 = swFeatData.GetRadius2(ver1,  True)
         If AsyRadius1 <> 0.008 Then ErrorMsg(SwApp, "Radius R1 at vertex V1 is wrong")
         Debug.Print("Radius R1 at vertex V1: " & AsyRadius1)

         AsyRadius2 = swFeatData.GetDistance(ver1)
         If AsyRadius2 <> 0.006 Then ErrorMsg(SwApp, "Radius R2 at vertex V1 is wrong")
         Debug.Print("Radius R2 at vertex V1: " & AsyRadius2)

         AsyRadius3 = swFeatData.GetRadius2(ver2,  True)
         If AsyRadius3 <> 0.009 Then ErrorMsg(SwApp, "Radius R1 for vertex V2 is wrong")
         Debug.Print("Radius R1 at vertex V2: " & AsyRadius3)

         AsyRadius4 = swFeatData.GetDistance(ver2)
         If AsyRadius4 <> 0.007 Then ErrorMsg(SwApp, "Radius R2 for vertex V2 is wrong")
         Debug.Print("Radius R2 at vertex V2: " & AsyRadius4)

         Fillet_ProfileTyp = swFeatData.ConicTypeForCrossSectionProfile
         If Fillet_ProfileTyp <> 0 Then ErrorMsg(SwApp, "Profile type is not elliptical")
         Debug.Print("Fillet profile type as defined in swFeatureFilletProfileType_e (0 = Elliptical): " & Fillet_ProfileTyp)

         swFeatData.ReleaseSelectionAccess()

     End Sub

     Sub ErrorMsg(ByVal SwApp As SldWorks, ByVal Message As String)
         SwApp.SendMsgToUser2(Message, 0, 0)
         SwApp.RecordLine("'*** WARNING - General")
         SwApp.RecordLine("'*** " & Message)
         SwApp.RecordLine("")
     End Sub

     Public swApp As SldWorks

 End  Class
```
