---
title: "Create Frequency Study with Mixed Mesh Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Frequency_Study_with_Mixed_Mesh_Example_VB.htm"
---

# Create Frequency Study with Mixed Mesh Example (VBA)

This example shows how to create a frequency study using a mixed mesh.

NOTE:To get persistent reference
identifiers (PIDs) for model selections, you can use[pidcollector.exe](GettingStarted-swsimulationapi.html)or IModelDocExtension::GetPersistReference3.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
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
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SwApp As SldWorks.SldWorks
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim COSMOSWORKS As Object
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim COSMOSObject As CosmosWorksLib.CwAddincallback
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim ActDoc As CosmosWorksLib.CWModelDoc
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim StudyMngr As CosmosWorksLib.CWStudyManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim Study As CosmosWorksLib.CWStudy
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SolidMgr As CosmosWorksLib.CWSolidManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SolidComponent As CosmosWorksLib.CWSolidComponent
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SolidBody As CosmosWorksLib.CWSolidBody
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim Shell As CosmosWorksLib.CWShell
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim CwMesh As CosmosWorksLib.CWMesh
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim CWResult As CosmosWorksLib.CWResults
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim Part As SldWorks.ModelDoc2
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim ShellMgr As CosmosWorksLib.CWShellManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim LBCMgr As CosmosWorksLib.CWLoadsAndRestraintsManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim ContactMgr As CosmosWorksLib.CWContactManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim CWContactSet As CosmosWorksLib.CWContactSet
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim CWRes1 As CosmosWorksLib.CWRestraint
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim pDisp1 As Object, pDisp2 As Object
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim oselect1 As Object, oselect2 As Object, oselect3 As Object, oselect4 As Object, oselect5 As Object
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim oselect6 As Object
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim var1 As Variant, var2 As Variant, var3 As Variant, var4 As Variant
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim var5 As Variant, var6 As Variant, var8 As Variant
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim var9 As Variant
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim varArray1 As Variant
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim varArray2 As Variant
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim varArray3 As Variant
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim varArray4 As Variant
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim Freq As Variant
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim bApp As Boolean
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim str1 As String, str2 As String
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim selectionShell As String
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim selection1 As String
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim selection2 As String
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim selection3 As String
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim selection4 As String
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim selection5 As String
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim selection6 As String
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim longstatus As Long, longwarnings As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim errCode As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim el As Double, tl As Double
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim i as Long
kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Open document
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set SwApp = Application.SldWorks
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}SwApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\mixedmesh-1.sldasm", swDocASSEMBLY, swOpenDocOptions_Silent, "", longstatus, longwarnings
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set Part = SwApp.ActiveDoc()

kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Get the SOLIDWORKS Simulation object
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set COSMOSObject = SwApp.GetAddInObject("SldWorks.Simulation")
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If COSMOSObject Is Nothing Then ErrorMsg SwApp, "COSMOSObject object not found"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "COSMOSWORKS object not found"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Open and get active document
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set ActDoc = COSMOSWORKS.ActiveDoc()
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"

kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Create new frequency study
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set StudyMngr = ActDoc.StudyManager()
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If StudyMngr Is Nothing Then ErrorMsg SwApp, "No CWStudyManager object"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set Study = StudyMngr.CreateNewStudy3("Frequency_Mixed", swsAnalysisStudyTypeFrequency, 0, errCode)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If Study Is Nothing Then ErrorMsg SwApp, "Frequency study not created"

kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}' Get selections for restraint
kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}' Faces of the six holes in the solid
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection1 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection1 = selection1 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,16,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection1 = selection1 & ",Type=1"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}StringtoArray selection1, var1
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set oselect1 = Part.Extension.GetObjectByPersistReference3((var1), longstatus)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection2 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection2 = selection2 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,15,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection2 = selection2 & ",Type=1"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}StringtoArray selection2, var2
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set oselect2 = Part.Extension.GetObjectByPersistReference3((var2), longstatus)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection3 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection3 = selection3 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,14,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection3 = selection3 & ",Type=1"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}StringtoArray selection3, var3
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set oselect3 = Part.Extension.GetObjectByPersistReference3((var3), longstatus)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection4 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection4 = selection4 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,11,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,6,0,0,0,0,0,0,0,0,0,0,0,0,0"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection4 = selection4 & ",Type=1"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}StringtoArray selection4, var4
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set oselect4 = Part.Extension.GetObjectByPersistReference3((var4), longstatus)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection5 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection5 = selection5 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,12,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,6,0,0,0,0,0,0,0,0,0,0,0,0,0"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection5 = selection5 & ",Type=1"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}StringtoArray selection5, var5
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set oselect5 = Part.Extension.GetObjectByPersistReference3((var5), longstatus)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection6 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,27,0,109,111,70,114,111,109,83,107,116,69,110,116,51,73,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,12"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection6 = selection6 & "0,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,65,0,0,0,33,58,104,66,13,0,0,0,255,255,255,255,0,0,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,2,0,0,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,6,0,0,0,0,0,0,0,0,0,0,0,0,0"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}selection6 = selection6 & ",Type=1"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}StringtoArray selection6, var6
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set oselect6 = Part.Extension.GetObjectByPersistReference3((var6), longstatus)

kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Get selections for contact set
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Shell edge
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}str1 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,69,100,103,101,82,101,102,95,99,1,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}str1 = str1 & ",0,112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,24,0,0,0,26,50,104,66,9,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,10,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,1,0,0,0,0,0,0,0,14,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,0,0,0,0,0,0,0,0,0,0,0,0"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}StringtoArray str1, var8
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set pDisp1 = Part.Extension.GetObjectByPersistReference3((var8), longstatus)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Solid face
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}str2 = "8,17,0,0,3,0,0,0,255,254,255,27,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,45,0,51,0,64,0,109,0,105,0,120,0,101,0,100,0,109,0,101,0,115,0,104,0,45,0,49,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,17,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,79,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,92,0,83,0,111,0,108,0,105,0,100,0,87,0,111,0,114,0,107,0,115,0,32,0,83,0,105,0,109,0,117,0,108,0,97,0,116,0,105,0,111,0,110,0,92,0,69,0,120,0,97,0,109,0"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}str2 = str2 & ",112,0,108,0,101,0,115,0,92,0,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,13,77,0,105,0,120,0,101,0,100,0,45,0,49,0,45,0,83,0,111,0,108,0,105,0,100,0,2,0,0,124,49,104,66,0,0,0,48,0,0,0,0,0,0,0,0,0,2,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,0,0,48,0,24,0,0,0,26,50,104,66,11,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,26,50,104,66,0,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,10,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,1,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,26,50,104,66,4,0,0,0,0,0,0,0,0,0,0,0,0,0"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}StringtoArray str2, var9
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set pDisp2 = Part.Extension.GetObjectByPersistReference3((var9), longstatus)

kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Create arrays
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}varArray2 = Array(oselect1, oselect2, oselect3, oselect4, oselect5, oselect6)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}varArray3 = Array(pDisp1)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}varArray4 = Array(pDisp2)

kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Add bonded contact set
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set ContactMgr = Study.ContactManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg SwApp, "No ContactManager object"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set CWContactSet = ContactMgr.CreateContactSet2(swsContactTypeBonded, 0, (varArray3), (varArray4), errCode)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg SwApp, "No CWContactSet object"
   Debug.Print CWContactSet.ContactName & " is suppressed? (1=yes, 0=no) " & CWContactSet.State
   ' If contact set is suppressed, unsuppress it
    If CWContactSet.State = 1 Then
        errCode = ContactMgr.SuppressUnsuppressContactPair(CWContactSet.ContactName, 0)
    End If
   kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Apply material to shell
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set ShellMgr = Study.ShellManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If ShellMgr Is Nothing Then ErrorMsg SwApp, "No CWShellManager object"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set Shell = ShellMgr.GetShellAt(0, errCode)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}bApp = Shell.SetLibraryMaterial2("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Ductile Iron")
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If bApp = False Then ErrorMsg SwApp, "No material applied"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Define shell properties
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Shell.ShellBeginEdit
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Shell.Formulation = 0
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Shell.ShellUnit = 0
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Shell.ShellThickness = 5#
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}errCode = Shell.ShellEndEdit
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg SwApp, "Shell not created"

kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Apply material to solid
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set SolidMgr = Study.SolidManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If SolidMgr Is Nothing Then ErrorMsg SwApp, "No CWSolidManager object"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set SolidComponent = SolidMgr.GetComponentAt(1, errCode)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg SwApp, "No solid component"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg SwApp, "No solid body"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}bApp = SolidBody.SetLibraryMaterial("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Ductile Iron")
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If bApp = False Then ErrorMsg SwApp, "No material applied"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Add fixed restraint
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set LBCMgr = Study.LoadsAndRestraintsManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set CWRes1 = LBCMgr.AddRestraint(swsRestraintTypeFixed, (varArray2), Nothing, errCode)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg SwApp, "No fixed restraint created"

kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Set meshing
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set CwMesh = Study.Mesh
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If CwMesh Is Nothing Then ErrorMsg SwApp, "No mesh object"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}CwMesh.Quality = 1
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Call CwMesh.GetDefaultElementSizeAndTolerance(swsLinearUnitMillimeters, el, tl)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}errCode = Study.CreateMesh(swsLinearUnitMillimeters, el, tl)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed"

kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Run analysis
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}errCode = Study.RunAnalysis
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Get results
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Set CWResult = Study.Results
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If CWResult Is Nothing Then ErrorMsg SwApp, "No result object"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Freq = CWResult.GetResonantFrequencies(errCode)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg SwApp, "No frequency result"

    Debug.Print "Resonant Frequencies:"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}For i = 0 To UBound(Freq)
kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}Debug.Print Freq(i)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Next i

End Sub

Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}SwApp.SendMsgToUser2 Message, 0, 0
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}SwApp.RecordLine "'*** WARNING - General"
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}SwApp.RecordLine "'*** " & Message
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}SwApp.RecordLine ""
End Sub

Function StringtoArray(inputSTR As String, varEntity As Variant)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim PID() As Byte
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim i As Integer
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}varEntity = Split(inputSTR, ",")
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}ReDim PID(UBound(varEntity))
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}For i = 0 To (UBound(varEntity) - 1)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}PID(i) = varEntity(i)
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Next i
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}varEntity = PID
End Function
```
