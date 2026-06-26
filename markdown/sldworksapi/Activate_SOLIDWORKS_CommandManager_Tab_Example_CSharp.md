---
title: "Activate SOLIDWORKS CommandManager Tab Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Activate_SOLIDWORKS_CommandManager_Tab_Example_CSharp.htm"
---

# Activate SOLIDWORKS CommandManager Tab Example (C#)

This example shows how to activate a SOLIDWORKS CommandManager tab.

```vb
 //----------------------------------------------------------------------------
 // Preconditions: Open a part.
 //
 // Postconditions:
 // 1. Inspect the Immediate window for the SOLIDWORKS CommandManager tab
 //    information.
 // 2. Inspect the CommandManager.
 //      * Sketch tab is activated.
 //      * Mold Tools tab (tab index 5) is visible.
 // ---------------------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 using System;
 using System.Diagnostics;
 namespace ActivateCommandManagerTab_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModelDoc;
         ModelDocExtension swModelDocExt;
         bool retval;
         object cmdTabs;
         string activeTab;

         int activeTabIndex;

         public void Main()
         {
             swModelDoc = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = swModelDoc.Extension;

             //Get SOLIDWORKS CommandManager tabs
             cmdTabs = swModelDocExt.GetCommandTabs();
             //Active CommandManager tab is "Features"
             activeTab = swModelDocExt.ActiveCommandTab;
             Debug.Print("Active tab is " + activeTab);
             activeTabIndex = swModelDocExt.ActiveCommandTabIndex;
             Debug.Print("Active tab index is " + activeTabIndex);
             //Tab with index 5 is not visible
             retval = swModelDocExt.get_CommandTabVisible(5);
             Debug.Print("Tab with index 5 is visible? " + retval);

             //Set the active CommandManager tab
             swModelDocExt.ActiveCommandTab = "Sketch";
             activeTabIndex = swModelDocExt.ActiveCommandTabIndex;
             //Make tab with index 5 visible
             swModelDocExt.set_CommandTabVisible(5, true);

         }

         public SldWorks swApp;

     }

 }
```
