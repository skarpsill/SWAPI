---
title: "Create Swept Flange Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Swept_Flange_Example_CSharp.htm"
---

# Create Swept Flange Example (C#)

This example shows how to create a swept flange on a sheet metal part.

//========================================================================

```vb
 // Preconditions: Ensure that the specified part template exists.
```

//

```vb
 // Postconditions:
 // 1. Base-Flange1 and Swept Flange1 are created.
 // 2. Inspect the graphics area and the FeatureManager design tree.
 // ================================================
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;

 namespace CreateSweptFlange_CSharp
 {
       public  partial  class   SolidWorksMacro
      {
           public  void Main()
          {
                   Feature swFeat;
                   Feature myFeature;
                   FeatureManager swFeatMgr;
                   SweptFlangeFeatureData swFeatData;
                   CustomBendAllowance customBendAllowanceData;
                   Feature swProfileSketch;
                   SketchSegment skSegment;
                   ModelDoc2 Part;
                   PartDoc swPart;
                   bool boolstatus;
                   double swSheetWidth;
                  swSheetWidth = 0;
                   double swSheetHeight;
                  swSheetHeight = 0;
                  Part = (ModelDoc2)swApp.NewDocument(@"E:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\Tutorial\part.prtdot", 0, swSheetWidth, swSheetHeight);

                  swPart = (PartDoc)Part;
                  Part = (ModelDoc2)swApp.ActiveDoc;

                  Part.SketchManager.InsertSketch(true);
                  boolstatus = Part.Extension.SelectByID2("Front",  "PLANE", -0.0350345417518034, 0.019677523162802, 0.00511863136830445,   false, 0,   null, 0);
                  Part.ClearSelection2(true);
                  boolstatus = Part.Extension.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstToRectEntity, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified,   false);
                  boolstatus = Part.Extension.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, (int)swUserPreferenceOption_e.swDetailingNoOptionSpecified,   true);
                   object vSkLines;
                  vSkLines = Part.SketchManager.CreateCornerRectangle(-0.0420403557341645, 0.0275066828701494, 0, 0.0475026757367474, -0.0220443628675665, 0);
                  Part.ClearSelection2(true);

                  Part.ShowNamedView2("*Trimetric", 8);
                  Part.ViewZoomtofit2();

                  customBendAllowanceData = Part.FeatureManager.CreateCustomBendAllowance();
                  customBendAllowanceData.KFactor = 0.5;

                  myFeature = Part.FeatureManager.InsertSheetMetalBaseFlange2(0.0007366,   false, 0.0007366, 0.02, 0.01,  false, 0, 0, 1, customBendAllowanceData,  false, 0, 0.0001, 0.0001, 0.5,  true,  false,  true,  true);

                  Part.ClearSelection2(true);
                  Part.SketchManager.InsertSketch(true);
                  boolstatus = Part.Extension.SelectByID2("",  "FACE", 0.0441584745988735, 0.0275066828701256, -0.000252375262334681,   true, 0,   null, 0);

                  skSegment = Part.SketchManager.CreateLine(0.047503, 0.0, 0.0, 0.047503, -0.015713, 0.0);
                  Part.ClearSelection2(true);
                  Part.SketchManager.InsertSketch(true);

                  boolstatus = Part.Extension.SelectByID2("Sketch6",  "SKETCH", 0.0254585357375204, -0.00378791126417555, -0.013876316631307,   true, 0,   null, 0);
                  boolstatus = Part.Extension.SelectByRay(0.0472949686339916, 0.0133307046879168, 0.000207707102561017, -0.499999999999997, -0.707106781186554, -0.499999999999995, 0.000423592175091009, 1,  true, 0, 0);
                  Part.ClearSelection2(true);

                   // Select the sketch for the profile
                  boolstatus = Part.Extension.SelectByID2("Sketch6",  "SKETCH", 0.0254585357375204, -0.00378791126417555, -0.013876316631307,   true, 0,   null, 0);
                  swProfileSketch = (Feature)((SelectionMgr)Part.SelectionManager).GetSelectedObject6(1, -1);
                  Part.ClearSelection2(true);

                   // Select an edge for the path
                   Edge[] swPathObj =   new   Edge[1];
                  boolstatus = Part.Extension.SelectByRay(0.0472949686339916, 0.0133307046879168, 0.000207707102561017, -0.499999999999997, -0.707106781186554, -0.499999999999995, 0.000423592175091009, 1,  true, 0, 0);
                  swPathObj[0] = (Edge)((SelectionMgr)Part.SelectionManager).GetSelectedObject6(1, -1);

              Part.ClearSelection2(true);

                  swFeatMgr = Part.FeatureManager;

                  swFeatData = (SweptFlangeFeatureData)swFeatMgr.CreateDefinition((int)swFeatureNameID_e.swFmSweptFlange);
                  swFeatData.EndOffset = 0;
                  swFeatData.FlangePosition = (int)swSweptFlangePositionTypes_e.swSweptFlangePositionType_MaterialInside;
                  swFeatData.FlattenAlongPath =   false;
                  swFeatData.OverrideDefaultSheetMetalParameters =   false;
                  swFeatData.Path = swPathObj;
                  swFeatData.Profile = swProfileSketch;
                  swFeatData.ReverseDirection =   false;
                  swFeatData.StartOffset = 0;
                  swFeatData.TrimSideBends =   false;
                  swFeatData.UseDefaultBendAllowance =  true;
                  swFeatData.UseDefaultBendRelief =   true;
                  swFeatData.UseDefaultRadius =   false;
                  swFeatData.UseGaugeTable =   false;
                  swFeatData.UseMaterialSheetMetalParameters =   false;
                  swFeat = swFeatMgr.CreateFeature(swFeatData);
                  Part.ClearSelection2(true);
              }

       // The SldWorks swApp variable is pre-assigned for you.
       public  SldWorks swApp;

      }
 }
```
