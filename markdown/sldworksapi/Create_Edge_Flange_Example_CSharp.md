---
title: "Create Edge Flange Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Edge_Flange_Example_CSharp.htm"
---

# Create Edge Flange Example (C#)

This example shows how to create a sheet metal edge flange.

```vb
 // -----------------------------------------------------
 // Preconditions: Open install_dir\samples\tutorial\sheetmetal\formtools\cover.sldprt.
 //
 // Postconditions: Creates Edge-Flange1 in the FeatureManager design tree.
 // ------------------------------------------------------
 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using System.Windows;
 using System.Windows.Forms;

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;

 namespace CreateEdgeFlange_CSharp
 {
       public  partial  class   SolidWorksMacro
      {
           public  void Main()
          {

                   ModelDoc2 swModel;
                   bool bValue;
                   Edge swEdge;
                   double dAngle;
                   double dLength;
                   Feature swFeature;
                   Entity swEntity;
                   Sketch swSketch;
                   object[] vSketchSegments =  new  object[1];
                   SketchLine swSketchLine;
                   SketchPoint swStartPoint;
                   SketchPoint swEndPoint;
                   double dSize;
                   double dFactor1;
                   double dFactor2;
                   Edge[] aFlangeEdges =   new   Edge[1];
                   object[] vFlangeEdges =   new   object[1];
                   Sketch[] aSketchFeats =   new   Sketch[1];
                   object[] vSketchFeats =   new   object[1];
                   EdgeFlangeFeatureData FeatData;
                   Feature edgeFlangeFeat;
                   CustomBendAllowance PBendData;

                  swModel = (ModelDoc2)swApp.ActiveDoc;

                   // Flange angle
                  dAngle = (90.0 / 180.0) * 3.1415926535897;

                   // Flange length
                  dLength = 0.02;

                  swModel.ShowNamedView2("*Back", -1);
                  swModel.ViewZoomtofit2();

                   // Select edge
                  bValue = swModel.Extension.SelectByRay(0.0353852695288734, 0.0527495553160953, 0.0485267999999905, 0, 0, 1, 0.000283299018635423, 1,   false, 0, 0);
                  swEdge = (Edge)((SelectionMgr)(swModel.SelectionManager)).GetSelectedObject6(1, -1);

                   // Insert a sketch of the edge flange
                  swFeature = (Feature)swModel.InsertSketchForEdgeFlange(swEdge, dAngle,  false);
                  bValue = swFeature.Select2(false, 0);

                  swModel.EditSketch();
                  swSketch = (Sketch)swModel.GetActiveSketch2();

                  swEntity = (Entity)swEdge;

                   // Select edge
                  bValue = swEntity.Select4(false,   null);

                   // Use the edge in the sketch
                  bValue = swModel.SketchManager.SketchUseEdge(false);

                   // Get the created sketch line
                  vSketchSegments = (Object[])swSketch.GetSketchSegments();
                  swSketchLine = (SketchLine)vSketchSegments[0];

                   // Get start and end point
                  swStartPoint = (SketchPoint)swSketchLine.GetStartPoint2();
                  swEndPoint = (SketchPoint)swSketchLine.GetEndPoint2();

                   // Create additional lines to define sketch

                   // Set parameters defining the sketch geometry
                  dSize = swEndPoint.X - swStartPoint.X;
                  dFactor1 = 0.1;
                  dFactor2 = 1.25;

                   // Add directly and do not display to speed things up
                  swModel.SetAddToDB(true);
                  swModel.SetDisplayWhenAdded(false);

                  swModel.CreateLine2(swStartPoint.X, swStartPoint.Y, 0.0, swStartPoint.X, swStartPoint.Y + dLength, 0.0);
                  swModel.CreateLine2(swStartPoint.X, swStartPoint.Y + dLength, 0.0, swStartPoint.X + dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0.0);
                  swModel.CreateLine2(swStartPoint.X + dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0.0, swEndPoint.X - dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0.0);
                  swModel.CreateLine2(swEndPoint.X - dFactor1 * dSize, swStartPoint.Y + dFactor2 * dLength, 0.0, swEndPoint.X, swEndPoint.Y + dLength, 0.0);
                  swModel.CreateLine2(swEndPoint.X, swEndPoint.Y, 0.0, swEndPoint.X, swEndPoint.Y + dLength, 0.0);

                  swModel.SetDisplayWhenAdded(true);
                  swModel.SetAddToDB(false);

                   // Commit changes made to the sketch
                  swModel.InsertSketch2(true);

                   // Insert the edge flange

                  aFlangeEdges[0] = swEdge;
                  aSketchFeats[0] = swSketch;

                  vFlangeEdges = aFlangeEdges;
                  vSketchFeats = aSketchFeats;

                  FeatData = (EdgeFlangeFeatureData)swModel.FeatureManager.CreateDefinition((int)swFeatureNameID_e.swFmEdgeFlange);

                  FeatData.AddEdges(vFlangeEdges, vSketchFeats);

                  FeatData.UseDefaultBendRadius =   false;
                  FeatData.BendRadius = 0.0007366;
                  FeatData.GapDistance = 0.001;
                  FeatData.BendAngle = dAngle;
                  FeatData.LockAngle =   true;
                  FeatData.OffsetType = (int)swFlangeOffsetTypes_e.swFlangeOffsetBlind;
                  FeatData.OffsetDistance = dLength;
                  FeatData.OffsetDimType = (int)swFlangeDimTypes_e.swFlangeDimTypeInnerVirtualSharp;
                  FeatData.PositionType = (int)swFlangePositionTypes_e.swFlangePositionTypeMaterialInside;
                  FeatData.UsePositionOffset =   true;
                  FeatData.PositionOffsetType = (int)swFlangeOffsetTypes_e.swFlangeOffsetBlind;
                  FeatData.PositionOffsetDistance = 0.01;
                  FeatData.UseDefaultBendAllowance =  false;
                  PBendData = FeatData.GetCustomBendAllowance();
                  PBendData.KFactor = 0.5;
                  PBendData.Type = (int)swBendAllowanceTypes_e.swBendAllowanceDeduction;
                  FeatData.SetCustomBendAllowance(PBendData);
                  FeatData.UseDefaultBendRelief =   false;
                  FeatData.UseReliefRatio =   true;
                  FeatData.ReliefRatio = 0.5;
                  FeatData.AutoReliefType = (int)swSheetMetalReliefTypes_e.swSheetMetalReliefTear;
                  FeatData.ReliefTearType = (int)swReliefTearTypes_e.swReliefTearTypeRip;

                  edgeFlangeFeat = swModel.FeatureManager.CreateFeature(FeatData);
              }

       // The SldWorks swApp variable is pre-assigned for you.
       public  SldWorks swApp;

      }
 }
```
