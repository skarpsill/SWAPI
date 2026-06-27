---
title: "Create Sheet Metal Corner Relief Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_SM_Corner_Relief_Feature_Example_VBNET.htm"
---

# Create Sheet Metal Corner Relief Feature Example (VB.NET)

This example shows how to create sheet metal corner reliefs.

```vb
  '=========================================================
 'Preconditions:
 '1. Ensure that the specified part template exists.
 '2. Open an Immediate window.
 '
 'Postconditions:
 ' 1. Press F5.
 ' 2. Creates:
 '     - Base-Flange1
 '     - Sketched Bend1
 '     - Sketched Bend2
 '     - Sketched Bend3
 '     - Sketched Bend4
 ' 3. Selects the sheet metal solid body.
 ' 4. Sets rectangular reliefs for the four corners.
 ' 5. Creates Corner Relief1.
 ' 6. Press F5.
 ' 7. Sets circular reliefs for the four corners.
 ' 8. Press F5.
 ' 9. Sets constant width reliefs for the four corners.
 '10. Inspect the Immediate window and the graphics area after each change.
  '===============================================================================
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim featMgr As FeatureManager
     Dim cornerReliefFeatData As CornerReliefFeatureData
     Dim swBody As Body2
     Dim selMgr As SelectionMgr
     Dim getCornerVar() As Object
     Dim cntr1 As Integer
     Dim cornerItr As SMCornerReliefData
     Dim Feat As Feature
     Dim featModData As CornerReliefFeatureData
     Dim cornerReliefMod3Data As CornerReliefFeatureData
     Dim UseRatio As Boolean
     Dim CFace1 As Face2
     Dim CFace2 As Face2
     Dim CFace3 As Face2
     Dim boolstatus As Boolean
     Dim longstatus As Integer

     Sub PrintReliefData(ByVal cornerIndex As Integer, ByVal cornerReliefFeatData As CornerReliefFeatureData)

         Dim smCornerReliefData1 As SMCornerReliefData
         boolstatus = cornerReliefFeatData.GetCornerAtIndex(cornerIndex, smCornerReliefData1)

         Debug.Print("Add filleted corners? " & smCornerReliefData1.AddFilletedCorners)
         Debug.Print("Corner fillet diameter = " & smCornerReliefData1.CornerFilletDiameter)
         Debug.Print("Use ratio to thickness? " & smCornerReliefData1.RatioToThickness)
         Debug.Print("Relief type as defined by swCornerBendReliefType_e = " & smCornerReliefData1.ReliefType)
         Debug.Print("Slot length = " & smCornerReliefData1.SlotLength)
         Debug.Print("Slot width = " & smCornerReliefData1.SlotWidth)
         Debug.Print("Center on bend lines? " & smCornerReliefData1.CenterOnBendLines)
         Debug.Print("Tangent to bend? " & smCornerReliefData1.TangentToBend)

         Call smCornerReliefData1.GetFaces(CFace1, CFace2, CFace3)

     End Sub

     Sub main()

         swModel = swApp.ActiveDoc

         Dim swSheetWidth As Double
         swSheetWidth = 0
         Dim swSheetHeight As Double
         swSheetHeight = 0
         swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2022\templates\\Part.PRTDOT", 0, swSheetWidth, swSheetHeight)
         featMgr = swModel.FeatureManager
         boolstatus = swModel.Extension.SelectByID2("Front Plane", "PLANE", -0.0754055245830957, 0.0542345258765876, 0.00294433115750138, False, 0, Nothing, 0)
         swModel.SketchManager.InsertSketch(True)
         swModel.ClearSelection2(True)
         Dim skSegment As Object
         skSegment = swModel.SketchManager.CreateLine(-0.049594, 0.029143, 0#, 0.026075, 0.029143, 0#)
         skSegment = swModel.SketchManager.CreateLine(0.026075, 0.029143, 0#, 0.026075, 0.015645, 0#)
         skSegment = swModel.SketchManager.CreateLine(0.026075, 0.015645, 0#, 0.04305, 0.015645, 0#)
         skSegment = swModel.SketchManager.CreateLine(0.04305, 0.015645, 0#, 0.04305, -0.034869, 0#)
         skSegment = swModel.SketchManager.CreateLine(0.04305, -0.034869, 0#, 0.026075, -0.034869, 0#)
         skSegment = swModel.SketchManager.CreateLine(0.026075, -0.034869, 0#, 0.026075, -0.048571, 0#)
         skSegment = swModel.SketchManager.CreateLine(0.026075, -0.048571, 0#, -0.049594, -0.048571, 0#)
         skSegment = swModel.SketchManager.CreateLine(-0.049594, -0.048571, 0#, -0.049594, -0.034869, 0#)
         skSegment = swModel.SketchManager.CreateLine(-0.049594, -0.034869, 0#, -0.066568, -0.034869, 0#)
         skSegment = swModel.SketchManager.CreateLine(-0.066568, -0.034869, 0#, -0.066568, 0.015645, 0#)
         skSegment = swModel.SketchManager.CreateLine(-0.066568, 0.015645, 0#, -0.049594, 0.015645, 0#)
         skSegment = swModel.SketchManager.CreateLine(-0.049594, 0.015645, 0#, -0.049594, 0.029143, 0#)
         swModel.ClearSelection2(True)
         swModel.SketchManager.InsertSketch(True)

         swModel.ShowNamedView2("*Trimetric", 8)
         swModel.ViewZoomtofit2
         swModel.SketchManager.InsertSketch(True)
         Dim customBendAllowanceData As CustomBendAllowance
         customBendAllowanceData = swModel.FeatureManager.CreateCustomBendAllowance()
         customBendAllowanceData.KFactor = 0.5
         Dim myFeature As Feature
         myFeature = swModel.FeatureManager.InsertSheetMetalBaseFlange2(0.0007366, False, 0.0007366, 0.02, 0.01, False, 0, 0, 1, customBendAllowanceData, False, 0, 0.0001, 0.0001, 0.5, True, False, True, True)

         boolstatus = swModel.Extension.SelectByRay(-0.0145172925108454, -0.00387700058865903, 0, -0.5, -0.707106781186547, -0.5, 0.000556802642645787, 2, False, 0, 0)
         swModel.SketchManager.InsertSketch(True)
         swModel.ClearSelection2(True)
         skSegment = swModel.SketchManager.CreateLine(-0.049594, 0.015645, 0#, -0.049594, -0.034869, 0#)
         swModel.ClearSelection2(True)
         swModel.SketchManager.InsertSketch(True)
         swModel.SketchManager.InsertSketch(True)
         boolstatus = swModel.Extension.SelectByRay(-0.0254254889823514, -0.00675397704068888, 0, 0, 0, -1, 0.000428258640921609, 2, True, 0, 0)
         Dim CBAObject As CustomBendAllowance
         myFeature = swModel.FeatureManager.InsertSheetMetal3dBend(1.5707963267949, True, 0.0007366, False, 3, CBAObject)
         boolstatus = swModel.Extension.SelectByRay(-0.0246697384395485, -0.00297522432667467, 0, 0, 0, -1, 0.000428258640921609, 2, False, 0, 0)
         swModel.SketchManager.InsertSketch(True)
         swModel.ClearSelection2(True)
         boolstatus = swModel.Extension.SelectByRay(-0.049594, 0.015645, 0, 0, 0, -1, 0.000392913800359539, 3, False, 0, 0)
         swModel.ClearSelection2(True)
         skSegment = swModel.SketchManager.CreateLine(-0.049594, 0.015645, 0#, 0.026075, 0.015645, 0#)
         swModel.ClearSelection2(True)
         swModel.SketchManager.InsertSketch(True)
         swModel.SketchManager.InsertSketch(True)
         boolstatus = swModel.Extension.SelectByRay(-0.0235965085767476, -0.00434032596567101, 0, 0, 0, -1, 0.000392913800359539, 2, True, 0, 0)
         myFeature = swModel.FeatureManager.InsertSheetMetal3dBend(1.5707963267949, True, 0.0007366, False, 3, CBAObject)
         boolstatus = swModel.Extension.SelectByRay(-0.0234809456942889, -0.0197101893326765, 0, 0, 0, -1, 0.000392913800359539, 2, False, 0, 0)
         swModel.SketchManager.InsertSketch(True)
         swModel.ClearSelection2(True)
         skSegment = swModel.SketchManager.CreateLine(-0.049594, -0.034869, 0#, 0.026075, -0.034869, 0#)
         swModel.ClearSelection2(True)
         swModel.SketchManager.InsertSketch(True)
         swModel.SketchManager.InsertSketch(True)
         boolstatus = swModel.Extension.SelectByRay(-0.0171484564194607, -0.00399245414393841, 0, 0, 0, -1, 0.000367699685812068, 2, True, 0, 0)
         myFeature = swModel.FeatureManager.InsertSheetMetal3dBend(1.5707963267949, True, 0.0007366, False, 3, CBAObject)
         boolstatus = swModel.Extension.SelectByRay(-0.0107677854009571, -0.00972424336395007, 0, 0, 0, -1, 0.000367699685812068, 2, False, 0, 0)
         swModel.SketchManager.InsertSketch(True)
         swModel.ClearSelection2(True)
         skSegment = swModel.SketchManager.CreateLine(0.026075, -0.034869, 0#, 0.026075, 0.015645, 0#)
         swModel.ClearSelection2(True)
         swModel.SketchManager.InsertSketch(True)
         swModel.SketchManager.InsertSketch(True)
         boolstatus = swModel.Extension.SelectByRay(-0.0259083606991011, -0.0062053705579176, 0, 0, 0, -1, 0.000367699685812068, 2, True, 0, 0)
         myFeature = swModel.FeatureManager.InsertSheetMetal3dBend(1.5707963267949, True, 0.0007366, False, 3, CBAObject)
         ' Zoom to Area
         swModel.ViewZoomTo2(0.0152447662706814, 0.00218199896815251, -0.00886660359613402, 0.022429935049572, -0.00638493303744786, -0.00886660359613402)

         cornerReliefFeatData = featMgr.CreateDefinition(swFeatureNameID_e.swFmCornerRelief)

         boolstatus = swModel.Extension.SelectByID2("Sketched Bend4", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)

         selMgr = swModel.SelectionManager

         swBody = selMgr.GetSelectedObject6(1, -1)

          cornerReliefFeatData.Initialize(swCornerReliefBendType_e.swCornerReliefBendType_TwoBend)
         cornerReliefFeatData.SetBodyScope(swBody)

         'Default is tear relief for all Sketched Bends
         longstatus = cornerReliefFeatData.CollectAllCorners(swCornerReliefType_e.swCornerTearRelief, getCornerVar)

         Debug.Print("")
         Debug.Print("-------------Creating corners with rectangular reliefs------------------- ")

         For cntr1 = 0 To UBound(getCornerVar)

             cornerItr = getCornerVar(cntr1)

             cornerItr.AddFilletedCorners = True
             cornerItr.CornerFilletDiameter = 0.00025
             cornerItr.CenterOnBendLines = True
             cornerItr.TangentToBend = True
             cornerItr.ReliefType = swCornerReliefType_e.swCornerRectangularRelief

             UseRatio = True

             If Not UseRatio Then
                 cornerItr.SlotLength = 0.009
             Else
                 cornerItr.RatioToThickness = True
             End If

             PrintReliefData(cntr1 + 1, cornerReliefFeatData)
             Debug.Print("")
         Next

         Feat = featMgr.CreateFeature(cornerReliefFeatData)

         Stop

         featModData = Feat.GetDefinition()

         featModData.AccessSelections(swModel, Nothing)

         getCornerVar = featModData.GetCorners(-1)

         Debug.Print("")
         Debug.Print("-------------Changing corners to circular reliefs------------------- ")

         For cntr1 = 0 To UBound(getCornerVar)

             cornerItr = getCornerVar(cntr1)

             cornerItr.ReliefType = swCornerReliefType_e.swCornerCircularRelief

             UseRatio = False

             If Not UseRatio Then
                 cornerItr.SlotWidth = 0.0008
             Else
                 cornerItr.RatioToThickness = True
             End If

             PrintReliefData(cntr1 + 1, featModData)
             Debug.Print("")

         Next

         Feat.ModifyDefinition(featModData, swModel, Nothing)

         Stop

         cornerReliefMod3Data = Feat.GetDefinition()

         cornerReliefMod3Data.AccessSelections(swModel, Nothing)

         getCornerVar = cornerReliefMod3Data.GetCorners(-1)

         Debug.Print("")
         Debug.Print("-------------Changing corners to constant width reliefs------------------- ")

         For cntr1 = 0 To UBound(getCornerVar)

             cornerItr = getCornerVar(cntr1)

             cornerItr.ReliefType = swCornerReliefType_e.swCornerConstantWidthRelief

             PrintReliefData(cntr1 + 1, cornerReliefMod3Data)
             Debug.Print("")

         Next

         Feat.ModifyDefinition(cornerReliefMod3Data, swModel, Nothing)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks
 End Class
```
