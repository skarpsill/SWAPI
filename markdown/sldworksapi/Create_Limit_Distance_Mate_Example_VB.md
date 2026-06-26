---
title: "Create and Edit Limit Distance Mate Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Limit_Distance_Mate_Example_VB.htm"
---

# Create and Edit Limit Distance Mate Example (VBA)

This example shows how to create and edit a limit distance mate.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open:
 '    public_documents\samples\tutorial\api\AdvancedMates\AdvancedMateDemo1.sldasm
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a limit distance mate.
 ' 2. Press F5 to continue.
 ' 3. Modifies the mate alignment of the limit distance mate.
 ' 4. Inspect the Immediate window and graphics area.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
 Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swAssy As SldWorks.AssemblyDoc
 Dim swDistMateData As SldWorks.DistanceMateFeatureData
 Dim swMateData As SldWorks.MateFeatureData
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim boolstatus As Boolean
 Dim feat As SldWorks.Feature
 Dim facesDist(1) As SldWorks.Face2
 Dim vFacesDist As Variant
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swAssy = swModel
     Set swSelMgr = swModel.SelectionManager

    Set swMateData = swAssy.CreateMateData(5) 'Distance mate

    Debug.Print "Type of mate as defined in swMateType_e: " & swMateData.TypeName

    Set swDistMateData = swMateData
     swDistMateData.MateAlignment = SwConst.swMateAlign_e.swMateAlignALIGNED
     swDistMateData.FlipDimension = False
     swDistMateData.Distance = 0.0254
     swDistMateData.MaximumDistance = 0.0254
     swDistMateData.MinimumDistance = 0.01

    boolstatus = swModel.Extension.SelectByRay(8.68857956595548E-03, 4.14144214960288E-02, 6.33435410960033E-02, -0.520148774728431, -0.59141018013918, -0.616181183562315, 4.68381592786756E-04, 2, True, 1, 0)
     boolstatus = swModel.Extension.SelectByRay(3.13565896258297E-02, 2.96508617577445E-02, 4.42099188854286E-02, 0.340524666870961, -0.380278973953885, -0.859901653226112, 4.31713609895031E-04, 2, True, 1, 0)

    Set facesDist(0) = swSelMgr.GetSelectedObject6(1, -1)
     Set facesDist(1) = swSelMgr.GetSelectedObject6(2, -1)

    vFacesDist = facesDist

    swDistMateData.EntitiesToMate = vFacesDist

    Set feat = swAssy.CreateMate(swDistMateData)

    swModel.GraphicsRedraw2

    Stop

    Set feat = swModel.Extension.GetLastFeatureAdded
     Debug.Print "Feature GetTypeName2 of mate created is " & feat.GetTypeName2

    Set swMateData = feat.GetDefinition

    If (swMateData.TypeName = SwConst.swMateType_e.swMateDISTANCE) Then

        Set swDistMateData = swMateData
         Debug.Print "Distance mate alignment is " & swDistMateData.MateAlignment

        If (swDistMateData.MateAlignment = SwConst.swMateAlign_e.swMateAlignALIGNED) Then
             swDistMateData.MateAlignment = SwConst.swMateAlign_e.swMateAlignANTI_ALIGNED
         Else
             swDistMateData.MateAlignment = SwConst.swMateAlign_e.swMateAlignALIGNED
         End If

        Debug.Print "Distance mate alignment changed to " & swDistMateData.MateAlignment
         Debug.Print "Distance: " & swDistMateData.Distance
         Debug.Print "Minimum distance: " & swDistMateData.MinimumDistance
         Debug.Print "Maximum distance: " & swDistMateData.MaximumDistance
         Debug.Print "Move entities to opposite sides of the dimension? " & swDistMateData.FlipDimension

        boolstatus = feat.ModifyDefinition(swDistMateData, swAssy, Nothing)

    End If
End Sub
```
