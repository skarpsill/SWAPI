---
title: "Change Beam to Solid Body and Back Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Change_Beam_to_Solid_Body_and_Back_Example_VBNET.htm"
---

# Change Beam to Solid Body and Back Example (VB.NET)

This example shows how to change a beam to a solid body and then back to a beam.

```vb
'----------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
'    Tools > Add-ins > SOLIDWORKS Simulation > OK).

' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference

'    (in the IDE, click Project > Add Reference > .NET >
'    SolidWorks.Interop.cosworks > OK).
' 3. Open the Immediate window.

' 4. Verify that the specified part exists.
'
' Postconditions: Examine the Immediate window to verify
' kadov_tag{{</spaces>}}that beams were converted to solid bodies and then back to beams.
' kadov_tag{{<spaces>}}You can also expand and examine the Simulation Study tree to verify the
' kadov_tag{{</spaces>}}macro.
'
' NOTES: Because the part document is used elsewhere, do not save kadov_tag{{</spaces>}}changes.
'-------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.cosworks
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim COSMOSWORKS As CosmosWorks
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim COSMOSObject As CwAddincallback
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim ActDoc As CWModelDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim StudyMngr As CWStudyManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Study As CWStudy
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim BeamMgr As CWBeamManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim BeamBody As CWBeamBody
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim SolidMgr As CWSolidManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim SolidComponent As CWSolidComponent
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim SolidBody As CWSolidBody
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim nbrBeamBodies As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim beamBodyType As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim errors As Integer, warnings As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim errCode As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim j As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim nbrSolidComponents As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim nbrSolidBodies As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim k As Integer

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Get the SOLIDWORKS Simulation object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If COSMOSObject Is Nothing Then ErrorMsg(swApp, "No CwAddincallbackobject")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}COSMOSWORKS = COSMOSObject.COSMOSWORKS
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "No COSMOSWORKS object")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Open and get the active document
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Beams\Beam_Truss.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ActDoc = COSMOSWORKS.ActiveDoc()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Get the study
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}StudyMngr = ActDoc.StudyManager()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If StudyMngr Is Nothing Then ErrorMsg(swApp, "No CWStudyManager object")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}StudyMngr.ActiveStudy = 0
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Study = StudyMngr.GetStudy(0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Study Is Nothing Then ErrorMsg(swApp, "No CWStudy object")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Get and set beams to solids and solids to beams
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Beams...")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}BeamMgr = Study.BeamManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}nbrBeamBodies = BeamMgr.BeamCount
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Number of beams: " & nbrBeamBodies)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}BeamBody = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Convert beams to solid bodies
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For j = 0 To (nbrBeamBodies - 1)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}BeamBody = BeamMgr.GetBeamBodyAt(0, errCode)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg(swApp, "No beam body")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Name of beam body: " & BeamBody.BeamBodyName)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}beamBodyType = BeamBody.BeamType
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If beamBodyType = 0 Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}BeamBody.ConvertToSolidBody()
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Beam converted to solid body")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}BeamBody = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next j

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" ")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Convert solid bodies to beams
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Solid components and bodies...")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Get solid bodies and components
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SolidMgr = Study.SolidManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If SolidMgr Is Nothing Then ErrorMsg(swApp, "No CWSolidManager object")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}nbrSolidComponents = SolidMgr.ComponentCount
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Number of solid components: " & nbrSolidComponents)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For j = 0 To (nbrSolidComponents - 1)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidComponent = SolidMgr.GetComponentAt(j, errCode)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If SolidComponent Is Nothing Then ErrorMsg(swApp, "No solid component")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Name of solid components: " & SolidComponent.ComponentName)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Get solid bodies
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}nbrSolidBodies = SolidComponent.SolidBodyCount
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}Number of solid bodies: " & nbrSolidBodies)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}For k = 0 To (nbrSolidBodies - 1)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg(swApp, "No solid body")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}          kadov_tag{{</spaces>}}Name of solid body: " & SolidBody.SolidBodyName)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}SolidBody.ConvertToBeamBody()
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Solid body converted to beam")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}SolidBody = Nothing
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Next k
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next j

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub ErrorMsg(ByVal SwApp As SldWorks, ByVal Message As String)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.SendMsgToUser2(Message, 0, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.RecordLine("'*** WARNING - General")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.RecordLine("'*** " & Message)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.RecordLine("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
