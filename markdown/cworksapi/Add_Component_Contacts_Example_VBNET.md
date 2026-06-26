---
title: "Add Component Contacts Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Component_Contacts_Example_VBNET.htm"
---

# Add Component Contacts Example (VB.NET)

This example shows how to add component contacts to a frequency study.

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
 '  1. Opens the model.
 '  2. Creates Frequency 1 study.
 '  3. Uses a soft spring to stabilize the model.
 '  4. Adds Component Contact-1 and Component Contact-2 to the
 '     Component Contacts folder in the Simulation study tree.
  '  5. Prints the component contacts' properties to the Immediate window.
 '  6. Applies ductile iron to the model.
 '  7. Meshes the model.
 '  8. Analyzes Frequency 1.
  '  9. Prints the resonant frequencies of each mode to the Immediate window.
  ' 10. Inspect the Immediate window, the Simulation study tree, and the
 '     graphics area.
 '
  ' NOTE: Because the model is used elsewhere, do not save changes.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim COSMOSWORKS As CosmosWorks
         Dim COSMOSObject As CwAddincallback
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim SolidMgr As CWSolidManager
         Dim SolidComponent As CWSolidComponent
         Dim SolidBody As CWSolidBody
         Dim CwMesh As CWMesh
         Dim CWResult As CWResults
         Dim Part As ModelDoc2
         Dim ContactMgr As CWContactManager
         Dim CWComponentContact As CWContactComponent
         Dim pDisp3 As Object, pDisp4 As Object
         Dim var20 As Object = Nothing
         Dim var21 As Object = Nothing
         Dim Freq As Object
         Dim bApp As Boolean
         Dim str3 As String, str4 As String
         Dim longstatus As Integer, longwarnings As Integer
         Dim errCode As Integer
         Dim el As Double, tl As Double
         Dim i As Integer

         swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Contact\quartereyebar.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", longstatus, longwarnings)
         Part = SwApp.ActiveDoc()

         COSMOSObject = SwApp.GetAddInObject("SldWorks.Simulation")
         If COSMOSObject Is Nothing Then ErrorMsg(SwApp, "Failed to get Simulation add-in")

         COSMOSWORKS = COSMOSObject.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(SwApp, "Failed to get COSMOSWORKS")

         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(SwApp, "Failed to get active document")

         ' Create new frequency study
         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(SwApp, "Failed to get study manager")

         Study = StudyMngr.CreateNewStudy3("Frequency 1", swsAnalysisStudyType_e.swsAnalysisStudyTypeFrequency, 0, errCode)
         If Study Is Nothing Then ErrorMsg(SwApp, "Failed to create frequency study")

         Dim StudyOptions As ICWFrequencyStudyOptions
         StudyOptions = Study.FrequencyStudyOptions
         StudyOptions.UseSoftSpring = 1

         str3 = "64,31,0,0,4,0,0,0,255,254,255,29,81,0,117,0,97,0,114,0,116,0,101,0,114,0,69,0,121,0,101,0,66,0,97,0,114,0,45,0,49,0,64,0,113,0,117,0,97,0,114,0,116,0,101,0,114,0,101,0,121,0,101,0,98,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,9,0,0,0,3,0,0,0,103,0,0,0,102,0,0,0,101,0,0,0"
         StringtoArray(str3, var20)
         pDisp3 = Part.Extension.GetObjectByPersistReference3((var20), longstatus)

         str4 = "64,31,0,0,5,0,0,0,255,254,255,27,81,0,117,0,97,0,114,0,116,0,101,0,114,0,66,0,111,0,108,0,116,0,45,0,49,0,64,0,113,0,117,0,97,0,114,0,116,0,101,0,114,0,101,0,121,0,101,0,98,0,97,0,114,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,11,0,0,0"
         StringtoArray(str4, var21)
         pDisp4 = Part.Extension.GetObjectByPersistReference3((var21), longstatus)

         ContactMgr = Study.ContactManager
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get contact manager")

         ContactMgr.DeleteContactComponent("Global Contact")

         ' Add bonded component contacts
         CWComponentContact = ContactMgr.CreateContactComponent(swsContactType_e.swsContactTypeBonded, swsMeshCompatibility_e.swsMeshCompatibilityCompatible, pDisp3, errCode)
         Debug.Print(CWComponentContact.ContactName)
         Debug.Print("  Type as defined in swsContactType_e: " & CWComponentContact.ContactComponentType)
         Debug.Print("  Include friction? " & CWComponentContact.IncludeFriction)
         If CWComponentContact.IncludeFriction = True Then
             Debug.Print("  Friction coefficient: " & CWComponentContact.FrictionValue)
         End If
         Debug.Print("  Global contact condition? (1=yes, 0=no) " & CWComponentContact.GlobalContact)
         Debug.Print("  Include non-touching faces? (1=yes, 0=no) " & CWComponentContact.IncludeClearance)
         If CWComponentContact.IncludeClearance = True Then
             Debug.Print("  Clearance value: " & CWComponentContact.ClearanceValue)
             Debug.Print("  Clearance units: " & CWComponentContact.ClearanceUnit)
             Debug.Print("  Automatically create contact sets? " & CWComponentContact.IncludeShellEdgeSolidOrShellFace)
         End If
         Debug.Print("  Mesh compatibility as defined in swsMeshCompatibility_e: " & CWComponentContact.Option)
         Debug.Print("  Suppression state as defined in swsSuppressionState_e: " & CWComponentContact.State)
         If CWComponentContact.State = 1 Then
             errCode = ContactMgr.SuppressUnsuppressComponentContact(CWComponentContact.ContactName, 0)
         End If
         Debug.Print("  ")

         CWComponentContact = ContactMgr.CreateContactComponent(swsContactType_e.swsContactTypeBonded, swsMeshCompatibility_e.swsMeshCompatibilityCompatible, pDisp4, errCode)
         Debug.Print(CWComponentContact.ContactName)
         Debug.Print("  Type as defined in swsContactType_e: " & CWComponentContact.ContactComponentType)
         Debug.Print("  Include friction? " & CWComponentContact.IncludeFriction)
         If CWComponentContact.IncludeFriction = True Then
             Debug.Print("  Friction coefficient: " & CWComponentContact.FrictionValue)
         End If
         Debug.Print("  Global contact condition? (1=yes, 0=no) " & CWComponentContact.GlobalContact)
         Debug.Print("  Include non-touching faces? (1=yes, 0=no) " & CWComponentContact.IncludeClearance)
         If CWComponentContact.IncludeClearance = True Then
             Debug.Print("  Clearance value: " & CWComponentContact.ClearanceValue)
             Debug.Print("  Clearance units: " & CWComponentContact.ClearanceUnit)
             Debug.Print("  Automatically create contact sets? " & CWComponentContact.IncludeShellEdgeSolidOrShellFace)
         End If
         Debug.Print("  Mesh compatibility as defined in swsMeshCompatibility_e: " & CWComponentContact.Option)
         Debug.Print("  Suppression state as defined in swsSuppressionState_e: " & CWComponentContact.State)
         If CWComponentContact.State = 1 Then
             errCode = ContactMgr.SuppressUnsuppressComponentContact(CWComponentContact.ContactName, 0)
         End If
         Debug.Print("  ")

         ' Apply material to model
         SolidMgr = Study.SolidManager
         If SolidMgr Is Nothing Then ErrorMsg(SwApp, "SolidMgr object not there")

         SolidComponent = SolidMgr.GetComponentAt(0, errCode)
         If errCode <> 0 Then ErrorMsg(SwApp, "No solid component")

         SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
         If errCode <> 0 Then ErrorMsg(SwApp, "No solid body")

         bApp = SolidBody.SetLibraryMaterial("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Ductile Iron")
         If bApp = False Then ErrorMsg(SwApp, "No material applied")

         SolidComponent = SolidMgr.GetComponentAt(1, errCode)
         If errCode <> 0 Then ErrorMsg(SwApp, "No solid component")

         SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
         If errCode <> 0 Then ErrorMsg(SwApp, "No solid body")

         bApp = SolidBody.SetLibraryMaterial("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Ductile Iron")
         If bApp = False Then ErrorMsg(SwApp, "No material applied")

         ' Mesh model
         CwMesh = Study.Mesh
         If CwMesh Is Nothing Then ErrorMsg(SwApp, "Failed to get mesh object")

         CwMesh.Quality = 1
         Call CwMesh.GetDefaultElementSizeAndTolerance(swsLinearUnit_e.swsLinearUnitMillimeters, el, tl)

         errCode = Study.CreateMesh(swsLinearUnit_e.swsLinearUnitMillimeters, el, tl)
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to create mesh")

         ' Run analysis
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(SwApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode)

         ' Get resonant frequencies for each mode
         CWResult = Study.Results
         If CWResult Is Nothing Then ErrorMsg(SwApp, "Failed to get results object")

         Freq = CWResult.GetResonantFrequencies(errCode)
         If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get resonant frequencies")

         Debug.Print("Resonant frequencies (mode number, radians/second, cycles/second, period in seconds):")
         For i = 0 To UBound(Freq)
             Debug.Print("  " & Freq(i))
         Next i

     End Sub

     Sub ErrorMsg(ByVal SwApp As SldWorks, ByVal Message As String)

         SwApp.SendMsgToUser2(Message, 0, 0)
         SwApp.RecordLine("'*** WARNING - General")
         SwApp.RecordLine("'*** " & Message)
         SwApp.RecordLine("")

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

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
