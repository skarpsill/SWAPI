---
title: "Create Standard Mates Example (VBA"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Standard_Mates_Example_VB.htm"
---

# Create Standard Mates Example (VBA

## Create Standard Mates Example (VBA)

This example shows how to create a variety of standard mates.

'----------------------------------------------------------------------------
' Preconditions: Ensure the specified file paths exist.
'
' Postconditions: Inspect the Mates folder in the FeatureManager design tree.
'
' NOTE: Because the models are used elsewhere, do not save changes.
'----------------------------------------------------------------------------

```vb
Dim swApp As SldWorks.SldWorks
 Dim swAssembly As SldWorks.AssemblyDoc
 Dim AssemblyTitle As String
 Dim tmpObj As SldWorks.ModelDoc2
 Dim swInsertedComponent As SldWorks.Component2
 Dim errors As Long
 Dim Part As SldWorks.ModelDoc2
 Dim TransformData(15) As Double
 Dim TransformDataVariant As Variant
 Dim swMathUtil As Object
 Dim swTransform As Object
 Dim MateData As SldWorks.TangentMateFeatureData
 Dim EntitiesToMate(1) As Object
 Dim EntitiesToMateVar As Variant
 Dim MateFeature As Feature
 Dim PerpMateData As SldWorks.PerpendicularMateFeatureData
 Dim CoincMateData As SldWorks.CoincidentMateFeatureData
 Dim ParMateData As SldWorks.ParallelMateFeatureData
 Dim ConcMateData As SldWorks.ConcentricMateFeatureData
 Dim LMateData As SldWorks.LockMateFeatureData
 Dim boolstatus As Boolean
 Dim longstatus As Long, longwarnings As Long
Sub main()
    Set swApp = Application.SldWorks
     Set Part = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\assem20.sldasm", 2, 0, "", longstatus, longwarnings)

    Set swAssembly = Part
     swApp.ActivateDoc2 "assem20.sldasm", False, longstatus
     Set Part = swApp.ActiveDoc

    AssemblyTitle = Part.GetTitle

    Set tmpObj = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\shaft.sldprt", 1, 32, "", errors, longwarnings)
     Set Part = swApp.ActivateDoc3(AssemblyTitle, True, 0, errors)

    Set swInsertedComponent = Part.AddComponent5("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\shaft.sldprt", 0, "", False, "", 0.29642267129384, 9.20506109250709E-02, -0.187506963149644)
     swApp.CloseDoc "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2019\samples\tutorial\api\shaft.sldprt"

    TransformData(0) = 1
     TransformData(1) = 0
     TransformData(2) = 0
     TransformData(3) = 0
     TransformData(4) = 1
     TransformData(5) = 0
     TransformData(6) = 0
     TransformData(7) = 0
     TransformData(8) = 1
     TransformData(9) = 0.29642267129384
     TransformData(10) = 4.20506109250709E-02
     TransformData(11) = -0.187506963149644
     TransformData(12) = 1
     TransformData(13) = 0
     TransformData(14) = 0
     TransformData(15) = 0

    TransformDataVariant = TransformData

    Set swMathUtil = swApp.GetMathUtility()

    Set swTransform = swMathUtil.CreateTransform((TransformDataVariant))
     boolstatus = swInsertedComponent.SetTransformAndSolve2(swTransform)

    boolstatus = Part.Extension.SelectByRay(4.43527596829085E-02, 2.97941775455115E-02, 2.19712535516692E-03, -0.400036026779312, -0.515038074910024, -0.758094294050284, 2.99151229353486E-03, 2, True, 1, 0)
     boolstatus = Part.Extension.SelectByRay(0.130082347379926, 5.12737883206569E-02, -2.38688162796734E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 2.99151229353486E-03, 2, True, 1, 0)

    ' Create TangentMateFeatureData
     Set MateData = Part.CreateMateData(4)

    ' Set the Entities To Mate
     Set EntitiesToMate(0) = Part.SelectionManager.GetSelectedObject6(1, -1)
     Set EntitiesToMate(1) = Part.SelectionManager.GetSelectedObject6(2, -1)

    EntitiesToMateVar = EntitiesToMate
     MateData.EntitiesToMate = (EntitiesToMateVar)

    ' Set the Mate Alignment
     MateData.MateAlignment = 1

    ' Create the mate
     Set MateFeature = Part.CreateMate(MateData)
     Part.ClearSelection2 True
     Part.EditRebuild3

    boolstatus = Part.Extension.SelectByRay(-2.47922125254263E-03, 0.028363044378807, 0.043532545142341, -0.400036026779312, -0.515038074910024, -0.758094294050284, 2.99151229353486E-03, 2, True, 1, 0)
     boolstatus = Part.Extension.SelectByRay(0.114306836013213, 7.19973430751679E-02, -5.18791456821077E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 2.99151229353486E-03, 2, True, 1, 0)

    ' Create PerpendicularMateFeatureData
     Set PerpMateData = Part.CreateMateData(2)

    ' Set the Entities To Mate
     Set EntitiesToMate(0) = Part.SelectionManager.GetSelectedObject6(1, -1)
     Set EntitiesToMate(1) = Part.SelectionManager.GetSelectedObject6(2, -1)
     EntitiesToMateVar = EntitiesToMate
     PerpMateData.EntitiesToMate = (EntitiesToMateVar)

    ' Create the mate
     Set MateFeature = Part.CreateMate(PerpMateData)
     Part.ClearSelection2 True
     Part.EditRebuild3

    boolstatus = Part.Extension.SelectByRay(-1.30850967460105E-02, 5.40093074191645E-02, 8.10230676393076E-04, -0.400036026779312, -0.515038074910024, -0.758094294050284, 2.99151229353486E-03, 2, True, 1, 0)
     boolstatus = Part.Extension.SelectByRay(0.107909556750883, 7.19973430752248E-02, -6.58876969148992E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 2.99151229353486E-03, 2, True, 1, 0)

    ' Create CoincidentMateFeatureData
     Set CoincMateData = Part.CreateMateData(0)

    ' Set the Entities To Mate
     Set EntitiesToMate(0) = Part.SelectionManager.GetSelectedObject6(1, -1)
     Set EntitiesToMate(1) = Part.SelectionManager.GetSelectedObject6(2, -1)
     EntitiesToMateVar = EntitiesToMate
     CoincMateData.EntitiesToMate = (EntitiesToMateVar)

    ' Set the Mate Alignment
     CoincMateData.MateAlignment = 0

    ' Create the mate
     Set MateFeature = Part.CreateMate(CoincMateData)
     Part.ClearSelection2 True
     Part.EditRebuild3

    boolstatus = Part.Extension.SelectByRay(-2.65813760897231E-02, 5.40093074191077E-02, -1.91102240282248E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 2.99151229353486E-03, 2, True, 1, 0)
     boolstatus = Part.Extension.SelectByRay(0.104493667114582, 5.40093074190509E-02, -0.053508121263917, -0.400036026779312, -0.515038074910024, -0.758094294050284, 2.99151229353486E-03, 2, True, 1, 0)

    ' Create ParallelMateFeatureData
     Set ParMateData = Part.CreateMateData(3)

    ' Set the Entities To Mate
     Set EntitiesToMate(0) = Part.SelectionManager.GetSelectedObject6(1, -1)
     Set EntitiesToMate(1) = Part.SelectionManager.GetSelectedObject6(2, -1)
     EntitiesToMateVar = EntitiesToMate
     ParMateData.EntitiesToMate = (EntitiesToMateVar)

    ' Set the Mate Alignment
     ParMateData.MateAlignment = 0

    ' Create the mate
     Set MateFeature = Part.CreateMate(ParMateData)
     Part.ClearSelection2 True
     Part.EditRebuild3

    boolstatus = Part.Extension.SelectByRay(0.153629139956536, 2.67016961580566E-02, -2.07225117635517E-02, -0.400036026779312, -0.515038074910024, -0.758094294050284, 2.99151229353486E-03, 2, True, 1, 0)
     boolstatus = Part.Extension.SelectByRay(0.31258643852118, 7.71807121026882E-02, -0.175728481540773, -0.400036026779312, -0.515038074910024, -0.758094294050284, 2.99151229353486E-03, 2, True, 1, 0)

    ' Create ConcentricMateFeatureData
     Set ConcMateData = Part.CreateMateData(1)

    ' Set the Entities To Mate
     Set EntitiesToMate(0) = Part.SelectionManager.GetSelectedObject6(1, -1)
     Set EntitiesToMate(1) = Part.SelectionManager.GetSelectedObject6(2, -1)
     EntitiesToMateVar = EntitiesToMate
     ConcMateData.EntitiesToMate = (EntitiesToMateVar)

    ' Set the Mate Alignment
     ConcMateData.MateAlignment = 1

    ' Set the Lock Rotation
     ConcMateData.LockRotation = False

    ' Create the mate
     Set MateFeature = Part.CreateMate(ConcMateData)
     Part.ClearSelection2 True
     Part.EditRebuild3

    boolstatus = Part.Extension.SelectByID2("cylinder20-1@assem20", "COMPONENT", 0.136504049029156, 0.042017793613752, -6.04340129007142E-03, True, 1, Nothing, 0)
     boolstatus = Part.Extension.SelectByID2("shaft-1@assem20", "COMPONENT", 0.116970722742224, 0.072421443211681, -5.24867796554531E-02, True, 1, Nothing, 0)

    ' Create LockMateFeatureData
     Set LMateData = Part.CreateMateData(16)

    ' Set the Entities To Mate
     Set EntitiesToMate(0) = Part.SelectionManager.GetSelectedObject6(1, -1)
     Set EntitiesToMate(1) = Part.SelectionManager.GetSelectedObject6(2, -1)
     EntitiesToMateVar = EntitiesToMate
     LMateData.EntitiesToMate = (EntitiesToMateVar)

    ' Create the mate
     Set MateFeature = Part.CreateMate(LMateData)
     Part.ClearSelection2 True
     Part.EditRebuild3
End Sub
```
