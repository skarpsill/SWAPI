---
title: "Get Spot Weld Connector Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Spot_Weld_Connector_Example_VBNET.htm"
---

# Get Spot Weld Connector Example (VB.NET)

This example shows how to get the properties of a spot weld connector.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Ensure the specified part exists.
 ' 4. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the specified part.
 ' 2. Activates the Ready study.
 ' 3. Prints properties of Spot Weld Connector-1 to the Immediate window.
 ' 4. Meshes the model.
 ' 5. Analyzes Ready.
  ' 6. Inspect the Immediate window, the Simulation study tree, and the
 '    graphics area.
 '
  ' NOTE: Because the part is used elsewhere, do not save any changes.
  '-----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim COSMOSWORKS As Object
         Dim CWObject As CwAddincallback
         Dim ActDoc As CWModelDoc
         Dim StudyMngr As CWStudyManager
         Dim Study As CWStudy
         Dim CwMesh As CWMesh
         Dim Part As ModelDoc2
         Dim LBCMgr As CWLoadsAndRestraintsManager
         Dim spotWeldConnector As CWSpotWeldConnector
         Dim longstatus As Integer, longwarnings As Integer
         Dim errCode As Integer
         Dim el As Double, tl As Double

         Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\car_model.sldasm", 2, 0, "", longstatus, longwarnings)
         If Part Is Nothing Then ErrorMsg(swApp, "Failed to open C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\car_model.sldasm")

         ' Get SOLIDWORKS Simulation add-in
         CWObject = SwApp.GetAddInObject("SldWorks.Simulation")
         If CWObject Is Nothing Then ErrorMsg(SwApp, "Failed to get the Simulation add-in")
         COSMOSWORKS = CWObject.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(SwApp, "Failed to get CosmosWorks")

         ' Get active document
         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(SwApp, "No active document")

         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(SwApp, "No CWStudyManager object")
         Study = StudyMngr.GetStudy(0)
         If Study Is Nothing Then ErrorMsg(SwApp, "No CWStudy object")

         StudyMngr.ActiveStudy = 0

         LBCMgr = Study.LoadsAndRestraintsManager
         If LBCMgr Is Nothing Then ErrorMsg(SwApp, "No CWLoadsAndRestraintsManager object")

         spotWeldConnector = LBCMgr.GetLoadsAndRestraints(2, errCode)
         Debug.Print("Spot Weld Connector-1")
         spotWeldConnector.SpotWeldConnectorBeginEdit()
         Debug.Print("  Source entity count: " & spotWeldConnector.GetSourceEntityCount)
         Debug.Print("  Target entity count: " & spotWeldConnector.GetTargetEntityCount)
         Debug.Print("  Location count: " & spotWeldConnector.GetSpotWeldLocationCount)
         Debug.Print("  Diameter: " & spotWeldConnector.SpotWeldDiameterValue)
         Debug.Print("  Diameter units as defined in swsLinearUnit_e: " & spotWeldConnector.SpotWeldDiameterUnit)
         spotWeldConnector.SpotWeldConnectorEndEdit()

         ' Mesh model
         CwMesh = Study.Mesh
         If CwMesh Is Nothing Then ErrorMsg(SwApp, "No CWMesh object")
         CwMesh.Quality = 1
         Call CwMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
         errCode = Study.CreateMesh(0, el, tl)
         If errCode <> 0 Then ErrorMsg(SwApp, "Mesh failed")

         ' Run analysis
         errCode = Study.RunAnalysis
         If errCode <> 0 Then ErrorMsg(SwApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode)

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
