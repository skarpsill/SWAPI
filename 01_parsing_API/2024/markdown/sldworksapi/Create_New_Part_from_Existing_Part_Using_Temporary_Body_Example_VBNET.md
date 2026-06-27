---
title: "Create New Part from Existing Part Using Temporary Body Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_New_Part_from_Existing_Part_Using_Temporary_Body_Example_VBNET.htm"
---

# Create New Part from Existing Part Using Temporary Body Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Function GetFacesWithAttribute(ByVal swApp As SldWorks, ByVal swBody As Body2, ByVal swAttDef As AttributeDef) As Object
kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}Dim swFace As Face2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swEnt As Entity
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swAttCopy As SolidWorks.Interop.sldworks.Attribute
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFaceArr() As Face2

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Search for faces on temporary body based on copied attributes
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ReDim swFaceArr(0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFace = swBody.GetFirstFace
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Do While Not Nothing Is swFace
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swEnt = swFace
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAttCopy = Nothing
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Only one instance of attribute on a face should exist
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAttCopy = swEnt.FindAttribute(swAttDef, 0)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If Not swAttCopy Is Nothing Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swFaceArr(UBound(swFaceArr)) = swFace
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}ReDim Preserve swFaceArr(UBound(swFaceArr) + 1)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFace = swFace.GetNextFace
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Loop

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Assert(UBound(swFaceArr) >= 1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ReDim Preserve swFaceArr(UBound(swFaceArr) - 1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}GetFacesWithAttribute = swFaceArr

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Function

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}1 = invisible
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}0 = visible
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Const CreateVisible As Long = 0
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Const sAttDefName As String = "temp_attrib"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Const sAttRootName As String = "root_attrib"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swAttDef As AttributeDef
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swPart As PartDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swBody As Body2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swCopyBody As Body2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSelMgr As SelectionMgr
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim nSelCount As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFace As Face2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swEnt As Entity
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swAtt() As SolidWorks.Interop.sldworks.Attribute
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim vFaceArr As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swNewPart As PartDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swNewModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swFeat As Feature
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim vBodies As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim bLocChk As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim bRet As Boolean

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swAttDef = swApp.DefineAttribute(sAttDefName)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swPart = swModel
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bRet = swAttDef.Register : Debug.Assert(bRet)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.02203398034251, 0.2107859236428, 0.005471558832284, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.03651723484872, 0.1911276369938, 0.007226351471076, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.01524, 0.1384548315647, 0.004444480215071, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.1306826750488, 0.0172129316129, 0.006448917397336, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.1068570742154, 0.01524000000001, 0.00670683128584, True, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.01652926606039, 0.01775444632528, 0.004157527166058, True, 0, Nothing, 0)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Add attribute to selected faces
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}nSelCount = swSelMgr.GetSelectedObjectCount2(-1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ReDim swAtt(nSelCount)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = 1 To nSelCount
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFace = swSelMgr.GetSelectedObject6(i, -1)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swEnt = swFace
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAtt(i - 1) = swAttDef.CreateInstance5(swModel, swEnt, sAttRootName & i, CreateVisible, swInConfigurationOpts_e.swAllConfiguration) : Debug.Assert(Not swAtt(i - 1) Is Nothing)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next i

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}vBodies = swPart.GetBodies2(swBodyType_e.swAllBodies, True)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swBody = vBodies(0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swCopyBody = swBody.Copy

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Remove attribute from faces
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = 1 To nSelCount
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bRet = swAtt(i - 1).Delete(True) : Debug.Assert(bRet)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next i

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}vFaceArr = GetFacesWithAttribute(swApp, swCopyBody, swAttDef)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Assert(nSelCount = UBound(vFaceArr) + 1)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Can only delete faces from a temporary body
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Assert(swCopyBody.IsTemporaryBody)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Should not assert because it may fail to delete faces or fail local check or both
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bRet = swCopyBody.DeleteFaces5(vFaceArr, swHealActionType_e.swHealAction_Shrink, swLoopProcessOption_e.swLoopProcess_Auto, True, vBodies, bLocChk) : Debug.Assert(bRet) : Debug.Assert(bLocChk)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swNewPart = swApp.NewDocument("C:\Documents and Settings\All Users\Application Data\SOLIDWORKS\SOLIDWORKS 2016\templates\part.prtdot", 0, 0, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swNewModel = swNewPart
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swFeat = swNewPart.CreateFeatureFromBody3(swCopyBody, False, swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck) : Debug.Assert(Not swFeat Is Nothing)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
