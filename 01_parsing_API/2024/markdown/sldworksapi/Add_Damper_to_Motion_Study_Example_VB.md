---
title: "Add Damper to Motion Study Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Damper_to_Motion_Study_Example_VB.htm"
---

# Add Damper to Motion Study Example (VBA)

This example shows how to add a damper to a motion study.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\wrench.sldasm.
 ' 2. Click View > MotionManager if the MotionStudy tabs are not visible.
 ' 3. Click Tools > Add-ins > SOLIDWORKS Motion to enable motion analysis.
 ' 4. Reference the SOLIDWORKS MotionStudy type library.
 '
 ' Postconditions:
 ' 1. Adds a damper feature, LinearDamper1, between the grips of the wrench.
 ' 2. Examine the Motion Analysis to verify.
 '
 ' NOTE: Because the assembly is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp As SldWorks.SldWorks
     Dim swModel As SldWorks.ModelDoc2
     Dim swModelDocExt As SldWorks.ModelDocExtension
     Dim swMotionMgr As MotionStudyManager
     Dim swMotionStudy1 As MotionStudy
     Dim swDamperFeat As SldWorks.SimulationDamperFeatureData
     Dim boolstatus As Boolean
     Dim swFeat As SldWorks.Feature
     Dim swSelMgr As SelectionMgr
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModelDocExt = swModel.Extension
     Set swSelMgr = swModel.SelectionManager
    ' Get the MotionManager
     Set swMotionMgr = swModelDocExt.GetMotionStudyManager()
    If (swMotionMgr Is Nothing) Then
           End
     End If
    ' Get and activate "MotionStudy1_Distance=0.5in"
     Set swMotionStudy1 = swMotionMgr.GetMotionStudy("MotionStudy1_Distance=0.5in")
    If (swMotionStudy1 Is Nothing) Then
         MsgBox "MotionStudy1_Distance=0.5in is not available."
         End
     End If
    ' Activate swMotionStudy1
     swMotionStudy1.Activate
    ' Define Damper feature
     Set swDamperFeat = swMotionStudy1.CreateDefinition(swFmAEMLinearDamper)
    If swDamperFeat Is Nothing Then
        Debug.Print "ERROR: Creation of Damper feature data object failed."
         Exit Sub
     End If
    ' Select the faces for the Damper's endpoints
     Dim swFace1 As Face2, swFace2 As Face2
    swModel.ShowNamedView2 "*Left", 3
     swModel.ViewZoomtofit2
     boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.03344586330968, 0.0525345575174, 0, True, 0, Nothing, 0)
     Set swFace1 = swSelMgr.GetSelectedObject6(1, -1)
     boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.02244533711473, 0.0131288302002, 2.238961779386E-04, True, 0, Nothing, 0)
     Set swFace2 = swSelMgr.GetSelectedObject6(2, -1)
    ' Set Damper's characteristics
     swDamperFeat.SetEndPoints swFace1, swFace2
    ' Create Damper feature
     Set swFeat = swMotionStudy1.CreateFeature(swDamperFeat)
    If swFeat Is Nothing Then
         Debug.Print " ERROR: Creation of the Damper feature failed."
     Else
         Debug.Print "Type of Damper as defined in swSimulationDamperType_e: " & swDamperFeat.Type
     End If

End Sub
```
