---
title: "Insert and Change DeleteFace Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Change_DeleteFace_Feature_Example_VBNET.htm"
---

# Insert and Change DeleteFace Feature Example (VB.NET)

This example shows how to insert a DeleteFace feature and how to then
modify that feature.

```vb
' ------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\fillets\knob.sldprt.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Creates and modifies a DeleteFace feature.
 ' 2. Examine the Immediate window.
 '
 ' NOTE: Because this part document is used elsewhere, do not save changes.
 ' ------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics
 Partial Class SolidWorksMacro

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeature As Feature
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swDeleteFaceFeature As DeleteFaceFeatureData
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim featureName As String
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim opt As Integer

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Select a face for the
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' DeleteFace feature
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModel.Extension.SelectByID2("", "FACE", 0.002251015125069, -0.001872569429423, 0.02015405789763, False, 0, Nothing, 0)

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Create a DeleteFace feature
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.InsertDeleteFace(swFaceDeleteOption_e.swFaceDelete_Default) kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get the DeleteFace feature
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeature = swModel.FirstFeature
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}While Not swFeature Is Nothing
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}featureName = swFeature.Name
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}While featureName <> "DeleteFace1"
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swFeature = swFeature.GetNextFeature
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}featureName = swFeature.Name
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End While
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Feature name: " & featureName)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDeleteFaceFeature = swFeature.GetDefinition
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swDeleteFaceFeature.AccessSelections(swModel, Nothing)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Number of deleted faces: " & swDeleteFaceFeature.GetDeletedFacesCount)

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Get the DeleteFace feature's option
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}opt = swDeleteFaceFeature.Options
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Before changing the option...")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DeleteFaceOptions(opt)

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Change the DeleteFace feature's option
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDeleteFaceFeature.Options = swFaceDeleteOption_e.swFaceDelete_Patch
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}opt = swDeleteFaceFeature.Options
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}After changing the option...")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DeleteFaceOptions(opt)

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Save modification made to DeleteFace feature
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swFeature.ModifyDefinition(swDeleteFaceFeature, swModel, Nothing)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Get next feature until no more features

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeature = swFeature.GetNextFeature
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End While

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub DeleteFaceOptions(ByVal options As Long)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case options
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 0
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Option = swFaceDelete_Default")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 1
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Option = swFaceDelete_Patch")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 2
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Option = swFaceDelete_Fill")
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 3
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Option = swFaceDelete_FillWithTangent")
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks
End Class
```
