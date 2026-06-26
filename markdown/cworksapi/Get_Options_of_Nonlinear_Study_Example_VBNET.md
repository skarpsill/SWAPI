---
title: "Get Options of Nonlinear Study Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Options_of_Nonlinear_Study_Example_VBNET.htm"
---

# Get Options of Nonlinear Study Example (VB.NET)

This example shows how to get the properties of nonlinear studies.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation primary interop assembly as a reference
 '    (in the IDE, click Project > Add Reference > .NET >
 '    SolidWorks.Interop.cosworks > OK).
 ' 3. Ensure that the specified file exists.
 ' 4. Open the Immediate window.
 '
 ' Postconditions:
  ' 1. Gets the properties of each nonlinear study.
  ' 2. Modifies the step/tolerance options in each nonlinear study.
  ' 3. Prints the properties of each nonlinear study in the model to the
 '    Immediate window.
 '
  ' NOTE: Because the model is used elsewhere, do not save any changes.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.cosworks
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swAddin As CwAddincallback
     Dim ssApp As CosmosWorks
     Dim ssModelDoc As CWModelDoc
     Dim ssStudyMgr As CWStudyManager
     Dim ssStudy As CWStudy
     Dim ssNonLinearStudyOptions As CWNonLinearStudyOptions
     Dim docName As String
     Dim errors As Integer
     Dim warnings As Integer
     Dim studyCnt As Integer
     Dim studyName As String
     Dim studyType As Integer
     Dim i As Integer
     Dim maxLoad As Double
     Dim maxDisplacement As Double
     Dim unit As Integer
     Dim maxArcSteps As Integer
     Dim arcLengthMultiplier As Double
     Dim displacementComponent As Integer
     Dim selectedEntity As Object
     Dim frequency As Integer
     Dim maximum As Integer
     Dim convergence As Double
     Dim tolerance As Double
     Dim factor As Double
     Dim swEntity As Entity
     Dim entityType As Integer
     Dim selEntityType As String

     Sub main()

         docName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Nonlinear\nl_plate.sldprt"
         swApp.OpenDoc6(docName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

         swAddin = swApp.GetAddInObject("SldWorks.Simulation")
         ssApp = swAddin.CosmosWorks
         ssModelDoc = ssApp.ActiveDoc
         ssStudyMgr = ssModelDoc.StudyManager

         studyCnt = ssStudyMgr.StudyCount
         For i = 0 To studyCnt - 1
             ssStudy = ssStudyMgr.GetStudy(i)
             studyName = ssStudy.Name
             Debug.Print("")
             Debug.Print("Study name: " & studyName)
             studyType = ssStudy.AnalysisType
             If (studyType = swsAnalysisStudyType_e.swsAnalysisStudyTypeNonlinear) Then
                 ssNonLinearStudyOptions = ssStudy.NonLinearStudyOptions
                 Debug.Print("  Nonlinear study subtype as defined in swsNonlinearAnalysisSubType_e: " & ssStudy.NonlinearAnalysisSubType)
                 Debug.Print("    Solution properties:")
                 Debug.Print("       Stepping options:")
                 Debug.Print("          Start time: " & ssNonLinearStudyOptions.StartTime)
                 Debug.Print("          End time: " & ssNonLinearStudyOptions.EndTime)
                 Debug.Print("          Save data for restarting analysis? (1=yes, 0=no) " & ssNonLinearStudyOptions.SaveDataForRestartingAnalysis)
                 Debug.Print("          Solution-time increment: " & ssNonLinearStudyOptions.TimeIncrement)
                 Debug.Print("          Fixed-time increment: " & ssNonLinearStudyOptions.FixedTimeIncrement)
                 Debug.Print("       Geometry nonlinearity options:")
                 Debug.Print("          Use large displacement formulation? (1=yes, 0=no) " & ssNonLinearStudyOptions.UseLargeDisplacement)
                 Debug.Print("          Update direction of load at every solution step with deflection? (1=yes, 0=no) " & ssNonLinearStudyOptions.UseUpdateLoadDirection)
                 Debug.Print("          Use large strain formulation? (1=yes, 0=no) " & ssNonLinearStudyOptions.UseLargeStrain)
                 Debug.Print("          Keep bolt pre-stress? (1=yes, 0=no) " & ssNonLinearStudyOptions.KeepBoltPreStress)
                 Debug.Print("       Solver type as defined in swsSolverType_e: " & ssNonLinearStudyOptions.SolverType)
                 Debug.Print("       Results folder path: " & ssNonLinearStudyOptions.ResultFolderPath)

                 Debug.Print("    Advanced properties:")
                 Debug.Print("       Methods:")
                 Debug.Print("          Control type as defined in swsNonLinearOptionControlMethodType_e: " & ssNonLinearStudyOptions.ControlMethodType)
                 Debug.Print("          Integration type as defined in swsNonLinearOptionIntegrationMethodType_e: " & ssNonLinearStudyOptions.IntegrationMethodType)
                 Debug.Print("          Iterative type as defined in swsNonLinearOptionIterativeMethodType_e: " & ssNonLinearStudyOptions.IterativeMethodType)

                 Debug.Print("       Displacement control options:")
                 selEntityType = "Nothing"
                 ssNonLinearStudyOptions.GetDisplacementControlOptions2(displacementComponent, unit, selectedEntity)
                 If Not selectedEntity Is Nothing Then
                     swEntity = selectedEntity
                     entityType = swEntity.GetType
                     Select Case entityType
                         Case 3
                             selEntityType = "vertex"
                         Case 6
                             selEntityType = "reference point"
                         Case 0
                             selEntityType = "Nothing"
                     End Select
                 End If
                 Debug.Print("          Displacement component as defined in swsDisplacementComponent_e: " & displacementComponent)
                 Debug.Print("          Units as defined in swsLinearUnit_e: " & unit)
                 Debug.Print("          Selected reference entity type: " & selEntityType)

                 ssNonLinearStudyOptions.GetArcLengthCompletionOptions(maxLoad, maxDisplacement, unit, maxArcSteps, arcLengthMultiplier)
                 Debug.Print("       Arc-Length completion options:")
                 Debug.Print("          Maximum load-pattern multiplier: " & maxLoad)
                 Debug.Print("          Maximum displacement: " & maxDisplacement)
                 Debug.Print("          Units as defined in swsLinearUnit_e: " & unit)
                 Debug.Print("          Maximum number of arc steps: " & maxArcSteps)
                 Debug.Print("          Initial arc length multiplier: " & arcLengthMultiplier)
                 Debug.Print("       Step/Tolerance options:")
                 ssNonLinearStudyOptions.GetStepToleranceOptions(frequency, maximum, convergence, tolerance, factor)
                 Debug.Print("          Tolerance: ")
                 Debug.Print("              Frequency of performing equilibrium in number of solution steps: " & frequency)
                 Debug.Print("              Maximum number of equilibrium iterations for any solution step: " & maximum)
                 Debug.Print("              Relative displacement tolerance used for equilibrium convergence: " & convergence)
                 Debug.Print("              Tolerance for strain increment for models with creep or plasticity: " & tolerance)
                 Debug.Print("              Stiffness singularity elimination factor: " & factor)
                 Dim status As Long
                 status = ssNonLinearStudyOptions.SetStepToleranceOptions(-1, 10, 0.002, 0.02, 1)
                 ssNonLinearStudyOptions.GetStepToleranceOptions(frequency, maximum, convergence, tolerance, factor)
                 Debug.Print("          New Tolerance: ")
                 Debug.Print("              Frequency of performing equilibrium in number of solution steps: " & frequency)
                 Debug.Print("              Maximum number of equilibrium iterations for any solution step: " & maximum)
                 Debug.Print("              Relative displacement tolerance used for equilibrium convergence: " & convergence)
                 Debug.Print("              Tolerance for strain increment for models with creep or plasticity: " & tolerance)
                 Debug.Print("              Stiffness singularity elimination factor: " & factor)

                 Debug.Print("    Flow/Thermal Effects:")
                 Debug.Print("       Thermal options:")
                 Debug.Print("          Temperature source as defined in swsThermalOption_e: " & ssNonLinearStudyOptions.ThermalResults)
                 Debug.Print("          Temperature source:")
                 If ssNonLinearStudyOptions.ThermalResults = 1 Then
                     Debug.Print("          Thermal study: " & ssNonLinearStudyOptions.ThermalStudyName)
                     Debug.Print("          Use temperature from thermal study at each nonlinear time step? (1=yes, 0=no): " & ssNonLinearStudyOptions.CheckUseTempFromThermalStudy)
                     If ssNonLinearStudyOptions.CheckUseTempFromThermalStudy = 0 Then
                         Debug.Print("             Time step of transient thermal study whose temperature to use: " & ssNonLinearStudyOptions.TimeStep)
                     End If
                 ElseIf ssNonLinearStudyOptions.ThermalResults = 2 Then
                     Debug.Print("               SOLIDWORKS Flow Simulation results file: "  & ssNonLinearStudyOptions.FlowTemperatureFile)
                 Else
                     Debug.Print("               The current model")
                 End If

                 Debug.Print("       Fluid pressure option:")
                 Debug.Print("          Import fluid pressure loads from SOLIDWORKS Flow Simulation? (1=yes, 0=no): " & ssNonLinearStudyOptions.CheckFlowPressure)
                 If ssNonLinearStudyOptions.CheckFlowPressure = 1 Then
                     Debug.Print("           SOLIDWORKS Flow Simulation results file: " & ssNonLinearStudyOptions.FlowPressureFile)
                     Debug.Print("           Use reference pressure offset from Flow Simulation? (1=yes, 0=no): " & ssNonLinearStudyOptions.ReferencePressureOption)
                     If ssNonLinearStudyOptions.ReferencePressureOption = 0 Then
                         Debug.Print("             Reference pressure offset: " & ssNonLinearStudyOptions.DefinedReferencePressure)
                     End If
                     Debug.Print("          Run as legacy study and import only the normal component of the pressure load? (1=yes, 0=no): " & ssNonLinearStudyOptions.CheckRunAsLegacy)
                 End If

             End If
         Next

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
