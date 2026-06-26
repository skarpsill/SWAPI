---
title: "Create Advanced Hole Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Advanced_Hole_Example_CSharp.htm"
---

# Create Advanced Hole Feature Example (C#)

This example shows how to create an Advanced Hole feature.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified part document exists.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Selects near and far side faces of the Advanced Hole.
 // 2. Defines an Advanced Hole at a sketch point on the edge of the block
 //    with the following:
 //    * Countersink near side element
 //    * Straight tap near side element
 //    * Counterbore far side element
 //    * Straight hole far side element
 // 3. Gets some near and far side element data for the Advanced Hole.
 // 4. Modifies the near side element array to contain a tapered tap element.
 // 5. Deletes the Advanced Hole's defining sketch point on the edge of the block.
 // 6. Adds two sketch points and creates two Advanced Holes at those locations
 //    using the previously defined Advanced Hole.
 // 7. Inspect the Immediate window and graphics area.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 //----------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Diagnostics;
 using System.Runtime.InteropServices;

 namespace CreateAdvancedHole_CSharp
 {
     public partial class SolidWorksMacro
     {
         public void Main()
         {

             ModelDoc2 swModel = default(ModelDoc2);
             Feature feat = default(Feature);
             bool boolstatus = false;
             AdvancedHoleElementData swAdvHole_Near_1 = default(AdvancedHoleElementData);
             AdvancedHoleElementData swAdvHole_Near_2 = default(AdvancedHoleElementData);
             AdvancedHoleElementData swAdvHole_Near_3 = default(AdvancedHoleElementData);
             AdvancedHoleElementData swAdvHole_Far_1 = default(AdvancedHoleElementData);
             AdvancedHoleElementData swAdvHole_Far_2 = default(AdvancedHoleElementData);
             CountersinkElementData swCounterSinkNear = default(CountersinkElementData);
             CounterboreElementData swCounterBoreFar = default(CounterboreElementData);
             StraightElementData swStraightHoleFar = default(StraightElementData);
             StraightTapElementData swStraightTapNear = default(StraightTapElementData);
             TaperedTapElementData swTaperedTapNear = default(TaperedTapElementData);
             FeatureManager swFeatureMgr = default(FeatureManager);
             double ConvFactorLength = 0;
             AdvancedHoleElementData[] advHoleNearArr = new AdvancedHoleElementData[2];
             AdvancedHoleElementData[] advHoleFarArr = new AdvancedHoleElementData[2];
             AdvancedHoleFeatureData featdata = default(AdvancedHoleFeatureData);
             AdvancedHoleElementData[] newNearArr = new AdvancedHoleElementData[2];
             AdvancedHoleElementData[] newFarArr = new AdvancedHoleElementData[2];
             Feature swSketchFeature = default(Feature);
             SelectionMgr swSelectionManager = default(SelectionMgr);
             Sketch swSketch = default(Sketch);
             object[] swSketchPointArray = null;
             int swMaxPointNumber = 0;
             object skPoint = null;
             object swSketchPoint = null;
             int swCurrentPointNumber = 0;
             int errors = 0;
             int warnings = 0;
             object ResultArray = null;
             string CalloutString = null;
             string StrDiam = null;
             string strDepth = null;
             object[] nearSide = null;
             object[] farSide = null;

             bool retval = false;

             swModel = swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\block20.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);
             swFeatureMgr = swModel.FeatureManager;

             //Conversion from inches to meters
             ConvFactorLength = 25.4 / 1000;

             //Select two faces for the near side and far side hole elements
             boolstatus = swModel.Extension.SelectByRay(-0.0589202612791269, 0.0260626824463657, 0.0560000000000969, -0.400036026779312, -0.515038074910024, -0.758094294050284, 0.000722831189342222, 2, false, 256,
             0);
             //Near side
             boolstatus = swModel.Extension.SelectByRay(-0.0110716643645077, 0.0211784489308116, -0.0639370439421896, 0.18261953966356, -0.612697461661826, 0.76892907618728, 0.000936301020408163, 2, false, 512,
             0);
             //Far side

             //Define near and far side hole elements

             //Near side countersink
             swAdvHole_Near_1 = (AdvancedHoleElementData)swModel.Extension.CreateAdvancedHoleElementData((int)swAdvWzdGeneralHoleTypes_e.swAdvWzdCounterSink);

             swAdvHole_Near_1.Orientation = (int)swHoleElementOrientation_e.swHoleElementOrientation_Nearside;
             swAdvHole_Near_1.Size = "#4";
             swAdvHole_Near_1.Standard = 0;
             swAdvHole_Near_1.FastenerType = (int)swWzdHoleStandardFastenerTypes_e.swStandardAnsiInchFlatHead100;
             swAdvHole_Near_1.Diameter = ConvFactorLength * 0.225;
             swAdvHole_Near_1.BlindDepth = 0.02055794 * ConvFactorLength;
             swAdvHole_Near_1.EndCondition = (int)swEndConditions_e.swEndCondBlind;
             swCounterSinkNear = (CountersinkElementData)swAdvHole_Near_1;
             swCounterSinkNear.EndConditionOverride = true;
             swCounterSinkNear.AngleOverride = false;

             //Near side straight tap
             swAdvHole_Near_2 = (AdvancedHoleElementData)swModel.Extension.CreateAdvancedHoleElementData((int)swAdvWzdGeneralHoleTypes_e.swAdvWzdStraightTap);

             swAdvHole_Near_2.Size = "#4-40";
             swAdvHole_Near_2.Standard = (int)swWzdHoleStandards_e.swStandardAnsiInch;
             swAdvHole_Near_2.FastenerType = (int)swWzdHoleStandardFastenerTypes_e.swStandardAnsiInchBottomingTappedHole;
             swAdvHole_Near_2.Diameter = ConvFactorLength * 0.089;
             swAdvHole_Near_2.EndCondition = (int)swEndConditions_e.swEndCondUpToNext;
             swAdvHole_Near_2.DiameterOverride = true;
             swStraightTapNear = (StraightTapElementData)swAdvHole_Near_2;
             swStraightTapNear.CustomSizing = (int)swStraightTapHoleCustomSizing_e.swStraightTapHoleCustomSizing_TapDrillDiameter;
             swStraightTapNear.ThreadClass = (int)swStraightTapHoleThreadClass_e.swStraightTapHoleThreadClass_1B;
             swStraightTapNear.ThreadClassOverride = true;

             //Near side tapered tap
             swAdvHole_Near_3 = (AdvancedHoleElementData)swModel.Extension.CreateAdvancedHoleElementData((int)swAdvWzdGeneralHoleTypes_e.swAdvWzdTaperTap);

             swAdvHole_Near_3.Orientation = (int)swHoleElementOrientation_e.swHoleElementOrientation_Nearside;
             swAdvHole_Near_3.Size = "1/16";
             swAdvHole_Near_3.Standard = (int)swWzdHoleStandards_e.swStandardAnsiInch;
             swAdvHole_Near_3.FastenerType = (int)swWzdHoleStandardFastenerTypes_e.swStandardAnsiInchTaperedPipeTap;
             swAdvHole_Near_3.Diameter = ConvFactorLength * 0.266;
             swAdvHole_Near_2.BlindDepth = 0.205 * ConvFactorLength;
             swAdvHole_Near_3.EndCondition = (int)swEndConditions_e.swEndCondBlind;
             swAdvHole_Near_3.DiameterOverride = true;
             swTaperedTapNear = (TaperedTapElementData)swAdvHole_Near_3;
             swTaperedTapNear.CustomSizing = (int)swTaperedTapCustomSizing_e.swTaperedTapCustomSizing_MinorDiameterWithCosmeticThread;
             swTaperedTapNear.ThreadClass = (int)swTaperedTapThreadClass_e.swTaperedTapThreadClass_1;
             swTaperedTapNear.ThreadClassOverride = true;
             swTaperedTapNear.EndConditionOverride = true;

             //Far side counterbore
             swAdvHole_Far_1 = (AdvancedHoleElementData)swModel.Extension.CreateAdvancedHoleElementData((int)swAdvWzdGeneralHoleTypes_e.swAdvWzdCounterBore);

             swAdvHole_Far_1.Orientation = (int)swHoleElementOrientation_e.swHoleElementOrientation_Farside;
             swAdvHole_Far_1.Size = "#8";
             swAdvHole_Far_1.Standard = (int)swWzdHoleStandards_e.swStandardAnsiInch;
             swAdvHole_Far_1.FastenerType = (int)swWzdHoleStandardFastenerTypes_e.swStandardAnsiInchBinding;
             swAdvHole_Far_1.Diameter = ConvFactorLength * 0.375;
             swAdvHole_Far_1.BlindDepth = 0.105 * ConvFactorLength;
             swAdvHole_Far_1.EndCondition = (int)swEndConditions_e.swEndCondBlind;
             swAdvHole_Far_1.DiameterOverride = true;
             swCounterBoreFar = (CounterboreElementData)swAdvHole_Far_1;
             swCounterBoreFar.EndConditionOverride = true;

             //Far side straight
             swAdvHole_Far_2 = (AdvancedHoleElementData)swModel.Extension.CreateAdvancedHoleElementData((int)swAdvWzdGeneralHoleTypes_e.swAdvWzdStraight);

             swAdvHole_Far_2.Size = "1/16";
             swAdvHole_Far_2.Standard = 0;
             swAdvHole_Far_2.FastenerType = (int)swWzdHoleStandardFastenerTypes_e.swStandardAnsiInchAllDrillSizes;
             swAdvHole_Far_2.Diameter = ConvFactorLength * 0.0625;
             swAdvHole_Far_2.BlindDepth = 0.2711 * ConvFactorLength;
             swAdvHole_Far_2.EndCondition = (int)swEndConditions_e.swEndCondBlind;
             swAdvHole_Far_2.DiameterOverride = true;

             //Customize the hole callout for this straight element
             StrDiam = swModel.Extension.GetCalloutVariableString((int)swCalloutVariable_e.swCalloutVariable_AH_Straight_Diameter);
             strDepth = swModel.Extension.GetCalloutVariableString((int)swCalloutVariable_e.swCalloutVariable_AH_Straight_Depth);
             CalloutString = "<MOD-DIAM> " + StrDiam + " " + "<HOLE-DEPTH> " + strDepth;
             swAdvHole_Far_2.CalloutString = CalloutString;

             swStraightHoleFar = (StraightElementData)swAdvHole_Far_2;

             //Set near and far side element arrays
             advHoleNearArr[0] = (AdvancedHoleElementData)swCounterSinkNear;
             advHoleNearArr[1] = (AdvancedHoleElementData)swStraightTapNear;
             advHoleFarArr[0] = (AdvancedHoleElementData)swCounterBoreFar;
             advHoleFarArr[1] = (AdvancedHoleElementData)swStraightHoleFar;
```

```
	    DispatchWrapper[] dispArray = ObjectArrayToDispatchWrapperArray(new object[] { advHoleNearArr[0], advHoleNearArr[1] });
            DispatchWrapper[] dispArray2 = ObjectArrayToDispatchWrapperArray(new object[] { advHoleFarArr[0], advHoleFarArr[1] });

            //Create the Advanced Hole using the near and far side element arrays; specify to not use baseline dimensions; customize Hole Callouts

            feat = swFeatureMgr.AdvancedHole2(dispArray, dispArray2, false, true, false, out ResultArray);

            //Get some near and far side element data

            featdata = (AdvancedHoleFeatureData)feat.GetDefinition();

            featdata.AccessSelections(swModel, null);

            Debug.Print("Number of near side hole elements: " + featdata.NearSideElementsCount);

            Debug.Print("Number of far side hole elements: " + featdata.FarSideElementsCount);

            nearSide = (object[])featdata.GetNearSideElements();

            swCounterSinkNear = (CountersinkElementData)nearSide[0];

            farSide = (object[])featdata.GetFarSideElements();

            swCounterBoreFar = (CounterboreElementData)farSide[0];

            swStraightHoleFar = (StraightElementData)farSide[1];

            Debug.Print("Near side countersink:");

            Debug.Print("   Hole element type as defined in swAdvWzdGeneralHoleTypes_e: " + ((AdvancedHoleElementData)swCounterSinkNear).ElementType);

            Debug.Print("   Size as defined on the Advanced Hole PropertyManager page: " + ((AdvancedHoleElementData)swCounterSinkNear).Size);

            Debug.Print("   Standard as defined in swWzdHoleStandards_e: " + ((AdvancedHoleElementData)swCounterSinkNear).Standard);

            Debug.Print("   Fastener type as defined in swWzdHoleStandardFastenerTypes_e: " + ((AdvancedHoleElementData)swCounterSinkNear).FastenerType);

            Debug.Print("   Diameter in m: " + ((AdvancedHoleElementData)swCounterSinkNear).Diameter);

            Debug.Print("   Blind depth in m: " + ((AdvancedHoleElementData)swCounterSinkNear).BlindDepth);

            Debug.Print("   Orientation as defined in swHoleElementOrientation_e: " + ((AdvancedHoleElementData)swCounterSinkNear).Orientation);

            Debug.Print("   End condition as defined in swEndConditions_e: " + ((AdvancedHoleElementData)swCounterSinkNear).EndCondition);

            Debug.Print("Far side straight:");

            Debug.Print("   Hole element type as defined in swAdvWzdGeneralHoleTypes_e: " + ((AdvancedHoleElementData)swStraightHoleFar).ElementType);

            Debug.Print("   Size as defined on the Advanced Hole PropertyManager page: " + ((AdvancedHoleElementData)swStraightHoleFar).Size);

            Debug.Print("   Standard as defined in swWzdHoleStandards_e: " + ((AdvancedHoleElementData)swStraightHoleFar).Standard);

            Debug.Print("   Fastener type as defined in swWzdHoleStandardFastenerTypes_e: " + ((AdvancedHoleElementData)swStraightHoleFar).FastenerType);

            Debug.Print("   Diameter in m: " + ((AdvancedHoleElementData)swStraightHoleFar).Diameter);

            Debug.Print("   Diameter override? " + ((AdvancedHoleElementData)swStraightHoleFar).DiameterOverride);

            Debug.Print("   Blind depth in m: " + ((AdvancedHoleElementData)swStraightHoleFar).BlindDepth);

            Debug.Print("   End condition as defined in swEndConditions_e: " + ((AdvancedHoleElementData)swStraightHoleFar).EndCondition);

            Debug.Print("   Customized hole callout: " + ((AdvancedHoleElementData)swStraightHoleFar).CalloutString);

            //Modify the near and far side element arrays

            newNearArr[0] = (AdvancedHoleElementData)swTaperedTapNear;

            newNearArr[1] = (AdvancedHoleElementData)swStraightTapNear;

            //newFarArr[0] = (AdvancedHoleElementData)swCounterBoreFar;

            //newFarArr[1] = (AdvancedHoleElementData)swStraightHoleFar;

            featdata.SetNearSideElements(newNearArr);

            //featdata.SetFarSideElements(newFarArr);

            feat.ModifyDefinition(featdata, swModel, null);

            //Delete the first point used to define the Advanced Hole

            swSketchFeature = (Feature)feat.GetFirstSubFeature();

            swSketchFeature.Select2(false, 0);

            swModel.EditSketch();

            swSelectionManager = (SelectionMgr)swModel.SelectionManager;

            swSketch = (Sketch)swSketchFeature.GetSpecificFeature2();

            swSketchPointArray = (object[])swSketch.GetSketchPoints2();

            swMaxPointNumber = swSketchPointArray.GetUpperBound(0);

            for (swCurrentPointNumber = 0; swCurrentPointNumber <= swMaxPointNumber; swCurrentPointNumber += 1)

            {

                swSketchPoint = swSketchPointArray[swCurrentPointNumber];

                retval = swSelectionManager.AddSelectionListObject(swSketchPoint, null);

                swModel.EditDelete();

            }

            //Create points for multiple Advanced Hole locations

            skPoint = swModel.SketchManager.CreatePoint(-0.0319158789518497, 0.0344489966898323, 0.05600000000004);

            skPoint = swModel.SketchManager.CreatePoint(-0.0494104502066557, 0.0080156770060853, 0.0560000000000969);

            swModel.SketchManager.InsertSketch(true);

        }
```

```
	public DispatchWrapper[] ObjectArrayToDispatchWrapperArray(object[] Objects)
        {
            int ArraySize = 0;
            ArraySize = Objects.GetUpperBound(0);
            DispatchWrapper[] d = new DispatchWrapper[ArraySize + 1];
            int ArrayIndex = 0;
            for (ArrayIndex = 0; ArrayIndex <= ArraySize; ArrayIndex++)
            {;
                d[ArrayIndex] = new DispatchWrapper(Objects[ArrayIndex]);
            }
            return d;
        }
```

```
        // The SldWorks swApp variable is pre-assigned for you.

        public SldWorks swApp;

    }

}
```
