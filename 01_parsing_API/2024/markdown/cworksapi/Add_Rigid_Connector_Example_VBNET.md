---
title: "Add Rigid Connector Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Rigid_Connector_Example_VBNET.htm"
---

# Add Rigid Connector Example (VB.NET)

This example shows how to add a rigid connector to a frequency study.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Ensure that the specified model document exists.
 ' 4. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the model.
 ' 2. Gets the Ready frequency study.
 ' 3. Adds Rigid Connector-1 to the Connectors folder in the Simulation study
 '    tree.
 ' 4. Prints the properties of Rigid Connector-1 to the Immediate window.
 ' 5. Meshes the model.
 ' 6. Analyzes Ready.
  ' 7. Prints the resonant frequency of each mode to the Immediate window.
  ' 8. Inspect the Immediate window, the Simulation Study tree, and the
 '    graphics area.
 '
  ' NOTE: Because the model is used elsewhere, do not save changes.
  ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim COSMOSWORKS As COSMOSWORKS
     Dim COSMOSObject As CwAddincallback
     Dim ActDoc As CWModelDoc
     Dim StudyMngr As CWStudyManager
     Dim Study As CWStudy
     Dim lrMngr As CWLoadsAndRestraintsManager
     Dim rigidConnector As CWRigidConnector
     Dim CwMesh As CwMesh
     Dim CWResult As CWResults
     Dim str3 As String, str4 As String
     Dim varArray1(0) As Object, varArray2(0), Freq As Object
     Dim pDisp3 As Object, pDisp4 As Object
     Dim var20 As Object, var21 As Object
     Dim errCode As Integer, i As Integer
     Dim el As Double, tl As Double
     Dim longstatus As Integer, longwarnings As Integer

     Sub main()

         Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\shaft.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", longstatus, longwarnings)
         SwApp.ActivateDoc2("shaft", False, longstatus)
         Part = SwApp.ActiveDoc

         COSMOSObject = SwApp.GetAddInObject("SldWorks.Simulation")
         If COSMOSObject Is Nothing Then ErrorMsg(SwApp, "Failed to get the Simulation add-in")

         COSMOSWORKS = COSMOSObject.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(SwApp, "Failed to get COSMOSWORKS")

         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(SwApp, "Failed to get the active document")

         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(SwApp, "Failed to get the CWStudyManager object")

         Study = StudyMngr.GetStudy(0)
         If Study Is Nothing Then ErrorMsg(SwApp, "Failed to get the frequency study")

         str3 = "64,31,0,0,3,0,0,0,255,254,255,28,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,45,0,49,0,64,0,115,0,104,0,97,0,102,0,116,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,20,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,8,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,63,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,"
         str3 = str3 & "101,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,20,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,2,0,0,130,66,58,52,0,144,22,28,65,1,0,0,0,0,0,0,0,34,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,52,0,0,0,0,0,0,0,144,22,28,65,11,0,0,0,217,67,58,52,1,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,8,0,0,0,157,67,58,52,1,0,0,0,255,255,255,255,255,255,1,0,19,0,109,111,70,105,108,108,101,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,26,0,0,0,45,77,58,52,1,0,0,0,15,128,0,0,5,128,8,0,26,0,0,0,45,77,58,52,3,0,0,0,15,128,0,0,5,128,8,0,26,0,0,0,45,77,58,52,5,0,0,0,12,128,0,0,5,128,8,0,8,0,0,0,157,67,58,52,1,0,0,0,255,255,255,255,3,128,0,0,5,128,8,0,17,0,0,0,91,68,58,52,2,0,0,0,0,0,0,0,0,0,0,0,0,0"
         str3 = str3 & ",Type=1"
         StringtoArray(str3, var20)
         pDisp3 = Part.Extension.GetObjectByPersistReference3((var20), longstatus)
         str4 = "64,31,0,0,3,0,0,0,255,254,255,28,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,45,0,50,0,64,0,115,0,104,0,97,0,102,0,116,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,21,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,8,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,63,67,0,58,0,92,0,67,0,79,0,83,0,77,0,79,0,83,0,68,0,111,0,99,0,115,0,92,0,69,0,120,0,97,0,109,0,112,0,108,0,101,0,115,0,95,0,102,0,111,0,114,0,67,0,117,0,115,0,116,0,111,0,109,0,101,0,114,0,115,0,92,0,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,"
         str4 = str4 & "101,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,20,112,0,98,0,32,0,98,0,101,0,97,0,114,0,105,0,110,0,103,0,95,0,49,0,46,0,53,0,48,0,32,0,98,0,111,0,114,0,101,0,2,0,0,130,66,58,52,0,144,22,28,65,1,0,0,0,0,0,0,0,34,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,52,0,0,0,0,0,0,0,144,22,28,65,11,0,0,0,217,67,58,52,1,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,8,0,0,0,157,67,58,52,1,0,0,0,255,255,255,255,255,255,1,0,19,0,109,111,70,105,108,108,101,116,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,26,0,0,0,45,77,58,52,1,0,0,0,15,128,0,0,5,128,8,0,26,0,0,0,45,77,58,52,3,0,0,0,15,128,0,0,5,128,8,0,26,0,0,0,45,77,58,52,5,0,0,0,12,128,0,0,5,128,8,0,8,0,0,0,157,67,58,52,1,0,0,0,255,255,255,255,3,128,0,0,5,128,8,0,17,0,0,0,91,68,58,52,2,0,0,0,0,0,0,0,0,0,0,0,0,0"
         str4 = str4 & ",Type=1"
         StringtoArray(str4, var21)
         pDisp4 = Part.Extension.GetObjectByPersistReference3((var21), longstatus)

         varArray1(0) = New DispatchWrapper(pDisp3)
         varArray2(0) = New DispatchWrapper(pDisp4)

         lrMngr = Study.LoadsAndRestraintsManager

         ' Add rigid connector
         rigidConnector = lrMngr.AddRigidConnector((varArray1), (varArray2), errCode)
         rigidConnector.RigidConnectorBeginEdit()
         Debug.Print("Number of entities in Rigid Connector-1")
         Debug.Print("  First location: " & rigidConnector.GetFirstLocationEntityCount)
         Debug.Print("  Second location: " & rigidConnector.GetSecondLocationEntityCount)
         rigidConnector.RigidConnectorEndEdit()

         ' Mesh model
         CwMesh = Study.Mesh
         If CwMesh Is Nothing Then ErrorMsg(SwApp, "Failed to get the CWMesh object")

         CwMesh.Quality = 1
         Call CwMesh.GetDefaultElementSizeAndTolerance(swsLinearUnit_e.swsLinearUnitMillimeters, el, tl)

         errCode = Study.CreateMesh(swsLinearUnit_e.swsLinearUnitMillimeters, el, tl)
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to create mesh")

         ' Run analysis
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(SwApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode)

         ' Get resonant frequency of each mode
         CWResult = Study.Results
         If CWResult Is Nothing Then ErrorMsg(SwApp, "Failed to get the CWResults object")

         Freq = CWResult.GetResonantFrequencies(errCode)
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get resonant frequencies")

         Debug.Print("")
         Debug.Print("Study " & Study.Name)
         Debug.Print("  Resonant frequencies (mode number, radians/second, cycles/second, period in seconds):")
         For i = 0 To UBound(Freq)
             Debug.Print("    " & Freq(i))
         Next i

     End Sub

     Sub StringtoArray(ByVal inputSTR As String, ByRef varEntity As Object)

         Dim PID() As Byte
         Dim i As Integer

         varEntity = Split(inputSTR, ",")

         ReDim PID(UBound(varEntity))

         For i = 0 To (UBound(varEntity) - 1)
             PID(i) = varEntity(i)
         Next i

         varEntity = PID

     End Sub

     Sub ErrorMsg(ByVal SwApp As SldWorks, ByVal Message As String)

         SwApp.SendMsgToUser2(Message, 0, 0)
         SwApp.RecordLine("'*** WARNING - General")
         SwApp.RecordLine("'*** " & Message)
         SwApp.RecordLine("")

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
