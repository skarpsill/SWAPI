---
title: "Set Composite Shell Options Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Set_Composite_Shell_Options_Example_VBNET.htm"
---

# Set Composite Shell Options Example (VB.NET)

This example shows how to set composite shell options.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim COSMOSWORKS As CosmosWorks
     Dim COSMOSObject As CwAddincallback
     Dim ActDoc As CWModelDoc
     Dim StudyMngr As CWStudyManager
     Dim Study As CWStudy
     Dim Shell As CWShell
     Dim Mesh As CWMesh
     Dim StaticOptions As CWStaticStudyOptions
     Dim Part As ModelDoc2
     Dim ShellMgr As CWShellManager
     Dim CWShellOptions As CWCompositeShellOptions
     Dim m As Integer
     Dim errCode As Integer
     Dim longstatus As Integer, longwarnings As Integer
     Dim bApp As Boolean
     Dim j As Integer

     Const MeshEleSize As Double = 1.4769
     Const MeshTol As Double = 0.073847

     Sub main()

         COSMOSObject = swApp.GetAddInObject("CosmosWorks.CosmosWorks")
         If COSMOSObject Is Nothing Then ErrorMsg(swApp, "Simulation add-in not loaded")
         COSMOSWORKS = COSMOSObject.COSMOSWORKS
         If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "No COSMOSWORKS object")

         Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\Simulation Examples\Composites\tjoint.SLDPRT", swDocumentTypes_e.swDocPART, 2, "", longstatus, longwarnings)
         If Part Is Nothing Then ErrorMsg(swApp, "Failed to open tjoint.SLDPRT")

         ActDoc = COSMOSWORKS.ActiveDoc()
         If ActDoc Is Nothing Then ErrorMsg(swApp, "No active document")

         StudyMngr = ActDoc.StudyManager()
         If StudyMngr Is Nothing Then ErrorMsg(swApp, "No study manager")
         StudyMngr.ActiveStudy = 1
         Study = StudyMngr.GetStudy(1)

         ShellMgr = Study.ShellManager
         If ShellMgr Is Nothing Then ErrorMsg(swApp, "No shell manager")

         Shell = ShellMgr.GetShellAt(0, errCode)
         If errCode <> 0 Then ErrorMsg(swApp, "No shell")

         Shell.ShellBeginEdit()
         bApp = Shell.SetLibraryMaterial("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Alloy Steel")
         Shell.Formulation = 2

         CWShellOptions = Shell.CompositeOptions
         If CWShellOptions Is Nothing Then ErrorMsg(swApp, "No composite shell options")

         CWShellOptions.RotateZeroDegreeReference2 = 0
         CWShellOptions.MappingType = 0
         CWShellOptions.Symmetric2 = 0
         CWShellOptions.Sandwich2 = 0
         CWShellOptions.PlyRelativeAngle2 = 0
         CWShellOptions.LengthUnit = 4
         CWShellOptions.AllPliesSameMaterial2 = -1

         m = CWShellOptions.GetTotalPlies()
         For j = 0 To m - 1
             errCode = CWShellOptions.SetPlyParameters2(j + 1, 0.1 * (j + 1), 0.05 * j, "solidworks materials", "Cast Stainless Steel")
         Next j

         Shell.ShellEndEdit()

         'Mesh
         Mesh = Study.Mesh
         Mesh.MesherType = 0
         Mesh.Quality = 0
         errCode = Study.CreateMesh(0, MeshEleSize, MeshTol)

         StaticOptions = Study.StaticStudyOptions
         StaticOptions.SolverType = 2

         'Run analysis
         errCode = Study.RunAnalysis

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
