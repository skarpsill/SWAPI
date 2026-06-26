---
title: "Get Spot Weld Connector Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Add_Spot_Weld_Connector_Example_VB.htm"
---

# Get Spot Weld Connector Example (VBA)

This example shows how to get the properties of a spot weld connector.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
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
 ' NOTE: Because the part is used elsewhere, do not save changes.
 '-----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim SwApp As SldWorks.SldWorks
     Dim COSMOSWORKS As Object
     Dim CWObject As CosmosWorksLib.CwAddincallback
     Dim ActDoc As CosmosWorksLib.CWModelDoc
     Dim StudyMngr As CosmosWorksLib.CWStudyManager
     Dim Study As CosmosWorksLib.CWStudy
     Dim CwMesh As CosmosWorksLib.CwMesh
     Dim Part As SldWorks.ModelDoc2
     Dim LBCMgr As CosmosWorksLib.CWLoadsAndRestraintsManager
     Dim spotWeldConnector As CosmosWorksLib.CWSpotWeldConnector
     Dim longstatus As Long, longwarnings As Long
     Dim errCode As Long
     Dim el As Double, tl As Double

     If SwApp Is Nothing Then Set SwApp = Application.SldWorks
     Set Part = SwApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\car_model.sldasm", 2, 0, "", longstatus, longwarnings)

    ' Get SOLIDWORKS Simulation add-in
     Set CWObject = SwApp.GetAddInObject("SldWorks.Simulation")
     If CWObject Is Nothing Then ErrorMsg SwApp, "Failed to get the Simulation add-in"
     Set COSMOSWORKS = CWObject.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "Failed to get CosmosWorks"
    ' Get active document
     Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"

    Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "No CWStudyManager object"
     Set Study = StudyMngr.GetStudy(0)
     If Study Is Nothing Then ErrorMsg SwApp, "No CWWtudy object"

    StudyMngr.ActiveStudy = 0
    Set LBCMgr = Study.LoadsAndRestraintsManager
     If LBCMgr Is Nothing Then ErrorMsg SwApp, "No CWLoadsAndRestraintsManagerobject"

    Set spotWeldConnector = LBCMgr.GetLoadsAndRestraints(2, errCode)
     Debug.Print "Spot Weld Connector-1"
     spotWeldConnector.SpotWeldConnectorBeginEdit
     Debug.Print "  Source entity count: " & spotWeldConnector.GetSourceEntityCount
     Debug.Print "  Target entity count: " & spotWeldConnector.GetTargetEntityCount
     Debug.Print "  Location count: " & spotWeldConnector.GetSpotWeldLocationCount
     Debug.Print "  Diameter: " & spotWeldConnector.SpotWeldDiameterValue
     Debug.Print "  Diameter units as defined in swsLinearUnit_e: " & spotWeldConnector.SpotWeldDiameterUnit
     spotWeldConnector.SpotWeldConnectorEndEdit
    ' Mesh model
     Set CwMesh = Study.Mesh
     If CwMesh Is Nothing Then ErrorMsg SwApp, "No CWMesh object"
     CwMesh.Quality = 1
     Call CwMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
     errCode = Study.CreateMesh(0, el, tl)
     If errCode <> 0 Then ErrorMsg SwApp, "Mesh failed"
    ' Run analysis
     errCode = Study.RunAnalysis
     If errCode <> 0 Then ErrorMsg SwApp, "Analysis failed with error code as defined in swsRunAnalysisError_e: " & errCode

 End Sub
Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""

End Sub
```
