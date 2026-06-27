---
title: "Get and Set Beams and Joints Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_and_Set_Beams_and_Joints_Example_VB.htm"
---

# Get and Set Beams and Joints Example (VBA)

This example shows how to get and set beams and joints.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Ensure that the specified part exists.
 ' 4. Ensure that the specified material library exists.
 ' 5. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Creates static study, frame.
 ' 2. Prints beam information to the Immediate window.
 ' 3. Applies Plain Carbon Steel material to all beams.
 ' 4. Calculates joints for all beams and displays a neutral axis for
 '    each beam.
 ' 5. Prints the pinball tolerance value and unit to the Immediate window.
 ' 6. Creates a mixed mesh and prints its type and state to the
 '    Immediate window.
 '
 ' NOTES:
 ' *  Creates beam elements by default for parts with structural members.
 ' *  Because the part document is used elsewhere, do not save any changes.
 '----------------------------------------------------------------------------
Option Explicit

Sub main()
   Dim SwApp As SldWorks.SldWorks
    Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
    Dim COSMOSObject As CosmosWorksLib.CwAddincallback
    Dim ActDoc As CosmosWorksLib.CWModelDoc
    Dim StudyMngr As CosmosWorksLib.CWStudyManager
    Dim Study As CosmosWorksLib.CWStudy
    Dim BeamMgr As CosmosWorksLib.CWBeamManager
    Dim BeamBody As CosmosWorksLib.CWBeamBody
    Dim Joints As CosmosWorksLib.CWJoints
    Dim Mesh As CosmosWorksLib.CWMesh
    Dim nbrBeamBodies As Long
    Dim beamBodyType As Long
    Dim ElementSize As Double
    Dim Tolerance As Double
    Dim errors As Long, warnings As Long
    Dim errCode As Long
    Dim j As Integer
    Dim bApp As Boolean
    Dim keepJointUpdates As Boolean

    If SwApp Is Nothing Then Set SwApp = Application.SldWorks
    Set COSMOSObject = SwApp.GetAddInObject("SldWorks.Simulation")
     If COSMOSObject Is Nothing Then ErrorMsg SwApp, "COSMOSObject object not found"
    Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "COSMOSWORKS object not found"
    'Open and get the active document
     SwApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\weldments\weldment_box2.sldprt", swDocPART, swOpenDocOptions_Silent, "", errors, warnings
    Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"
    'Create new static study named frame
     Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "CWStudyManager object not found"
    Set Study = StudyMngr.CreateNewStudy3("frame", swsAnalysisStudyTypeStatic, 0, errCode)
     If Study Is Nothing Then ErrorMsg SwApp, "Study not created"
    'Get and set beam info
     Set BeamMgr = Study.BeamManager
    nbrBeamBodies = BeamMgr.BeamCount

    Debug.Print "Beams..."
     Debug.Print "  Number of beams: " & nbrBeamBodies
    Set BeamBody = Nothing
    For j = 0 To (nbrBeamBodies - 1)
         Set BeamBody = BeamMgr.GetBeamBodyAt(j, errCode)
         If errCode <> 0 Then ErrorMsg SwApp, "No beam body"
         Debug.Print "    Name of beam body: " & BeamBody.BeamBodyName
         beamBodyType = BeamBody.BeamType
         If beamBodyType = 0 Then
             Debug.Print "      Type of beam body: beam"
         Else
             Debug.Print "      Type of beam body: truss"
         End If
         Debug.Print "      Beam cross-section properties:"
         Debug.Print "         Maximum distance from the shear center to the furthest point: " & BeamBody.BeamDistForMaxShearStress
         Debug.Print "         Beam shear:"
         Debug.Print "           Direction 1: " & BeamBody.BeamShearY
         Debug.Print "           Direction 2: " & BeamBody.BeamShearZ
         Debug.Print "         Beam torsional stiffness constant: " & BeamBody.BeamTorsionalConstant
         Debug.Print "           Units of length as defined in swsLinearUnit_e: " & BeamBody.BeamTorsionalConstantUnit
         bApp = BeamBody.SetLibraryMaterial2("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Plain Carbon Steel")
         If bApp = False Then ErrorMsg SwApp, "No material applied"
         Set BeamBody = Nothing
     Next j
    'Calculate joints
     Set Joints = BeamMgr.GetJointGroup(errCode)
    Debug.Print " "
     Debug.Print "Joints..."
    If errCode <> 0 Then ErrorMsg SwApp, "No joint group"
    Joints.JointsBeginEdit
     Joints.IncludeAllSelectedBeam = True
     Joints.IncludeDisplayNeutralAxis = True
     Joints.CalculateJoints
     Joints.JointsEndEdit
    keepJointUpdates = Joints.IncludeKeepModifiedJointOnUpdate
    If (keepJointUpdates = True) Then
        Debug.Print (" Keep joint updates? yes")
     Else
        Debug.Print (" Keep joint updates? no")
     End If

    Debug.Print " Overwrite the pinball value: " & Joints.IncludeTreatAsJointForClearanceLessThan
     Debug.Print "  Pinball radius: " & Joints.PinBallRadius * 0.001
    Select Case Joints.PinBallRadiusUnit
         Case 0
             Debug.Print "  Pinball radius unit: mm"
         Case 1
             Debug.Print "  Pinball radius unit: cm"
         Case 2
             Debug.Print "  Pinball radius unit: m"
         Case 3
             Debug.Print "  Pinball radius unit: in"
         Case 4
             Debug.Print "  Pinball radius unit: ft"
         Case 5
             Debug.Print "  Pinball radius unit: ft-in"
         Case 6
             Debug.Print "  Pinball radius unit: am"
         Case 7
             Debug.Print "  Pinball radius unit: nm"
         Case 8
             Debug.Print "  Pinball radius unit: micron"
         Case 9
             Debug.Print "  Pinball radius unit: mil"
         Case 10
             Debug.Print "  Pinball radius unit: MicroIn"
     End Select
    'Mesh the part
     Set Mesh = Study.Mesh
     If Mesh Is Nothing Then ErrorMsg SwApp, "No mesh object"
    Mesh.Quality = swsMeshQualityHigh
     Mesh.GetDefaultElementSizeAndTolerance swsLinearUnitMillimeters, ElementSize, Tolerance
    errCode = Study.CreateMesh(swsLinearUnitMillimeters, ElementSize, Tolerance)
     If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed"
    Debug.Print " "
     Debug.Print "Mesh..."
     Debug.Print "  Time to create mesh: " & Mesh.TimeToCompleteMesh
    Select Case Mesh.MeshType
         Case 0
             Debug.Print "  Mesh type: solid"
         Case 1
             Debug.Print "  Mesh type: midsurface"
         Case 2
             Debug.Print "  Mesh type: surface"
         Case 3
             Debug.Print "  Mesh type: mixed"
         Case 4
             Debug.Print "  Mesh type: beam"
     End Select
    Debug.Print "  Number of mesh controls: " & Mesh.MeshControlCount
    Select Case Mesh.MeshState
         Case 0
             Debug.Print "  Mesh state: no mesh"
         Case 1
             Debug.Print "  Mesh state: exists and is current"
         Case 2
             Debug.Print "  Mesh state: exists and is not current"
         Case 3
             Debug.Print "  Mesh state: failed"
         Case 4
             Debug.Print "  Mesh state: interrupted"
     End Select
End Sub
Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
    SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
End Sub
```
