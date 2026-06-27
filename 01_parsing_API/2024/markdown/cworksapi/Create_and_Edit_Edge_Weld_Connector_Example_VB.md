---
title: "Create and Edit Edge Weld Connector Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_and_Edit_Edge_Weld_Connector_Example_VB.htm"
---

# Create and Edit Edge Weld Connector Example (VBA)

This example shows how to create and edit an edge weld connector.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Open public_documents\samples\tutorial\api\tjoint.sldprt.
 '
 ' Postconditions: Creates and modifies Edge Weld Connector-3.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
 Option Explicit
Sub main()
    Dim SwApp           As SldWorks.SldWorks
     Dim Part            As SldWorks.ModelDoc2
     Dim errCode         As Long
     Dim COSMOSWORKS     As CosmosWorksLib.COSMOSWORKS
     Dim CWAddinCallBack As CosmosWorksLib.CWAddinCallBack
     Dim ActDoc          As CosmosWorksLib.CWModelDoc
     Dim StudyMngr       As CosmosWorksLib.CWStudyManager
     Dim Study           As CosmosWorksLib.CWStudy
     Dim LoadAndRestraintMngr As CosmosWorksLib.CWLoadsAndRestraintsManager
     Dim theCurrentLoad  As CosmosWorksLib.CWEdgeWeldConnector
     Dim theNewLoad      As CosmosWorksLib.CWEdgeWeldConnector
     Dim var1 As Variant, var2 As Variant
     Dim var4 As Variant
     Dim pDisp1 As Object, pDisp2 As Object, pDisp4 As Object
     Dim varArray9 As Variant, varArray2 As Variant, varArray As Variant, var As Variant
     Dim FirstFace As Object, SecondFace As Object
     Dim NWeakMaterial As Long
     Dim DUltimateTensileStrength As Double
     Dim NTensileStrengthUnit As Long
     Dim DCorrelationFactor As Double
     Dim DPartialSafetyFactor As Double
     Dim BIsEstimatedWeldSize As Boolean
     Dim nElectrodeMaterial As Long
     Dim dWeldStrength As Double
     Dim nWeldStrengthUnit As Long
     Dim nFOSOption As Long
     Dim dFOS As Double
     Dim bEstimatedWeldSize As Boolean
     Dim dEstimatedWeldSize As Double
     Dim nEstimatedWeldSizeUnit As Long
     Dim EdgeWeldType As Long
     Dim WeldOrientation As Long
     Dim InducedBendingMomentIncluded As Long
     Dim CodeType As Long
     Dim PIDCollection As New Collection

    Set SwApp = Application.SldWorks
     Set CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
     Set COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     Set StudyMngr = ActDoc.StudyManager()
     StudyMngr.ActiveStudy = 0
     Set Study = StudyMngr.GetStudy(StudyMngr.ActiveStudy)
     Set LoadAndRestraintMngr = Study.LoadsAndRestraintsManager

    Set PIDCollection = PIDInitializer()
    Set Part = SwApp.ActiveDoc

    SelectByPID "selection1", PIDCollection, var1
     SelectByPID "selection2", PIDCollection, var2
     SelectByPID "selection4", PIDCollection, var4

    Set pDisp1 = Part.Extension.GetObjectByPersistReference3((var1), errCode) 'face
     Set pDisp2 = Part.Extension.GetObjectByPersistReference3((var2), errCode) 'face
     Set pDisp4 = Part.Extension.GetObjectByPersistReference3((var4), errCode) 'edge
    Set theCurrentLoad = LoadAndRestraintMngr.GetEdgeWeldConnector(5, errCode)
     If theCurrentLoad Is Nothing Then ErrorMsg SwApp, "Failed to get edge weld connector"

    varArray9 = Array(pDisp4)
     Set theNewLoad = LoadAndRestraintMngr.AddEdgeWeldConnector(pDisp1, pDisp2, varArray9, 0, False, errCode)
     If theNewLoad Is Nothing Then ErrorMsg SwApp, "Failed to add edge weld connector"

    errCode = theNewLoad.SetEdgeWeldType(3)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to set edge weld type"

    EdgeWeldType = theNewLoad.GetEdgeWeldType(errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get edge weld type"
    Set FirstFace = theNewLoad.GetFirstFace(errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get Face Set1"

    Set SecondFace = theNewLoad.GetSecondFace(errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get Face Set2"

    errCode = theNewLoad.ReplaceFacesThenAutoGenerateTouchingEdges(0, pDisp1, pDisp2)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to replace faces and find touching edges"

    var = theNewLoad.GetEdgeList(errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get edge list"

    varArray = Array(var(0))
     errCode = theNewLoad.ReplaceFacesAndEdges(0, pDisp1, pDisp2, varArray)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to replace faces and edges"

    varArray2 = Array(var(1))
     errCode = theNewLoad.AddEdges(0, varArray2)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to add edges"

    errCode = theNewLoad.RemoveEdges(0, varArray)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to remove edges"

    errCode = theNewLoad.SetEdgeWeldType(3)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to set edge weld type"

    errCode = theNewLoad.SetWeldOrientation(True)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to set whether to show weld orientation"

    WeldOrientation = theNewLoad.IsWeldOrientation(errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get whether to show weld orientation"

    errCode = theNewLoad.SetInducedBendingMomentIncluded(True)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to set whether induced bending moment is included"

    InducedBendingMomentIncluded = theNewLoad.IsInducedBendingMomentIncluded(errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get whether induced bending moment is included"

    CodeType = theNewLoad.GetCodeType(errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get weld code"

    'American Standard weld sizing
     errCode = theNewLoad.SetCodeType(0)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to set American Standard weld code"

    errCode = theNewLoad.SetWeldSizingSettingUS(4, 100.1, 4, 1, 1, True, 98, 0)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to set American Standard weld sizing"

    errCode = theNewLoad.GetWeldSizingSettingUS(nElectrodeMaterial, dWeldStrength, nWeldStrengthUnit, nFOSOption, dFOS, bEstimatedWeldSize, dEstimatedWeldSize, nEstimatedWeldSizeUnit)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get American Standard weld sizing"
    'European weld sizing
     errCode = theNewLoad.SetCodeType(1)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to set european weld code"

    errCode = theNewLoad.SetWeldSizingSettingEuro(1, 155.2, 4, 1, 1, True, 98, 0)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to set european weld sizing"

    errCode = theNewLoad.GetWeldSizingSettingEuro(NWeakMaterial, DUltimateTensileStrength, NTensileStrengthUnit, DCorrelationFactor, DPartialSafetyFactor, BIsEstimatedWeldSize, dEstimatedWeldSize, nEstimatedWeldSizeUnit)
     If errCode <> 0 Then ErrorMsg SwApp, "Failed to get european weld sizing"
End Sub
Sub SelectByPID(PIDName As String, PIDCollection As Collection, varEntity As Variant)

    Dim SelObj As Object
     Dim PID() As Byte
     Dim PIDVariant As Variant
     Dim PIDString As String
     Dim i As Integer

    'Get the string from the collection
     PIDString = ""
     PIDString = PIDCollection.Item(PIDName)

    'Parse the string into an array
     PIDVariant = Split(PIDString, ",")
     ReDim PID(UBound(PIDVariant))

    'Change to a byte array
     For i = 0 To (UBound(PIDVariant) - 1)
         PID(i) = PIDVariant(i)
     Next i
         varEntity = PID
     Set SelObj = Nothing
 End Sub
Function PIDInitializer() As Collection

    Dim PIDCollection As New Collection

    Dim selection1 As String
     Dim selection2 As String
    'Faces
     selection1 = "233,35,0,0,3,0,0,0,255,254,255,0,0,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,4,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,78,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,115,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,116,0,117,0,116,0,111,0,114,0,105,0,97,0,108,0,92,0,97,0,112,0,105,0,92,0,116,0,106,0,111,0,105,0,110,0,116,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,6,116,0,106,0,111,0,105,0,110,0,116,0,2,0,"
     selection1 = selection1 & "0,239,130,43,72,255,254,255,0,255,254,255,0,0,176,178,110,16,0,0,0,0,0,0,0,0,0,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,176,178,110,16,45,0,0,0,80,132,43,72,1,0,0,0,255,255,1,0,16,0,109,111,84,111,112,69,100,103,101,73,100,82,101,112,95,99,0,0,5,128,8,0,45,0,0,0,80,132,43,72,1,0,0,0,12,128,0,0,5,128,8,0,45,0,0,0,80,132,43,72,1,0,0,0,0,0,255,255,1,0,19,0,109,111,66,111,116,116,111,109,69,100,103,101,73,100,82,101,112,95,99,0,0,5,128,8,0,45,0,0,0,80,132,43,72,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
     selection1 = selection1 & ",Type=1"
    selection2 = "233,35,0,0,3,0,0,0,255,254,255,0,0,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,4,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,78,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,115,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,116,0,117,0,116,0,111,0,114,0,105,0,97,0,108,0,92,0,97,0,112,0,105,0,92,0,116,0,106,0,111,0,105,0,110,0,116,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,6,116,0,106,0,111,0,105,0,110,0,116,0,2,"
     selection2 = selection2 & "0,0,239,130,43,72,255,254,255,0,255,254,255,0,0,176,178,110,16,0,0,0,0,0,0,0,0,0,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,176,178,110,16,26,0,0,0,36,131,43,72,1,0,0,0,255,255,1,0,16,0,109,111,84,111,112,69,100,103,101,73,100,82,101,112,95,99,0,0,5,128,8,0,26,0,0,0,36,131,43,72,1,0,0,0,0,0,255,255,1,0,19,0,109,111,66,111,116,116,111,109,69,100,103,101,73,100,82,101,112,95,99,0,0,5,128,8,0,26,0,0,0,36,131,43,72,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
     selection2 = selection2 & ",Type=1"
    'Store constants in a collection.
     PIDCollection.Add selection1, "selection1"
     PIDCollection.Add selection2, "selection2"

    Dim selection4 As String
    'Edge
     selection4 = "233,35,0,0,3,0,0,0,255,254,255,0,0,0,0,0,255,255,1,0,11,0,109,111,69,100,103,101,82,101,102,95,99,1,0,0,0,0,0,0,0,5,0,0,0,4,3,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,78,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,115,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,116,0,117,0,116,0,111,0,114,0,105,0,97,0,108,0,92,0,97,0,112,0,105,0,92,0,116,0,106,0,111,0,105,0,110,0,116,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,6,116,0,106,0,111,0,105,0,110,0,116,0,2,"
     selection4 = selection4 & "0,0,239,130,43,72,255,254,255,0,255,254,255,0,0,176,178,110,16,0,0,0,0,0,0,0,0,0,0,0,0,255,254,255,7,68,0,101,0,102,0,97,0,117,0,108,0,116,0,0,0,0,0,0,0,0,0,176,178,110,16,26,0,0,0,36,131,43,72,1,0,0,0,0,0,255,255,1,0,21,0,109,111,76,101,102,116,84,114,105,109,69,100,103,101,73,100,82,101,112,95,99,0,0,5,128,8,0,46,0,0,0,139,132,43,72,3,128,0,0,5,128,8,0,45,0,0,0,80,132,43,72,1,0,0,0,1,0,0,0,12,128,0,0,5,128,8,0,46,0,0,0,139,132,43,72,3,128,0,0,5,128,8,0,45,0,0,0,80,132,43,72,1,0,0,0,1,0,0,0,12,128,0,0,5,128,8,0,46,0,0,0,139,132,43,72,3,128,0,0,5,128,8,0,45,0,0,0,80,132,43,72,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0"
     selection4 = selection4 & ",Type=1"
    'Store constants in a collection.
     PIDCollection.Add selection4, "selection4"
    Set PIDInitializer = PIDCollection

 End Function
Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub
```
