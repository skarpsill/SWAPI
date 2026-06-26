---
title: "Add Spring to Motion Study Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Spring_to_Motion_Study_Example_VBNET.htm"
---

# Add Spring to Motion Study Example (VB.NET)

This example shows how to add a spring to a motion study.

```vb
'---------------------------------------------------------------------------
 ' Preconditions: kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
 ' 1. Open public_documents\samples\tutorial\api\wrench.sldasm.
 ' kadov_tag{{<spaces>}}2. Verify that the MotionManager tab is visible. If it is not visible,
 ' kadov_tag{{<spaces>}}   click View > MotionManager.
 ' kadov_tag{{<spaces>}}3. Right-click the project, select Add Reference, click Browse, and
 '    select install_dir\api\redist\SolidWorks.Interop.swmotionstudy.dll.
 ' 4. Open the Immediate window.
 '
 ' Postconditions:
 ' 1 Adds a spring feature between the grips of the wrench.
 ' 2. Examine the Immediate window.
 '
 ' kadov_tag{{<spaces>}}NOTE: Because the assembly is used elsewhere, do not save changes.
 '--------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SwMotionStudy
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swMotionMgr As MotionStudyManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swMotionStudy1 As MotionStudy
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSpringFeat As SimulationSpringFeatureData
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeat As Feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSelMgr As SelectionMgr

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get the MotionManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swMotionMgr = swModelDocExt.GetMotionStudyManager()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If (swMotionMgr Is Nothing) Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get "MotionStudy1_Distance=0.5in"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swMotionStudy1 = swMotionMgr.GetMotionStudy("MotionStudy1_Distance=0.5in")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If (swMotionStudy1 Is Nothing) Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MsgBox("MotionStudy1_Distance=0.5in is not available.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Activate "MotionStudy1_Distance=0.5in"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swMotionStudy1.Activate()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Define spring feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSpringFeat = swMotionStudy1.CreateDefinition(swFeatureNameID_e.swFmAEMLinearMotionSpring)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If swSpringFeat Is Nothing Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("ERROR: Creation of Spring feature data object failed.")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Exit Sub
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}' Select spring's endpoints
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFace1 As Face2, swFace2 As Face2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ShowNamedView2("*Left", 3)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.03344586330968, 0.0525345575174, 0, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFace1 = swSelMgr.GetSelectedObject6(1, -1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.02244533711473, 0.0131288302002, 0.0002238961779386, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFace2 = swSelMgr.GetSelectedObject6(2, -1)

kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}' Set spring characteristics
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSpringFeat.SetEndPoints(swFace1, swFace2)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSpringFeat.CoilDiameter = 0.0102
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSpringFeat.NumberOfCoils = 3
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSpringFeat.WireDiameter = 0.00152
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSpringFeat.FreeLength = 0.02

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Create Spring feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeat = swMotionStudy1.CreateFeature(swSpringFeat)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If swFeat Is Nothing Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" ERROR: Creation of the Spring feature failed.")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Type of the feature added: " & swFeat.GetTypeName2)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If

         Debug.Print("Type of spring as defined in swSpringType_e: " & swSpringFeat.Type)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
