---
title: "Get Forces for Selected Beams (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Forces_for_Selected_Beams_Example_VBNET.htm"
---

# Get Forces for Selected Beams (VB.NET)

## Get Forces for Selected Beams Example (VB.NET)

This example shows how to get the force load values for structural members.

```vb
'---------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
'    Tools > Add-ins > SOLIDWORKS Simulation > OK).

' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference

'    (in the IDE, click Project > Add Reference > .NET >
'    SolidWorks.Interop.cosworks > OK).
' 3. Open the Immediate window.
' 4. Open a SOLIDWORKS model that has structural members and a
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Simulation static study with force loads
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}applied to the structural members.
' 5. Select the Simulation study tab.
' 6. Click the Run button on the Simulation CommandManager to
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}refresh the study results.
' 7. In the Simulation Study tree, select the beams for which
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}you want to know their force loads.
' 8. Run the macro.
'
' Postconditions: The selected beams' forces are printed to the
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}the Immediate window.
'-------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.cosworks
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swSelMgr As SelectionMgr
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim COSMOSWORKS As COSMOSWORKS
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim COSMOSObject As CwAddincallback
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim ActDoc As CWModelDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim StudyMngr As CWStudyManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Study As CWStudy
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim BeamMgr As CWBeamManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Results As CWResults
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim actStudy As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim beamForce As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim nbrSteps As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim unit As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim errCode As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim selBeams() As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim nbrSelectedBeams As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim varArray As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim arrBeamForces As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim k As Long

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Connect to SOLIDWORKS
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swSelMgr = swModel.SelectionManager

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get the SOLIDWORKS Simulation object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If COSMOSObject Is Nothing Then ErrorMsg(swApp, "COSMOSObject object not found")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}COSMOSWORKS = COSMOSObject.COSMOSWORKS
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "COSMOSWORKS object not found")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get the active document
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ActDoc = COSMOSWORKS.ActiveDoc()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get the active study
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}StudyMngr = ActDoc.StudyManager()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If StudyMngr Is Nothing Then ErrorMsg(swApp, "No CWStudyManager object")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}actStudy = StudyMngr.ActiveStudy
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Study = StudyMngr.GetStudy(actStudy)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Study Is Nothing Then ErrorMsg(swApp, "Study not created")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get the results
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Results = Study.Results

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get the selected beams' forces
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}BeamMgr = Study.BeamManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}beamForce = swsBeamForceType_e.swsBeamForceMomentDirection1
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}nbrSteps = 1
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}unit = swsUnit_e.swsUnitSI
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}nbrSelectedBeams = swSelMgr.GetSelectedObjectCount2(-1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ReDim selBeams(nbrSelectedBeams)

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For k = 0 To (nbrSelectedBeams - 1)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}selBeams(k) = swSelMgr.GetSelectedObject6(k + 1, -1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next k

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ReDim Preserve selBeams(nbrSelectedBeams - 1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}varArray = selBeams

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}arrBeamForces = Results.GetBeamForcesForEntities(beamForce, nbrSteps, (varArray), unit, errCode)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For i = 0 To UBound(arrBeamForces)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(arrBeamForces(i))
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}'Error routine
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub ErrorMsg(ByVal SwApp As Object, ByVal Message As String)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SwApp.SendMsgToUser2(Message, 0, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SwApp.RecordLine("'*** WARNING - General")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SwApp.RecordLine("'*** " & Message)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SwApp.RecordLine("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}   kadov_tag{{<spaces>}}Public swApp As SldWorks

End Class
```
