---
title: "Fire Events When Dragging Instant3D Manipulator in a Part Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Dragging_Instant3D_Manipulator_in_a_Part_Example_CSharp.htm"
---

# Fire Events When Dragging Instant3D Manipulator in a Part Example (C#)

This example shows how to fire events when dragging an Instant3D manipulator
in a part document.

```vb
//------------------------------------
 // Preconditions:
 // 1. Open a part document.
 // 2. Open the Immediate window.
 //
 // kadov_tag{{</spaces>}}NOTE: Instant3D is enabled by the macro.
 //
 // Postconditions:
 // 1. Select an Instant3D manipulator in the
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}open part. For example,
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}double-click an extrude feature in a part,
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}then select one of the Instant3D manipulators
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}and drag it.
 // 2. Writes a debug statement to the Immediate
 //    window informing you that kadov_tag{{</spaces>}}dragging of an
 //    Instant3D manipulator has started.
 // 3. Stop dragging the manipulator.
 // kadov_tag{{<spaces>}}4. Writes a debug statement to the Immediate
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}window informing you that dragging of
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}an Instant3D manipulator has stopped.
 // 5. Examine the Immediate window.
 //----------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Collections;
 using System.Diagnostics;
 namespace DragStateChangeNotifyPartCSharp.csproj
 {
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public PartDoc pDoc;
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public FeatureManager swFeatMgr;
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Hashtable openPart;

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Enable Instant3D manipulators
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeatMgr = (FeatureManager)swModel.FeatureManager;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeatMgr.MoveSizeFeatures = true;

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Set up event handler
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pDoc = (PartDoc)swModel;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}openPart = new Hashtable();

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachEventHandlers();
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachEventHandlers()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachSWEvents();
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachSWEvents()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if ((pDoc != null))
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pDoc.DragStateChangeNotify += this.pDoc_DragStateChangeNotify;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}private int pDoc_DragStateChangeNotify(bool State)
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int functionReturnValue = 0;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Write debug statement when dragging of manipulator started and stopped kadov_tag{{<spaces>}}
 kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (State == true)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Dragging of manipulator started.");
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = 1;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Dragging of manipulator stopped.");
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = 0;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return functionReturnValue;
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
 }
```
