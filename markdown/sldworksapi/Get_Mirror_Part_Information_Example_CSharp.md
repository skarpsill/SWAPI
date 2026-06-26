---
title: "Get Mirror Part Information Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mirror_Part_Information_Example_CSharp.htm"
---

# Get Mirror Part Information Example (C#)

This example shows how to get information about a mirror part.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. Open a part that contains a reference plane about which to mirror the part.
 // 2. Select the reference plane in the FeatureManager design tree.
 //
 // Postconditions:
 // 1. Creates and mirrors a part about the selected reference plane.
 // 2. Shows the reference plane in the graphics area.
 // 3. Inspect the Immediate window for mirror part feature data.
 //---------------------------------------------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;

 namespace GetMirrorPartFeatureData_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         SelectionMgr selMgr;
         PartDoc swPart;
         Feature mirrorFeature;
         Feature myFeature;
         ModelDoc2 resultPart;
         MirrorPartFeatureData mirrorFeatData;
         RefPlane refPlane;
         Face2 facePlane;
         int mirrorOptions;
         int faceType;
         swSelectType_e selType;

         string message;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;

             if (swModel == null)
                 return;
             if (swModel.GetType() != (int)swDocumentTypes_e.swDocPART)
                 return;

             selMgr = (SelectionMgr)swModel.SelectionManager;

             if (selMgr.GetSelectedObjectCount2(-1) == 0)
                 return;

             selType = (swSelectType_e)selMgr.GetSelectedObjectType3(1, -1);
             if (!(selType == swSelectType_e.swSelDATUMPLANES | selType == swSelectType_e.swSelFACES))
                 return;

             swPart = (PartDoc)swModel;

             mirrorOptions = (int)swMirrorPartOptions_e.swMirrorPartOptions_ImportSolids + (int)swMirrorPartOptions_e.swMirrorPartOptions_ImportCustomProperties + (int)swMirrorPartOptions_e.swMirrorPartOptions_ImportCutListProperties;

             mirrorFeature = swPart.MirrorPart2(false, mirrorOptions, out resultPart);

             if (mirrorFeature == null)
             {
                 message = "No Feature";
             }
             else
             {
                 message = "Feature: " + mirrorFeature.Name;
             }

             if (resultPart == null)
             {
                 Debug.Print("No new part. " + message);
             }
             else
             {
                 Debug.Print(resultPart.GetTitle() + ". " + message);
             }

             swModel = (ModelDoc2)swApp.ActiveDoc;
             selMgr = (SelectionMgr)swModel.SelectionManager;
             mirrorFeature.Select2(false, -1);

             myFeature = (Feature)selMgr.GetSelectedObject6(1, -1);
             mirrorFeatData = (MirrorPartFeatureData)myFeature.GetDefinition();

             mirrorFeatData.AccessSelections(swModel,  null);

             Debug.Print("  Path name = " + mirrorFeatData.PathName);
             Debug.Print("  Import surface bodies? = " + mirrorFeatData.SurfaceBodies);
             Debug.Print("  Import solid bodies? = " + mirrorFeatData.SolidBodies);
             Debug.Print("  Import custom properties? = " + mirrorFeatData.CustomProperties);
             Debug.Print("  Import cut-list properties? = " + mirrorFeatData.CutListProperties);

             faceType = mirrorFeatData.GetMirrorPlaneType();
             Debug.Print("  Mirror plane type as defined in swMirrorPlaneType_e = " + faceType);

             Entity plane = default(Entity);
             if (faceType == 1)
             {
                 refPlane = (RefPlane)mirrorFeatData.GetMirrorPlane();
                 mirrorFeatData.ReleaseSelectionAccess();
                 plane = (Entity)refPlane;
                 plane.Select(false);
             }
             else
             {
                 facePlane = (Face2)mirrorFeatData.GetMirrorPlane();
                 mirrorFeatData.ReleaseSelectionAccess();
                 plane = (Entity)facePlane;
                 plane.Select(false);
             }

         }

         public SldWorks swApp;

     }

 }
```
