---
title: "Create and Edit Edge Weld Connector Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_and_Edit_Edge_Weld_Connector_Example_VBNET.htm"
---

# Create and Edit Edge Weld Connector Example (VB.NET)

This example shows how to create and edit an edge weld connector.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
'    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Open public_documents\samples\tutorial\api\tjoint.sldprt.
 '
' Postconditions: Creates and modifies Edge Weld Connector-3.
 '
' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

    Sub main()

        Dim Part As ModelDoc2
        Dim errCode As Integer
        Dim COSMOSWORKS As CosmosWorks
        Dim CWAddinCallBack As CwAddincallback
        Dim ActDoc As CWModelDoc
        Dim StudyMngr As CWStudyManager
        Dim Study As CWStudy
        Dim LoadAndRestraintMngr As CWLoadsAndRestraintsManager
        Dim theCurrentLoad As CWEdgeWeldConnector
        Dim theNewLoad As CWEdgeWeldConnector
        Dim var1 As Object = Nothing
        Dim var2 As Object = Nothing
        Dim var4 As Object = Nothing
        Dim pDisp1 As Object, pDisp2 As Object, pDisp4 As Object
        Dim FirstFace As Object, SecondFace As Object
        Dim NWeakMaterial As Integer
        Dim DUltimateTensileStrength As Double
        Dim NTensileStrengthUnit As Integer
        Dim DCorrelationFactor As Double
        Dim DPartialSafetyFactor As Double
        Dim BIsEstimatedWeldSize As Boolean
        Dim nElectrodeMaterial As Integer
        Dim dWeldStrength As Double
        Dim nWeldStrengthUnit As Integer
        Dim nFOSOption As Integer
        Dim dFOS As Double
        Dim bEstimatedWeldSize As Boolean
        Dim dEstimatedWeldSize As Double
        Dim nEstimatedWeldSizeUnit As Integer
        Dim EdgeWeldType As Integer
        Dim WeldOrientation As Integer
        Dim InducedBendingMomentIncluded As Integer
        Dim CodeType As Integer
        Dim PIDCollection As New Collection

        CWAddinCallBack = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
        COSMOSWORKS = CWAddinCallBack.COSMOSWORKS
        ActDoc = COSMOSWORKS.ActiveDoc()
        StudyMngr = ActDoc.StudyManager()
        StudyMngr.ActiveStudy = 0
        Study = StudyMngr.GetStudy(StudyMngr.ActiveStudy)
        LoadAndRestraintMngr = Study.LoadsAndRestraintsManager

        PIDCollection = PIDInitializer()

        Part = SwApp.ActiveDoc

        SelectByPID("selection1", PIDCollection, var1)
        SelectByPID("selection2", PIDCollection, var2)
        SelectByPID("selection4", PIDCollection, var4)

        pDisp1 = Part.Extension.GetObjectByPersistReference((var1)) 'face
        pDisp2 = Part.Extension.GetObjectByPersistReference((var2)) 'face
        pDisp4 = Part.Extension.GetObjectByPersistReference((var4)) 'edge

        theCurrentLoad = LoadAndRestraintMngr.GetEdgeWeldConnector(5, errCode)
        If theCurrentLoad Is Nothing Then ErrorMsg(swApp, "Failed to get edge weld connector")

        Dim varArray9 As Object() = {pDisp4}
        theNewLoad = LoadAndRestraintMngr.AddEdgeWeldConnector(pDisp1, pDisp2, (varArray9), 0, 0, errCode)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to add edge weld connector")

        errCode = theNewLoad.SetEdgeWeldType(3)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to set edge weld type")

        EdgeWeldType = theNewLoad.GetEdgeWeldType(errCode)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get edge weld type")

        FirstFace = theNewLoad.GetFirstFace(errCode)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get Face Set1")

        SecondFace = theNewLoad.GetSecondFace(errCode)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get Face Set2")

        errCode = theNewLoad.ReplaceFacesThenAutoGenerateTouchingEdges(0, pDisp1, pDisp2)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to replace faces and find touching edges")

        Dim var() As Object = theNewLoad.GetEdgeList(errCode)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get edge list")

        Dim varArray As Object() = {var(0)}
        errCode = theNewLoad.ReplaceFacesAndEdges(0, pDisp1, pDisp2, varArray)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to replace faces and edges")

        Dim varArray2 As Object() = {var(1)}
        errCode = theNewLoad.AddEdges(0, varArray2)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to add edges")

        errCode = theNewLoad.RemoveEdges(0, varArray)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to remove edges")

        errCode = theNewLoad.SetEdgeWeldType(3)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to set edge weld type")

        errCode = theNewLoad.SetWeldOrientation(True)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to set whether to show weld orientation")

        WeldOrientation = theNewLoad.IsWeldOrientation(errCode)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get whether to show weld orientation")

        errCode = theNewLoad.SetInducedBendingMomentIncluded(True)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to set whether induced bending moment is included")

        InducedBendingMomentIncluded = theNewLoad.IsInducedBendingMomentIncluded(errCode)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get whether induced bending moment is included")

        CodeType = theNewLoad.GetCodeType(errCode)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get weld code")

        'American Standard weld sizing
        errCode = theNewLoad.SetCodeType(0)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to set American Standard weld code")

        errCode = theNewLoad.SetWeldSizingSettingUS(4, 100.1, 4, 1, 1, True, 98, 0)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to set American Standard weld sizing")

        errCode = theNewLoad.GetWeldSizingSettingUS(nElectrodeMaterial, dWeldStrength, nWeldStrengthUnit, nFOSOption, dFOS, bEstimatedWeldSize, dEstimatedWeldSize, nEstimatedWeldSizeUnit)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get American Standard weld sizing")

        'European weld sizing
        errCode = theNewLoad.SetCodeType(1)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to set european weld code")

        errCode = theNewLoad.SetWeldSizingSettingEuro(1, 155.2, 4, 1, 1, True, 98, 0)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to set european weld sizing")

        errCode = theNewLoad.GetWeldSizingSettingEuro(NWeakMaterial, DUltimateTensileStrength, NTensileStrengthUnit, DCorrelationFactor, DPartialSafetyFactor, BIsEstimatedWeldSize, dEstimatedWeldSize, nEstimatedWeldSizeUnit)
        If errCode <> 0 Then ErrorMsg(SwApp, "Failed to get european weld sizing")

    End Sub

    Private Sub SelectByPID(ByVal PIDName As String, ByVal PIDCollection As Collection, ByRef varEntity As Object)

        Dim PID() As Byte
        Dim PIDVariant As Object
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
            PID(i) = Convert.ToByte(PIDVariant(i))
        Next i
        varEntity = PID

    End Sub

    Public Function PIDInitializer() As Collection

        Dim PIDCollection As New Collection

         Dim selection1 As String
         Dim selection2 As String

         'Faces
         selection1 =         "233,35,0,0,3,0,0,0,255,254,255,0,0,0,0,0,255,255,1,0,11,0,109,111,70,97,99,101,82,101,102,95,99,1,0,0,0,0,0,0,0,6,0,0,0,4,2,0,0,0,0,0,0,125,195,148,37,173,73,178,84,125,195,148,37,173,73,178,84,0,0,255,255,1,0,23,0,109,111,70,114,111,109,83,107,116,69,110,116,83,117,114,102,73,100,82,101,112,95,99,0,0,255,255,1,0,6,0,109,111,70,82,95,99,255,255,1,0,13,0,109,111,69,120,116,79,98,106,101,99,116,95,99,255,255,1,0,17,0,109,111,67,83,116,114,105,110,103,72,97,110,100,108,101,95,99,255,254,255,78,67,0,58,0,92,0,80,0,114,0,111,0,103,0,114,0,97,0,109,0,32,0,70,0,105,0,108,0,101,0,115,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,32,0,67,0,111,0,114,0,112,0,92,0,83,0,79,0,76,0,73,0,68,0,87,0,79,0,82,0,75,0,83,0,92,0,115,0,97,0,109,0,112,0,108,0,101,0,115,0,92,0,116,0,117,0,116,0,111,0,114,0,105,0,97,0,108,0,92,0,97,0,112,0,105,0,92,0,116,0,106,0,111,0,105,0,110,0,116,0,46,0,115,0,108,0,100,0,112,0,114,0,116,0,9,128,255,254,255,6,116,0,106,0,111,0,105,0,110,0,116,0,2,0,"
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

        PIDInitializer = PIDCollection
    End Function

    Private Sub ErrorMsg(ByVal SwApp As SldWorks, ByVal Message As String)
        SwApp.SendMsgToUser2(Message, 0, 0)
        SwApp.RecordLine("'*** WARNING - General")
        SwApp.RecordLine("'*** " & Message)
        SwApp.RecordLine("")
    End Sub

    Public swApp As SldWorks

 End Class
```
