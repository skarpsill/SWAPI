---
title: "Get and Set Connection Point Feature Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Connection_Point_Feature_Data_Example_CSharp.htm"
---

# Get and Set Connection Point Feature Example (C#)

This example shows how to get and set data for connection point features.

```vb
 //----------------------------------------------------------------------------
 // Preconditions:
 // 1. Ensure that the latest SOLIDWORKS Design Library is loaded.
 // 2. Drag and drop design library > routing > electrical > db9 male.sldprt
  //      into the main view.
 // 3. Observe CPoint1 in the FeatureManager design tree.
 // 4. Run (F5) this macro.

 // Postconditions:
 // 1. Inspect the Immediate Window.
 // 2. CPoint1 is now MyCPoint in the FeatureManager design tree.
 //
 // NOTE:  Because this is a Design Library part, close it without saving changes.
 //----------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace CPoint2_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {

             ModelDoc2 Part = default(ModelDoc2);
             SelectionMgr selMgr = default(SelectionMgr);
             int selCount = 0;
             int selType = 0;
             object selObj = null;
             Feature selFeat = null;
             object vLocation = null;
             double xLoc = 0;
             double yLoc = 0;
             double zLoc = 0;
             object vDirection = null;
             double xDir = 0;
             double yDir = 0;
             double zDir = 0;
             bool boolstatus = false;

             Part = (ModelDoc2)swApp.ActiveDoc;
             selMgr = (SelectionMgr)Part.SelectionManager;

             boolstatus = Part.Extension.SelectByID2("CPoint1", "CONNECTIONPOINT", 0, 0, 0, false, 0, null, 0);

             selCount = selMgr.GetSelectedObjectCount2(-1);
             if ((selCount > 0))
             {
                 selType = selMgr.GetSelectedObjectType3(1, -1);
                 selObj = selMgr.GetSelectedObject6(1, -1);
                 if ((selType == (long)swSelectType_e.swSelCONNECTIONPOINTS))
                 {
                     selFeat = (Feature)selObj;
                 }
             }

             Part.ClearSelection2(true);

             object featData = null;
             if ((selFeat != null))
             {
                 featData = selFeat.GetDefinition();
             }
             IConnectionPointFeatureData cPointData = default(IConnectionPointFeatureData);
             cPointData = (IConnectionPointFeatureData)featData;

             if ((cPointData != null))
             {
                 Debug.Print("Get stublength = " + cPointData.StubLength);
                 cPointData.StubLength = 0.009;
                 Debug.Print("Set stublength = " + cPointData.StubLength);

                 Debug.Print("Get diameter = " + cPointData.RouteDiameter);
                 cPointData.RouteDiameter = 0.011;
                 Debug.Print("Set diameter = " + cPointData.RouteDiameter);

                 Debug.Print("Get route type = " + cPointData.RouteType);
                 cPointData.RouteType = 2;
                 Debug.Print("Set route type = " + cPointData.RouteType);

                 Debug.Print("Get route sub type = " + cPointData.RouteSubType);
                 cPointData.RouteSubType = 3;
                 Debug.Print("Set route sub type = " + cPointData.RouteSubType);

                 Debug.Print("Get electrical Pin ID = " + cPointData.ElectricalPinID);
                 cPointData.ElectricalPinID =  "zxc";
                 Debug.Print("Set electrical Pin ID = " + cPointData.ElectricalPinID);

                 Debug.Print("Get port ID = " + cPointData.PortID);
                 cPointData.PortID =  "newPortID";
                 Debug.Print("Set port ID = " + cPointData.PortID);

                 Debug.Print("Get CPoint name = " + cPointData.Name2);
                 cPointData.Name2 =  "myCPoint";
                 Debug.Print("Set CPoint name = " + cPointData.Name2);

                 vLocation = cPointData.Location;

                 double[] location;
                 location = (double[])vLocation;
                 xLoc = location[0];
                 yLoc = location[1];
                 zLoc = location[2];

                 Debug.Print("Get location: " + xLoc +  " " + yLoc + " " + zLoc);

                 vDirection = cPointData.Direction;

                 double[] direction;
                 direction = (double[])vDirection;
                 xDir =  direction[0];
                 yDir =  direction[1];
                 zDir =  direction[2];

                 Debug.Print("Get direction vector: " + xDir +  " " + yDir + " " + zDir);
             }
             Part.ForceRebuild3(false);
             cPointData = null;
             featData = null;
         }

         public SldWorks swApp;

     }
 }
```
