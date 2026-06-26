---
title: "Create and Edit Linear-Linear Coupler Mate Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Linear_Coupler_Mate_Example_VB.htm"
---

# Create and Edit Linear-Linear Coupler Mate Example (VBA)

This example shows how to create and edit a linear/linear coupler mate.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open:
 '    public_documents\samples\tutorial\api\AdvancedMates\AdvancedMateDemo4.sldasm
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a linear/linear coupler mate.
 ' 2. Press F5 to continue.
 ' 3. Changes the reverse property of the mate.
 ' 4. Inspect the Immediate window and graphics area.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
 Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swAssy As SldWorks.AssemblyDoc
 Dim swLinearMateData As SldWorks.LinearCouplerMateFeatureData
 Dim swMateData As SldWorks.MateFeatureData
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim boolstatus As Boolean
 Dim feat As SldWorks.Feature
 Dim facesLC(1) As SldWorks.Face2
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swAssy = swModel
     Set swSelMgr = swModel.SelectionManager

    Set swMateData = swAssy.CreateMateData(18) 'Linear/linear coupler mate

     If (swMateData.TypeName = SwConst.swMateType_e.swMateLINEARCOUPLER) Then

        Set swLinearMateData = swMateData

        swLinearMateData.CouplerRatioNumerator = 0.00099
         Debug.Print "Linear/linear coupler ratio numerator is " & swLinearMateData.CouplerRatioNumerator

        swLinearMateData.CouplerRatioDenominator = 0.00199
         Debug.Print "Linear/linear coupler ratio denominator is " & swLinearMateData.CouplerRatioDenominator

        swLinearMateData.Reverse = False

        boolstatus = swModel.Extension.SelectByRay(-8.05427342211829E-02, 6.8649651763053E-04, 1.19585811536354E-02, 0.722099295067451, -0.530192163929043, -0.44437470379324, 1.35613437918167E-03, 2, False, 0, 0)
         boolstatus = swModel.Extension.SelectByRay(-4.35951139756412E-02, -9.15195091067744E-03, 2.34497167883774E-02, 0.722099295067451, -0.530192163929043, -0.44437470379324, 1.35613437918167E-03, 2, True, 0, 0)

        Set facesLC(0) = swSelMgr.GetSelectedObject6(1, -1)
         Set facesLC(1) = swSelMgr.GetSelectedObject6(2, -1)

        Dim vFacesLC As Variant
         vFacesLC = facesLC

        swLinearMateData.MateEntity1 = facesLC(0)
         swLinearMateData.MateEntity2 = facesLC(1)

        Set feat = swAssy.CreateMate(swLinearMateData)

    End If

    swModel.GraphicsRedraw2

    Stop

    Set feat = swModel.Extension.GetLastFeatureAdded

    Debug.Print "Feature GetTypeName2 of mate created is " & feat.GetTypeName2

    Set swMateData = feat.GetDefinition

    If (swMateData.TypeName = SwConst.swMateType_e.swMateLINEARCOUPLER) Then

        Set swLinearMateData = swMateData

        Debug.Print "Linear/linear coupler mate reverse is " & swLinearMateData.Reverse

        If (swLinearMateData.Reverse = True) Then
             swLinearMateData.Reverse = False
         Else
             swLinearMateData.Reverse = True
         End If

        Debug.Print "Linear/linear coupler mate reverse changed to " & swLinearMateData.Reverse

        boolstatus = feat.ModifyDefinition(swLinearMateData, swAssy, Nothing)

    End If
End Sub
```
