---
title: "Create Frequency Study with Solid Mesh Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Create_Frequency_Study_with_Solid_Mesh_Example_VB.htm"
---

# Create Frequency Study with Solid Mesh Example (VBA)

This example shows how to create a frequency study with solid mesh.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation version type library).
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
Option Explicit
kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
Sub main()

kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim swApp As SldWorks.SldWorks
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim COSMOSWORKS As Object
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim COSMOSObject As CosmosWorksLib.CwAddincallback
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim ActDoc As CosmosWorksLib.CWModelDoc
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim StudyMngr As CosmosWorksLib.CWStudyManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim Study As CosmosWorksLib.CWStudy
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SolidMgr As CosmosWorksLib.CWSolidManager
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SolidComponent As CosmosWorksLib.CWSolidComponent
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim SolidBody As CosmosWorksLib.CWSolidBody
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim CwMesh As CosmosWorksLib.CwMesh
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim CWResult As CosmosWorksLib.CWResults
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim FrequencyOptions As CosmosWorksLib.CWFrequencyStudyOptions
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim CWMat As CosmosWorksLib.CWMaterial
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim longstatus As Long, longwarnings As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim errCode As Long, errorCode As Long, pValue As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim lStatus As Long
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim CompCount As Integer
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim BodyCount As Integer
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim j As Integer
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim i As Integer
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim bApp As Boolean
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim Freq As Variant
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim MassPart As Variant
kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}Dim el As Double, tl As Double
kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Connect to SolidWork software
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If swApp Is Nothing Then Set swApp = Application.SldWorks

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get SOLIDWORKS Simulation object
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set COSMOSObject = swApp.GetAddInObject("SldWorks.Simulation")
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If COSMOSObject Is Nothing Then ErrorMsg swApp, "COSMOSObject object not found"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If COSMOSWORKS Is Nothing Then ErrorMsg swApp, "COSMOSWORKS object not found"

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get active document
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swApp.OpenDoc6 "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\shaft.sldasm", swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_Silent, "", longstatus, longwarnings
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set ActDoc = COSMOSWORKS.ActiveDoc()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If ActDoc Is Nothing Then ErrorMsg swApp, "No active document"

     ' Add default frequency study results plots of resultant amplitudes for all mode shapes
     errCode = ActDoc.AddDefaultFrequencyOrBucklingStudyPlot(True, 0, True, swsFrequencyBucklingDisplacement_URES)

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Create new frequency study
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set StudyMngr = ActDoc.StudyManager()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If StudyMngr Is Nothing Then ErrorMsg swApp, "No CWStudyManager object"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set Study = StudyMngr.CreateNewStudy3("Frequency", swsAnalysisStudyTypeFrequency, swsMeshTypeSolid, errCode)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If Study Is Nothing Then ErrorMsg swApp, "Study not created"

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get number of solid components
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set SolidMgr = Study.SolidManager
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If SolidMgr Is Nothing Then ErrorMsg swApp, "No CWSolidManager object"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CompCount = SolidMgr.ComponentCount

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Apply SOLIDWORKS material to rest of components
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set SolidBody = Nothing
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set SolidComponent = Nothing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For j = 0 To (CompCount - 1)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set SolidComponent = SolidMgr.GetComponentAt(j, errorCode)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}BodyCount = SolidComponent.SolidBodyCount
kadov_tag{{<spaces>}}          kadov_tag{{</spaces>}}For i = 0 To (BodyCount - 1)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set SolidBody = SolidComponent.GetSolidBodyAt(i, errCode)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg swApp, "No solid body"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bApp = SolidBody.SetLibraryMaterial("c:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\sldmaterials\solidworks materials.sldmat", "Ductile Iron (SN)")
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If bApp = False Then ErrorMsg swApp, "No material applied"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set SolidBody = Nothing
kadov_tag{{<spaces>}}          kadov_tag{{</spaces>}}Next i
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next j

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Set meshing
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set CwMesh = Study.Mesh
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If CwMesh Is Nothing Then ErrorMsg swApp, "No mesh object"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}CwMesh.Quality = 1
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Call CwMesh.GetDefaultElementSizeAndTolerance(0, el, tl)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}errCode = Study.CreateMesh(0, el, tl)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg swApp, "Mesh failed"
kadov_tag{{<spaces>}}
    ' Set frequency study options
     Set FrequencyOptions = Study.FrequencyStudyOptions
     If FrequencyOptions Is Nothing Then ErrorMsg swApp, "No CWFrequencyStudyOptions object"

    FrequencyOptions.Options = swsFrequencyStudyOptionNumberFrequencies
     FrequencyOptions.NoOfFrequencies = 8

    Debug.Print "Study: " & Study.Name
     Debug.Print "  Option as defined in swsFrequencyStudyOption_e: " & FrequencyOptions.Options
     If FrequencyOptions.Options = 1 Then
         Debug.Print "  Upper-bound frequency: " & FrequencyOptions.UpperBoundFrequency
     ElseIf FrequencyOptions.Options = 0 Then
         Debug.Print "  Number of frequencies: " & FrequencyOptions.NoOfFrequencies
         Debug.Print "  Calculate frequencies around a specified frequency? (True=yes, False=no): " & FrequencyOptions.UseLowerBoundFrequency
         If FrequencyOptions.UseLowerBoundFrequency2 Then
             Debug.Print "    Lower bound frequency: " & FrequencyOptions.LowerBoundFrequency
         End If
     End If

    Debug.Print "  Result folder: " & FrequencyOptions.ResultFolder
     Debug.Print "  Solver type as defined in swsSolverType_e: " & FrequencyOptions.SolverType
     Debug.Print "  Use soft spring to stabilize the model? (True=yes, False=no): " & FrequencyOptions.UseSoftSpring2
     Dim zeroStrainTemp As Double
     Dim tempUnit As Long
     FrequencyOptions.GetZeroStrainTemperature zeroStrainTemp, tempUnit
     Debug.Print "  Flow/Thermal Effects:"
     Debug.Print "    Temperature source as defined in swsThermalOption_e: " & FrequencyOptions.ThermalResults
     Debug.Print "    Temperature source:"
     If FrequencyOptions.ThermalResults = 1 Then
         Debug.Print "        Thermal study: " & FrequencyOptions.ThermalStudyName
         Debug.Print "        Time step of transient thermal study: " & FrequencyOptions.TimeStep
     ElseIf FrequencyOptions.ThermalResults = 2 Then
         Debug.Print "        SOLIDWORKS Flow Simulation results file: " & FrequencyOptions.FlowTemperatureFile
     Else
         Debug.Print "        Model"
     End If
     Debug.Print "    Reference temperature at zero strain: " & zeroStrainTemp
    Debug.Print "    Import fluid pressure loads from SOLIDWORKS Flow Simulation? (True=yes, False=no): " & FrequencyOptions.CheckFlowPressure2
     If FrequencyOptions.CheckFlowPressure2 Then
         Debug.Print "        SOLIDWORKS Flow Simulation results file: " & FrequencyOptions.FlowPressureFile
         Debug.Print "        Use reference pressure offset from Flow Simulation? (1=yes, 0=no): " & FrequencyOptions.ReferencePressureOption
         If Not FrequencyOptions.ReferencePressureOption Then
             Debug.Print "          Reference pressure offset: " & FrequencyOptions.DefinedReferencePressure
         End If
         Debug.Print "        Run as legacy study and import only the normal component of the pressure load? (True=yes, False=no): " & FrequencyOptions.CheckRunAsLegacy2
     End If

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Run analysis
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}errCode = Study.RunAnalysis
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If errCode <> 0 Then ErrorMsg swApp, "Analysis failed"

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get results: frequencies and mass participation factors
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set CWResult = Study.Results
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If CWResult Is Nothing Then ErrorMsg swApp, "No result object"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Freq = CWResult.GetResonantFrequencies(errCode)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}MassPart = CWResult.GetMassParticipation(errCode)
End Sub

' Error function
Function ErrorMsg(swApp As SldWorks.SldWorks, Message As String)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swApp.SendMsgToUser2 Message, 0, 0
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swApp.RecordLine "'*** WARNING - General"
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swApp.RecordLine "'*** " & Message
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}swApp.RecordLine ""
End Function
```
