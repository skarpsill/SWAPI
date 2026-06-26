---
title: "Undo Deleted Note and Fire Undo Post-Notify Event Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm"
---

# Undo Deleted Note and Fire Undo Post-Notify Event Example (C#)

## Undo Deleted Note and Fire Undo Pre- and Post-Notify Events Example
(C#)

This example demonstrates firing Undo pre- and post-notification events
in a drawing document.

```vb
//---------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\AutoCAD\7550-021.slddrw.
 //
 // Postconditions:
 // 1. Selects and deletes the note in Drawing View1.
 // 2. Undoes the deleted note.
 // 3. Fires pre-notification event indicating that an undo action is about to
 //    occur and fires post-notification event indicating that an undo
 //    action occurred.
 // 4. Click OK to close each message box.
 //
 // NOTE: Because the drawing is used elsewhere, do not save changes.
 //---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Collections;
using System.Windows.Forms;
namespace UndoPostNotifyDrawingCSharp.csproj
{
partial class SolidWorksMacro
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public DrawingDoc swDrawing;

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Hashtable openDrawing = default(Hashtable);

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = (ModelDocExtension)swModel.Extension;

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Event notification
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDrawing = (DrawingDoc)swModel;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}openDrawing = new Hashtable();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachEventHandlers();

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Activate the drawing view that contains
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// the note you want to delete
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swDrawing.ActivateView("Drawing View3");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("DetailItem77@Drawing View3", "NOTE", 0.3058741216774, 0.1870419466786, 0, false, 0, null, 0);

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Delete the selected note
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.EditDelete();

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Undo deletion of note
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.EditUndo2(1);

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Post-notification is fired

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Rebuild the drawing
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.ForceRebuild3(true);
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public void AttachEventHandlers()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}AttachSWEvents();
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public void AttachSWEvents()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDrawing.UndoPostNotify += this.swDrawing_UndoPostNotify;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swDrawing.UndoPreNotify += this.swDrawing_UndoPreNotify;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private int swDrawing_UndoPostNotify()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Display message after Undo
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// NOTE: Because the message box may be displayed
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// behind an opened window, you might not see it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// If so, then check the Taskbar. kadov_tag{{<spaces>}}       kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MessageBox.Show("An undo post-notification event has been fired.");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}return 1;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}private int b()
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// Display message after Undo
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// NOTE: Because the message box may be displayed
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// behind an opened window, you might not see it.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}// If so, then check the Taskbar.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}MessageBox.Show("An Undo pre-notification event has been fired.");
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}return 1;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public SldWorks swApp;
}
}
```
