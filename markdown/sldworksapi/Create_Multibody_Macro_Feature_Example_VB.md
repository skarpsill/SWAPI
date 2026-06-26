---
title: "Create Multibody Macro Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Multibody_Macro_Feature_Example_VB.htm"
---

# Create Multibody Macro Feature Example (VBA)

This example shows how to create a multibody macro feature.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\multibody\multi_local.sldprt.
 ' 2. Copy main module to the macro code window.
 ' 3. Right-click the project name and click Insert > Module.
 ' 4. Type mMacroFeature in (Name) in the module's Properties window
 '    (if necessary, right-click Module1 to display the Properties window).
 ' 5. Copy macro feature to the mMacroFeature code window.
 '
 ' Postconditions:
 ' 1. Creates MacroFeature1, which:
 '    * Consumes the part's solid bodies, Fillet5 and Fillet6.
 '    * Creates two solid bodies, MacroFeature1[1] and MacroFeature1[2].
 ' 2. Examine the graphics area and FeatureManager design tree.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
```

```vb
'main module
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swPart As SldWorks.PartDoc
 Option Explicit
Sub main()
     Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swPart = swModel

    Dim strMacroMethods(8) As String
     'Rebuild function
     strMacroMethods(0) = swApp.GetCurrentMacroPathName
     strMacroMethods(1) = "mMacroFeature"
     strMacroMethods(2) = "swmRebuild"
     'Edit definition function
     strMacroMethods(3) = swApp.GetCurrentMacroPathName
     strMacroMethods(4) = "mMacroFeature"
     strMacroMethods(5) = "swmEditDefinition"
     'Security function
     strMacroMethods(6) = swApp.GetCurrentMacroPathName
     strMacroMethods(7) = "mMacroFeature"
     strMacroMethods(8) = "swmSecurity"

    'Collect input bodies
     Dim vBodies As Variant
     vBodies = swPart.GetBodies2(swAllBodies, False)

    'Create the macro feature
     swModel.FeatureManager.InsertMacroFeature3 "MacroFeature", "", strMacroMethods, _
         Nothing, Nothing, Nothing, Nothing, Nothing, vBodies, Nothing,  swMacroFeatureByDefault
 End Sub
```

[Go to top](#top)

```vb
'macro feature
Function swmRebuild(app As Variant, model As Variant, feat As Variant) As Variant
     Dim OutputBodies As New Collection
     Dim swBody As SldWorks.Body2
     Dim swBodies() As SldWorks.Body2
     Dim swMacroFeatData As SldWorks.MacroFeatureData
     Set swMacroFeatData = feat.GetDefinition
     swMacroFeatData.EnableMultiBodyConsume = True

    Dim swModeler As SldWorks.Modeler
     Set swModeler = app.GetModeler
     Dim dblData(8) As Double
     dblData(0) = 0: dblData(1) = 0: dblData(2) = 0
     dblData(3) = 1: dblData(4) = 0: dblData(5) = 0
     dblData(6) = 0.1: dblData(7) = 0.1: dblData(8) = 0.1

    'Output body 1
     Set swBody = swModeler.CreateBodyFromBox3(dblData)
     OutputBodies.Add swBody

    'Output body 2
     dblData(1) = 0.15
     Set swBody = swModeler.CreateBodyFromBox3(dblData)
     OutputBodies.Add swBody

    Dim i As Integer, j As Integer
     Dim vFaces As Variant
     Dim vEdges As Variant
     ReDim swBodies(OutputBodies.Count - 1)

    For i = 1 To OutputBodies.Count
         Set swBody = OutputBodies.Item(i)
         vEdges = swBody.GetEdges
         vFaces = swBody.GetFaces
        For j = 0 To UBound(vEdges)
             swMacroFeatData.SetEdgeUserId vEdges(j), j, 0
         Next j
         For j = 0 To UBound(vFaces)
             swMacroFeatData.SetFaceUserId vFaces(j), j, 0
         Next j
        Set swBodies(i - 1) = OutputBodies.Item(i)
     Next i
    swmRebuild = swBodies

 End Function
Function swmEditDefinition(app As Variant, model As Variant, feat As Variant) As Variant
End Function
Function swmSecurity(app As Variant, model As Variant, feat As Variant) As Variant
End Function
```

[Go to top](#top)
