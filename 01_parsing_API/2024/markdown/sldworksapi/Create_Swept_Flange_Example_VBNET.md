---
title: "Create Swept Flange Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Swept_Flange_Example_VBNET.htm"
---

# Create Swept Flange Example (VB.NET)

This example shows how to create a swept flange on a sheet metal part.

'================================================================

```vb
 'Preconditions: Ensure that the specified part template exists.
```

'

```vb
 'Postconditions:
 '1. Base-Flange1 and Swept Flange1 are created.
 '2. Inspect the graphics area and the FeatureManager design tree.
  '================================================
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial   Class   SolidWorksMacro
       Public  Sub main()

           Dim swFeat  As  Feature
           Dim myFeature   As   Feature
           Dim swFeatMgr   As   FeatureManager
           Dim swFeatData   As   SweptFlangeFeatureData
           Dim customBendAllowanceData   As   CustomBendAllowance
           Dim swProfileSketch   As   Feature
           Dim skSegment   As   SketchSegment
           Dim Part  As  ModelDoc2
           Dim swPart  As  PartDoc
           Dim boolstatus   As   Boolean
           Dim longstatus   As   Integer
           Dim swSheetWidth   As   Double
          swSheetWidth = 0
           Dim swSheetHeight   As   Double
          swSheetHeight = 0
          Part = swApp.NewDocument("E:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\Tutorial\part.prtdot", 0, swSheetWidth, swSheetHeight)

          swPart = Part
          swApp.ActivateDoc2("Part1",   False, longstatus)
          Part = swApp.ActiveDoc

          Part.SketchManager.InsertSketch(True)
          boolstatus = Part.Extension.SelectByID2("Front",  "PLANE", -0.0350345417518034, 0.019677523162802, 0.00511863136830445,   False, 0,   Nothing, 0)
          Part.ClearSelection2(True)
          boolstatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity,   swUserPreferenceOption_e.swDetailingNoOptionSpecified,   False)
          boolstatus = Part.Extension.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType,   swUserPreferenceOption_e.swDetailingNoOptionSpecified,   True)
           Dim vSkLines  As  Object
          vSkLines = Part.SketchManager.CreateCornerRectangle(-0.0420403557341645, 0.0275066828701494, 0, 0.0475026757367474, -0.0220443628675665, 0)
          Part.ClearSelection2(True)

          Part.ShowNamedView2("*Trimetric", 8)
          Part.ViewZoomtofit2

          customBendAllowanceData = Part.FeatureManager.CreateCustomBendAllowance()
          customBendAllowanceData.KFactor = 0.5

          myFeature = Part.FeatureManager.InsertSheetMetalBaseFlange2(0.0007366,   False, 0.0007366, 0.02, 0.01,  False, 0, 0, 1, customBendAllowanceData,  False, 0, 0.0001, 0.0001, 0.5,  True,  False,  True,  True)

          Part.ClearSelection2(True)
          Part.SketchManager.InsertSketch(True)
          boolstatus = Part.Extension.SelectByID2("",  "FACE", 0.0441584745988735, 0.0275066828701256, -0.000252375262334681,   True, 0,   Nothing, 0)

          skSegment = Part.SketchManager.CreateLine(0.047503, 0#, 0#, 0.047503, -0.015713, 0#)
          Part.ClearSelection2(True)
          Part.SketchManager.InsertSketch(True)

          boolstatus = Part.Extension.SelectByID2("Sketch6",   "SKETCH", 0.0254585357375204, -0.00378791126417555, -0.013876316631307,   True, 0,   Nothing, 0)
          boolstatus = Part.Extension.SelectByRay(0.0472949686339916, 0.0133307046879168, 0.000207707102561017, -0.499999999999997, -0.707106781186554, -0.499999999999995, 0.000423592175091009, 1,  True, 0, 0)
          Part.ClearSelection2(True)

           'Select the sketch for the profile
          boolstatus = Part.Extension.SelectByID2("Sketch6",  "SKETCH", 0.0254585357375204, -0.00378791126417555, -0.013876316631307,   True, 0,   Nothing, 0)
          swProfileSketch = Part.SelectionManager.GetSelectedObject6(1, -1)
          Part.ClearSelection2(True)

           'Select an edge for the path
           Dim swPathObj(0)   As   Edge
          boolstatus = Part.Extension.SelectByRay(0.0472949686339916, 0.0133307046879168, 0.000207707102561017, -0.499999999999997, -0.707106781186554, -0.499999999999995, 0.000423592175091009, 1,  True, 0, 0)
          swPathObj(0) = Part.SelectionManager.GetSelectedObject6(1, -1)

          Part.ClearSelection2(True)

          swFeatMgr = Part.FeatureManager

          swFeatData = swFeatMgr.CreateDefinition(swFeatureNameID_e.swFmSweptFlange)
          swFeatData.EndOffset = 0
          swFeatData.FlangePosition =   swSweptFlangePositionTypes_e.swSweptFlangePositionType_MaterialInside
          swFeatData.FlattenAlongPath =   False
          swFeatData.OverrideDefaultSheetMetalParameters =   False
          swFeatData.Path = swPathObj
          swFeatData.Profile = swProfileSketch
          swFeatData.ReverseDirection =   False
          swFeatData.StartOffset = 0
          swFeatData.TrimSideBends =   False
          swFeatData.UseDefaultBendAllowance =   True
          swFeatData.UseDefaultBendRelief =   True
          swFeatData.UseDefaultRadius =   False
          swFeatData.UseGaugeTable =   False
          swFeatData.UseMaterialSheetMetalParameters =   False
          swFeat = swFeatMgr.CreateFeature(swFeatData)
          Part.ClearSelection2(True)

       End  Sub
       '''  <summary>
       ''' The SldWorks swApp variable is pre-assigned for you.
       '''  </summary>
       Public swApp  As  SldWorks
 End  Class
```
