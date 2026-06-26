---
title: "Set Composite Shell Options Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Set_Composite_Shell_Options_Example_VB.htm"
---

# Set Composite Shell Options Example (VBA)

This example shows how to set composite shell options.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
 ' 3. Verify that the specified material library exists.
 ' 4. Verify that the specified model document exists.
 '
 ' Postconditions:
 ' 1. Opens the model.
 ' 2. Activates Ready - 8 plies.
 ' 3. Sets composite shell options.
 ' 4. Meshes the model.
 ' 5. Analyzes the study.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
 Dim SwApp As SldWorks.SldWorks
 Dim COSMOSWORKS As CosmosWorksLib.COSMOSWORKS
 Dim COSMOSObject As CosmosWorksLib.CWAddinCallBack
 Dim ActDoc As CosmosWorksLib.CWModelDoc
 Dim StudyMngr As CosmosWorksLib.CWStudyManager
 Dim Study As CosmosWorksLib.CWStudy
 Dim Shell As CosmosWorksLib.CWShell
 Dim Mesh As CosmosWorksLib.CwMesh
 Dim StaticOptions As CosmosWorksLib.CWStaticStudyOptions
 Dim Part As SldWorks.ModelDoc2
 Dim ShellMgr As CosmosWorksLib.CWShellManager
 Dim CWShellOptions As CosmosWorksLib.CWCompositeShellOptions
 Dim m As Integer
 Dim errCode As Long
 Dim longstatus As Long, longwarnings As Long
 Dim bApp As Boolean
 Dim j As Integer
Const MeshEleSize   As Double = 1.4769
 Const MeshTol       As Double = 0.073847
Option Explicit
 Sub main()

    Set SwApp = Application.SldWorks
    Set COSMOSObject = SwApp.GetAddInObject("CosmosWorks.CosmosWorks")
     If COSMOSObject Is Nothing Then ErrorMsg SwApp, "Simulation add-in not loaded"
     Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "No COSMOSWORKS object"

    Set Part = SwApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\Simulation Examples\Composites\tjoint.SLDPRT", swDocPART, 2, "", longstatus, longwarnings)
     If Part Is Nothing Then ErrorMsg SwApp, "Failed to open tjoint.SLDPRT"

    Set ActDoc = COSMOSWORKS.ActiveDoc()
     If ActDoc Is Nothing Then ErrorMsg SwApp, "No active document"

    Set StudyMngr = ActDoc.StudyManager()
     If StudyMngr Is Nothing Then ErrorMsg SwApp, "No study manager"
     StudyMngr.ActiveStudy = 1
     Set Study = StudyMngr.GetStudy(1)

    Set ShellMgr = Study.ShellManager
     If ShellMgr Is Nothing Then ErrorMsg SwApp, "No shell manager"

    Set Shell = ShellMgr.GetShellAt(0, errCode)
     If errCode <> 0 Then ErrorMsg SwApp, "No shell"

    Shell.ShellBeginEdit
     bApp = Shell.SetLibraryMaterial("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Alloy Steel")
     Shell.Formulation = 2

    Set CWShellOptions = Shell.CompositeOptions
     If CWShellOptions Is Nothing Then ErrorMsg SwApp, "No composite shell options"

     CWShellOptions.RotateZeroDegreeReference2 = 0
     CWShellOptions.MappingType = 0
     CWShellOptions.Symmetric = 0
     CWShellOptions.Sandwich2 = 0
     CWShellOptions.PlyRelativeAngle2 = 0
     CWShellOptions.LengthUnit = 4
     CWShellOptions.AllPliesSameMaterial2 = -1
    m = CWShellOptions.GetTotalPlies()
     For j = 0 To m - 1
         errCode = CWShellOptions.SetPlyParameters2(j + 1, 0.1 * (j + 1), 0.05 * j, "solidworks materials", "Cast Stainless Steel")
     Next j

    Shell.ShellEndEdit

    'Mesh
     Set Mesh = Study.Mesh
     Mesh.MesherType = 0
     Mesh.Quality = 0
     errCode = Study.CreateMesh(0, MeshEleSize, MeshTol)

    Set StaticOptions = Study.StaticStudyOptions
     StaticOptions.SolverType = 2
    'Run analysis
     errCode = Study.RunAnalysis

End Sub
Sub ErrorMsg(SwApp As SldWorks.SldWorks, Message As String)
     SwApp.SendMsgToUser2 Message, 0, 0
     SwApp.RecordLine "'*** WARNING - General"
     SwApp.RecordLine "'*** " & Message
     SwApp.RecordLine ""
 End Sub
```
