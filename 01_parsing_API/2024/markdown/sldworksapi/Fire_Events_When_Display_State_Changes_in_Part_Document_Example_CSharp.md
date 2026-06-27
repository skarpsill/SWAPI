---
title: "Fire Events When Display State Changes in Part Document (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Display_State_Changes_in_Part_Document_Example_CSharp.htm"
---

# Fire Events When Display State Changes in Part Document (C#)

This example shows how to fire the events related to changing display
states of a configuration in a part document.

```vb
//---------------------------------------------------------------
// Preconditions:
// kadov_tag{{<spaces>}}1. Open a part document that has kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}
// kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}a configuration with multiple display states.
// 2. Run this macro in debug mode.
// 3. Change the display state of the active configuration in SOLIDWORKS
// kadov_tag{{<spaces>}}   (click the ConfigurationManager tab and double-click
// kadov_tag{{<spaces>}}   a different display state).
//
// Postcondition: A message box is displayed informing
// kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}you that the display state is about change. After the display state changes,
// kadov_tag{{<spaces>}}another message box is displayed informing you that the display
// kadov_tag{{</spaces>}}state has changed.
//---------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Collections;
using System.Windows.Forms;
namespace FireEventsWhenDisplayStateChangesCSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public PartDoc swPart;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Hashtable openPart;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Set up events
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart = (PartDoc)swModel;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}openPart = new Hashtable();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachEventHandlers();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachEventHandlers()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachSWEvents();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachSWEvents()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart.ActiveDisplayStateChangePreNotify += this.swPart_ActiveDisplayStateChangePreNotify;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swPart.ActiveDisplayStateChangePostNotify += this.swPart_ActiveDisplayStateChangePostNotify;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int swPart_ActiveDisplayStateChangePreNotify()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Send message when user changes display state in the ConfigurationManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MessageBox.Show("The active configuration's display state is about to change.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 1;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int swPart_ActiveDisplayStateChangePostNotify(string DisplayStateName)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Send message after user changes display state in the ConfigurationManager
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MessageBox.Show("The active configuration's display state has changed.");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 1;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
