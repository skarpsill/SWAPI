---
title: "Apply Material to Bodies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Apply_Material_to_Bodies_Example_VB.htm"
---

# Apply Material to Bodies Example (VBA)

This example shows how to apply user-defined and SOLIDWORKS-defined
material to different bodies.

```vb
 '----------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click

'    Tools > Add-ins > SOLIDWORKS Simulation > OK).

' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,

'    click Tools > References > SOLIDWORKS Simulation version type library).
' 3. Verify that the specified material library exists.
' 4. Verify that the specified assembly exists.
'
' Postconditions:
' 1. Opens the assembly.
' 2. Creates a nonlinear study.
' 3. Gets the number of components.
' 4. Applies materials to all components.
' 5. Expand the Parts folder in the Simulation Study tree
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}to verify step 4.
'
' NOTE: Because this assembly is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
Option Explicit

Sub main()

kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SwApp As SldWorks.SldWorks
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim COSMOSWORKS As Object
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim COSMOSObject As CosmosWorksLib.CwAddincallback
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim ActDoc As CosmosWorksLib.CWModelDoc
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim StudyMngr As CosmosWorksLib.CWStudyManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim Study As CosmosWorksLib.CWStudy
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SolidMgr As CosmosWorksLib.CWSolidManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SolidComponent As CosmosWorksLib.CWSolidComponent
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SolidBody As CosmosWorksLib.CWSolidBody
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim errorCode As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim longstatus As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim longwarnings As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim errCode As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim CompCount As Integer
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim j As Integer
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim CWMat As CosmosWorksLib.CWMaterial
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim returnValue As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SName As String
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}' Connect to SOLIDWORKS
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If SwApp Is Nothing Then Set SwApp = Application.SldWorks
kadov_tag{{<spaces>}}     kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get SOLIDWORKS Simulation object>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set COSMOSObject = SwApp.GetAddInObject("SldWorks.Simulation")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If COSMOSObject Is Nothing Then ErrorMsg SwApp, "No CwAddincallback object"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "No COSMOSWORKS object"

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Open and get document
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SwApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\basketball_hoop.sldasm", swDocASSEMBLY, swOpenDocOptions_Silent, "", longstatus, longwarnings
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set ActDoc = COSMOSWORKS.ActiveDoc()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Create new nonlinear study
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set StudyMngr = ActDoc.StudyManager()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If StudyMngr Is Nothing Then ErrorMsg SwApp, "No CWStudyManager object"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set Study = StudyMngr.CreateNewStudy("Nonlinear", swsAnalysisStudyTypeNonlinear, swsMeshTypeSolid, errCode)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If Study Is Nothing Then ErrorMsg SwApp, "No CWStudy object"

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get number of solid components
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set SolidMgr = Study.SolidManager
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If SolidMgr Is Nothing Then ErrorMsg SwApp, "No CWSolidManager object"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CompCount = SolidMgr.ComponentCount
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set SolidComponent = SolidMgr.GetComponentAt(0, errorCode)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If SolidComponent Is Nothing Then ErrorMsg SwApp, "No CWSolidComponent object"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get name of solid component
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SName = SolidComponent.ComponentName

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Apply user-defined material for the first component in the tree
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg SwApp, "No solid body"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If SolidBody Is Nothing Then ErrorMsg SwApp, "No CWSolidBody object"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set CWMat = SolidBody.GetDefaultMaterial
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CWMat.MaterialUnits = 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If CWMat Is Nothing Then ErrorMsg SwApp, "No CWMaterial object"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CWMat.MaterialName = "Alloy Steel"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CWMat.SetPropertyByName "EX", 210000000000#, 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Debug.Print "Property EX: " & CWMat.GetPropertyByName(swsUnitSystemSI, "EX", 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CWMat.SetPropertyByName "NUXY", 0.28, 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CWMat.SetPropertyByName "GXY", 79000000000#, 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CWMat.SetPropertyByName "DENS", 7700, 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CWMat.SetPropertyByName "SIGXT", 723825600, 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CWMat.SetPropertyByName "SIGYLD", 620422000, 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CWMat.SetPropertyByName "ALPX", 0.000013, 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CWMat.SetPropertyByName "KX", 50, 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CWMat.SetPropertyByName "C", 460, 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}errCode = SolidBody.SetSolidBodyMaterial(CWMat)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg SwApp, "Failed to apply material"

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Apply a different SOLIDWORKS Simulation library material to other components
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set SolidBody = Nothing
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set SolidComponent = Nothing
kadov_tag{{<spaces>}}         kadov_tag{{</spaces>}}For j = 1 To (CompCount - 1)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set SolidComponent = SolidMgr.GetComponentAt(j, errorCode)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SName = SolidComponent.ComponentName
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg SwApp, "No CWSolidBody object"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}returnValue = SolidBody.SetLibraryMaterial("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "2024 Alloy (SN)")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If returnValue = 0 Then ErrorMsg SwApp, "No material applied"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set SolidBody = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next j
End Sub

' Error function
Function ErrorMsg(SwApp As Object, Message As String)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SwApp.SendMsgToUser2 Message, 0, 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SwApp.RecordLine "'*** WARNING - General"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SwApp.RecordLine "'*** " & Message
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SwApp.RecordLine ""
kadov_tag{{<spaces>}}
End Function
```
