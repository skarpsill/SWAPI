---
title: "Fire Undo and Redo Pre- and Post-notifications in Part Document (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Part_Document_Example_CSharp.htm"
---

# Fire Undo and Redo Pre- and Post-notifications in Part Document (C#)

This example shows how to fire Undo and Redo pre- and post-notifications
in a part document.

```vb
// --------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\api\cstick.sldprt.
 //
 // Postconditions:
 // 1. Creates a circle, undoes it, redoes it, and undoes it again.
 // 2. Fires a pre- and post-notification and displays a message box
 //    before and after each Undo and Redo.
 // 3. Click OK to close each message box.
 //
 // NOTE: Because the part is used elsewhere, do not save changes.
 // ---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Collections;
using System.Windows.Forms;
namespace RedoPostNotifyPartCSharp.csproj
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
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Hashtable openPart;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Set up event notification
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart = (PartDoc)swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}openPart = new Hashtable();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachEventHandlers();

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Create a circle on the
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// top face of the candlestick
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.00140404215739, 0.2199999999999, 0.001897848026772, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketchManager = swModel.SketchManager;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swSketchSegment = swSketchManager.CreateCircle(0.0, 0.0, 0.0, 0.01296, -0.006347, 0.0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Undo creation of circle
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// and fire an Undo pre- and post-
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// notification
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.EditUndo2(1);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Redo creation of circle
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// and fire a Redo pre- and post-
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// notification
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.EditRedo2(1);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Undo creation of circle again
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// to leave model document unchanged
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// and fire another Undo pre- and post-
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// notification
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.EditUndo2(1);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ForceRebuild3(true);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachSWEvents();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart.UndoPostNotify += this.swPart_UndoPostNotify;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart.UndoPreNotify += this.swPart_UndoPreNotify;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart.RedoPostNotify += this.swPart_RedoPostNotify;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart.RedoPreNotify += this.swPart_RedoPreNotify;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int swPart_UndoPostNotify()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Show message after an Undo kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Display message after Undo
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// NOTE: Because the message box may be displayed
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// behind an opened window, you might not see it.
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// If so, then check the Taskbar for it.
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MessageBox.Show("An Undo post-notification event has been fired.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 1;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int swPart_UndoPreNotify()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Show message after an Undo kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Display message after Undo
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// NOTE: Because the message box may be displayed
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// behind an opened window, you might not see it.
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// If so, then check the Taskbar for it. kadov_tag{{<spaces>}}  kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MessageBox.Show("An Undo pre-notification event has been fired.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 1;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int swPart_RedoPostNotify()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Show message after an Undo kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Display message after Undo
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// NOTE: Because the message box may be displayed
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// behind an opened window, you might not see it.
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// If so, then check the Taskbar for it. kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MessageBox.Show("A Redo post-notification event has been fired.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 1;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int swPart_RedoPreNotify()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Show message after an Undo kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Display message after Undo
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// NOTE: Because the message box may be displayed
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// behind an opened window, you might not see it.
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// If so, then check the Taskbar for it. kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MessageBox.Show("A Redo pre-notification event has been fired.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 1;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
