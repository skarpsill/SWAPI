---
title: "Create Advanced Hole Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Advanced_Hole_Example_VBNET.htm"
---

# Create Advanced Hole Feature Example (VB.NET)

This example shows how to create an Advanced Hole feature.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified part document exists.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Selects near and far side faces of the Advanced Hole.
 ' 2. Defines an Advanced Hole at a sketch point on the edge of the block
 '    with the following:
 '    * Countersink near side element
 '    * Straight tap near side element
 '    * Counterbore far side element
 '    * Straight hole far side element
 ' 3. Gets some near and far side element data for the Advanced Hole.
 ' 4. Modifies the near side element array to contain a tapered tap element.
 ' 5. Deletes the Advanced Hole's defining sketch point on the edge of the block.
 ' 6. Adds two sketch points and creates two Advanced Holes at those locations
 '    using the previously defined Advanced Hole.
 ' 7. Inspect the Immediate window and graphics area.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices

 Partial Class SolidWorksMacro

     Public Sub main()

         Dim swModel As ModelDoc2
         Dim feat As Feature
         Dim boolstatus As Boolean
         Dim swAdvHole_Near_1 As AdvancedHoleElementData
         Dim swAdvHole_Near_2 As AdvancedHoleElementData
         Dim swAdvHole_Near_3 As AdvancedHoleElementData
         Dim swAdvHole_Far_1 As AdvancedHoleElementData
         Dim swAdvHole_Far_2 As AdvancedHoleElementData
         Dim swCounterSinkNear As CountersinkElementData
         Dim swCounterBoreFar As CounterboreElementData
         Dim swStraightHoleFar As StraightElementData
         Dim swStraightTapNear As StraightTapElementData
         Dim swTaperedTapNear As TaperedTapElementData
         Dim swFeatureMgr As FeatureManager
         Dim ConvFactorLength As Double
         Dim advHoleNearArr(1) As AdvancedHoleElementData
         Dim advHoleFarArr(1) As AdvancedHoleElementData
         Dim featdata As AdvancedHoleFeatureData
         Dim newNearArr(1) As AdvancedHoleElementData
         Dim newFarArr(1) As AdvancedHoleElementData
         Dim swSketchFeature As Feature
         Dim swSelectionManager As SelectionMgr
         Dim swSketch As Sketch
         Dim swSketchPointArray As Object
         Dim swMaxPointNumber As Integer
         Dim skPoint As Object
         Dim swSketchPoint As Object
         Dim swCurrentPointNumber As Integer
         Dim errors As Long, warnings As Integer
         Dim ResultArray As Object = Nothing
         Dim CalloutString As String
         Dim StrDiam As String
         Dim strDepth As String

         Dim retval As Boolean

         swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\block20.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         swFeatureMgr = swModel.FeatureManager

         'Conversion from inches to meters
         ConvFactorLength = 25.4 / 1000

         'Select two faces for the near side and far side hole elements
         boolstatus = swModel.Extension.SelectByRay(-0.0589202612791269, 0.0260626824463657, 0.0560000000000969, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000722831189342222, 2, False, 256, 0) 'Near side
         boolstatus = swModel.Extension.SelectByRay(-0.0110716643645077, 0.0211784489308116, -0.0639370439421896, 0.18261953966356, -0.612697461661826, 0.76892907618728, 0.000936301020408163, 2, False, 512, 0) 'Far side

         'Define near and far side hole elements

         'Near side countersink
         swAdvHole_Near_1 = swModel.Extension.CreateAdvancedHoleElementData(swAdvWzdGeneralHoleTypes_e.swAdvWzdCounterSink)

         swAdvHole_Near_1.Orientation = swHoleElementOrientation_e.swHoleElementOrientation_Nearside
         swAdvHole_Near_1.Size = "#4"
         swAdvHole_Near_1.Standard = 0
         swAdvHole_Near_1.FastenerType = swWzdHoleStandardFastenerTypes_e.swStandardAnsiInchFlatHead100
         swAdvHole_Near_1.Diameter = ConvFactorLength * 0.225
         swAdvHole_Near_1.BlindDepth = 0.02055794 * ConvFactorLength
         swAdvHole_Near_1.EndCondition = swEndConditions_e.swEndCondBlind
         swCounterSinkNear = swAdvHole_Near_1
         swCounterSinkNear.EndConditionOverride = True
         swCounterSinkNear.AngleOverride = False

         'Near side straight tap
         swAdvHole_Near_2 = swModel.Extension.CreateAdvancedHoleElementData(swAdvWzdGeneralHoleTypes_e.swAdvWzdStraightTap)

         swAdvHole_Near_2.Size = "#4-40"
         swAdvHole_Near_2.Standard = swWzdHoleStandards_e.swStandardAnsiInch
         swAdvHole_Near_2.FastenerType = swWzdHoleStandardFastenerTypes_e.swStandardAnsiInchBottomingTappedHole
         swAdvHole_Near_2.Diameter = ConvFactorLength * 0.089
         swAdvHole_Near_2.EndCondition = swEndConditions_e.swEndCondUpToNext
         swAdvHole_Near_2.DiameterOverride = True
         swStraightTapNear = swAdvHole_Near_2
         swStraightTapNear.CustomSizing = swStraightTapHoleCustomSizing_e.swStraightTapHoleCustomSizing_TapDrillDiameter
         swStraightTapNear.ThreadClass = swStraightTapHoleThreadClass_e.swStraightTapHoleThreadClass_1B
         swStraightTapNear.ThreadClassOverride = True

         'Near side tapered tap
         swAdvHole_Near_3 = swModel.Extension.CreateAdvancedHoleElementData(swAdvWzdGeneralHoleTypes_e.swAdvWzdTaperTap)

         swAdvHole_Near_3.Orientation = swHoleElementOrientation_e.swHoleElementOrientation_Nearside
         swAdvHole_Near_3.Size = "1/16"
         swAdvHole_Near_3.Standard = swWzdHoleStandards_e.swStandardAnsiInch
         swAdvHole_Near_3.FastenerType = swWzdHoleStandardFastenerTypes_e.swStandardAnsiInchTaperedPipeTap
         swAdvHole_Near_3.Diameter = ConvFactorLength * 0.266
         swAdvHole_Near_2.BlindDepth = 0.205 * ConvFactorLength
         swAdvHole_Near_3.EndCondition = swEndConditions_e.swEndCondBlind
         swAdvHole_Near_3.DiameterOverride = True
         swTaperedTapNear = swAdvHole_Near_3
         swTaperedTapNear.CustomSizing = swTaperedTapCustomSizing_e.swTaperedTapCustomSizing_MinorDiameterWithCosmeticThread
         swTaperedTapNear.ThreadClass = swTaperedTapThreadClass_e.swTaperedTapThreadClass_1
         swTaperedTapNear.ThreadClassOverride = True
         swTaperedTapNear.EndConditionOverride = True

         'Far side counterbore
         swAdvHole_Far_1 = swModel.Extension.CreateAdvancedHoleElementData(swAdvWzdGeneralHoleTypes_e.swAdvWzdCounterBore)

         swAdvHole_Far_1.Orientation = swHoleElementOrientation_e.swHoleElementOrientation_Farside
         swAdvHole_Far_1.Size = "#8"
         swAdvHole_Far_1.Standard = swWzdHoleStandards_e.swStandardAnsiInch
         swAdvHole_Far_1.FastenerType = swWzdHoleStandardFastenerTypes_e.swStandardAnsiInchBinding
         swAdvHole_Far_1.Diameter = ConvFactorLength * 0.375
         swAdvHole_Far_1.BlindDepth = 0.105 * ConvFactorLength
         swAdvHole_Far_1.EndCondition = swEndConditions_e.swEndCondBlind
         swAdvHole_Far_1.DiameterOverride = True
         swCounterBoreFar = swAdvHole_Far_1
         swCounterBoreFar.EndConditionOverride = True

         'Far side straight
         swAdvHole_Far_2 = swModel.Extension.CreateAdvancedHoleElementData(swAdvWzdGeneralHoleTypes_e.swAdvWzdStraight)

         swAdvHole_Far_2.Size = "1/16"
         swAdvHole_Far_2.Standard = 0
         swAdvHole_Far_2.FastenerType = swWzdHoleStandardFastenerTypes_e.swStandardAnsiInchAllDrillSizes
         swAdvHole_Far_2.Diameter = ConvFactorLength * 0.0625
         swAdvHole_Far_2.BlindDepth = 0.2711 * ConvFactorLength
         swAdvHole_Far_2.EndCondition = swEndConditions_e.swEndCondBlind
         swAdvHole_Far_2.DiameterOverride = True

         'Customize the hole callout for this straight element
         StrDiam = swModel.Extension.GetCalloutVariableString(swCalloutVariable_e.swCalloutVariable_AH_Straight_Diameter)
         strDepth = swModel.Extension.GetCalloutVariableString(swCalloutVariable_e.swCalloutVariable_AH_Straight_Depth)
         CalloutString = "<MOD-DIAM> " & StrDiam & " " & "<HOLE-DEPTH> " & strDepth
         swAdvHole_Far_2.CalloutString = CalloutString

         swStraightHoleFar = swAdvHole_Far_2

         'Set near and far side element arrays
         advHoleNearArr(0) = swCounterSinkNear
         advHoleNearArr(1) = swStraightTapNear
         advHoleFarArr(0) = swCounterBoreFar
         advHoleFarArr(1) = swStraightHoleFar
