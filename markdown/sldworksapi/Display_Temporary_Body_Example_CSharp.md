---
title: "Display Temporary Body Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Display_Temporary_Body_Example_CSharp.htm"
---

# Display Temporary Body Example (C#)

This example shows how to display a temporary body.

```
//-------------------------------------------------
// Preconditions:
// 1. Verify that the specified assembly document to
//    open exists.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Opens the specified assembly document.
// 2. Selects a component for the temporary body.
// 3. Displays the temporary body.
// 4. Examine the graphics area and the Immediate
//    window.
//
// NOTE: Because the assembly is used elsewhere, do
// not save changes.
//-------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 Part = default(ModelDoc2);
            Body2 Body = default(Body2);
            Body2 BodyCopy = default(Body2);
            bool status = false;
            Component2 Component = default(Component2);
            MathUtility MathUtility = default(MathUtility);
            MathTransform MathXform = default(MathTransform);
            SelectionMgr SelMgr = default(SelectionMgr);
            double[] Xform = new double[16];
            object vXform = null;
            int retval = 0;
            string fileName = null;
            int errors = 0;
            int warnings = 0;

            Xform[0] = 1.0;
            Xform[1] = 0.0;
            Xform[2] = 0.0;
            Xform[3] = 0.0;
            Xform[4] = 1.0;
            Xform[5] = 0.0;
            Xform[6] = 0.0;
            Xform[7] = 0.0;
            Xform[8] = 1.0;
            Xform[9] = 0.15;
            Xform[10] = 0.0;
            Xform[11] = 0.0;
            Xform[12] = 1.0;
            Xform[13] = 0.0;
            Xform[14] = 0.0;
            Xform[15] = 0.0;
            vXform = Xform;

            MathUtility = (MathUtility)swApp.GetMathUtility();
            MathXform = (MathTransform)MathUtility.CreateTransform(vXform);

            //Open assembly
            fileName = "C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\assem1.sldasm";
            Part = (ModelDoc2)swApp.OpenDoc6(fileName, (int)swDocumentTypes_e.swDocASSEMBLY, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref errors, ref warnings);

            //Select component and create temporary body
            status = Part.Extension.SelectByID2("TestPart1-1@assem1", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            SelMgr = (SelectionMgr)Part.SelectionManager;
            Component = (Component2)SelMgr.GetSelectedObjectsComponent3(1, 0);
            Body = (Body2)Component.GetBody();
            BodyCopy = (Body2)Body.Copy();
            BodyCopy.ApplyTransform(MathXform);

            //Display temporary body
            retval = BodyCopy.Display3(Component, 255, (int)swTempBodySelectOptions_e.swTempBodySelectable);
            Debug.Print("Temporary body displayed (0 = success)? " + retval);

            Part.ViewZoomtofit2();

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
