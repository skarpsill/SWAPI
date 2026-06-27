---
title: "Create New Part from Existing Part Using Temporary Body Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_New_Part_from_Existing_Part_Using_Temporary_Body_Example_VB.htm"
---

# Create New Part from Existing Part Using Temporary Body Example (VBA)

This example shows how to delete faces from a temporary body and how
to create a new part using that temporary body.

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\toolbox\braceright.sldprt.
' 2. Verify that the specified part template exists..
'
' Postconditions:
' 1. Creates a new part; the new part has same body as original part
'    but with selected faces deleted.
' 2. Close the new part without saving it.
' 3. Close braceright.sldprt without saving it.
'----------------------------------------------------------------------------
```

```vb
Option Explicit

Function GetFacesWithAttribute(swApp As SldWorks.SldWorks, swBody As SldWorks.Body2, swAttDef As SldWorks.AttributeDef) As Variant

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swFace kadov_tag{{<spaces>}}                 kadov_tag{{</spaces>}}As SldWorks.Face2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swEnt kadov_tag{{<spaces>}}                  kadov_tag{{</spaces>}}As SldWorks.Entity
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swAttCopy kadov_tag{{<spaces>}}              kadov_tag{{</spaces>}}As SldWorks.Attribute
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swFaceArr() kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}As SldWorks.Face2

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Search for faces on temporary body based on copied attributes
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ReDim swFaceArr(0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swFace = swBody.GetFirstFace

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Do While Not Nothing Is swFace
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set swEnt = swFace
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set swAttCopy = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Only one instance of attribute on a face should exist
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set swAttCopy = swEnt.FindAttribute(swAttDef, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Not swAttCopy Is Nothing Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set swFaceArr(UBound(swFaceArr)) = swFace
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ReDim Preserve swFaceArr(UBound(swFaceArr) + 1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set swFace = swFace.GetNextFace
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Loop

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Assert UBound(swFaceArr) >= 1
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ReDim Preserve swFaceArr(UBound(swFaceArr) - 1)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}GetFacesWithAttribute = swFaceArr
End Function

Sub main()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}1 = invisible
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}0 = visible
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Const CreateVisible kadov_tag{{</spaces>}}As Long = 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Const sAttDefName kadov_tag{{</spaces>}}As String = "temp_attrib"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Const sAttRootName kadov_tag{{</spaces>}}As String = "root_attrib"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swApp kadov_tag{{</spaces>}}As SldWorks.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swAttDef kadov_tag{{</spaces>}}As SldWorks.AttributeDef
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModel kadov_tag{{</spaces>}}As SldWorks.ModelDoc2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swModelDocExt kadov_tag{{</spaces>}}As SldWorks.ModelDocExtension
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swPart kadov_tag{{</spaces>}}As SldWorks.PartDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swBody kadov_tag{{</spaces>}}As SldWorks.Body2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swCopyBody kadov_tag{{</spaces>}}As SldWorks.Body2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swSelMg kadov_tag{{</spaces>}}As SldWorks.SelectionMgr
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim nSelCount kadov_tag{{</spaces>}}As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swFace kadov_tag{{</spaces>}}As SldWorks.Face2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swEnt kadov_tag{{</spaces>}}As SldWorks.Entity
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swAtt() kadov_tag{{</spaces>}}As SldWorks.Attribute
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vFaceArr kadov_tag{{</spaces>}}As Variant
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swNewPart kadov_tag{{</spaces>}}As SldWorks.PartDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swNewModel kadov_tag{{</spaces>}}As SldWorks.ModelDoc2
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swFeat kadov_tag{{</spaces>}}As SldWorks.Feature
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim swFaultEntity kadov_tag{{</spaces>}}As SldWorks.FaultEntity
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim vBodies kadov_tag{{</spaces>}}As Variant
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim boolstatus kadov_tag{{</spaces>}}As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim i kadov_tag{{</spaces>}}As Long
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim bLocChk kadov_tag{{</spaces>}}As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim bRet kadov_tag{{</spaces>}}As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swApp = Application.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swAttDef = swApp.DefineAttribute(sAttDefName)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swModelDocExt = swModel.Extension
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swSelMgr = swModel.SelectionManager
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swPart = swModel
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}bRet = swAttDef.Register: Debug.Assert bRet
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.02203398034251, 0.2107859236428, 0.005471558832284, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.03651723484872, 0.1911276369938, 0.007226351471076, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.01524, 0.1384548315647, 0.004444480215071, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.1306826750488, 0.0172129316129, 0.006448917397336, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.1068570742154, 0.01524000000001, 0.00670683128584, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.01652926606039, 0.01775444632528, 0.004157527166058, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Add attribute to selected faces
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}nSelCount = swSelMgr.GetSelectedObjectCount2(-1)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ReDim swAtt(nSelCount)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}For i = 1 To nSelCount
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set swFace = swSelMgr.GetSelectedObject6(i, -1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set swEnt = swFace
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set swAtt(i - 1) = swAttDef.CreateInstance5(swModel, swEnt, sAttRootName & i, CreateVisible, swAllConfiguration): Debug.Assert Not swAtt(i - 1) Is Nothing
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Next i
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}vBodies = swPart.GetBodies2(swAllBodies, True)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swBody = vBodies(0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swCopyBody = swBody.Copy

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Remove attribute from faces
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}For i = 1 To nSelCount
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bRet = swAtt(i - 1).Delete(True): Debug.Assert bRet
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Next i
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}vFaceArr = GetFacesWithAttribute(swApp, swCopyBody, swAttDef)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Assert nSelCount = UBound(vFaceArr) + 1
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Can only delete faces from a temporary body
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Assert swCopyBody.IsTemporaryBody
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Should not assert because it may fail to delete faces or fail local check or both
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}bRet = swCopyBody.DeleteFaces5(vFaceArr, swHealAction_Shrink, swLoopProcess_Auto, True, vBodies, bLocChk): Debug.Assert bRet: Debug.Assert bLocChk
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swNewPart = swApp.NewDocument("C:\Documents and Settings\All Users\Application Data\SOLIDWORKS\SOLIDWORKS 2016\templates\part.prtdot", 0, 0, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swNewModel = swNewPart
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set swFeat = swNewPart.CreateFeatureFromBody3(swCopyBody, False, swCreateFeatureBodyCheck): Debug.Assert Not swFeat Is Nothing

End Sub
```