```

```
	Dim dispArray As DispatchWrapper() = ObjectArrayToDispatchWrapperArray(New Object() {advHoleNearArr(0), advHoleNearArr(1)})
        Dim dispArray2 As DispatchWrapper() = ObjectArrayToDispatchWrapperArray(New Object() {advHoleFarArr(0), advHoleFarArr(1)})
```

```vb
         'Create the Advanced Hole using the near and far side element arrays; specify to not use baseline dimensions; customize Hole Callouts
         feat = swFeatureMgr.AdvancedHole2(dispArray, dispArray2, False, True, False, ResultArray)

         'Get some near and far side element data
         featdata = feat.GetDefinition
         featdata.AccessSelections(swModel, Nothing)
         Debug.Print("Number of near side hole elements: " & featdata.NearSideElementsCount)
         Debug.Print("Number of far side hole elements: " & featdata.FarSideElementsCount)
         swCounterSinkNear = featdata.GetNearSideElements(0)
         swCounterBoreFar = featdata.GetFarSideElements(0)
         swStraightHoleFar = featdata.GetFarSideElements(1)
         Debug.Print("Near side countersink:")
         Debug.Print("   Hole element type as defined in swAdvWzdGeneralHoleTypes_e: " & swCounterSinkNear.ElementType)
         Debug.Print("   Size as defined on the Advanced Hole PropertyManager page: " & swCounterSinkNear.Size)
         Debug.Print("   Standard as defined in swWzdHoleStandards_e: " & swCounterSinkNear.Standard)
         Debug.Print("   Fastener type as defined in swWzdHoleStandardFastenerTypes_e: " & swCounterSinkNear.FastenerType)
         Debug.Print("   Diameter in m: " & swCounterSinkNear.Diameter)
         Debug.Print("   Blind depth in m: " & swCounterSinkNear.BlindDepth)
         Debug.Print("   Orientation as defined in swHoleElementOrientation_e: " & swCounterSinkNear.Orientation)
         Debug.Print("   End condition as defined in swEndConditions_e: " & swCounterSinkNear.EndCondition)
         Debug.Print("Far side straight:")
         Debug.Print("   Hole element type as defined in swAdvWzdGeneralHoleTypes_e: " & swStraightHoleFar.ElementType)
         Debug.Print("   Size as defined on the Advanced Hole PropertyManager page: " & swStraightHoleFar.Size)
         Debug.Print("   Standard as defined in swWzdHoleStandards_e: " & swStraightHoleFar.Standard)
         Debug.Print("   Fastener type as defined in swWzdHoleStandardFastenerTypes_e: " & swStraightHoleFar.FastenerType)
         Debug.Print("   Diameter in m: " & swStraightHoleFar.Diameter)
         Debug.Print("   Diameter override? " & swStraightHoleFar.DiameterOverride)
         Debug.Print("   Blind depth in m: " & swStraightHoleFar.BlindDepth)
         Debug.Print("   End condition as defined in swEndConditions_e: " & swStraightHoleFar.EndCondition)
         Debug.Print("   Customized hole callout: " & swStraightHoleFar.CalloutString)

         'Modify the near and far side element arrays
         newNearArr(0) = swTaperedTapNear
         newNearArr(1) = swStraightTapNear
         'newFarArr(0) = swCounterBoreFar
         'newFarArr(1) = swStraightHoleFar
         featdata.SetNearSideElements(newNearArr)
         'featdata.SetFarSideElements(newFarArr)
         feat.ModifyDefinition(featdata, swModel, Nothing)

         'Delete the first point used to define the Advanced Hole
         swSketchFeature = feat.GetFirstSubFeature
         swSketchFeature.Select2(False, 0)
         swModel.EditSketch
         swSelectionManager = swModel.SelectionManager
         swSketch = swSketchFeature.GetSpecificFeature2()
         swSketchPointArray = swSketch.GetSketchPoints2()
         swMaxPointNumber = UBound(swSketchPointArray)
         For swCurrentPointNumber = 0 To swMaxPointNumber Step 1
             swSketchPoint = swSketchPointArray(swCurrentPointNumber)
             retval = swSelectionManager.AddSelectionListObject(swSketchPoint, Nothing)
             swModel.EditDelete
         Next swCurrentPointNumber

         'Create points for multiple Advanced Hole locations
         skPoint = swModel.SketchManager.CreatePoint(-0.0319158789518497, 0.0344489966898323, 0.05600000000004)
         skPoint = swModel.SketchManager.CreatePoint(-0.0494104502066557, 0.0080156770060853, 0.0560000000000969)

         swModel.SketchManager.InsertSketch(True)

     End Sub
```

```
Public Function ObjectArrayToDispatchWrapperArray(ByVal Objects As Object()) As DispatchWrapper()
        Dim ArraySize As Integer = 0
        ArraySize = Objects.GetUpperBound(0)
        Dim d As DispatchWrapper() = New DispatchWrapper(ArraySize + 1 - 1) {}
        Dim ArrayIndex As Integer = 0
        For ArrayIndex = 0 To ArraySize
            d(ArrayIndex) = New DispatchWrapper(Objects(ArrayIndex))
        Next

        Return d
    End Function
```

```vb
     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
