---
title: "Undo Hidden Component and Fire Undo Post-Notify Event Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Undo_Hidden_Component_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm"
---

# Undo Hidden Component and Fire Undo Post-Notify Event Example (C#)

This example shows how to fire an undo post-notification in
an assembly document.

```
//--------------------------------------------------------------------------
// Preconditions: Open public_documents\samples\tutorial\smartcomponents\stepped_shaft.sldasm.
//
// Postconditions:
// 1. Selects and hides the base-plate<1> component.
// 2. Undoes the hiding of the base-plate<1> component.
// 3. Fires a post-notification indicating that an undo action occurred.
// 4. Click OK to close the message box.
//
// NOTE: Because the assembly is used elsewhere, do not save changes.
//--------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
```

```vb
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
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.EditUndo2(1);

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Fire undo post-notiifcation

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
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int swAssembly_UndoPostNotify()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Display message after undo action occurs
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MessageBox.Show("An undo post-notification event has been fired.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 1;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}

}
```
