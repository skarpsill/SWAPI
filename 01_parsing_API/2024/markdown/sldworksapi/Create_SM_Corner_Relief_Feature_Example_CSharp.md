---
title: "Create Sheet Metal Corner Relief Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_SM_Corner_Relief_Feature_Example_CSharp.htm"
---

# Create Sheet Metal Corner Relief Feature Example (C#)

This example shows how to create sheet metal corner reliefs.

```vb
 // =========================================================
 // Preconditions:
 // 1. Ensure that the specified part template exists.
 // 2. Open an Immediate window.
 //
 // Postconditions:
 // 1. Press F5.
 // 2. Creates:
 //    - Base-Flange1
 //    - Sketched Bend1
 //    - Sketched Bend2
 //    - Sketched Bend3
 //    - Sketched Bend4
 // 3. Selects the sheet metal solid body.
 // 4. Sets rectangular reliefs for the four corners.
 // 5. Creates Corner Relief1.
 // 6. Press F5.
 // 7. Sets circular reliefs for the four corners.
 // 8. Press F5.
 // 9. Sets constant width reliefs for the four corners.
 // 10. Inspect the Immediate window and the graphics area after each change.
 // ===============================================================================

 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;

 namespace Macro1_CSharp
 {
     public partial class SolidWorksMacro
     {
         private ModelDoc2 swModel;
         private FeatureManager featMgr;
         private CornerReliefFeatureData cornerReliefFeatData;
         private Body2 swBody;
         private SelectionMgr selMgr;
         private object[] getCornerVar;
         private object corners;
         private int cntr1;
         private SMCornerReliefData cornerItr;
         private Feature Feat;
         private CornerReliefFeatureData featModData;
         private CornerReliefFeatureData cornerReliefMod3Data;
         private bool UseRatio;
         private object CFace1;
         private object CFace2;
         private object CFace3;
         private bool boolstatus;
         private int longstatus;

         public void PrintReliefData(int cornerIndex, CornerReliefFeatureData cornerReliefFeatData)
         {
             object smCornerReliefData1;
             longstatus = cornerReliefFeatData.GetCornerAtIndex(cornerIndex, out smCornerReliefData1);
             Debug.Print("Add filleted corners? " + ((SMCornerReliefData)smCornerReliefData1).AddFilletedCorners);
             Debug.Print("Corner fillet diameter = " + ((SMCornerReliefData)smCornerReliefData1).CornerFilletDiameter);
             Debug.Print("Use ratio to thickness? " + ((SMCornerReliefData)smCornerReliefData1).RatioToThickness);
             Debug.Print("Relief type as defined by swCornerBendReliefType_e = " + ((SMCornerReliefData)smCornerReliefData1).ReliefType);
             Debug.Print("Slot length = " + ((SMCornerReliefData)smCornerReliefData1).SlotLength);
             Debug.Print("Slot width = " + ((SMCornerReliefData)smCornerReliefData1).SlotWidth);
             Debug.Print("Center on bend lines? " + ((SMCornerReliefData)smCornerReliefData1).CenterOnBendLines);
             Debug.Print("Tangent to bend? " + ((SMCornerReliefData)smCornerReliefData1).TangentToBend);
             ((SMCornerReliefData)smCornerReliefData1).GetFaces(out CFace1, out CFace2, out CFace3);
         }

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             double swSheetWidth;
             swSheetWidth = 0d;
             double swSheetHeight;
             swSheetHeight = 0d;
             swModel = (ModelDoc2)swApp.NewDocument(@"C:\ProgramData\SolidWorks\SOLIDWORKS 2022\templates\\Part.PRTDOT", 0, swSheetWidth, swSheetHeight);
             featMgr = swModel.FeatureManager;
             boolstatus = swModel.Extension.SelectByID2("Front Plane", "PLANE", -0.0754055245830957d, 0.0542345258765876d, 0.00294433115750138d, false, 0, null, 0);
             swModel.SketchManager.InsertSketch(true);
             swModel.ClearSelection2(true);
             object skSegment;
             skSegment = swModel.SketchManager.CreateLine(-0.049594d, 0.029143d, 0d, 0.026075d, 0.029143d, 0d);
             skSegment = swModel.SketchManager.CreateLine(0.026075d, 0.029143d, 0d, 0.026075d, 0.015645d, 0d);
             skSegment = swModel.SketchManager.CreateLine(0.026075d, 0.015645d, 0d, 0.04305d, 0.015645d, 0d);
             skSegment = swModel.SketchManager.CreateLine(0.04305d, 0.015645d, 0d, 0.04305d, -0.034869d, 0d);
             skSegment = swModel.SketchManager.CreateLine(0.04305d, -0.034869d, 0d, 0.026075d, -0.034869d, 0d);
             skSegment = swModel.SketchManager.CreateLine(0.026075d, -0.034869d, 0d, 0.026075d, -0.048571d, 0d);
             skSegment = swModel.SketchManager.CreateLine(0.026075d, -0.048571d, 0d, -0.049594d, -0.048571d, 0d);
             skSegment = swModel.SketchManager.CreateLine(-0.049594d, -0.048571d, 0d, -0.049594d, -0.034869d, 0d);
             skSegment = swModel.SketchManager.CreateLine(-0.049594d, -0.034869d, 0d, -0.066568d, -0.034869d, 0d);
             skSegment = swModel.SketchManager.CreateLine(-0.066568d, -0.034869d, 0d, -0.066568d, 0.015645d, 0d);
             skSegment = swModel.SketchManager.CreateLine(-0.066568d, 0.015645d, 0d, -0.049594d, 0.015645d, 0d);
             skSegment = swModel.SketchManager.CreateLine(-0.049594d, 0.015645d, 0d, -0.049594d, 0.029143d, 0d);
             swModel.ClearSelection2(true);
             swModel.SketchManager.InsertSketch(true);
             swModel.ShowNamedView2("*Trimetric", 8);
             swModel.ViewZoomtofit2();
             swModel.SketchManager.InsertSketch(true);
             CustomBendAllowance customBendAllowanceData;
             customBendAllowanceData = swModel.FeatureManager.CreateCustomBendAllowance();
             customBendAllowanceData.KFactor = 0.5d;
             Feature myFeature;
             myFeature = swModel.FeatureManager.InsertSheetMetalBaseFlange2(0.0007366d, false, 0.0007366d, 0.02d, 0.01d, false, 0, 0, 1, customBendAllowanceData, false, 0, 0.0001d, 0.0001d, 0.5d, true, false, true, true);
             boolstatus = swModel.Extension.SelectByRay(-0.0145172925108454d, -0.00387700058865903d, 0, -0.5d, -0.707106781186547d, -0.5d, 0.000556802642645787d, 2, false, 0, 0);
             swModel.SketchManager.InsertSketch(true);
             swModel.ClearSelection2(true);
             skSegment = swModel.SketchManager.CreateLine(-0.049594d, 0.015645d, 0d, -0.049594d, -0.034869d, 0d);
             swModel.ClearSelection2(true);
             swModel.SketchManager.InsertSketch(true);
             swModel.SketchManager.InsertSketch(true);
             boolstatus = swModel.Extension.SelectByRay(-0.0254254889823514d, -0.00675397704068888d, 0, 0, 0, -1, 0.000428258640921609d, 2, true, 0, 0);
             var CBAObject = default(CustomBendAllowance);
             myFeature = swModel.FeatureManager.InsertSheetMetal3dBend(1.5707963267949d, true, 0.0007366d, false, 3, CBAObject);
             boolstatus = swModel.Extension.SelectByRay(-0.0246697384395485d, -0.00297522432667467d, 0, 0, 0, -1, 0.000428258640921609d, 2, false, 0, 0);
             swModel.SketchManager.InsertSketch(true);
             swModel.ClearSelection2(true);
             boolstatus = swModel.Extension.SelectByRay(-0.049594d, 0.015645d, 0, 0, 0, -1, 0.000392913800359539d, 3, false, 0, 0);
             swModel.ClearSelection2(true);
             skSegment = swModel.SketchManager.CreateLine(-0.049594d, 0.015645d, 0d, 0.026075d, 0.015645d, 0d);
             swModel.ClearSelection2(true);
             swModel.SketchManager.InsertSketch(true);
             swModel.SketchManager.InsertSketch(true);
             boolstatus = swModel.Extension.SelectByRay(-0.0235965085767476d, -0.00434032596567101d, 0, 0, 0, -1, 0.000392913800359539d, 2, true, 0, 0);
             myFeature = swModel.FeatureManager.InsertSheetMetal3dBend(1.5707963267949d, true, 0.0007366d, false, 3, CBAObject);
             boolstatus = swModel.Extension.SelectByRay(-0.0234809456942889d, -0.0197101893326765d, 0, 0, 0, -1, 0.000392913800359539d, 2, false, 0, 0);
             swModel.SketchManager.InsertSketch(true);
             swModel.ClearSelection2(true);
             skSegment = swModel.SketchManager.CreateLine(-0.049594d, -0.034869d, 0d, 0.026075d, -0.034869d, 0d);
             swModel.ClearSelection2(true);
             swModel.SketchManager.InsertSketch(true);
             swModel.SketchManager.InsertSketch(true);
             boolstatus = swModel.Extension.SelectByRay(-0.0171484564194607d, -0.00399245414393841d, 0, 0, 0, -1, 0.000367699685812068d, 2, true, 0, 0);
             myFeature = swModel.FeatureManager.InsertSheetMetal3dBend(1.5707963267949d, true, 0.0007366d, false, 3, CBAObject);
             boolstatus = swModel.Extension.SelectByRay(-0.0107677854009571d, -0.00972424336395007d, 0, 0, 0, -1, 0.000367699685812068d, 2, false, 0, 0);
             swModel.SketchManager.InsertSketch(true);
             swModel.ClearSelection2(true);
             skSegment = swModel.SketchManager.CreateLine(0.026075d, -0.034869d, 0d, 0.026075d, 0.015645d, 0d);
             swModel.ClearSelection2(true);
             swModel.SketchManager.InsertSketch(true);
             swModel.SketchManager.InsertSketch(true);
             boolstatus = swModel.Extension.SelectByRay(-0.0259083606991011d, -0.0062053705579176d, 0, 0, 0, -1, 0.000367699685812068d, 2, true, 0, 0);
             myFeature = swModel.FeatureManager.InsertSheetMetal3dBend(1.5707963267949d, true, 0.0007366d, false, 3, CBAObject);
             // Zoom to Area
             swModel.ViewZoomTo2(0.0152447662706814d, 0.00218199896815251d, -0.00886660359613402d, 0.022429935049572d, -0.00638493303744786d, -0.00886660359613402d);
             cornerReliefFeatData = (CornerReliefFeatureData)featMgr.CreateDefinition((int)swFeatureNameID_e.swFmCornerRelief);
             boolstatus = swModel.Extension.SelectByID2("Sketched Bend4", "SOLIDBODY", 0, 0, 0, false, 0, null, 0);
             selMgr = (SelectionMgr)swModel.SelectionManager;
             swBody = (Body2)selMgr.GetSelectedObject6(1, -1);
              cornerReliefFeatData.Initialize((int)swCornerReliefBendType_e.swCornerReliefBendType_TwoBend);
             cornerReliefFeatData.SetBodyScope(swBody);

             // Default is tear relief for all Sketched Bends
             longstatus = cornerReliefFeatData.CollectAllCorners((int)swCornerReliefType_e.swCornerTearRelief, out corners);
             getCornerVar = (object[])corners;
             Debug.Print("");
             Debug.Print("-------------Creating corners with rectangular reliefs------------------- ");
             var loopTo = getCornerVar.GetUpperBound(0);
             for (cntr1 = 0; cntr1 <= loopTo; cntr1++)
             {
                 cornerItr = (SMCornerReliefData)getCornerVar[cntr1];
                 cornerItr.AddFilletedCorners = true;
                 cornerItr.CornerFilletDiameter = 0.00025d;
                 cornerItr.CenterOnBendLines = true;
                 cornerItr.TangentToBend = true;
                 cornerItr.ReliefType = (int)swCornerReliefType_e.swCornerRectangularRelief;
                 UseRatio = true;
                 if (!UseRatio)
                 {
                     cornerItr.SlotLength = 0.009d;
                 }
                 else
                 {
                     cornerItr.RatioToThickness = true;
                 }

                 PrintReliefData(cntr1 + 1, cornerReliefFeatData);
                 Debug.Print("");
             }

             Feat = featMgr.CreateFeature(cornerReliefFeatData);
             Debugger.Break();
             featModData = (CornerReliefFeatureData)Feat.GetDefinition();
             featModData.AccessSelections(swModel, null);
             getCornerVar = (object[])featModData.GetCorners(-1);
             Debug.Print("");
             Debug.Print("-------------Changing corners to circular reliefs------------------- ");
             var loopTo1 = getCornerVar.GetUpperBound(0);
             for (cntr1 = 0; cntr1 <= loopTo1; cntr1++)
             {
                 cornerItr = (SMCornerReliefData)getCornerVar[cntr1];
                 cornerItr.ReliefType = (int)swCornerReliefType_e.swCornerCircularRelief;
                 UseRatio = false;
                 if (!UseRatio)
                 {
                     cornerItr.SlotWidth = 0.0008d;
                 }
                 else
                 {
                     cornerItr.RatioToThickness = true;
                 }

                 PrintReliefData(cntr1 + 1, featModData);
                 Debug.Print("");
             }

             Feat.ModifyDefinition(featModData, swModel, null);
             Debugger.Break();
             cornerReliefMod3Data = (CornerReliefFeatureData)Feat.GetDefinition();
             cornerReliefMod3Data.AccessSelections(swModel, null);
             getCornerVar = (object[])cornerReliefMod3Data.GetCorners(-1);
             Debug.Print("");
             Debug.Print("-------------Changing corners to constant width reliefs------------------- ");
             var loopTo2 = getCornerVar.GetUpperBound(0);
             for (cntr1 = 0; cntr1 <= loopTo2; cntr1++)
             {
                 cornerItr = (SMCornerReliefData)getCornerVar[cntr1];
                 cornerItr.ReliefType = (int)swCornerReliefType_e.swCornerConstantWidthRelief;
                 PrintReliefData(cntr1 + 1, cornerReliefMod3Data);
                 Debug.Print("");
             }

             Feat.ModifyDefinition(cornerReliefMod3Data, swModel, null);
         }

         // The SldWorks swApp variable is pre-assigned for you.
         public SldWorks swApp;

     }
 }
```
