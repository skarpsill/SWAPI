---
title: "Selective Open Post-Notify Event Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Selective_Open_Post_Notify_Event_Example_CSharp.htm"
---

# Selective Open Post-Notify Event Example (C#)

This example shows how to handle the post-notification event that fires when
components are selected for Quick View/Selective Open.

```
//------------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly to open
//    exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. If the Large Design Review dialog displays,
//    then click OK to close it.
// 2. When prompted, select the components to open
//    and click Open Selected.
// 3. Click OK to close the message box.
// 4. If prompted to rebuild, then click Rebuild.
// 5. After reading the next message box displayed,
//    click OK to close it.
// 6. Displays only the selected components.
// 7. Inspect the Immediate Window and graphics area.
//
// NOTE: Because the assembly is used elsewhere, do not save
// changes.
//--------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
```

```vb
using SolidWorks.Interop.swconst;
using System;
namespace SelectiveOpenPostNotify_CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public AssemblyDoc swAssembly;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, false);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DocumentSpecification swDocSpecification = default(DocumentSpecification);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDocSpecification = (DocumentSpecification)swApp.GetOpenDocSpec("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\bowl and chute.sldasm");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDocSpecification.InteractiveComponentSelection = true;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDocSpecification.DocumentType = (int)swDocumentTypes_e.swDocASSEMBLY;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = swApp.OpenDoc7(swDocSpecification);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAssembly = (AssemblyDoc)swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Set up event
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachEventHandlers();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachSWEvents();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAssembly.SelectiveOpenPostNotify += this.swAssembly_SelectiveOpenPostNotify;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int swAssembly_SelectiveOpenPostNotify(string NewAddedDisplayStateName, ref object SelectedComponentNames)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}System.Windows.Forms.MessageBox.Show("A post-notification event has been fired for the selective open.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}System.Diagnostics.Debug.Print("New display state name: " + NewAddedDisplayStateName);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}System.Diagnostics.Debug.Print("Selected component names:");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}long i = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}String[] selected;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}selected = (String[])SelectedComponentNames;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (i = 0; i <= selected.GetUpperBound(0); i++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}System.Diagnostics.Debug.Print(" " + selected[i]);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
