---
title: "Undo Feature and Fire Undo Post-Notify Event Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Undo_Feature_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm"
---

# Undo Feature and Fire Undo Post-Notify Event Example (C#)

This example shows how to fire an undo post-notification in a part.

```vb
 //-----------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\api\cstick.sldprt.
 //
 // Postconditions:
 // 1. Creates a cut-extrude feature on the top face of the
 //    candlestick.
 // 2. Undoes the cut-extrude feature and fires an undo post-notification.
 // 3. Click OK to close the message box.
 // 4. Deletes the cut-extrude sketch and all absorbed features.
 //
 // NOTE: Because the part is used elsewhere, do not save changes.
 //-----------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Collections;
using System.Windows.Forms;
namespace UndoPostNotifyCSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public PartDoc swPart;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SketchManager swSketchManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SketchSegment swSketchSegment;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}FeatureManager swFeatureManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Feature swFeature;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus = false;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Hashtable openPart;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Set up event notification
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart = (PartDoc)swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}openPart = new Hashtable();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachEventHandlers();

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Create a cut-extrude feature on the
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// top face of the candlestick
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.00140404215739, 0.2199999999999, 0.001897848026772, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketchManager = swModel.SketchManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketchSegment = swSketchManager.CreateCircle(0.0, 0.0, 0.0, 0.01296, -0.006347, 0.0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeatureManager = swModel.FeatureManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeature = swFeatureManager.FeatureCut(true, false, false, 0, 0, 0.01, 0.01, false, false, false,
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}false, 0.01745329251994, 0.01745329251994, false, false, false, false, false, true, true
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}});
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Undo the cut-extrude feature
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.EditUndo2(1);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Fire undo notification

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Select the circle and delete it
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.DeleteSelection2((int)swDeleteSelectionOptions_e.swDelete_Absorbed);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ForceRebuild3(true);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachSWEvents();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart.UndoPostNotify += this.swPart_UndoPostNotify;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int swPart_UndoPostNotify()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Show message after undo action occurs
kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}// NOTE: Because the message box might be displayed
kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}// behind an opened window, you might not see it.
kadov_tag{{<spaces>}}           kadov_tag{{</spaces>}}// If so, then check the Taskbar.
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MessageBox.Show("An undo post-notification event has been fired.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 1;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
