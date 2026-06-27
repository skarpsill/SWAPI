---
title: "Add Elastic Support Fixture Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Elastic_Support_Connector_Example_VB.htm"
---

# Add Elastic Support Fixture Example (VBA)

This example shows how to add an elastic support fixture to a frequency study.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Ensure that the specified model document exists.
 ' 4. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the model.
 ' 2. Gets the Ready frequency study.
 ' 3. Deletes Fixture-1 from Ready.
 ' 4. Adds an Elastic Support-1 fixture to Ready.
 ' 5. Prints the properties of Elastic Support-1 to the Immediate window.
 ' 6. Meshes the model.
 ' 7. Analyzes Ready.
 ' 8. Prints the resonant frequency of each mode to the Immediate window.
 ' 9. Inspect the Immediate window, the Simulation Study tree, and the
 '    graphics area.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
Dim SwApp As SldWorks.SldWorks
 Dim Part As SldWorks.ModelDoc2
 Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
 Dim COSMOSObject As CosmosWorksLib.CwAddincallback
 Dim ActDoc As CosmosWorksLib.CWModelDoc
 Dim StudyMngr As CosmosWorksLib.CWStudyManager
 Dim Study As CosmosWorksLib.CWStudy
 Dim lrMngr As CosmosWorksLib.CWLoadsAndRestraintsManager
 Dim lr As CosmosWorksLib.CWLoadsAndRestraints
 Dim elasticSupport As CosmosWorksLib.CWElasticConnector
 Dim CwMesh As CosmosWorksLib.CwMesh
 Dim CWResult As CosmosWorksLib.CWResults
 Dim str3 As String, str4 As String
 Dim varArray1 As Variant, Freq As Variant
 Dim pDisp3 As Object, pDisp4 As Object
 Dim var20 As Variant, var21 As Variant
 Dim errCode As Long, i As Long
 Dim el As Double, tl As Double
 Dim longstatus As Long, longwarnings As Long
