---
title: "Fire Events When Display State Changes Example(C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Display_State_Changes_Example_CSharp.htm"
---

# Fire Events When Display State Changes Example(C#)

## Fire Events When Display State Changes Example (C#)

This example shows how to fire the events related to changing display
states of a configuration in an assembly document.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Open an assembly document that has a configuration with multiple
//    display states.
// 2. Run this macro in debug mode.
// 3. Change the display state of the active configuration in SOLIDWORKS
//    (click the ConfigurationManager tab and double-click
//    a different display state).
//
// Postconditions:
// 1. Displays a message box informing you that the display state is about to
//    change.
// 2. After the display state changes, displays another message informing you
//    that the display state has changed.
//
// NOTE: This example also fires these events when you change
// configurations in an assembly document.
//---------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Collections;
using System.Windows.Forms;

namespace Macro1.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public
 partial class SolidWorksMacro
```

```vb
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public AssemblyDoc swAssem;
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Hashtable openAssem;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
 kadov_tag{{<spaces>}}
             kadov_tag{{</spaces>}}//Set up events
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAssem = (AssemblyDoc)swModel;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}openAssem = new Hashtable();
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
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAssem.ActiveDisplayStateChangePreNotify += this.swAssem_ActiveDisplayStateChangePreNotify;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swAssem.ActiveDisplayStateChangePostNotify += this.swAssem_ActiveDisplayStateChangePostNotify;
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int swAssem_ActiveDisplayStateChangePreNotify()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Send message when user changes display state in the ConfigurationManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MessageBox.Show("The active configuration's display state is about to change.");
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 1;
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public int swAssem_ActiveDisplayStateChangePostNotify(string DisplayStateName)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}//Send message after user changes display state in the ConfigurationManager
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}MessageBox.Show("The active configuration's display state has changed.");
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return 1;
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
 }
```
