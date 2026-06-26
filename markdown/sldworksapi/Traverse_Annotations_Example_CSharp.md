---
title: "Traverse Annotations Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Traverse_Annotations_Example_CSharp.htm"
---

# Traverse Annotations Example (C#)

This example shows how to get display dimension annotations.

```
//-----------------------------------------------------------
// Preconditions:
// 1. Verify that the specified part document exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified part document and selects
//    a sketch containing multiple dimensions.
// 2. Iterates the display dimensions and gets
//    each display dimension annotation and its position.
// 3. Moves each display dimension annotation 100mm to
//    the right.
// 4. Examine the graphics area and Immediate window.
//
// NOTE: Because the part document is used elsewhere, do not
// save changes.
//------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace TraverseAnnotationsCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelMgr = default(SelectionMgr);
            Annotation swAnnotation = default(Annotation);
            double[] annotationPosition = null;
            Feature swFeature = default(Feature);
            DisplayDimension swDispDim = default(DisplayDimension);
            string fileName = null;
            int errors = 0;
            int warnings = 0;
            bool status = false;

            //Open part document
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\tolanalyst\\offset\\top_plate.sldprt";
            swModel = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Get and edit sketch with dimensions
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            swFeature = (Feature)swSelMgr.GetSelectedObject6(1, -1);
            swModel.EditSketch();

            //Get the first display dimension
            swDispDim = (DisplayDimension)swFeature.GetFirstDisplayDimension();

            //Iterate through all of the display dimension
            //annotations in the sketch
            while ((swDispDim != null))
            {
                Debug.Print("Display dimension annotation name:");
                //Get the display dimension annotation
                swAnnotation = (Annotation)swDispDim.GetAnnotation();
                Debug.Print("  " + swAnnotation.GetName());
                //Get the position of the display dimension annotation
                annotationPosition = (double[])swAnnotation.GetPosition();
                if ((annotationPosition != null))
                {
                    //Move the display dimension annotation 100mm to the right
                    swAnnotation.SetPosition2(annotationPosition[0] + 0.1, annotationPosition[1], annotationPosition[2]);
                }
                //Get the next display dimension
                swDispDim = (DisplayDimension)swFeature.GetNextDisplayDimension(swDispDim);
            }

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