Option Explicit
Sub main()
    Set SwApp = Application.SldWorks

    Set Part = SwApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\shaft.sldasm", swDocASSEMBLY, swOpenDocOptions_Silent, "", longstatus, longwarnings)
     SwApp.ActivateDoc2 "shaft", False, longstatus
     Set Part = SwApp.ActiveDoc

    Set COSMOSObject = SwApp.GetAddInObject("SldWorks.Simulation")
     If COSMOSObject Is Nothing Then ErrorMsg SwApp, "Failed to get the Simulation add-in"
    Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "Failed to get COSMOSWORKS"

    Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "Failed to get the active document"
    Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "Failed to get the CWStudyManager object"
    Set Study = StudyMngr.GetStudy(0)
     If Study Is Nothing Then ErrorMsg SwApp, "Failed to get frequency study"

    str3 = "64,31,0,0,3,0,0,0,255,254,255,28,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,45,0,49,0,64,0,115,0,104,0,97,0,102,0,116,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,20,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,63,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,"
     str3 = str3 & "101,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,20,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,2,0,0,130,66,58,52,0,144,22,28,65,1,0,0,0,0,0,0,0,34,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,52,0,0,0,0,0,0,0,144,22,28,65,8,0,0,0,157,67,58,52,1,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,8,0,0,0,157,67,58,52,0,0,0,0,255,255,255,255,3,128,0,0,5,128,8,0,8,0,0,0,157,67,58,52,8,0,0,0,12,128,0,0,5,128,8,0,8,0,0,0,157,67,58,52,1,0,0,0,255,255,255,255,3,128,0,0,5,128,8,0,8,0,0,0,157,67,58,52,2,0,0,0,0,0,0,0,0,0,0,0,0,0"
     StringtoArray str3, var20
     Set pDisp3 = Part.Extension.GetObjectByPersistReference3((var20), longstatus)

    str4 = "64,31,0,0,3,0,0,0,255,254,255,28,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,45,0,50,0,64,0,115,0,104,0,97,0,102,0,116,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,21,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,63,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,"
     str4 = str4 & "101,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,20,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,2,0,0,130,66,58,52,0,144,22,28,65,1,0,0,0,0,0,0,0,34,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,52,0,0,0,0,0,0,0,144,22,28,65,8,0,0,0,157,67,58,52,1,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,8,0,0,0,157,67,58,52,0,0,0,0,255,255,255,255,3,128,0,0,5,128,8,0,8,0,0,0,157,67,58,52,8,0,0,0,12,128,0,0,5,128,8,0,8,0,0,0,157,67,58,52,1,0,0,0,255,255,255,255,3,128,0,0,5,128,8,0,8,0,0,0,157,67,58,52,2,0,0,0,0,0,0,0,0,0,0,0,0,0"
     StringtoArray str4, var21
     Set pDisp4 = Part.Extension.GetObjectByPersistReference3((var21), longstatus)

    varArray1 = Array(pDisp3, pDisp4)

     Set lrMngr = Study.LoadsAndRestraintsManager

     ' Delete Fixture-1
     lrMngr.DeleteLoadsAndRestraints ("Fixture-1")

    ' Add elastic support fixture
     Set elasticSupport = lrMngr.AddElasticConnector((varArray1), errCode)

    Set lr = lrMngr.GetLoadsAndRestraints(0, errCode)
     Dim dir As Variant
     dir = lr.GetDirection
     Debug.Print "Fixture " & lr.Name
     Debug.Print "  Direction: " & dir(0) & ", " & dir(1) & ", " & dir(2)
     Debug.Print "  Number of entities: " & lr.EntityCount
     Debug.Print "  Suppression state as defined in swsSuppressionState_e: " & lr.State
     Debug.Print "  Type of fixture as defined in swsLoadsAndRestraintsType_e: " & lr.Type

    elasticSupport.ElasticConnectorBeginEdit
    'Debug.Print "  Number of entities: " & elasticSupport.GetEntityCount
     Debug.Print "  Stiffness"
     Debug.Print "    Normal: " & elasticSupport.NormalStiffnessValue
     Debug.Print "    Shear: " & elasticSupport.ShearStiffnessValue
     Debug.Print "  Units as defined in swsUnit_e: " & elasticSupport.Unit
    elasticSupport.ElasticConnectorEndEdit

    ' Mesh model
     Set CwMesh = Study.Mesh
     If CwMesh Is Nothing Then ErrorMsg SwApp, "Failed to get the CWMesh object"
    CwMesh.Quality = 1
     Call CwMesh.GetDefaultElementSizeAndTolerance(swsLinearUnitMillimeters, el, tl)
    errCode = Study.CreateMesh(swsLinearUnitMillimeters, el, tl)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to create mesh"

    ' Run analysis
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode

    ' Get resonant frequency of each mode
     Set CWResult = Study.Results
     If CWResult Is Nothing Then ErrorMsg SwApp, "Failed to get the CWResults object"
    Freq = CWResult.GetResonantFrequencies(errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get resonant frequencies"
    Debug.Print ""
     Debug.Print "Study " & Study.Name
     Debug.Print "  Resonant frequencies (mode number, radians/second, cycles/second, period in seconds):"
     For i = 0 To UBound(Freq)
        Debug.Print "    " & Freq(i)
     Next i
End Sub
Sub StringtoArray(inputSTR As String, varEntity As Variant)
   Dim PID() As Byte
    Dim i As Integer
   varEntity = Split(inputSTR, ",")
   ReDim PID(UBound(varEntity))
   For i = 0 To (UBound(varEntity) - 1)
       PID(i) = varEntity(i)
    Next i
   varEntity = PID
End Sub

Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
   SwApp.SendMsgToUser2 Message, 0, 0
    SwApp.RecordLine "'*** WARNING - General"
    SwApp.RecordLine "'*** " & Message
    SwApp.RecordLine ""

End Sub
```
