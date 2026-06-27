---
title: "Create Base Flange Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Base_Flange_Feature_Example_VBNET.htm"
---

# Create Base Flange Feature Example (VB.NET)

This example shows how to create a base flange feature.

```vb
  '===========================================================
 'Preconditions:
 '1. Ensure the specified part template exists.
 '2. Open the Immediate window.
 '
 'Postconditions:
 '1. Creates a flange profile sketch.
 '2. Creates  Base-Flange1 in the FeatureManager design tree.
 '3. Inspect the Immediate window, graphics area,
 '   and FeatureManager design tree.
  '==================================================
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial   Class   SolidWorksMacro

       Dim Part  As  ModelDoc2
       Dim swPart  As  PartDoc
       Dim swModel  As  ModelDoc2
       Dim swSKFeat  As  Feature
       Dim skSegment  As   SketchSegment
       Dim swBaseFlangeFeat  As   BaseFlangeFeatureData
       Dim baseFlangeFeatData  As   BaseFlangeFeatureData
       Dim cba  As  CustomBendAllowance
       Dim var()  As  Object
       Dim parent  As  Feature
       Dim SHFeat  As  Feature
       Dim smFeatData  As   SheetMetalFeatureData
       Dim cba1  As  CustomBendAllowance
       Dim boolstatus  As   Boolean
       Dim longstatus  As   Long, longwarnings  As   Long

       Sub main()

           Part = swApp.ActiveDoc

            Dim swSheetWidth  As   Double
           swSheetWidth = 0
            Dim swSheetHeight  As   Double
           swSheetHeight = 0

           Part = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2022\templates\Part.prtdot", 0, swSheetWidth, swSheetHeight)
           swPart = Part
           swModel = swApp.ActiveDoc

           boolstatus = Part.Extension.SelectByID2("Top",  "PLANE", -0.0598881514598713, 0.0393749830258702, 0.00485137895479469,   False, 0,   Nothing, 0)
           Part.SketchManager.InsertSketch(True)
           Part.ClearSelection2(True)

           skSegment = Part.SketchManager.CreateLine(-0.140779, 0.050824, 0#, -0.106481, -0.06735, 0#)
           skSegment = Part.SketchManager.CreateLine(-0.106481, -0.06735, 0#, 0.084966, -0.049265, 0#)
           skSegment = Part.SketchManager.CreateLine(0.084966, -0.049265, 0#, 0.143274, 0.063608, 0#)
           Part.ClearSelection2(True)
           Part.SketchManager.InsertSketch(True)

           swSKFeat = swModel.SelectionManager.GetSelectedObject6(1, -1)
            Debug.Print("Flange profile name : " & swSKFeat.Name   " and type : " & swSKFeat.GetTypeName2)

           swBaseFlangeFeat = swModel.FeatureManager.CreateDefinition(swFeatureNameID_e.swFmBaseFlange)

           cba = swBaseFlangeFeat.GetCustomBendAllowance()

           cba.Type =   swBendAllowanceTypes_e.swBendAllowanceDirect
           cba.BendAllowance = 0.05

           swBaseFlangeFeat.D1EndConditionType = 1
           swBaseFlangeFeat.D1EndConditionDistance = 0.02
           swBaseFlangeFeat.ReverseDirection =   True
           swBaseFlangeFeat.OffsetDirections = 2
           swBaseFlangeFeat.D2EndConditionType = 1
           swBaseFlangeFeat.D2EndConditionDistance = 0.05
           swBaseFlangeFeat.OverrideDefaultSheetMetalParameters =   True
           swBaseFlangeFeat.Thickness = 0.035

            'Initialize the base flange feature
            'Initialize(
             'UseMaterialSheetMetalParameters=False,
            'UseDefaultBendAllowance=False,
            'CustomBendAllowance,
            'UseDefaultBendRelief=False,
             'ReliefType=swSheetMetalReliefTypes_e.swSheetMetalReliefRectangular,
            'UseReliefRatio=True,
            'ReliefRatio=0.8m,
            'ReliefWidth,
            'ReliefDepth)

            Call swBaseFlangeFeat.Initialize(False,   False, cba,   False,   swSheetMetalReliefTypes_e.swSheetMetalReliefRectangular,   True, 0.8, 0#, 0#)

           SHFeat = swModel.FeatureManager.CreateFeature(swBaseFlangeFeat)

           baseFlangeFeatData = SHFeat.GetDefinition()

            Debug.Print("Use material sheet metal parameters? " & baseFlangeFeatData.UseMaterialSheetMetalParameters)
            Debug.Print("Use default bend allowance? " & baseFlangeFeatData.UseDefaultBendAllowance)
            Debug.Print("Use default bend relief? " & baseFlangeFeatData.UseDefaultBendRelief)
          Debug.Print("Use relief ratio? " & baseFlangeFeatData.UseReliefRatio)
            Debug.Print("Relief type as defined by swSheetMetalReliefTypes_e: " & baseFlangeFeatData.ReliefType)
            Debug.Print("Relief width: " & baseFlangeFeatData.ReliefWidth)
          Debug.Print("Relief depth: " & baseFlangeFeatData.ReliefDepth)
            Debug.Print("Relief ratio: " & baseFlangeFeatData.ReliefRatio)

            'Modify the relief ratio and override default AutoRelief in the parent sheet metal feature
           var = SHFeat.GetParents()
           parent = var(1)
            Debug.Print("Parent type: " & parent.GetTypeName2())

           smFeatData = parent.GetDefinition()

           cba1 = smFeatData.GetCustomBendAllowance()

            Debug.Print("Custom bend allowance type as defined in swBendAllowanceTypes_e: " & cba1.Type)
            Debug.Print("Bend allowance: " & cba1.BendAllowance)
            Debug.Print("Result code for override of AutoRelief as defined by swSheetMetalModifierError_e: " & smFeatData.SetOverrideDefaultParameter2(swSheetMetalOverrideDefaultParameters_e.swSheetMetalOverrideDefaultParameters_AutoRelief,   True))
           smFeatData.ReliefRatio = 0.7

            Debug.Print("Base flange successfully modified? " & parent.ModifyDefinition(smFeatData, swModel,  Nothing))
            Debug.Print("Base flange feature name : " & SHFeat.Name    " and type : " & SHFeat.GetTypeName2)

       End  Sub

       '''  <summary>
       ''' The SldWorks swApp variable is pre-assigned for you.
       '''  </summary>
      Public swApp  As   SldWorks
 End  Class
```
