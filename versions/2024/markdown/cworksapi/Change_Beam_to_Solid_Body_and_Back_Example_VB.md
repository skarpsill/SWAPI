---
title: "Change Beam to Solid Body and Back Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Change_Beam_to_Solid_Body_and_Back_Example_VB.htm"
---

# Change Beam to Solid Body and Back Example (VBA)

This example shows how to change a beam to a solid body and then back to a beam.

```vb
'---------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click

'    Tools > Add-ins > SOLIDWORKS Simulation > OK).

' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,

'    click Tools > References > SOLIDWORKS Simulation version type library).
' 3. Open the Immediate window.

' 4. Verify that the specified part exists.
'
' Postconditions: Examine the output in the Immediate window to verify
' kadov_tag{{<spaces>}}that beams were converted to solid bodies and then back to beams.
' kadov_tag{{</spaces>}}You can also expand and examine the Simulation Study tree to verify the
' kadov_tag{{</spaces>}}macro.
'
' NOTES: Because the part document is used elsewhere, do not save kadov_tag{{</spaces>}}changes.
'---------------------------------------------------------------------------
Option Explicit
kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
Sub main()

kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SwApp As SldWorks.SldWorks
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim COSMOSObject As CosmosWorksLib.CwAddincallback
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim ActDoc As CosmosWorksLib.CWModelDoc
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim StudyMngr As CosmosWorksLib.CWStudyManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim Study As CosmosWorksLib.CWStudy
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim BeamMgr As CosmosWorksLib.CWBeamManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim BeamBody As CosmosWorksLib.CWBeamBody
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SolidMgr As CosmosWorksLib.CWSolidManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SolidComponent As CosmosWorksLib.CWSolidComponent
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SolidBody As CosmosWorksLib.CWSolidBody
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim nbrBeamBodies As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim beamBodyType As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim errors As Long, warnings As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim errCode As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim j As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim nbrSolidComponents As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim nbrSolidBodies As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim k As Long
kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Connect to SOLIDWORKS
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If SwApp Is Nothing Then Set SwApp = Application.SldWorks
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Get the SOLIDWORKS Simulation object
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set COSMOSObject = SwApp.GetAddInObject("SldWorks.Simulation")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If COSMOSObject Is Nothing Then ErrorMsg SwApp, "No CwAddincallback object"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "No COSMOSWORKS object"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Open and get the active document
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SwApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Beams\Beam_Truss.sldprt", swDocPART, swOpenDocOptions_Silent, "", errors, warnings
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set ActDoc = COSMOSWORKS.ActiveDoc()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Get the study
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set StudyMngr = ActDoc.StudyManager()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If StudyMngr Is Nothing Then ErrorMsg SwApp, "No CWStudyManager object"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}StudyMngr.ActiveStudy = 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set Study = StudyMngr.GetStudy(0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If Study Is Nothing Then ErrorMsg SwApp, "No CWStudy object"

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Get and set beams to solids and solids to beams
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Beams..."
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set BeamMgr = Study.BeamManager
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}nbrBeamBodies = BeamMgr.BeamCount
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Number of beams: " & nbrBeamBodies
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set BeamBody = Nothing
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Convert beams to solid bodies
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}For j = 0 To (nbrBeamBodies - 1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set BeamBody = BeamMgr.GetBeamBodyAt(0, errCode)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg SwApp, "No beam body"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Name of beam body: " & BeamBody.BeamBodyName
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}beamBodyType = BeamBody.BeamType
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If beamBodyType = 0 Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}BeamBody.ConvertToSolidBody
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Beam converted to solid body"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set BeamBody = Nothing
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Next j
kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print " "
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Convert solid bodies to beams
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Solid components and bodies..."
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Get solid bodies and components
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set SolidMgr = Study.SolidManager
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If SolidMgr Is Nothing Then ErrorMsg SwApp, "No CWSolidManager object"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}nbrSolidComponents = SolidMgr.ComponentCount
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Number of solid components: " & nbrSolidComponents
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}For j = 0 To (nbrSolidComponents - 1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set SolidComponent = SolidMgr.GetComponentAt(j, errCode)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If SolidComponent Is Nothing Then ErrorMsg SwApp, "No solid component"
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Name of solid components: " & SolidComponent.ComponentName
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get solid bodies
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}nbrSolidBodies = SolidComponent.SolidBodyCount
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}Number of solid bodies: " & nbrSolidBodies
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For k = 0 To (nbrSolidBodies - 1)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg SwApp, "No solid body"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}          kadov_tag{{</spaces>}}Name of solid body: " & SolidBody.SolidBodyName
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidBody.ConvertToBeamBody
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print " kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Solid body converted to beam"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set SolidBody = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next k
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Next j

End Sub
Function ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SwApp.SendMsgToUser2 Message, 0, 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SwApp.RecordLine "'*** WARNING - General"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SwApp.RecordLine "'*** " & Message
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SwApp.RecordLine ""
kadov_tag{{<spaces>}}
End Function
```
