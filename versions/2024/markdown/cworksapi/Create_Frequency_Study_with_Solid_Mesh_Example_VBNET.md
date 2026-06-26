---
title: "Create Frequency Study with Solid Mesh Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Frequency_Study_with_Solid_Mesh_Example_VBNET.htm"
---

# Create Frequency Study with Solid Mesh Example (VB.NET)

This example shows how to create a frequency study with solid mesh.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Ensure that the specified model exists.
 ' 4. Ensure that the specified material library exists.
 ' 5. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Opens the assembly.
 ' 2. Specifies the default frequency study results plots.
 ' 3. Creates a frequency study.
 ' 4. Applies the same material to all bodies.
 ' 5. Creates a mesh with default global size and tolerance parameters.
 ' 6. Sets the number of frequencies.
 ' 7. Runs the analysis.
 ' 8. Gets the result frequencies and mass participation factors.
 ' 9. Inspect the results plots and the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save any changes.
 ' -----------------------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.cosworks
Imports System

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim COSMOSWORKS As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim COSMOSObject As CwAddincallback
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim ActDoc As CWModelDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim StudyMngr As CWStudyManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Study As CWStudy
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim SolidMgr As CWSolidManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim SolidComponent As CWSolidComponent
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim SolidBody As CWSolidBody
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim CwMesh As CwMesh
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim CWResult As CWResults
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim FrequencyOptions As CWFrequencyStudyOptions
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim longstatus As Integer, longwarnings As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim errCode As Integer, errorCode As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim CompCount As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim BodyCount As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim j As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim i As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim bApp As Boolean
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim Freq As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim MassPart As Object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim el As Double, tl As Double

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get SOLIDWORKS Simulation object
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If COSMOSObject Is Nothing Then ErrorMsg("COSMOSObject object not found")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}COSMOSWORKS = COSMOSObject.COSMOSWORKS
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If COSMOSWORKS Is Nothing Then ErrorMsg("COSMOSWORKS object not found")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get active document
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\shaft.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", longstatus, longwarnings)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ActDoc = COSMOSWORKS.ActiveDoc()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If ActDoc Is Nothing Then ErrorMsg("No active document")
```

```vb
        ' Add default frequency study results plots of resultant amplitudes for all mode shapes
         errCode = ActDoc.AddDefaultFrequencyOrBucklingStudyPlot(True, 0, True, swsFrequencyBucklingResultDisplacementComponentTypes_e.swsFrequencyBucklingDisplacement_URES)
