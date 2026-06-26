---
title: "Add Spring Connector Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Spring_Connector_Example_VB.htm"
---

# Add Spring Connector Example (VBA)

This example shows how to add a spring connector to a frequency study.

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
 ' 2. Activates the Sample study.
 ' 3. Deletes Connectors-2.
 ' 4. Adds Spring Connector-4 to the Connectors folder in the Simulation study
 '    tree.
 ' 5. Prints the properties of Spring Connector-4 to the Immediate window.
 ' 6. Meshes the model.
 ' 7. Analyzes Sample.
 ' 8. Inspect the Immediate window, the Simulation Study tree, and the
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
 Dim springConnector As CosmosWorksLib.CWSpringConnector
 Dim CwMesh As CosmosWorksLib.CwMesh
 Dim str3 As String, str4 As String
 Dim varArray1 As Variant, varArray2 As Variant
 Dim pDisp3 As Object, pDisp4 As Object
 Dim var20 As Variant, var21 As Variant
 Dim errCode As Long
 Dim el As Double, tl As Double
 Dim longstatus As Long, longwarnings As Long
Option Explicit

Sub main()
    Set SwApp = Application.SldWorks
    Set Part = SwApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Verification\frequency_8.sldasm", swDocASSEMBLY, swOpenDocOptions_Silent, "", longstatus, longwarnings)
     Set Part = SwApp.ActiveDoc
    Set COSMOSObject = SwApp.GetAddInObject("SldWorks.Simulation")
     If COSMOSObject Is Nothing Then ErrorMsg SwApp, "Failed to get the Simulation add-in"
    Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "Failed to get COSMOSWORKS"
    Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "Failed to get active document"
    Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "Failed to get the CWStudyManager object"
    Set Study = StudyMngr.GetStudy(0)
     If Study Is Nothing Then ErrorMsg SwApp, "Failed to get the frequency study"

    StudyMngr.ActiveStudy = 0
    str3 = "64,31,0,0,3,0,0,0,255,254,255,16,80,0,51,0,45,0,49,0,64,0,102,0,114,0,101,0,113,0,117,0,101,0,110,0,99,0,121,0,95,0,56,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,18,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,32,69,0,58,0,92,0,65,0,115,0,104,0,105,0,115,0,104,0,92,0,118,0,101,0,114,0,105,0,102,0,105,0,99,0,97,0,116,0,105,0,111,0,110,0,92,0,80,0,51,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,2,80,0,51,0,2,0,0,217,166,36,65,0,105,167,36,65,0,0,0,0,0,0,0,0,1,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,105,167,36,65,24,0,0,0,162,167,3"
     str3 = str3 & "6,65,4,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,24,0,0,0,162,167,36,65,0,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,162,167,36,65,1,0,0,0,12,128,0,0,5,128,8,0,24,0,0,0,162,167,36,65,1,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,24,0,0,0,162,167,36,65,3,0,0,0,0,0,0,0,0,0,0,0,0,0"
     str3 = str3 & ",Type=1"
    str4 = "64,31,0,0,3,0,0,0,255,254,255,16,80,0,52,0,45,0,50,0,64,0,102,0,114,0,101,0,113,0,117,0,101,0,110,0,99,0,121,0,95,0,56,0,4,0,0,0,16,0,0,0,1,0,0,0,1,0,0,0,21,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,0,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,32,69,0,58,0,92,0,65,0,115,0,104,0,105,0,115,0,104,0,92,0,118,0,101,0,114,0,105,0,102,0,105,0,99,0,97,0,116,0,105,0,111,0,110,0,92,0,80,0,52,0,46,0,83,0,76,0,68,0,80,0,82,0,84,0,9,128,255,254,255,2,80,0,52,0,2,0,0,217,166,36,65,0,105,167,36,65,0,0,0,0,0,0,0,0,0,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,105,167,36,65,18,0,0,0,105,167"
     str4 = str4 & ",36,65,2,0,0,0,255,255,1,0,20,0,109,111,69,110,100,70,97,99,101,83,117,114,102,73,100,82,101,112,95,99,0,0,5,128,8,0,18,0,0,0,105,167,36,65,0,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,18,0,0,0,105,167,36,65,1,0,0,0,12,128,0,0,5,128,8,0,18,0,0,0,105,167,36,65,1,0,0,0,0,0,0,0,3,128,0,0,5,128,8,0,18,0,0,0,105,167,36,65,3,0,0,0,0,0,0,0,0,0,0,0,0,0"
     str4 = str4 & ",Type=1"

    StringtoArray str3, var20
     Set pDisp3 = Part.Extension.GetObjectByPersistReference3((var20), longstatus)
    StringtoArray str4, var21
     Set pDisp4 = Part.Extension.GetObjectByPersistReference3((var21), longstatus)
    varArray1 = Array(pDisp3)
     varArray2 = Array(pDisp4)
    Set lrMngr = Study.LoadsAndRestraintsManager
     lrMngr.DeleteLoadsAndRestraints "Connectors-2"
    ' Add spring connector
     Set springConnector = lrMngr.AddSpringConnector(swsSpringConnectoryTypeFlatParallelFaces, (varArray1), (varArray2), errCode)

    springConnector.SpringConnectorBeginEdit
     springConnector.Unit = swsUnitEnglish
     springConnector.NormalRadialStiffnessValue = 800#
     springConnector.TangentialOrShearStiffnessValue = 100000#
     Debug.Print "Spring Connector-4"
     Dim sType As Long, sSubType As Long
     springConnector.GetSpringType sType, sSubType
     Debug.Print "  Type as defined in swsSpringType_e: " & sType
     Debug.Print "  Sub-type as defined in swsSpringSubType_e: " & sSubType
     Debug.Print "  Source entity count: " & springConnector.GetSourceEntityCount
     Debug.Print "  Target entity count: " & springConnector.GetTargetEntityCount
     springConnector.SpringConnectorEndEdit
     Debug.Print "  Normal radial stiffness: " & springConnector.NormalRadialStiffnessValue
     Debug.Print "  Preload force type as defined in swsPreloadForceType_e: " & springConnector.PreLoadForceType
     Debug.Print "  Preload force: " & springConnector.PreLoadForceValue
     Debug.Print "  Rotational stiffness: " & springConnector.RotationalStiffnessValue
     Debug.Print "  Stiffness type as defined in swsStiffnessType_e: " & springConnector.StiffnessType
     Debug.Print "  Tangential or shear stiffness: " & springConnector.TangentialOrShearStiffnessValue
     Debug.Print "  Units of stiffness as defined in swsUnit_e: " & springConnector.Unit

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
