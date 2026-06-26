---
title: "Create Corner Relief Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Corner_Relief_Feature_Example_CSharp.htm"
---

# Create Corner Relief Feature Example (C#)

This example shows how to create a corner relief feature.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // Open public_documents\samples\tutorial\sheetmetal\formtools\cover.sldprt.
 //
 // Postconditions:
 // 1. The model is rotated to the back view.
 // 2. An edge flange is created.
 // 3. The model is rotated slightly about the x-axis.
 // 4. A corner relief feature is created:
 //    * A rectangular corner relief is added to one corner of the edge flange.
 //    * An obround corner relief is added to another corner of the edge flange.
 //----------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 namespace TwoCorners_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             bool bValue = false;
             Edge swEdge = default(Edge);
             double dAngle = 0;
             double dLength = 0;
             Feature swFeature = default(Feature);
             Entity swEntity = default(Entity);
             Sketch swSketch = default(Sketch);
             object[] vSketchSegments = null;
             SketchLine swSketchLine = default(SketchLine);
             SketchPoint swStartPoint = default(SketchPoint);
             SketchPoint swEndPoint = default(SketchPoint);
             int nOptions = 0;
             double dSize = 0;
             double dFactor1 = 0;
             double dFactor2 = 0;
             Edge[] aFlangeEdges = new Edge[1];
             object vFlangeEdges = null;
             Sketch[] aSketchFeats = new Sketch[1];
             object vSketchFeats = null;

             // Get active document
             swModel = (ModelDoc2)swApp.ActiveDoc;

             // Flange parameters

             // Set the angle
             dAngle = (90.0 / 180.0) * 3.1415926535897;

             dLength = 0.01;

             // Rotate model so that IModelDocExtension::SelectByID2 coordinates can be found
             swModel.ShowNamedView2("*Back", -1);
             swModel.ViewZoomtofit2();

             // Select edge for flange
             bValue = swModel.Extension.SelectByID2("", "EDGE", 0.0372105002552985, 0.052846642716446, -9.93711211094706E-06,  false, 0,  null, 0);

             // Get edge
             swEdge = (Edge)((SelectionMgr)(swModel.SelectionManager)).GetSelectedObject6(1, -1);

             // Insert a sketch for an edge flange
             swFeature = (Feature)swModel.InsertSketchForEdgeFlange(swEdge, dAngle, false);

             // Select
             bValue = swFeature.Select2(false, 0);

             // Start sketch editing
             swModel.EditSketch();

             // Get the active sketch
             swSketch = (Sketch)swModel.SketchManager.ActiveSketch;

             // Add the edge to the sketch

             // Cast edge to entity
             swEntity = (Entity)swEdge;

             // Select edge
             bValue = swEntity.Select4(false, null);

             // Use the edge in the sketch
             bValue = swModel.SketchManager.SketchUseEdge(false);

             // Get the created sketch line
             vSketchSegments = (object[])swSketch.GetSketchSegments();

             swSketchLine = (SketchLine)vSketchSegments[0];

             // Get start and end point
             swStartPoint = (SketchPoint)swSketchLine.GetStartPoint2();
             swEndPoint = (SketchPoint)swSketchLine.GetEndPoint2();

             // Create additional lines to define sketch
             // Set parameters defining the sketch geometry
             dSize = swEndPoint.X - swStartPoint.X;
             dFactor1 = 0.1;
             dFactor2 = 1.25;

             swModel.SetAddToDB(true);
             swModel.SetDisplayWhenAdded(false);

             swModel.SketchManager.CreateLine(swStartPoint.X, swStartPoint.Y, 0.0, swStartPoint.X, swStartPoint.Y + dLength, 0.0);
             swModel.SketchManager.CreateLine(swStartPoint.X, swStartPoint.Y + dLength, 0.0, swStartPoint.X + dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0.0);
             swModel.SketchManager.CreateLine(swStartPoint.X + dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0.0, swEndPoint.X - dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0.0);
             swModel.SketchManager.CreateLine(swEndPoint.X - dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0.0, swEndPoint.X, swEndPoint.Y + dLength, 0.0);
             swModel.SketchManager.CreateLine(swEndPoint.X, swEndPoint.Y, 0.0, swEndPoint.X, swEndPoint.Y + dLength, 0.0);

             // Reset
             swModel.SetDisplayWhenAdded(true);
             swModel.SetAddToDB(false);

             // Commit changes made to the sketch
             swModel.SketchManager.InsertSketch(true);

             // Set options
             nOptions = (int)swInsertEdgeFlangeOptions_e.swInsertEdgeFlangeUseDefaultRadius + (int)swInsertEdgeFlangeOptions_e.swInsertEdgeFlangeUseDefaultRelief;

             aFlangeEdges[0] = swEdge;
             aSketchFeats[0] = swSketch;

             vFlangeEdges = aFlangeEdges;
             vSketchFeats = aSketchFeats;

             swFeature = swModel.FeatureManager.InsertSheetMetalEdgeFlange2((vFlangeEdges), (vSketchFeats), nOptions, dAngle, 0.0, (int)swFlangePositionTypes_e.swFlangePositionTypeBendOutside, dLength, (int)swSheetMetalReliefTypes_e.swSheetMetalReliefNone, 0.0, 0.0,
             0.0, (int)swFlangeDimTypes_e.swFlangeDimTypeInnerVirtualSharp, null);

             // Rotate view so that IModelDocExtension::SelectByID2 coordinates can be found
             ModelView myModelView = default(ModelView);
             myModelView = (ModelView)swModel.ActiveView;
             myModelView.RotateAboutCenter(45, 0.00911235438195936);

             // Select the sheet metal body to which to apply a corner relief
             bValue = swModel.Extension.SelectByID2("Edge-Flange1", "SOLIDBODY", 0, 0, 0, true, 0, null, 0);
             swModel.ClearSelection2(true);

             // Specify two corners of the edge flange for which to create a corner relief

             // Select faces that define the first corner
             bValue = swModel.Extension.SelectByID2("", "FACE", 0.0549242492243928, 0.053073918098565, 0.0242634000000049,  true, 4,  null, 0);
             bValue = swModel.Extension.SelectByID2("", "FACE", 0.0276778697571744, 0.0530739180985651, -0.00104170971004399,  true, 4,  null, 0);
             long myCorner = 0;
             myCorner = swModel.FeatureManager.AddCornerReliefCorner();

             // Specify the type of corner relief to apply to the first corner
             bool myReliefType = false;
             myReliefType = swModel.FeatureManager.AddCornerReliefType(-1, (int)swCornerReliefType_e.swCornerSquareRelief, 0.0001, 0.0007366, 0.00018415, false, false, false, true, false);
             swModel.ClearSelection2(true);

             // Select faces that define the second corner
             bValue = swModel.Extension.SelectByID2("", "FACE", 0.0276778697571744, 0.0530739180985651, -0.00104170971004399,  true, 4,  null, 0);
             bValue = swModel.Extension.SelectByID2("", "FACE", 0.000431490289955978, 0.053073918098565, 0.0242634000000049,  true, 4,  null, 0);
             myCorner = swModel.FeatureManager.AddCornerReliefCorner();

             // Specify the type of corner relief to apply to the second corner
             myReliefType = swModel.FeatureManager.AddCornerReliefType(-1, (int)swCornerReliefType_e.swCornerObroundRelief, 0.0001, 0.0029464, 0.0007366, false, false, false, false, false);

             // Create the corner relief feature
             Feature myFeature = default(Feature);
             myFeature = swModel.FeatureManager.FinishCornerRelief();

         }

         public SldWorks swApp;

     }

 }
```
