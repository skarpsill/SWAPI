---
title: "Create Belt/Chain Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Belt_Chain_Feature_Example_VBNET.htm"
---

# Create Belt/Chain Feature Example (VB.NET)

This example shows how to create a Belt/Chain assembly feature.

```vb
  '=====================================================================
  'Preconditions: Ensure the specified assembly template and part exist.
  '
  'Postconditions:
  '1. Creates an assembly of two steel discs.
  '2. Press F5 to create Belt1 in the FeatureManager design tree.
  '   If a Save As dialog appears, click Cancel.
  '3. Modifies Belt1's belt length, belt thickness,
  '   and pulley diameters. If a Save As dialog appears, click Cancel.
  '============================================================
  Imports SolidWorks.Interop.sldworks
  Imports SolidWorks.Interop.swconst
  Imports System.Runtime.InteropServices
  Imports System

  Partial   Class   SolidWorksMacro

        Function ObjectArrayToDispatchWrapperArray(ByVal Objects   As   Object())   As   DispatchWrapper()
            Dim ArraySize   As   Integer
          ArraySize = Objects.GetUpperBound(0)
            Dim d(ArraySize)   As   DispatchWrapper
            Dim ArrayIndex   As   Integer
            For ArrayIndex = 0   To ArraySize
              d(ArrayIndex) =   New   DispatchWrapper(Objects(ArrayIndex))
            Next
            Return d
        End   Function

        Sub main()

            Dim swModel   As   ModelDoc2
            Dim selMgr   As   SelectionMgr
            Dim beltChainFeatData   As   BeltChainFeatureData
            Dim pulleyComps(1)   As   Object
            Dim pulleyDiams(1)   As   Double
            Dim pullyFlips(1)   As   Boolean
            Dim pulleyDiamsOri(1)   As   Double
            Dim swFeat   As   Feature
            Dim swFeatData   As   BeltChainFeatureData
            Dim I   As   Integer
            Dim J   As   Integer
            Dim boolstatus   As   Boolean
            Dim longwarnings   As   Integer

            Dim swSheetWidth   As   Double
          swSheetWidth = 0
            Dim swSheetHeight   As   Double
          swSheetHeight = 0
          swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2022\templates\Assembly.asmdot", 0, swSheetWidth, swSheetHeight)
            Dim swAssembly   As   AssemblyDoc
          swAssembly = swModel

            ' Insert steel disc component

            Dim AssemblyTitle   As   String
          AssemblyTitle = swModel.GetTitle
            Dim tmpObj   As   ModelDoc2
            Dim errors   As   Long
          tmpObj = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\AdvancedMates\steel disc.sldprt", 1, 1,   "", errors, longwarnings)
          swModel = swApp.ActivateDoc3(AssemblyTitle,   True, 0, errors)
            Dim swInsertedComponent   As   Component2
          swInsertedComponent = swModel.AddComponent5("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\AdvancedMates\steel disc.sldprt", 0,   "",   False,   "", 0.00404421078452853, 0.00404421078422676, 0.0122628871084471)
          swApp.CloseDoc("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\AdvancedMates\steel disc.sldprt")

            ' Insert steel disc component

          AssemblyTitle = swModel.GetTitle
          tmpObj = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\AdvancedMates\steel disc.sldprt", 1, 1,   "", errors, longwarnings)
          swModel = swApp.ActivateDoc3(AssemblyTitle,   True, 0, errors)
          swInsertedComponent = swModel.AddComponent5("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\AdvancedMates\steel disc.sldprt", 0,   "",   False,   "", 0.0200044210784528, 0.0200044210784227, 0.0122628871084471)
          swApp.CloseDoc("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\AdvancedMates\steel disc.sldprt")

            ' Float the components

          boolstatus = swModel.Extension.SelectByID2("steel disc-1",   "COMPONENT", 0, 0, 0,   False, 0,   Nothing, 0)
          swModel.UnfixComponent
          swModel.ClearSelection2(True)
          boolstatus = swModel.Extension.SelectByID2("steel disc-2",   "COMPONENT", 0, 0, 0,   False, 0,   Nothing, 0)
          swModel.UnfixComponent
          swModel.ClearSelection2(True)

            ' Move one disc

          boolstatus = swModel.Extension.SelectByID2("steel disc-2@Assem14",   "COMPONENT", 0, 0, 0,   False, 0,   Nothing, 0)
          boolstatus = swModel.Extension.SelectByID2("Unknown",   "MANIPULATOR", 0.0340009836225566, -0.00352899570186584, -0.0115173288530189,   False, 0,   Nothing, 0)
          swModel.ClearSelection2(True)
          boolstatus = swModel.Extension.SelectByID2("steel disc-2@Assem14",   "COMPONENT", 0, 0, 0,   False, 0,   Nothing, 0)
            Dim TransformData(15)   As   Double
          TransformData(0) = 1
          TransformData(1) = 0
          TransformData(2) = 0
          TransformData(3) = 0
          TransformData(4) = 1
          TransformData(5) = 0
          TransformData(6) = 0
          TransformData(7) = 0
          TransformData(8) = 1
          TransformData(9) = 0.0664528131333411
          TransformData(10) = 0.0046349356621274
          TransformData(11) = 0.00919716533133533
          TransformData(12) = 1
          TransformData(13) = 0
          TransformData(14) = 0
          TransformData(15) = 0
            Dim TransformDataVariant   As   Object
          TransformDataVariant = TransformData
            Dim swMathUtil   As   Object
          swMathUtil = swApp.GetMathUtility()
            Dim swTransForm   As   Object
          swTransForm = swMathUtil.CreateTransform((TransformDataVariant))
            Dim swComp   As   Object
          swComp = swModel.SelectionManager.GetSelectedObjectsComponent4(1, -1)
          boolstatus = swComp.SetTransformAndSolve2(swTransForm)
          boolstatus = swModel.ForceRebuild3(False)
          swModel.ClearSelection2(True)

            ' Select the pulley faces

          boolstatus = swModel.Extension.SelectByRay(0.0130157615084272, 0.00990176398499898, 0.0121640119419908, -0.333333333266778, -0.333333333254022, -0.881917103743329, 0.000973554376657825, 2,   False, 0, 0)
          boolstatus = swModel.Extension.SelectByRay(0.0769710902559098, 0.00667589089525222, 0.0112969076145077, -0.333333333266778, -0.333333333254022, -0.881917103743329, 0.000973554376657825, 2,   False, 0, 0)

          selMgr = swModel.SelectionManager

            For I = 0   To UBound(pulleyComps)
              pulleyComps(I) = selMgr.GetSelectedObject6(I + 1, -1)
            Next

            ' Create Belt/Chain feature

          beltChainFeatData = swModel.FeatureManager.CreateDefinition(swFeatureNameID_e.swFmBeltAndChain)

            For J = 0   To UBound(pulleyComps)
              pulleyDiams(J) = 0.005 * (J + 2)
            Next

            Dim dArray()   As   DispatchWrapper

          dArray = ObjectArrayToDispatchWrapperArray(pulleyComps)

          beltChainFeatData.PulleyComponents = dArray
          beltChainFeatData.PulleyDiameters = pulleyDiams

          pullyFlips(0) =   False
          pullyFlips(1) =   False

          beltChainFeatData.FlipSides = pullyFlips

          beltChainFeatData.BeltLocationPlane = selMgr.GetSelectedObject6(3, -1)

          beltChainFeatData.DrivingLength =   True
          beltChainFeatData.BeltLength = 0.59492

          beltChainFeatData.UseBeltThickness =   True
          beltChainFeatData.BeltThickness = 0.003

          beltChainFeatData.CreateBeltPart =   True
          beltChainFeatData.EngageBelt =   False

            Stop

          swFeat = (swModel.FeatureManager).CreateFeature(beltChainFeatData)

          swFeatData = swFeat.GetDefinition()

            ' Modify Belt/Chain feature

          boolstatus = swFeatData.AccessSelections(swModel,   Nothing)

          pulleyDiamsOri = swFeatData.PulleyDiameters
          pulleyDiamsOri(0) = 0.02
          pulleyDiamsOri(1) = 0.02

          swFeatData.PulleyDiameters = pulleyDiamsOri
            Debug.Print("Pulley diameters changed to 20 mm")

          swFeatData.DrivingLength =   True
          swFeatData.BeltLength = 0.3
            Debug.Print("Belt length (m) changed to " & swFeatData.BeltLength)

          swFeatData.BeltThickness = 0.002
            Debug.Print("Belt thickness (m) changed to " & swFeatData.BeltThickness)

          boolstatus = swFeat.ModifyDefinition(swFeatData, swModel,   Nothing)

        End   Sub

        '''   <summary>
        ''' The SldWorks swApp variable is pre-assigned for you.
        '''   </summary>
        Public swApp   As   SldWorks
  End   Class
```
