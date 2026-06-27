---
title: "Rotate and Copy 3D Sketch About Vector Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_and_Copy_3D_Sketch_About_Vector_Example_CSharp.htm"
---

# Rotate and Copy 3D Sketch About Vector Example (C#)

This example shows how to rotate and copy 3D sketches about a vector.

```
//---------------------------------------------------
// Preconditions:
// 1. Open a part that contains two 3D sketches,
//    3DSketch1 and 3DSketch2.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Copies and rotates the 3DSketch2 sketch around
//    the center point of the 3DSketch1 sketch's arc.
// 2. Rotates the 3DSketch1 sketch around the center
//    point of its arc.
// 3. Examine the Immediate window.
//---------------------------------------------------
```

```vb
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace RotateorCopy3DAboutVectorXYZ_CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectionMgr swSelMgr = default(SelectionMgr);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SelectData swSelData = default(SelectData);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SketchManager swSketchMgr = default(SketchManager);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Sketch swSketch = default(Sketch);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolStatus = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}object[] varSketchSegments = null;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int i = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (swApp == null) return;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Document with two 3D sketches, named 3DSketch2 and
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// 3DSketch1, is open and active
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (swModel == null)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}System.Windows.Forms.MessageBox.Show("Failed to open document.");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelMgr = (SelectionMgr)swModel.SelectionManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSelData = (SelectData)swSelMgr.CreateSelectData();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketchMgr = swModel.SketchManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Select 3DSketch2 sketch
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolStatus = swModelDocExt.SelectByID2("3DSketch2", "SKETCH", 0, 0, 0, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (boolStatus == false)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}System.Windows.Forms.MessageBox.Show("Failed to select sketch 3DSketch2.");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Open 3DSketch2 sketch in edit mode
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.EditSketch();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketch = swSketchMgr.ActiveSketch;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (swSketch == null)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}System.Windows.Forms.MessageBox.Show("Failed to get pointer to 3DSketch2 sketch.");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Select all sketch segments in 3DSketch2 sketch
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}varSketchSegments = (object[])swSketch.GetSketchSegments();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (i = 0; i <= varSketchSegments.GetUpperBound(0); i++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}boolStatus = ((SketchSegment)varSketchSegments[i]).Select4(true, swSelData);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (boolStatus == false) System.Windows.Forms.MessageBox.Show("Failed to select sketch segment instance." + i + ".");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Copy and rotate 3DSketch2 sketch about center
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// point of 3DSketch1 sketch's arc
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Rotating and copying 3DSketch2 sketch about the center point of 3DSketch1's arc? " + swSketchMgr.RotateOrCopy3DAboutVector(true, 1, true, -0.09925811702374, 0.004131001848179, 0, 1, 0, 0, 1.5707963267949
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}));
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Exit 3DSketch2 sketch
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketchMgr.InsertSketch(true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Select 3DSketch1 sketch
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolStatus = swModelDocExt.SelectByID2("3DSketch1", "SKETCH", 0, 0, 0, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (boolStatus == false)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}System.Windows.Forms.MessageBox.Show("Failed to select sketch 3DSketch1.");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Edit 3DSketch1 sketch
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.EditSketch();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketch = (Sketch)swModel.GetActiveSketch2();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (swSketch == null)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}System.Windows.Forms.MessageBox.Show("Failed to get pointer to sketch 3DSketch1.");
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Select all sketch segments in 3DSketch1 sketch
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}varSketchSegments = (object[])swSketch.GetSketchSegments();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (i = 0; i <= varSketchSegments.GetUpperBound(0); i++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}boolStatus = ((SketchSegment)varSketchSegments[i]).Select4(true, swSelData);
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}if (boolStatus == false)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}System.Windows.Forms.MessageBox.Show("Failed to select sketch segment instance." + i + ".");
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}return;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Rotate 3DSketch1 sketch about the
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// center point of its arc
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Rotating 3DSketch1 sketch about the center point of its arc? " + swSketchMgr.RotateOrCopy3DAboutVector(false, 1, true, -0.09925811702374, 0.004131001848179, 0, 1, 0, 0, 1.5707963267949
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}));
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Exit 3DSketch1 sketch
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketchMgr.InsertSketch(true);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
