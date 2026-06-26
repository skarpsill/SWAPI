---
title: "Get Object ID of GTol Annotation Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Object_ID_of_GTol_Annotation_Example_CSharp.htm"
---

# Get Object ID of GTol Annotation Example (C#)

This example shows how to get the object ID of a GTol annotation.

```
//---------------------------------------------
// Preconditions:
// 1. Verify that the drawing to open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified drawing.
// 2. Selects the GTol annotation.
// 3. Gets the type of annotation selected.
// 4. Gets the selected GTol annotation's object ID.
// 5. Examine the Immediate window.
//--------------------------------------------

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace GetObjectIDCSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            DrawingDoc swDrawing = default(DrawingDoc);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            SelectionMgr swSelectionMgr = default(SelectionMgr);
            Gtol swGTol = default(Gtol);
            Annotation swGTolAnnotation = default(Annotation);
            bool status = false;
            int errors = 0;
            int warnings = 0;
            int id = 0;

            //Open the drawing
            swModel = (ModelDoc2)swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\gtolwitnessline.slddrw", 3, 0, "", ref errors, ref warnings);
            swDrawing = (DrawingDoc)swModel;

            //Select GTol
            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("DetailItem40@Drawing View3", "GTOL", 0.44609485235144, 0.381203477032446, 0, false, 0, null, 0);
            swSelectionMgr = (SelectionMgr)swModel.SelectionManager;
            swGTol = (Gtol)swSelectionMgr.GetSelectedObject6(1, -1);

            //Print type of annotation and its object ID
            swGTolAnnotation = (Annotation)swGTol.GetAnnotation();
            Debug.Print("Annotation type: " + swGTolAnnotation.GetType());
            id = swModelDocExt.GetObjectId(swGTolAnnotation);
            Debug.Print("ID = " + id);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
