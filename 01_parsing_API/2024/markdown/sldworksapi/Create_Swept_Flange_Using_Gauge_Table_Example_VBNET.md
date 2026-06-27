---
title: "Create Swept Flange using Gauge Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Swept_Flange_Using_Gauge_Table_Example_VBNET.htm"
---

# Create Swept Flange using Gauge Table Example (VB.NET)

This example shows how to create a swept flange using a bend table on a non-sheet metal part.

```vb
  '====================================================================================
 'Preconditions:
 '1. Ensure that the paths to templates and gauge tables are valid.
 '2. Open an Immediate window.
 '3. Press F5 repeatedly and inspect the Immediate window and FeatureManager design tree as instructed.
 '
 'Postconditions:
 '1. Creates Sketch1 for the sweep path.
 '2. Creates Sketch2 for the sweep profile.
 '3. Creates Swept Flange1 using a gauge table installed with SOLIDWORKS.
 '4. Displays gauge table parameters.
 '5. Modifies Swept Flange1 to override the gauge number, bend radius, and gauge thickness.
 '6. Displays new gauge parameters.
  '============================================
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial   Class   SolidWorksMacro
       Public  Sub main()

           Dim swPart  As  PartDoc
           Dim swModel  As  ModelDoc2
           Dim swFeat  As  Feature
           Dim swFeatMgr   As   FeatureManager
           Dim swSweptFlangeFeatureData   As   SweptFlangeFeatureData
           Dim featData  As  SweptFlangeFeatureData
           Dim smGaugeTableParam   As   SheetMetalGaugeTableParameters
           Dim skSegment   As   SketchSegment
           Dim myRefPlane   As   RefPlane
           Dim swFeatNameID   As   Integer
           Dim swSketch(0)   As   Feature
           Dim boolstatus   As   Boolean
           Dim errCode  As  Integer
           Dim swSheetWidth   As   Double
           Dim swSheetHeight   As   Double
           Dim gaugePath   As   String =   Nothing
           Dim gaugeCount   As   Integer
           Dim gaugeNumbers   As   Object
           Dim i  As  Integer
           Dim radiiCount   As   Integer
           Dim radii  As  Object
           Dim newgaugePath   As   String =   Nothing

          swSheetWidth = 0
          swSheetHeight = 0
          swModel = swApp.NewDocument("E:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\Tutorial\part.prtdot", 0, swSheetWidth, swSheetHeight)

          swPart = swModel
          swModel = swApp.ActiveDoc

          skSegment = swModel.SketchManager.Create3PointArc(-0.058601, -0.015313, 0#, -0.003828, -0.021603, 0#, 0.002265, -0.05642, 0#)
          swModel.ClearSelection2(True)
          swModel.SketchManager.InsertSketch(True)   'Sketch1
          swModel.ClearSelection2(True)

          boolstatus = swModel.Extension.SelectByID2("Point2@Sketch1",   "EXTSKETCHPOINT", -0.003828, -0.021603, 0,  True, 0,  Nothing, 0)
          boolstatus = swModel.Extension.SelectByID2("Arc1@Sketch1",   "EXTSKETCHSEGMENT", 0.00285760095397308, -0.0342380271903227, 0,  True, 1,   Nothing, 0)

          myRefPlane = swModel.FeatureManager.InsertRefPlane(4, 0, 2, 0, 0, 0)

          boolstatus = swModel.Extension.SelectByID2("Plane1",  "PLANE", 0.0103901931573406, -0.00917038599747196, -0.00622490227027586,   True, 0,   Nothing, 0)

          swModel.SketchManager.InsertSketch(True)
          skSegment = swModel.SketchManager.CreateLine(0#, 0#, 0#, 0#, 0.018316, 0#)
          skSegment = swModel.SketchManager.CreateLine(0#, 0.018316, 0#, 0.008362, 0.035435, 0#)
          swModel.ClearSelection2(True)
          swModel.SketchManager.InsertSketch(True)   'Sketch2

          swFeatNameID =   swFeatureNameID_e.swFmSweptFlange
          swFeatMgr = swModel.FeatureManager
          swSweptFlangeFeatureData = swFeatMgr.CreateDefinition(swFeatNameID)

          swModel.ClearSelection2(True)

           'Select the sweep path
          boolstatus = swModel.Extension.SelectByID2("Sketch1",  "SKETCH", 0, 0, 0,   False, 0,   Nothing, 0)
          swSketch(0) = swModel.SelectionManager.GetSelectedObject6(1, -1)

          swSweptFlangeFeatureData.Path = swSketch

           'Select the sweep profile
          boolstatus = swModel.Extension.SelectByID2("Sketch2",  "SKETCH", 0, 0, 0,   False, 0,   Nothing, 0)
          swSweptFlangeFeatureData.Profile = swModel.SelectionManager.GetSelectedObject6(1, -1)

          errCode = swSweptFlangeFeatureData.GetErrorCodes
           Debug.Print("Swept flange definition error code: " +  CStr(errCode))

           Stop  'Inspect the Immediate window for the swept flange definition error

          swSweptFlangeFeatureData.UseMaterialSheetMetalParameters =   False
          swSweptFlangeFeatureData.UseGaugeTable =   True

           Debug.Print("Use gauge table? " +  CStr(swSweptFlangeFeatureData.UseGaugeTable))

          smGaugeTableParam = swSweptFlangeFeatureData.GetGaugeTableParameters
          boolstatus = smGaugeTableParam.GetGaugeTablePath(gaugePath)

           If boolstatus =   False   Then
              smGaugeTableParam.SetGaugeTablePath("E:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\LANG\ENGLISH\SHEET METAL GAUGE TABLES\BEND ALLOWANCE MM SAMPLE.XLS")
           End  If

          boolstatus = smGaugeTableParam.GetGaugeTablePath(gaugePath)
           Debug.Print("Got gauge table path? " +  CStr(boolstatus))
           Debug.Print("Gauge table path: " + gaugePath)
           Debug.Print("Process: " + smGaugeTableParam.Process)

          gaugeCount = smGaugeTableParam.GetGaugeNumberCount()
           Debug.Print("Gauge number count: " +  CStr(gaugeCount))

           Debug.Print("Available gauge numbers: ")

          gaugeNumbers = smGaugeTableParam.GetAvailableGaugeNumbers()

           For i = 0  To gaugeCount - 1
               Debug.Print(gaugeNumbers(i))
           Next
           Debug.Print("Current gauge number: " + smGaugeTableParam.GetCurrentGaugeNumber())

           Stop  'Inspect the Immediate window for the current gauge number

          radiiCount = smGaugeTableParam.GetRadiiCount()
           Debug.Print("Bend radii count: " +  CStr(smGaugeTableParam.GetRadiiCount()))

           Debug.Print("Available bend radii: ")
          radii = smGaugeTableParam.GetAvailableRadii()
           For i = 0  To radiiCount - 1
               Debug.Print(radii(i))
           Next
           Debug.Print("Current bend radius: " +  CStr(smGaugeTableParam.GetCurrentRadius))
           Debug.Print("Thickness: " +  CStr(smGaugeTableParam.GetThickness))
           Debug.Print("Override thickness? " +  CStr(smGaugeTableParam.OverrideThickness))
           Debug.Print("Override bend radius? " +  CStr(smGaugeTableParam.OverrideRadius))
           Debug.Print("Reverse direction? " +  CStr(smGaugeTableParam.ReverseDirection))

           Stop  'Inspect the Immediate window for current bend radius and current gauge thickness

          swSweptFlangeFeatureData.SetGaugeTableParameters(smGaugeTableParam)

          swFeat = swFeatMgr.CreateFeature(swSweptFlangeFeatureData)

          errCode = swSweptFlangeFeatureData.GetErrorCodes()
           Debug.Print("Swept flange creation error code: " +  CStr(errCode))
          swModel.ClearSelection2(True)

           Stop  'Inspect the Immediate window for the swept flange creation status
           'Observe Sheet-Metal, Swept Flange1, and Flat-Pattern in the FeatureManager design tree

           'Set new gauge number and override gauge thickness and bend radius
          featData = swFeat.GetDefinition()
          smGaugeTableParam = featData.GetGaugeTableParameters

          smGaugeTableParam.ReverseDirection =   True
          smGaugeTableParam.SetCurrentGaugeNumber("Gauge 3")
          smGaugeTableParam.SetThickness(0.006,   True)
          smGaugeTableParam.SetRadius(0.006,   True)

          featData.SetGaugeTableParameters(smGaugeTableParam)
          boolstatus = swFeat.ModifyDefinition(featData, swModel,  Nothing)
           Debug.Print("Swept flange modification status: " +  CStr(boolstatus))

           Stop  'Inspect the Immediate window for the swept flange modification status

           'Get new gauge number
          boolstatus = featData.AccessSelections(swModel,  Nothing)
          smGaugeTableParam = featData.GetGaugeTableParameters

          boolstatus = smGaugeTableParam.GetGaugeTablePath(newgaugePath)
           Debug.Print("Got gauge table path? " +  CStr(boolstatus))
           Debug.Print("Gauge table path: " + newgaugePath)

           Debug.Print("Process: " + smGaugeTableParam.Process)

          gaugeCount = smGaugeTableParam.GetGaugeNumberCount()
           Debug.Print("Gauge number count: " +  CStr(gaugeCount))
           Debug.Print("Available gauge numbers: ")
          gaugeNumbers = smGaugeTableParam.GetAvailableGaugeNumbers()

           For i = 0  To gaugeCount - 1
               Debug.Print(gaugeNumbers(i))
           Next
           Debug.Print("Current gauge number: " + smGaugeTableParam.GetCurrentGaugeNumber())

          Stop   'Inspect the Immediate window for the new gauge number

           'Get new bend radius and gauge thickness
          radiiCount = smGaugeTableParam.GetRadiiCount()
           Debug.Print("Bend radii count: " +  CStr(radiiCount))

           Debug.Print("Available bend radii: ")
          radii = smGaugeTableParam.GetAvailableRadii()
           For i = 0  To radiiCount - 1
               Debug.Print(radii(i))
           Next
           Debug.Print("Current bend radius: " +  CStr(smGaugeTableParam.GetCurrentRadius))

           Debug.Print("Thickness: " +  CStr(smGaugeTableParam.GetThickness))
           Debug.Print("Override thickness? " +  CStr(smGaugeTableParam.OverrideThickness))
           Debug.Print("Override bend radius? " +  CStr(smGaugeTableParam.OverrideRadius))
           Debug.Print("Reverse direction? " +  CStr(smGaugeTableParam.ReverseDirection))

          featData.ReleaseSelectionAccess

           Stop  'Inspect the Immediate window for the new bend radius and gauge thickness

       End  Sub
       '''  <summary>
       ''' The SldWorks swApp variable is pre-assigned for you.
       '''  </summary>
       Public swApp  As  SldWorks
 End  Class
```
