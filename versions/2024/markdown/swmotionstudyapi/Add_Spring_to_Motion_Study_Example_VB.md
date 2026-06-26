---
title: "Add Spring to Motion Study (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swmotionstudyapi/Add_Spring_to_Motion_Study_Example_VB.htm"
---

# Add Spring to Motion Study (VBA)

This example shows how to add a spring to a motion study.

```vb
'--------------------------------------------------------
'
' Preconditions: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}(1) Open wrench.sldasm in any SOLIDWORKS 2009
' kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}<install dir>\samples\whats new\motion study
' kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}folder.
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}(2) The MotionManager tab is visible. If it is not visible,
' kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}click View, MotionManager.
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}(3) SOLIDWORKS MotionStudy type library is
' kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}referenced.
'
'
' Postconditions: Spring feature is added between the grips of the wrench.
'
' kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}NOTE: Do not save the model after running the macro. The model
' kadov_tag{{<spaces>}}                      kadov_tag{{</spaces>}}is intended for use with the SOLIDWORKS 2009 "What's New" book.
' kadov_tag{{<spaces>}}                      kadov_tag{{</spaces>}}The model is used in this example for demonstration purposes only.
'
'-------------------------------------------------------
Option Explicit

Sub main()

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swApp As SldWorks.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModel As SldWorks.ModelDoc2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModelDocExt As SldWorks.ModelDocExtension
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swMotionMgr As MotionStudyManager
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swMotionStudy1 As MotionStudy
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSpringFeat As SimulationSpringFeatureData
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swFeat As SldWorks.Feature
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSelMgr As SelectionMgr
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swApp = Application.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModelDocExt = swModel.Extension
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swSelMgr = swModel.SelectionManager
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get the MotionManager
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swMotionMgr = swModelDocExt.GetMotionStudyManager()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If (swMotionMgr Is Nothing) Then
kadov_tag{{<spaces>}}          kadov_tag{{</spaces>}}End
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get and activate "MotionStudy1_Distance=0.5in"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swMotionStudy1 = swMotionMgr.GetMotionStudy("MotionStudy1_Distance=0.5in")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If (swMotionStudy1 Is Nothing) Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MsgBox "MotionStudy1_Distance=0.5in is not available."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Activate swMotionStudy1
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swMotionStudy1.Activate
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Define Spring feature
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swSpringFeat = swMotionStudy1.CreateDefinition(swFmAEMLinearMotionSpring)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If swSpringFeat Is Nothing Then
kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}Debug.Print "ERROR: Creation of Spring feature data object failed."
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Select the faces for the spring's endpoints
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swFace1 As face2, swFace2 As face2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swModel.ShowNamedView2 "*Left", 3
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swModel.ViewZoomtofit2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.03344586330968, 0.0525345575174, 0, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swFace1 = swSelMgr.GetSelectedObject6(1, -1)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.02244533711473, 0.0131288302002, 2.238961779386E-04, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swFace2 = swSelMgr.GetSelectedObject6(2, -1)

kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Set spring's characteristics
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swSpringFeat.SetEndPoints swFace1, swFace2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swSpringFeat.CoilDiameter = 0.0102
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swSpringFeat.NumberOfCoils = 3
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swSpringFeat.WireDiameter = 0.00152
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swSpringFeat.FreeLength = 0.02
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}' Create Spring feature
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swFeat = swMotionStudy1.CreateFeature(swSpringFeat)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If swFeat Is Nothing Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " ERROR: Creation of the Spring feature failed."
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print "Type of the feature added: " & swFeat.GetTypeName2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
End Sub
```
