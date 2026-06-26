---
title: "Get Forces and Stresses for Selected Beams (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Forces_for_Selected_Beams_Example_VB.htm"
---

# Get Forces and Stresses for Selected Beams (VBA)

## Get Forces and Stresses for Selected Beams Example (VBA)

This example shows how to get the force load and stress values for structural members.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Open the Immediate window.
 ' 4. Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
 ' 5. Select the Simulation study tab called frame.
 ' 6. Click the Run button on the Simulation CommandManager to
 '    refresh the study results.
 ' 7. Click Yes in the dialog box.
 ' 8. In the Simulation Study tree, select SolidBody1(Structural Member1[3]).
 ' 9. Run the macro.
 '
 ' Postconditions: The load forces and stresses for the selected beam are listed in
 ' the Immediate window.
 '-------------------------------------------------------------------------------
Option Explicit
Sub main()
   Dim SwApp As SldWorks.SldWorks
    Dim swModel As ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
    Dim COSMOSObject As CosmosWorksLib.CwAddincallback
    Dim ActDoc As CosmosWorksLib.CWModelDoc
    Dim StudyMngr As CosmosWorksLib.CWStudyManager
    Dim Study As CosmosWorksLib.CWStudy
    Dim BeamMgr As CosmosWorksLib.CWBeamManager
    Dim BeamBody As CosmosWorksLib.CWBeamBody
    Dim Results As CosmosWorksLib.CWResults
    Dim actStudy As Long
    Dim beamForce As Long
    Dim nbrSteps As Long
    Dim unit As Long
    Dim errCode As Long
    Dim selBeams() As Object
    Dim nbrSelectedBeams As Long
    Dim varArray As Variant
    Dim arrBeamForces As Variant
    Dim i As Long
    Dim k As Long
    ' Connect to SOLIDWORKS
     If SwApp Is Nothing Then Set SwApp = Application.SldWorks
     Set swModel = SwApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
    ' Get the SOLIDWORKS Simulation object
     Set COSMOSObject = SwApp.GetAddInObject("SldWorks.Simulation")
     If COSMOSObject Is Nothing Then ErrorMsg SwApp, "COSMOSObject object not found"
     Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "COSMOSWORKS object not found"
    ' Get the active document
     Set ActDoc = COSMOSWORKS.ActiveDoc
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"
    ' Get the active study
     Set StudyMngr = ActDoc.StudyManager
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "No CWStudyManager object"
     actStudy = StudyMngr.ActiveStudy
     Set Study = StudyMngr.GetStudy(actStudy)
     If Study Is Nothing Then ErrorMsg SwApp, "Study not created"
    ' Get the results
     Set Results = Study.Results
    ' Get the selected beams' forces and stresses
     Set BeamMgr = Study.BeamManager
     nbrSteps = 1
     unit = swsUnitSI
    nbrSelectedBeams = swSelMgr.GetSelectedObjectCount2(-1)
     Debug.Print "Number of selected beams is " & nbrSelectedBeams
     ReDim selBeams(nbrSelectedBeams)
     For k = 0 To (nbrSelectedBeams - 1)
         Set selBeams(k) = swSelMgr.GetSelectedObject6(k + 1, -1)
     Next k
    ReDim Preserve selBeams(nbrSelectedBeams - 1)
     varArray = selBeams

    beamForce = swsBeamForceMomentDirection1
     arrBeamForces = Results.GetBeamForcesForEntities(beamForce, nbrSteps, (varArray), unit, errCode)
     Dim size As Long
     size = UBound(arrBeamForces) - LBound(arrBeamForces) + 1
     Debug.Print "Number of beam segments: " & size
    ' Print beam segment number, beam end1 force moment,
     ' and beam end2 force moment for each beam segment
     For i = 0 To UBound(arrBeamForces)
          Debug.Print (arrBeamForces(i))
     Next

    beamForce = swsBeamStressTorsional
     arrBeamForces = Results.GetBeamStressForEntities(beamForce, nbrSteps, (varArray), unit, errCode)
    ' Print beam segment number, beam end1 torsional stress,
     ' and beam end2 torsional stress for each beam segment
     For i = 0 To UBound(arrBeamForces)
          Debug.Print (arrBeamForces(i))
     Next
End Sub
'Error function
Function ErrorMsg(SwApp As Object, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Function
```
