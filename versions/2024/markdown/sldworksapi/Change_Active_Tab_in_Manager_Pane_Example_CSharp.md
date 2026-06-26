---
title: "Change Active Tab in Manager Pane Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Active_Tab_in_Manager_Pane_Example_CSharp.htm"
---

# Change Active Tab in Manager Pane Example (C#)

This example shows how to change the active tab in the Manager Pane.

```
//-----------------------------------------------------------------
// Preconditions:
// 1. Open an assembly and click the FeatureManager design tree tab
//    in the Manager Pane.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Ensures that the Manager Pane is visible.
// 2. Traverses the tabs in the Manager Pane:
//    a. Changes the active tab.
//    b. Fires a notification.
// 3. Examine the Immediate window and Manager Pane.
//----------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;
using System.Collections;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public AssemblyDoc swAssy;

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExtension = default(ModelDocExtension);
            ModelViewManager swModelViewManager = default(ModelViewManager);
            object[] tabs = null;
            int nbrTabs = 0;
            int nbrTab = 0;
            Hashtable openAssy = default(Hashtable);

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swAssy = (AssemblyDoc)swModel;
            swModelDocExtension = (ModelDocExtension)swModel.Extension;

            //Set up events
            openAssy = new Hashtable();
            AttachEventHandlers();

            swModelViewManager = (ModelViewManager)swModel.ModelViewManager;

            //Ensure that Manager Pane is visible
            swModelDocExtension.HideFeatureManager(false);

            //Get the tabs in the Manager Pane
            tabs = (object[])swModelViewManager.GetFeatureManagerTabs();
            nbrTabs = tabs.GetLength(0);
            Debug.Print("Number of tabs in Manager Pane: " + nbrTabs);

            //Traverse the tabs in the Manager Pane and change the active tab
            for (nbrTab = 0; nbrTab < nbrTabs; nbrTab++)
            {
                swModelViewManager.ActiveFeatureManagerTabIndex = nbrTab;
            }

            Debug.Print("");

            Debug.Print("FeatureManager design tree tab index: " + swModelViewManager.GetFeatureManagerTreeTabIndex());
            Debug.Print("PropertyManager tab index:            " + swModelViewManager.GetPropertyManagerTabIndex());
            Debug.Print("ConfigurationManager tab index:       " + swModelViewManager.GetConfigurationManagerTabIndex());
            Debug.Print("DimXpertManager tab index:            " + swModelViewManager.GetDimXpertManagerTabIndex());
            Debug.Print("DisplayManager tab index:             " + swModelViewManager.GetDisplayManagerTabIndex());
        }

        public void AttachEventHandlers()
        {
            AttachSWEvents();
        }

        public void AttachSWEvents()
        {
            swAssy.FeatureManagerTabActivatedNotify += this.swAssy_FeatureManagerTabActivatedNotify;
        }

        public int swAssy_FeatureManagerTabActivatedNotify(int commandIndex, string commandTabName)
        {
            Debug.Print("Activated tab " + commandIndex + " whose name is " + commandTabName);
            return 0;
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
