---
title: "Fire Undo and Redo Pre- and Post-notifications in Assembly Document (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Assembly_Document_Example_CSharp.htm"
---

# Fire Undo and Redo Pre- and Post-notifications in Assembly Document (C#)

This example shows how to fire Undo and Redo post-notifications in an
assembly document.

```vb
//----------------------------------------------------------------------------
 // Preconditions: Open public_documents\samples\tutorial\smartcomponents\stepped_shaft.sldasm.
 //
 // 1. Selects  and hides the base-plate<1> component and
 //    fires pre- and post-notifications indicating that an
 //    Undo has occurred.
 // 2. Performs a Redo and fires pre- and post-notifications.
 // 3. Performs another Undo and fires pre- and post-notifications
 //    so that the assembly document returns to its just-opened state.
 // 4. Click OK to close each message box.
 //
 // NOTE: Because the assembly is used elsewhere, do not save changes.
 //---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Collections;
using System.Windows.Forms;
namespace Macro1.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public AssemblyDoc swAssemblyDoc;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus = false;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Hashtable openAssembly = default(Hashtable);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = (ModelDocExtension)swModel.Extension;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Event notification
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAssemblyDoc = (AssemblyDoc)swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}openAssembly = new Hashtable();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachEventHandlers();

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Select a component and hide it
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("base_plate-1@stepped_shaft", "COMPONENT", 0, 0, 0, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.HideComponent2();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ClearSelection2(true);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Undo hiding of the component
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// and fire pre- and post-notifications
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.EditUndo2(1);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Redo hiding of the component
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// and fire pre- and post-notifications
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.EditRedo2(1);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Undo hiding of the component
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// so that the assembly document
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// is unchanged
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.EditUndo2(1);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Rebuild model
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.ForceRebuild3(true);
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachSWEvents();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAssemblyDoc.UndoPostNotify += this.swAssembly_UndoPostNotify;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAssemblyDoc.UndoPreNotify += this.swAssembly_UndoPreNotify;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAssemblyDoc.RedoPostNotify += this.swAssembly_RedoPostNotify;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAssemblyDoc.RedoPreNotify += this.swAssembly_RedoPreNotify;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int swAssembly_UndoPostNotify()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Display message after undo action occurs
// NOTE: Because the message box may be displayed
// behind an opened window, you might not see it.
// If so, then check the Taskbar for it.
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MessageBox.Show("An Undo post-notification event has been fired.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 1;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int swAssembly_UndoPreNotify()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Display message after undo action occurs
// NOTE: Because the message box may be displayed
// behind an opened window, you might not see it.
// If so, then check the Taskbar for it.
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MessageBox.Show("An Undo pre-notification event has been fired.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 1;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int swAssembly_RedoPostNotify()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Display message after undo action occurs
// NOTE: Because the message box may be displayed
// behind an opened window, you might not see it.
// If so, then check the Taskbar for it.
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MessageBox.Show("A Redo post-notification event has been fired.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 1;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int swAssembly_RedoPreNotify()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Display message after undo action occurs
// NOTE: Because the message box may be displayed
// behind an opened window, you might not see it.
// If so, then check the Taskbar for it.
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MessageBox.Show("A Redo pre-notification event has been fired.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 1;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
