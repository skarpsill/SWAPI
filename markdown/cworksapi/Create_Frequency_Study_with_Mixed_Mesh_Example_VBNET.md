---
title: "Create Frequency Study with Mixed Mesh Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Frequency_Study_with_Mixed_Mesh_Example_VBNET.htm"
---

# Create Frequency Study with Mixed Mesh Example (VB.NET)

This example shows how to create a frequency study using a mixed mesh.

NOTE:To get persistent reference
identifiers (PIDs) for model selections, you can use[pidcollector.exe](GettingStarted-swsimulationapi.html)or IModelDocExtension::GetPersistReference3.

```vb
'----------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Ensure that the specified material library exists.
 ' 4. Ensure that the specified model document exists.
 ' 5. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the model.
 ' 2. Creates a frequency mixed-mesh study.
 ' 3. Applies material.
 ' 4. Adds a fixed restraint.
 ' 5. Adds a bonded contact set.
 ' 6. Creates a mesh.
 ' 7. Runs an analysis.
 ' 8. Inspect the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.cosworks
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim COSMOSWORKS As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim COSMOSObject As CwAddincallback
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim ActDoc As CWModelDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim StudyMngr As CWStudyManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Study As CWStudy
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim SolidMgr As CWSolidManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim SolidComponent As CWSolidComponent
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim SolidBody As CWSolidBody
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Shell As CWShell
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim CwMesh As CWMesh
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim CWResult As CWResults
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Part As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim ShellMgr As CWShellManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim LBCMgr As CWLoadsAndRestraintsManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim ContactMgr As CWContactManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim CWContactSet As CWContactSet
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim CWRes1 As CWRestraint
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim pDisp1 As Object, pDisp2 As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim oselect1 As Object, oselect2 As Object, oselect3 As Object, oselect4 As Object, oselect5 As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim oselect6 As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim var1 As Object = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim var2 As Object = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim var3 As Object = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim var4 As Object = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim var5 As Object = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim var6 As Object = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim var8 As Object = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim var9 As Object = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Freq As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim bApp As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim str1 As String, str2 As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim selection1 As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim selection2 As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim selection3 As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim selection4 As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim selection5 As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim selection6 As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim longstatus As Long, longwarnings As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim errCode As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim el As Double, tl As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i as Long

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Open document
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\mixedmesh-1.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", longstatus, longwarnings)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Part = swApp.ActiveDoc()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get the SOLIDWORKS Simulation object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If COSMOSObject Is Nothing Then ErrorMsg(swApp, "COSMOSObject object not found")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}COSMOSWORKS = COSMOSObject.COSMOSWORKS
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "COSMOSWORKS object not found")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Open and get active document
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ActDoc = COSMOSWORKS.ActiveDoc()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Create new frequency study
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}StudyMngr = ActDoc.StudyManager()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If StudyMngr Is Nothing Then ErrorMsg(swApp, "No CWStudyManager object")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Study = StudyMngr.CreateNewStudy3("Frequency_Mixed", swsAnalysisStudyType_e.swsAnalysisStudyTypeFrequency, 0, errCode)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Study Is Nothing Then ErrorMsg(swApp, "Frequency study not created")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get selections for restraint
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Faces of the six holes in the solid
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection1 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection1 = selection1 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,16,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection1 = selection1 & ",Type=1"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}StringtoArray(selection1, var1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}oselect1 = Part.Extension.GetObjectByPersistReference3((var1), longstatus)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection2 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection2 = selection2 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,15,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection2 = selection2 & ",Type=1"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}StringtoArray(selection2, var2)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}oselect2 = Part.Extension.GetObjectByPersistReference3((var2), longstatus)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection3 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection3 = selection3 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,14,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection3 = selection3 & ",Type=1"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}StringtoArray(selection3, var3)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}oselect3 = Part.Extension.GetObjectByPersistReference3((var3), longstatus)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection4 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection4 = selection4 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,11,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,6,0,0,0,0,0,0,0,0,0,0,0,0,0"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection4 = selection4 & ",Type=1"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}StringtoArray(selection4, var4)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}oselect4 = Part.Extension.GetObjectByPersistReference3((var4), longstatus)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection5 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection5 = selection5 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,12,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,6,0,0,0,0,0,0,0,0,0,0,0,0,0"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection5 = selection5 & ",Type=1"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}StringtoArray(selection5, var5)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}oselect5 = Part.Extension.GetObjectByPersistReference3((var5), longstatus)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection6 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection6 = selection6 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,13,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,6,0,0,0,0,0,0,0,0,0,0,0,0,0"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}selection6 = selection6 & ",Type=1"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}StringtoArray(selection6, var6)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}oselect6 = Part.Extension.GetObjectByPersistReference3((var6), longstatus)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get selections for contact set
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Shell edge
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str1 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,69,100,103,101,82,101,102,95,99,1,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str1 = str1 & ",0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,24,0,0,0,26,50,104,66,9,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,10,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,1,0,0,0,0,0,0,0,14,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,0,0,0,0,0,0,0,0,0,0,0,0"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}StringtoArray(str1, var8)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}pDisp1 = Part.Extension.GetObjectByPersistReference3((var8), longstatus)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Solid face
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str2 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}str2 = str2 & ",112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,24,0,0,0,26,50,104,66,11,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,0,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,10,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,1,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}StringtoArray(str2, var9)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}pDisp2 = Part.Extension.GetObjectByPersistReference3((var9), longstatus)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Create arrays
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim varArray2 As Object() = {oselect1, oselect2, oselect3, oselect4, oselect5, oselect6}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim varArray3 As Object() = {pDisp1}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim varArray4 As Object() = {pDisp2}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Add bonded contact set
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ContactMgr = Study.ContactManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg(swApp, "No CWContactManager object")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}CWContactSet = ContactMgr.CreateContactSet2(swsContactType_e.swsContactTypeBonded, 0, (varArray3), (varArray4), errCode)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg(swApp, "No CWContactSet object")
          Debug.Print(CWContactSet.ContactName & " is suppressed? (1=yes, 0=no) " & CWContactSet.State)

         ' If contact set is suppressed, unsuppress it
         If CWContactSet.State = 1 Then
             errCode = ContactMgr.SuppressUnsuppressContactPair(CWContactSet.ContactName, 0)
         End If

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Apply material to shell
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ShellMgr = Study.ShellManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If ShellMgr Is Nothing Then ErrorMsg(swApp, "No CWShellManager object")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Shell = ShellMgr.GetShellAt(0, errCode)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bApp = Shell.SetLibraryMaterial("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Ductile Iron")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If bApp = False Then ErrorMsg(swApp, "No material applied")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Define shell properties
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Shell.ShellBeginEdit()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Shell.Formulation = 0
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Shell.ShellUnit = 0
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Shell.ShellThickness = 5.0#
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}errCode = Shell.ShellEndEdit
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg(swApp, "Shell not created")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Apply material to solid
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SolidMgr = Study.SolidManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If SolidMgr Is Nothing Then ErrorMsg(swApp, "No CWSolidManager object")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SolidComponent = SolidMgr.GetComponentAt(1, errCode)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg(swApp, "No solid component")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg(swApp, "No solid body")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bApp = SolidBody.SetLibraryMaterial2("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Ductile Iron")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If bApp = False Then ErrorMsg(swApp, "No material applied")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Add fixed restraint
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}LBCMgr = Study.LoadsAndRestraintsManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}CWRes1 = LBCMgr.AddRestraint(swsRestraintType_e.swsRestraintTypeFixed, (varArray2), Nothing, errCode)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg(swApp, "No fixed restraint created")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Set meshing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}CwMesh = Study.Mesh
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If CwMesh Is Nothing Then ErrorMsg(swApp, "No CWMesh object")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}CwMesh.Quality = 1
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call CwMesh.GetDefaultElementSizeAndTolerance(swsLinearUnit_e.swsLinearUnitMillimeters, el, tl)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}errCode = Study.CreateMesh(swsLinearUnit_e.swsLinearUnitMillimeters, el, tl)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg(swApp, "Mesh failed")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Run analysis
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}errCode = Study.RunAnalysis
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg(swApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get results
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}CWResult = Study.Results
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If CWResult Is Nothing Then ErrorMsg(swApp, "No CWResults object")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Freq = CWResult.GetResonantFrequencies(errCode)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg(swApp, "No frequency result")
        Debug.Print("Resonant frequencies:)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = 0 To UBound(Freq)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print (Freq(i))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next i
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub ErrorMsg(ByVal SwApp As Object, ByVal Message As String)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.SendMsgToUser2(Message, 0, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.RecordLine("'*** WARNING - General")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.RecordLine("'*** " & Message)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.RecordLine("")
kadov_tag{{<spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub StringtoArray(ByVal inputSTR As String, ByRef varEntity As Object)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim PID() As Byte
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}varEntity = Split(inputSTR, ",")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ReDim PID(UBound(varEntity))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = 0 To (UBound(varEntity) - 1)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}PID(i) = varEntity(i)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next i
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}varEntity = PID
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks
End Class
```