```

```vb
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Create new frequency study
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}StudyMngr = ActDoc.StudyManager()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If StudyMngr Is Nothing Then ErrorMsg("No CWStudyManager object")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Study = StudyMngr.CreateNewStudy3("Frequency", swsAnalysisStudyType_e.swsAnalysisStudyTypeFrequency, swsMeshType_e.swsMeshTypeSolid, errCode)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If Study Is Nothing Then ErrorMsg("Study not created")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get number of solid components
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SolidMgr = Study.SolidManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If SolidMgr Is Nothing Then ErrorMsg("No CWSolidManager object")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}CompCount = SolidMgr.ComponentCount

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Apply SOLIDWORKS material to rest of components
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SolidBody = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}SolidComponent = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For j = 0 To (CompCount - 1)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SolidComponent = SolidMgr.GetComponentAt(j, errorCode)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}BodyCount = SolidComponent.SolidBodyCount
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}For i = 0 To (BodyCount - 1)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}SolidBody = SolidComponent.GetSolidBodyAt(i, errCode)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg("No solid body")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}bApp = SolidBody.SetLibraryMaterial("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Ductile Iron (SN)")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}If bApp = False Then ErrorMsg("No material applied")
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}SolidBody = Nothing
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Next i
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next j

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Set meshing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}CwMesh = Study.Mesh
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If CwMesh Is Nothing Then ErrorMsg("No mesh object")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}CwMesh.Quality = 1
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Call CwMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}errCode = Study.CreateMesh(0, el, tl)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg("Mesh failed")
kadov_tag{{<spaces>}}
          ' Set frequency study options
         FrequencyOptions = Study.FrequencyStudyOptions
         If FrequencyOptions Is Nothing Then ErrorMsg("No CWFrequencyStudyOptions object")

         FrequencyOptions.Options = swsFrequencyStudyOption_e.swsFrequencyStudyOptionNumberFrequencies
         FrequencyOptions.NoOfFrequencies = 8

         Debug.Print("Study: " & Study.Name)
         Debug.Print("  Option as defined in swsFrequencyStudyOption_e: " & FrequencyOptions.Options)
         If FrequencyOptions.Options = 1 Then
             Debug.Print("  Upper-bound frequency: " & FrequencyOptions.UpperBoundFrequency)
         ElseIf FrequencyOptions.Options = 0 Then
             Debug.Print("  Number of frequencies: " & FrequencyOptions.NoOfFrequencies)
             Debug.Print("  Calculate frequencies around a specified frequency? (True=yes, False=no): " & FrequencyOptions.UseLowerBoundFrequency2)
             If FrequencyOptions.UseLowerBoundFrequency2 Then
                 Debug.Print("    Lower bound frequency: " & FrequencyOptions.LowerBoundFrequency)
             End If
         End If

         Debug.Print("  Result folder: " & FrequencyOptions.ResultFolder)
         Debug.Print("  Solver type as defined in swsSolverType_e: " & FrequencyOptions.SolverType)
         Debug.Print("  Use soft spring to stabilize the model? (True=yes, False=no): " & FrequencyOptions.UseSoftSpring2)
         Dim zeroStrainTemp As Double
         Dim tempUnit As Integer
         FrequencyOptions.GetZeroStrainTemperature(zeroStrainTemp, tempUnit)
         Debug.Print("  Flow/Thermal Effects:")
         Debug.Print("    Temperature source as defined in swsThermalOption_e: " & FrequencyOptions.ThermalResults)
         Debug.Print("    Temperature source:")
         If FrequencyOptions.ThermalResults = 1 Then
             Debug.Print("        Thermal study: " & FrequencyOptions.ThermalStudyName)
             Debug.Print("        Time step of transient thermal study: " & FrequencyOptions.TimeStep)
         ElseIf FrequencyOptions.ThermalResults = 2 Then
             Debug.Print("        SOLIDWORKS Flow Simulation results file: " & FrequencyOptions.FlowTemperatureFile)
         Else
             Debug.Print("        Model")
         End If
         Debug.Print("    Reference temperature at zero strain: " & zeroStrainTemp)
         Debug.Print("    Import fluid pressure loads from SOLIDWORKS Flow Simulation? (True=yes, False=no): " & FrequencyOptions.CheckFlowPressure2)
         If FrequencyOptions.CheckFlowPressure2 Then
             Debug.Print("        SOLIDWORKS Flow Simulation results file: " & FrequencyOptions.FlowPressureFile)
             Debug.Print("        Use reference pressure offset from Flow Simulation? (1=yes, 0=no): " & FrequencyOptions.ReferencePressureOption)
             If Not FrequencyOptions.ReferencePressureOption Then
                 Debug.Print("          Reference pressure offset: " & FrequencyOptions.DefinedReferencePressure)
             End If
             Debug.Print("        Run as legacy study and import only the normal component of the pressure load? (True=yes, False=no): " & FrequencyOptions.CheckRunAsLegacy2)
         End If

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Run analysis
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}errCode = Study.RunAnalysis
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg("Analysis failed")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get results: frequencies and mass participation factors
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}CWResult = Study.Results
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If CWResult Is Nothing Then ErrorMsg("No result object")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Freq = CWResult.GetResonantFrequencies(errCode)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MassPart = CWResult.GetMassParticipation(errCode)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Error routine
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Private Sub ErrorMsg(ByVal Message As String)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.SendMsgToUser2(Message, 0, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.RecordLine("'*** WARNING - General")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.RecordLine("'*** " & Message)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.RecordLine("")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks
End Class
```
