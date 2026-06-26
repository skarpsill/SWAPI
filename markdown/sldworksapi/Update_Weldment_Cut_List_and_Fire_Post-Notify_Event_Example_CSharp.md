---
title: "Update Weldment Cut List and Fire Post-Notify Event Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Update_Weldment_Cut_List_and_Fire_Post-Notify_Event_Example_CSharp.htm"
---

# Update Weldment Cut List and Fire Post-Notify Event Example (C#)

This example shows how to handle the post-notification
event that fires

when the weldment cut list is updated.

```vb
//------------------------------------------------------
// Preconditions:
// Specified file to open exists.
//
// Postconditions:
// 1. Right-click on the Cut list folder.
// 2. Select Update from the right-click menu.
// 3. A message box displays (look in the taskbar for the hidden dialog).
// 4. Click OK.
// 5. Stop the macro (CTRL-ALT-Break).
//------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
namespace UpdateWeldmentCutListandFirePostNotifyEvent_CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public PartDoc swPart;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, false);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}DocumentSpecification swDocSpecification = default(DocumentSpecification);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDocSpecification = (DocumentSpecification)swApp.GetOpenDocSpec("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\weldments\\weldment_box2.sldprt");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swDocSpecification.DocumentType = (int)swDocumentTypes_e.swDocPART;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = swApp.OpenDoc7(swDocSpecification);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart = (PartDoc)swModel;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Set up event
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachEventHandlers();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachSWEvents();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart.WeldmentCutListUpdatePostNotify += this.swPart_WeldmentCutListUpdatePostNotify;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int swPart_WeldmentCutListUpdatePostNotify()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}System.Windows.Forms.MessageBox.Show("The cut list is updated.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swStopDebuggingVstaOnExit, true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 0;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
