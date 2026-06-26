---
title: "Slice a Model Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Slice_a_Model_Example_CSharp.htm"
---

# Slice a Model Example (C#)

This example shows how to slice a model.

```vb
 // =====================================================================================
 // Preconditions:
 // 1. Open Public_Documents\SOLIDWORKS\SOLIDWORKS 2020\samples\tutorial\api\cube.sldprt.
 // 2. Change units to MKS.
 // 3. Open the Immediate window.
 // Postconditions:
 // 1. Selects Front Plane as the first slicing plane.
 // 2. Gets the default slicing parameters.
 // 3. Specifies new slicing parameters.
 // 4. Performs slicing and adds Slice1 to the FeatureManager design tree.
 // 5. Inspect the graphics area and the Immediate window.
 // NOTE: Because the model is used elsewhere, do not save changes to it.
 // =======================================================================================

 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;

 namespace SliceModel_CSharp
 {
       partial  class   SolidWorksMacro
      {
            private  ModelDoc2 modDoc;
            private  FeatureManager swFeatMgr;
            private  SlicingData sliceData;
            private  bool boolstatus;
            private  int errors;
            private  object vars;

            public  void Main()
           {
              modDoc = (ModelDoc2)swApp.ActiveDoc;
              swFeatMgr = modDoc.FeatureManager;

               // Select Case the first slicing plane
              boolstatus = modDoc.Extension.SelectByID2("Front Plane",   "PLANE", 0, 0, 0,   false, 0,   null/* TODO Change to default(_) if this is not a reference type */, 0);
               // Get default slicing parameters
              sliceData = (SlicingData)swFeatMgr.GetSlicingData();

               Debug.Print("Default slicing values:");
               Debug.Print("");
               Debug.Print("Bounding box direction 1: " + sliceData.GetBoundingBoxDirection1());
               Debug.Print("Bounding box direction 2: " + sliceData.GetBoundingBoxDirection2());
               Debug.Print("Bounding box direction 3: " + sliceData.GetBoundingBoxDirection3());
               Debug.Print("Bounding box direction 4: " + sliceData.GetBoundingBoxDirection4());
               Debug.Print("Reverse direction? " + sliceData.ReverseDirection);
               Debug.Print("Number of slices: " + sliceData.NumberOfPlanes);
               Debug.Print("Distance between slices: " + sliceData.Offset);
               Debug.Print("Type of slicing as defined in swSlicingTypes_e: " + sliceData.SlicesToGenerate);
               Debug.Print("Add slicing planes and sketches to folder? " + sliceData.AddSlicingPlanesAndSketchesToFolder);

              sliceData.ReverseDirection =   false;
              boolstatus = sliceData.SetBoundingBoxDirection1(0.1397);
              boolstatus = sliceData.SetBoundingBoxDirection2(0.1397);
              boolstatus = sliceData.SetBoundingBoxDirection3(-0.1397);
              boolstatus = sliceData.SetBoundingBoxDirection4(-0.1397);
              sliceData.NumberOfPlanes = 6;
              sliceData.Offset = 0.01;
              sliceData.SlicesToGenerate = (int)swSlicingTypes_e.swSlicingTypes_Rectangle;
               sliceData.AddSlicingPlanesAndSketchesToFolder =   true;

               Debug.Print("");
               Debug.Print("New values:");
               Debug.Print("");
               Debug.Print("Bounding box direction 1: " + sliceData.GetBoundingBoxDirection1());
               Debug.Print("Bounding box direction 2: " + sliceData.GetBoundingBoxDirection2());
               Debug.Print("Bounding box direction 3: " + sliceData.GetBoundingBoxDirection3());
                Debug.Print("Bounding box direction 4: " + sliceData.GetBoundingBoxDirection4());
               Debug.Print("Reverse direction? " + sliceData.ReverseDirection);
               Debug.Print("Number of slices: " + sliceData.NumberOfPlanes);
               Debug.Print("Distance between slices: " + sliceData.Offset);
               Debug.Print("Type of slicing as defined in swSlicingTypes_e: " + sliceData.SlicesToGenerate);
               Debug.Print("Add slicing planes and sketches to folder? " + sliceData.AddSlicingPlanesAndSketchesToFolder);

              vars = swFeatMgr.InsertSlicing(sliceData,  out errors);

               Debug.Print("");
               Debug.Print("Slicing error code as defined in swInsertSlicingError_e: " + errors);
           }

            ///  <summary>
            ///     ''' The SldWorks swApp variable is pre-assigned for you.
            ///     '''  </summary>
            public  SldWorks swApp;
      }

 }
```
