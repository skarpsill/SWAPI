---
title: "Create Nonlinear Study and Apply Materials Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Nonlinear_Study_and_Apply_Materials_Example_VB.htm"
---

# Create Nonlinear Study and Apply Materials Example (VBA)

This example shows how to create a nonlinear study and apply user-defined
and SOLIDWORKS materials to an assembly's components.

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
' 3. Applies user-defined material to the first component and
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}SOLIDWORKS material to the remaining components.
' 4. To verify, expand the Parts folder in the Simulation Study tree,
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}which is located beneath the FeatureManager design tree, and
' kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}observe the names of the materials applied to holder-1 and pipe-1.
'
' NOTE: Because the assembly is used elsewhere, do not save changes.
'----------------------------------------------------------------------------
Option Explicit
Sub main()

kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SwApp As SldWorks.SldWorks
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim COSMOSWORKS As Object
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim COSMOSObject As Object
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim ActDoc As CosmosWorksLib.CWModelDoc
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim StudyMngr As CosmosWorksLib.CWStudyManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim Study As CosmosWorksLib.CWStudy
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SolidMgr As CosmosWorksLib.CWSolidManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SolidComponent As CosmosWorksLib.CWSolidComponent
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SolidBody As CosmosWorksLib.CWSolidBody
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SName As String
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim errors As Long, warnings As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim errorCode As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim errCode As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim CompCount As Integer
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim j As Integer
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim CWMat As CosmosWorksLib.CWMaterial
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim bApp As Boolean
   Dim swVersion As Long
   Dim cwVersion As Long
   Dim cwProgID As String

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Connect to SOLIDWORKS
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If SwApp Is Nothing Then Set SwApp = Application.SldWorks

   'Determine host SOLIDWORKS version

     swVersion  = Left(SwApp.RevisionNumber, 2)

     'Calculate the correct Simulation ProgID for this version of SOLIDWORKS

     cwVersion  =  swVersion  -  15

     cwProgID  =  "SldWorks.Simulation." & cwVersion

     Debug.Print (cwProgID)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get the SOLIDWORKS Simulation object
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set COSMOSObject = SwApp.GetAddInObject(cwProgID)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If COSMOSObject Is Nothing Then ErrorMsg SwApp, "COSMOSObject object not found", True
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "COSMOSWORKS object not found", True
kadov_tag{{<spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Open and get the active document
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Skadov_tag{{</spaces>}}wApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Nonlinear\nl_pipe_holder.sldasm", swDocASSEMBLY, swOpenDocOptions_Silent, "", errors, warnings
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set ActDoc = COSMOSWORKS.ActiveDoc()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document", True
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Create new nonlinear study
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set StudyMngr = ActDoc.StudyManager()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If StudyMngr Is Nothing Then ErrorMsg SwApp, "CWStudyManager object not created", True
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set Study = StudyMngr.CreateNewStudy("NonLinear", swsAnalysisStudyTypeNonlinear, swsMeshTypeSolid, errCode)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If Study Is Nothing Then ErrorMsg SwApp, "Study not created", True
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get number of solid components
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set SolidMgr = Study.SolidManager
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If SolidMgr Is Nothing Then ErrorMsg SwApp, "CWSolidManager object not created", True
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CompCount = SolidMgr.ComponentCount
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set SolidComponent = SolidMgr.GetComponentAt(0, errorCode)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If SolidComponent Is Nothing Then ErrorMsg SwApp, "CWSolidComponent object not created", True
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get name of solid component
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SName = SolidComponent.ComponentName
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Apply user-defined material to the first component in the tree
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg SwApp, "No solid body", True
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If SolidBody Is Nothing Then ErrorMsg SwApp, "CWSolidBody object not created", True
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set CWMat = SolidBody.GetDefaultMaterial
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CWMat.MaterialUnits = 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If CWMat Is Nothing Then ErrorMsg SwApp, "No default material object", True
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CWMat.MaterialName = "Alloy Steel"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call CWMat.SetPropertyByName("EX", 210000000000#, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call CWMat.SetPropertyByName("NUXY", 0.28, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call CWMat.SetPropertyByName("GXY", 79000000000#, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call CWMat.SetPropertyByName("DENS", 7700, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call CWMat.SetPropertyByName("SIGXT", 723825600, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call CWMat.SetPropertyByName("SIGYLD", 620422000, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call CWMat.SetPropertyByName("ALPX", 0.000013, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call CWMat.SetPropertyByName("KX", 50, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call CWMat.SetPropertyByName("C", 460, 0)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}errCode = SolidBody.SetSolidBodyMaterial(CWMat)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg SwApp, "Failed to apply material", True
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Apply SOLIDWORKS library material to rest of components
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set SolidBody = Nothing
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set SolidComponent = Nothing
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}For j = 1 To (CompCount - 1)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set SolidComponent = SolidMgr.GetComponentAt(j, errorCode)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SName = SolidComponent.ComponentName
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set SolidBody = SolidComponent.GetSolidBodyAt(0, errCode)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg SwApp, "No solid body", True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bApp = SolidBody.SetLibraryMaterial2("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Gray Cast Iron (SN)")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If bApp = False Then ErrorMsg SwApp, "No material applied", True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set SolidBody = Nothing
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Next j

End Sub

' Error function
Function ErrorMsg(SwApp As SldWorks.SldWorks, Message As String, EndTest As Boolean)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SwApp.SendMsgToUser2 Message, 0, 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SwApp.RecordLine "'*** WARNING - General"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SwApp.RecordLine "'*** " & Message
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}SwApp.RecordLine ""
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If EndTest Then
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If
End Function
```
