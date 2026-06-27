---
title: "Get and Set Beams and Joints Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_and_Set_Beams_and_Joints_Example_VBNET.htm"
---

# Get and Set Beams and Joints Example (VB.NET)

This example shows how to get and set beams and joints.

```vb
'--------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
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
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Joints As CWJoints
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Mesh As CWMesh
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim nbrBeamBodies As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim beamBodyType As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim ElementSize As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Tolerance As Double
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim errors As Integer, warnings As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim errCode As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim j As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim bApp As Boolean
```

Dim keepJointUpdates As Boolean

```vb
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Get the SOLIDWORKS Simulation object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If COSMOSObject Is Nothing Then ErrorMsg(swApp, "COSMOSObject object not found")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}COSMOSWORKS = COSMOSObject.CosmosWorks
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "COSMOSWORKS object not found")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Open and get the active document
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\weldments\weldment_box2.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ActDoc = COSMOSWORKS.ActiveDoc()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Create new static study named frame
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}StudyMngr = ActDoc.StudyManager()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If StudyMngr Is Nothing Then ErrorMsg(swApp, "CWStudyManager object not found")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Study = StudyMngr.CreateNewStudy3("frame", swsAnalysisStudyType_e.swsAnalysisStudyTypeStatic, 0, errCode)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Study Is Nothing Then ErrorMsg(swApp, "Study not created")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Get and set beam info
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}BeamMgr = Study.BeamManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}nbrBeamBodies = BeamMgr.BeamCount
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Beams...")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Number of beams: " & nbrBeamBodies)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}BeamBody = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For j = 0 To (nbrBeamBodies - 1)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}BeamBody = BeamMgr.GetBeamBodyAt(j, errCode)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg(swApp, "No beam body")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Name of beam body: " & BeamBody.BeamBodyName)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}beamBodyType = BeamBody.BeamType
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If beamBodyType = 0 Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Type of beam body: beam")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Else
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}Type of beam body: truss")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
             Debug.Print("      Beam cross-section properties:")

             Debug.Print("         Maximum distance from the shear center to the furthest point: " & BeamBody.BeamDistForMaxShearStress)

             Debug.Print("         Beam shear:")

             Debug.Print("           Direction 1: " & BeamBody.BeamShearY)

             Debug.Print("           Direction 2: " & BeamBody.BeamShearZ)

             Debug.Print("         Beam torsional stiffness constant: " & BeamBody.BeamTorsionalConstant)

             Debug.Print("           Units of length as defined in swsLinearUnit_e: " & BeamBody.BeamTorsionalConstantUnit)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bApp = BeamBody.SetLibraryMaterial2("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Plain Carbon Steel")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If bApp = False Then ErrorMsg(swApp, "No material applied")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}BeamBody = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next j

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Calculate joints
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Joints = BeamMgr.GetJointGroup(errCode)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" ")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Joints...")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg(swApp, "No joint group")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Joints.JointsBeginEdit()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Joints.IncludeAllSelectedBeam = True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Joints.IncludeDisplayNeutralAxis = True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Joints.CalculateJoints()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Joints.JointsEndEdit()
```

```vb
        keepJointUpdates = Joints.IncludeKeepModifiedJointOnUpdate
        If (keepJointUpdates = True) Then
           Debug.Print(" Keep joint updates: yes")
        Else
           Debug.Print(" Keep joint updates: no")
        End If
        Debug.Print(" Overwrite pinball value: " & Joints.IncludeTreatAsJointForClearanceLessThan)
```

```vb
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Pinball radius: " & Joints.PinBallRadius * 0.001)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case Joints.PinBallRadiusUnit
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 0
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Pinball radius unit: mm")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 1
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Pinball radius unit: cm")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 2
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Pinball radius unit: m")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 3
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Pinball radius unit: in")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 4
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Pinball radius unit: ft")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 5
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Pinball radius unit: ft-in")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 6
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Pinball radius unit: am")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 7
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Pinball radius unit: nm")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 8
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Pinball radius unit: micron")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 9
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Pinball radius unit: mil")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 10
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Pinball radius unit: MicroIn")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}'Mesh the part
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Mesh = Study.Mesh
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Mesh Is Nothing Then ErrorMsg(swApp, "No mesh object")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Mesh.Quality = swsMeshQuality_e.swsMeshQualityHigh
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Mesh.GetDefaultElementSizeAndTolerance(swsLinearUnit_e.swsLinearUnitMillimeters, ElementSize, Tolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}errCode = Study.CreateMesh(swsLinearUnit_e.swsLinearUnitMillimeters, ElementSize, Tolerance)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg(swApp, "Mesh failed")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" ")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Mesh...")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Time to create mesh (hh:mm:ss): " & Mesh.TimeToCompleteMesh)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case Mesh.MeshType
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 0
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Mesh type: solid")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 1
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Mesh type: midsurface")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 2
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Mesh type: surface")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 3
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Mesh type: mixed")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 4
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Mesh type: beam")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Number of mesh controls: " & Mesh.MeshControlCount)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Select Case Mesh.MeshState
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 0
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Mesh state: no mesh")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 1
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Mesh state: exists and is current")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 2
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Mesh state: exists and is not current")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 3
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Mesh state: failed")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Case 4
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print(" kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}Mesh state: interrupted")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End Select
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub ErrorMsg(ByVal SwApp As Object, ByVal Message As String)
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
