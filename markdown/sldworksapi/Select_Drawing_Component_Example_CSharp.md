---
title: "Select Drawing Component Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Select_Drawing_Component_Example_CSharp.htm"
---

# Select Drawing Component Example (C#)

This example shows how to select an assembly component in a drawing.

```
//--------------------------------------------
// Preconditions:
// 1. Open a drawing of an assembly.
// 2. Select an assembly component in the drawing.
//
// Postconditions: Displays a message box
// containing the name of the selected assembly
// component.
//---------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Windows.Forms;

namespace GetSelectedDrawingComponent4CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public void Main()
        {
            ModelDoc2 swModelDoc;
            SelectionMgr swSelMgr;
            Component2 swComponent;
            DrawingComponent swDrawingComponent;

            swModelDoc = (ModelDoc2)swApp.ActiveDoc;
            if (swModelDoc == null)
            {
                return;
            }
            swSelMgr = (SelectionMgr)swModelDoc.SelectionManager;

            if (swSelMgr.GetSelectedObjectCount2(0) == 0)
            {
                MessageBox.Show("No selections detected.");
                return;
            }

            if (swSelMgr.GetSelectedObjectType3(1, 0) == (int)swSelectType_e.swSelCOMPONENTS)
            {
                swDrawingComponent = (DrawingComponent)swSelMgr.GetSelectedObjectsComponent4(1, 0);

                if (swDrawingComponent == null)
                {
                    MessageBox.Show("The component is empty.");
                    return;
                }
                else
                {
                    swComponent = (Component2)swDrawingComponent.Component;
                    MessageBox.Show(swComponent.Name2);
                }
            }
            else
            {
                MessageBox.Show("The selection is not an assembly component.");
                return;
            }

        }

        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>

        public SldWorks swApp;

    }
}
```
