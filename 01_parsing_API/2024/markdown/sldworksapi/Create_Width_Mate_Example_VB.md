---
title: "Create and Edit Width Mate Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Width_Mate_Example_VB.htm"
---

# Create and Edit Width Mate Example (VBA)

This example shows how to create and edit a width mate.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open:
 '    public_documents\samples\tutorial\api\AdvancedMates\AdvancedMateDemo1.sldasm
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a width mate of constraint type, dimension.
 ' 2. Press F5 to continue.
 ' 3. Changes the width mate to constraint type, percent.
 ' 4. Inspect the Immediate window and graphics area.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
 Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swAssy As SldWorks.AssemblyDoc
 Dim swWidthMateData As SldWorks.WidthMateFeatureData
 Dim swMateData As SldWorks.MateFeatureData
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim boolstatus As Boolean
 Dim feat As SldWorks.Feature
 Dim faceTab(1) As SldWorks.Face2
 Dim facesWidth(1) As SldWorks.Face2
 Dim vFacesTab As Variant
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swAssy = swModel
     Set swSelMgr = swModel.SelectionManager

    Set swMateData = swAssy.CreateMateData(11) 'Width mate

    If (swMateData.TypeName = SwConst.swMateType_e.swMateWIDTH) Then

        Set swWidthMateData = swMateData
         swWidthMateData.ConstraintType = SwConst.swMateWidthOptions_e.swMateWidth_Dimension

        Debug.Print "Width Mate Constraint Type is " & swWidthMateData.ConstraintType

        ' Select faces for the width and tab of this width mate
        boolstatus = swModel.Extension.SelectByRay(8.68857956595548E-03, 4.14144214960288E-02, 6.33435410960033E-02, -0.520148774728431, -0.59141018013918, -0.616181183562315, 4.68381592786756E-04, 2, True, 1, 0)
         boolstatus = swModel.Extension.SelectByRay(0.040068521476087, 3.99799509449394E-02, 5.85753748188154E-02, 0.320596315934938, -0.422312467890091, -0.847862124212143, 4.68381592786756E-04, 2, True, 1, 0)
         boolstatus = swModel.Extension.SelectByRay(3.13565896258297E-02, 2.96508617577445E-02, 4.42099188854286E-02, 0.340524666870961, -0.380278973953885, -0.859901653226112, 4.31713609895031E-04, 2, True, 16, 0)
         boolstatus = swModel.Extension.SelectByRay(2.67766714922573E-02, 2.59424893815421E-02, 3.80784753310763E-02, -0.849725692314326, -0.107993323108602, 0.516046209156602, 4.31713609895031E-04, 2, True, 16, 0)

        Set facesWidth(0) = swSelMgr.GetSelectedObject6(1, -1)
         Set facesWidth(1) = swSelMgr.GetSelectedObject6(2, -1)

        Dim vFacesWidth As Variant
         vFacesWidth = facesWidth

        swWidthMateData.WidthSelection = vFacesWidth

        Set faceTab(0) = swSelMgr.GetSelectedObject6(3, -1)
         Set faceTab(1) = swSelMgr.GetSelectedObject6(4, -1)

         vFacesTab = faceTab

        swWidthMateData.TabSelection = (vFacesTab)

        If (swWidthMateData.ConstraintType = SwConst.swMateWidthOptions_e.swMateWidth_Dimension) Then
             swWidthMateData.DistanceFromEnd = 0.04975511004
             swWidthMateData.FlipDimension = True
         End If

        Set feat = swAssy.CreateMate(swWidthMateData)

    End If

    swModel.GraphicsRedraw2

    Stop

    Set feat = swModel.Extension.GetLastFeatureAdded

    Set swMateData = feat.GetDefinition

    If (swMateData.TypeName = SwConst.swMateType_e.swMateWIDTH) Then
        Set swWidthMateData = swMateData

        Debug.Print "Width mate constraint type is " & swWidthMateData.ConstraintType

        swWidthMateData.ConstraintType = SwConst.swMateWidthOptions_e.swMateWidth_Percent
         swWidthMateData.PercentDistanceFromEnd = 47
         swWidthMateData.FlipDimension = False
        Debug.Print "Width mate constraint type changed to " & swWidthMateData.ConstraintType
         Debug.Print "Distance from the end of this width mate: " & swWidthMateData.DistanceFromEnd
         Debug.Print "Percentage of distance from the end of this width mate: " & swWidthMateData.PercentDistanceFromEnd
         Debug.Print "Move entities to opposite sides of the dimension? " & swWidthMateData.FlipDimension

        boolstatus = feat.ModifyDefinition(swWidthMateData, swAssy, Nothing)

    End If
End Sub
```
