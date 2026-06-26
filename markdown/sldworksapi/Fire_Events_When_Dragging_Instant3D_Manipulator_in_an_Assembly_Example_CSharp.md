---
title: "Fire Events When Dragging Instant3D Manipulator in an Assembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Events_When_Dragging_Instant3D_Manipulator_in_an_Assembly_Example_CSharp.htm"
---

# Fire Events When Dragging Instant3D Manipulator in an Assembly Example (C#)

This example shows how to fire events when dragging an Instant3D manipulator
in an assembly document.

```vb
//------------------------------------
 // Preconditions:
 // 1. Open an assembly document.
 // 2. Open the Immediate window.
 //
 // kadov_tag{{</spaces>}}NOTE: Instant3D is enabled by the macro.
 //
 // Postconditions:
 // 1. Select an Instant3D manipulator in the
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}open assembly by right-clicking a floating
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}assembly component, clicking the down arrows
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}at the bottom of the shortcut menu, and selecting
 // kadov_tag{{<spaces>}}   Move with Triad.
 // 2. Drag the Instant3D handle kadov_tag{{</spaces>}}to move the assembly component.
 // 3. Writes a debug statement to the Immediate window
 //    informing you that kadov_tag{{</spaces>}}dragging of an Instant3D manipulator
 //    has started.
 // 4. Stop dragging the manipulator.
 // kadov_tag{{<spaces>}}5. Writes a debug statement to the Immediate
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}window informing you that dragging of
 // kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}an Instant3D manipulator has stopped.
 // 6. Examine the Immediate window.
 //----------------------------------------
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Collections;
 using System.Diagnostics;
 namespace DragStateChangeNotifyAssemblyCSharp.csproj
 { kadov_tag{{<spaces>}}   kadov_tag{{</spaces>}}partial class SolidWorksMacro
 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public AssemblyDoc pDoc;
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public FeatureManager swFeatMgr;
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Hashtable openAssembly;

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}//Enable Instant3D manipulators
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeatMgr = (FeatureManager)swModel.FeatureManager;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swFeatMgr.MoveSizeFeatures = true;

 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Set up event handler
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pDoc = (AssemblyDoc)swModel;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}openAssembly = new Hashtable();
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachEventHandlers();
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachEventHandlers()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}AttachSWEvents();
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

 kadov_tag{{<spaces>}}
 kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void AttachSWEvents()
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if ((pDoc != null)) kadov_tag{{<spaces>}}
 kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pDoc.DragStateChangeNotify += this.pDoc_DragStateChangeNotify;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}private int pDoc_DragStateChangeNotify(bool State) kadov_tag{{<spaces>}}
 kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int functionReturnValue = 0;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Write debug statement when dragging of manipulator started and stopped kadov_tag{{<spaces>}}
 kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}if (State == true)
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Dragging of manipulator started.");
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = 1;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}else
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Dragging of manipulator stopped.");
 kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}functionReturnValue = 0;
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}return functionReturnValue;
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
 kadov_tag{{<spaces>}}
 kadov_tag{{</spaces>}}kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
 kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;

 kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
 }
```
