---
title: "Create and Edit Profile Center Mate Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Profile_Center_Mate_Example_VB.htm"
---

# Create and Edit Profile Center Mate Example (VBA)

This example shows how to create and edit a profile center mate.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open:
 '    public_documents\samples\tutorial\api\AdvancedMates\AdvancedMateDemo2.sldasm
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a profile center mate.
 ' 2. Press F5 to continue.
 ' 3. Changes the mate alignment of the mate.
 ' 4. Inspect the Immediate window and graphics area.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
 Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swModel As SldWorks.ModelDoc2
 Dim swAssy As SldWorks.AssemblyDoc
 Dim swProfileMateData As SldWorks.ProfileCenterMateFeatureData
 Dim swMateData As SldWorks.MateFeatureData
 Dim swSelMgr As SldWorks.SelectionMgr
 Dim boolstatus As Boolean
 Dim feat As SldWorks.Feature
 Dim facesPC(1) As SldWorks.Face2
Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swAssy = swModel
     Set swSelMgr = swModel.SelectionManager

    Set swMateData = swAssy.CreateMateData(24) 'Profile center mate

    If (swMateData.TypeName = SwConst.swMateType_e.swMatePROFILECENTER) Then

        Set swProfileMateData = swMateData

        swProfileMateData.MateAlignment = SwConst.swMateAlign_e.swMateAlignALIGNED
         Debug.Print "Profile Center mate alignment is " & swProfileMateData.MateAlignment

        swProfileMateData.FlipDimension = False
         Debug.Print "ProfileCenter flip dimension is " & swProfileMateData.FlipDimension

        swProfileMateData.LockRotation = False
         Debug.Print "Profile center mate lock rotation is " & swProfileMateData.LockRotation

        swProfileMateData.OffsetDistance = 0.0254
         Debug.Print "Profile center mate offset distance is " & swProfileMateData.OffsetDistance

        boolstatus = swModel.Extension.SelectByRay(1.52510997612296E-02, 5.25002489357007E-02, 0.132234612849345, -0.271844060659921, -0.167859116984408, -0.947588583473408, 7.08485696755524E-04, 2, True, 1, 0)
         boolstatus = swModel.Extension.SelectByRay(0.136053581313973, 1.98237342244454E-02, 9.53905211266601E-02, -0.30846884126036, 0.319767565972896, -0.895877043864425, 7.08485696755524E-04, 2, False, 0, 0)

        Set facesPC(0) = swSelMgr.GetSelectedObject6(1, -1)
         Set facesPC(1) = swSelMgr.GetSelectedObject6(2, -1)

        Dim vFacesPC As Variant
         vFacesPC = facesPC

        swProfileMateData.EntitiesToMate = vFacesPC

        Set feat = swAssy.CreateMate(swProfileMateData)

    End If

    swModel.GraphicsRedraw2

    Stop

    Set feat = swModel.Extension.GetLastFeatureAdded

    Debug.Print "Feature GetTypeName2 of mate created is " & feat.GetTypeName2
    Set swMateData = feat.GetDefinition

    If (swMateData.TypeName = SwConst.swMateType_e.swMatePROFILECENTER) Then
        Set swProfileMateData = swMateData

        Debug.Print "Profile center mate alignment is " & swProfileMateData.MateAlignment

        If (swProfileMateData.MateAlignment = SwConst.swMateAlign_e.swMateAlignALIGNED) Then
             swProfileMateData.MateAlignment = SwConst.swMateAlign_e.swMateAlignANTI_ALIGNED
         Else
             swProfileMateData.MateAlignment = SwConst.swMateAlign_e.swMateAlignALIGNED

        End If

        Debug.Print "Profile center mate alignment changed to " & swProfileMateData.MateAlignment

        boolstatus = feat.ModifyDefinition(swProfileMateData, swAssy, Nothing)

    End If
End Sub
```
