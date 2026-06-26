---
title: "Get Options of Nonlinear Study Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "cworksapi/Get_Options_of_Nonlinear_Study_Example_VB.htm"
---

# Get Options of Nonlinear Study Example (VBA)

This example shows how to get the properties of nonlinear studies.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Add the SOLIDWORKS Simulation as an add-in (in SOLIDWORKS, click
 '    Tools > Add-ins > SOLIDWORKS Simulation > OK).
 ' 2. Add the SOLIDWORKS Simulation type library as a reference (in the IDE,
 '    click Tools > References > SOLIDWORKS Simulation  version type library).
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
 Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swAddin As CosmosWorksLib.CwAddincallback
 Dim ssApp As CosmosWorksLib.CosmosWorks
 Dim ssModelDoc As CosmosWorksLib.CWModelDoc
 Dim ssStudyMgr As CosmosWorksLib.CWStudyManager
 Dim ssStudy As CosmosWorksLib.CWStudy
 Dim ssNonLinearStudyOptions As CosmosWorksLib.CWNonLinearStudyOptions
 Dim docName As String
 Dim errors As Long
 Dim warnings As Long
 Dim studyCnt As Long
 Dim studyName As String
 Dim studyType As Long
 Dim i As Long
 Dim maxLoad As Double
 Dim maxDisplacement As Double
 Dim unit As Long
 Dim maxArcSteps As Long
 Dim arcLengthMultiplier As Double
 Dim displacementComponent As Long
 Dim selectedEntity As Object
 Dim frequency As Long
 Dim maximum As Long
 Dim convergence As Double
 Dim tolerance As Double
 Dim factor As Double
 Dim swEntity As Entity
 Dim entityType As Long
 Dim selEntityType As String

Sub main()
    Set swApp = Application.SldWorks
     docName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\Simulation Examples\Nonlinear\nl_plate.sldprt"
     swApp.OpenDoc6 docName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings

     Set swAddin = swApp.GetAddInObject("SldWorks.Simulation")
     Set ssApp = swAddin.CosmosWorks
     Set ssModelDoc = ssApp.ActiveDoc
     Set ssStudyMgr = ssModelDoc.StudyManager
    studyCnt = ssStudyMgr.StudyCount
     For i = 0 To studyCnt - 1
         Set ssStudy = ssStudyMgr.GetStudy(i)
         studyName = ssStudy.Name
         Debug.Print ""
         Debug.Print "Study name: " & studyName
         studyType = ssStudy.AnalysisType
         If (studyType = swsAnalysisStudyTypeNonlinear) Then
             Set ssNonLinearStudyOptions = ssStudy.NonLinearStudyOptions
             Debug.Print "  Nonlinear study subtype as defined in swsNonlinearAnalysisSubType_e: " & ssStudy.NonlinearAnalysisSubType
             Debug.Print "    Solution properties:"
             Debug.Print "       Stepping options:"
             Debug.Print "          Start time: " & ssNonLinearStudyOptions.StartTime
             Debug.Print "          End time: " & ssNonLinearStudyOptions.EndTime
             Debug.Print "          Save data for restarting analysis? (1=yes, 0=no) " & ssNonLinearStudyOptions.SaveDataForRestartingAnalysis
             Debug.Print "          Solution-time increment: " & ssNonLinearStudyOptions.TimeIncrement
             Debug.Print "          Fixed-time increment: " & ssNonLinearStudyOptions.FixedTimeIncrement
             Debug.Print "       Geometry nonlinearity options:"
             Debug.Print "          Use large displacement formulation? (1=yes, 0=no) " & ssNonLinearStudyOptions.UseLargeDisplacement
             Debug.Print "          Update direction of load at every solution step with deflection? (1=yes, 0=no) " & ssNonLinearStudyOptions.UseUpdateLoadDirection
             Debug.Print "          Use large strain formulation? (1=yes, 0=no) " & ssNonLinearStudyOptions.UseLargeStrain
             Debug.Print "          Keep bolt pre-stress? (1=yes, 0=no) " & ssNonLinearStudyOptions.KeepBoltPreStress
             Debug.Print "       Solver type as defined in swsSolverType_e: " & ssNonLinearStudyOptions.SolverType
             Debug.Print "       Results folder path: " & ssNonLinearStudyOptions.ResultFolderPath

            Debug.Print "    Advanced properties:"
             Debug.Print "       Methods:"
             Debug.Print "          Control type as defined in swsNonLinearOptionControlMethodType_e: " & ssNonLinearStudyOptions.ControlMethodType
             Debug.Print "          Integration type as defined in swsNonLinearOptionIntegrationMethodType_e: " & ssNonLinearStudyOptions.IntegrationMethodType
             Debug.Print "          Iterative type as defined in swsNonLinearOptionIterativeMethodType_e: " & ssNonLinearStudyOptions.IterativeMethodType

             Debug.Print "       Displacement control options:"
             selEntityType = "Nothing"
             ssNonLinearStudyOptions.GetDisplacementControlOptions2 displacementComponent, unit, selectedEntity
             If Not selectedEntity Is Nothing Then
                 Set swEntity = selectedEntity
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
             Debug.Print "          Displacement component as defined in swsDisplacementComponent_e: " & displacementComponent
             Debug.Print "          Units as defined in swsLinearUnit_e: " & unit
             Debug.Print "          Selected reference entity type: " & selEntityType

            ssNonLinearStudyOptions.GetArcLengthCompletionOptions maxLoad, maxDisplacement, unit, maxArcSteps, arcLengthMultiplier
             Debug.Print "       Arc-Length completion options:"
             Debug.Print "          Maximum load-pattern multiplier: " & maxLoad
             Debug.Print "          Maximum displacement: " & maxDisplacement
             Debug.Print "          Units as defined in swsLinearUnit_e: " & unit
             Debug.Print "          Maximum number of arc steps: " & maxArcSteps
             Debug.Print "          Initial arc length multiplier: " & arcLengthMultiplier
             Debug.Print "       Step/Tolerance options:"
             ssNonLinearStudyOptions.GetStepToleranceOptions frequency, maximum, convergence, tolerance, factor
             Debug.Print "          Tolerance: "
             Debug.Print "              Frequency of performing equilibrium in number of solution steps: " & frequency
             Debug.Print "              Maximum number of equilibrium iterations for any solution step: " & maximum
             Debug.Print "              Relative displacement tolerance used for equilibrium convergence: " & convergence
             Debug.Print "              Tolerance for strain increment for models with creep or plasticity: " & tolerance
             Debug.Print "              Stiffness singularity elimination factor: " & factor
             Dim status As Long
             status = ssNonLinearStudyOptions.SetStepToleranceOptions(-1, 10, 0.002, 0.02, 1)
             ssNonLinearStudyOptions.GetStepToleranceOptions frequency, maximum, convergence, tolerance, factor
             Debug.Print "          New Tolerance: "
             Debug.Print "              Frequency of performing equilibrium in number of solution steps: " & frequency
             Debug.Print "              Maximum number of equilibrium iterations for any solution step: " & maximum
             Debug.Print "              Relative displacement tolerance used for equilibrium convergence: " & convergence
             Debug.Print "              Tolerance for strain increment for models with creep or plasticity: " & tolerance
             Debug.Print "              Stiffness singularity elimination factor: " & factor
            Debug.Print "    Flow/Thermal Effects:"
             Debug.Print "       Thermal options:"
             Debug.Print "          Temperature source as defined in swsThermalOption_e: " & ssNonLinearStudyOptions.ThermalResults
             Debug.Print "          Temperature source:"
             If ssNonLinearStudyOptions.ThermalResults = 1 Then
                 Debug.Print "          Thermal study: " & ssNonLinearStudyOptions.ThermalStudyName
                 Debug.Print "          Use temperature from thermal study at each nonlinear time step? (1=yes, 0=no): " & ssNonLinearStudyOptions.CheckUseTempFromThermalStudy
                 If ssNonLinearStudyOptions.CheckUseTempFromThermalStudy = 0 Then
                     Debug.Print "             Time step of transient thermal study whose temperature to use: " & ssNonLinearStudyOptions.TimeStep
                 End If
             ElseIf ssNonLinearStudyOptions.ThermalResults = 2 Then
                 Debug.Print "               SOLIDWORKS Flow Simulation results file: " & ssNonLinearStudyOptions.FlowTemperatureFile
             Else
                 Debug.Print "               The current model"
             End If

            Debug.Print "       Fluid pressure option:"
             Debug.Print "          Import fluid pressure loads from SOLIDWORKS Flow Simulation? (1=yes, 0=no): " & ssNonLinearStudyOptions.CheckFlowPressure
             If ssNonLinearStudyOptions.CheckFlowPressure = 1 Then
                  Debug.Print "           SOLIDWORKS Flow Simulation results file: " & ssNonLinearStudyOptions.FlowPressureFile
                  Debug.Print "           Use reference pressure offset from Flow Simulation? (1=yes, 0=no): " & ssNonLinearStudyOptions.ReferencePressureOption
                  If ssNonLinearStudyOptions.ReferencePressureOption = 0 Then
                      Debug.Print "             Reference pressure offset: " & ssNonLinearStudyOptions.DefinedReferencePressure
                  End If
                  Debug.Print "          Run as legacy study and import only the normal component of the pressure load? (1=yes, 0=no): " & ssNonLinearStudyOptions.CheckRunAsLegacy
             End If
          End If
         Next
End Sub
```
