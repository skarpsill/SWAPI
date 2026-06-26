---
title: "Create Split Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Split-body_Feature_Example_VB.htm"
---

# Create Split Feature Example (VBA)

This example shows how to create a Split feature.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part document that contains a body that is bisected by
 '    Top Plane.
 ' 2. Verify that c:\temp exists.
 ' 3. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates Split1.
 ' 2. Saves a split body to c:\temp\Body1.sldprt.
 ' 3. Inspect the Immediate window, FeatureManager design tree, graphics area,
 '    and c:\temp.
 '---------------------------------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim swModelDocExt As SldWorks.ModelDocExtension
 Dim swFeat As SldWorks.Feature
 Dim swFeatMgr As SldWorks.FeatureManager
 Dim swSplitBodyFeat As SldWorks.SplitBodyFeatureData
 Dim boolstatus As Boolean
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension
     Set swSelMgr = swModel.SelectionManager
     Set swFeatMgr = swModel.FeatureManager
    'Select the cutting tool
     boolstatus = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
    'Get bodies resulting from the split operation
     Dim vResultingBodies As Variant
     vResultingBodies = swFeatMgr.PreSplitBody2
    swModel.ClearSelection2 True
    Dim vBodiesToMark As Variant
     Dim vBodyNames As Variant
     Dim vBodyOrigins As Variant
     Dim bodiesToMark(1) As Object
     Dim bodyNames(1) As String
     Dim bodyOrigins(1) As Object

     'Set up the arrays for the post-split operation
    'Specify the origins of the bodies to save; specify Nothing to use the default origins
     Set bodyOrigins(0) = Nothing
     Set bodyOrigins(1) = Nothing

     Set bodiesToMark(0) = vResultingBodies(0)
     Set bodiesToMark(1) = vResultingBodies(1)
    'Save the first body to a separate part document
     'Substitute the name of the actual folder where to save the body
     bodyNames(0) = "c:\temp\Body1.sldprt"
    'Do not save the second body
     bodyNames(1) = ""
    vBodiesToMark = bodiesToMark
     vBodyNames = bodyNames
     vBodyOrigins = bodyOrigins
    'Create the Split feature, consuming all split bodies
     Set swFeat = swFeatMgr.PostSplitBody2((vBodiesToMark), True, (vBodyOrigins), (vBodyNames), "")
    If (Not swFeat Is Nothing) Then
         Debug.Print "Split feature: " & swFeat.Name
         Set swSplitBodyFeat = swFeat.GetDefinition
         Debug.Print "Consumed? " & swSplitBodyFeat.Consume
         Debug.Print " "
     End If
End Sub
```
