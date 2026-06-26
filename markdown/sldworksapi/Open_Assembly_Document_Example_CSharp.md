---
title: "Open Assembly Document Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Assembly_Document_Example_CSharp.htm"
---

# Open Assembly Document Example (C#)

This example shows how to specify how to open an assembly document.

```
//------------------------------------------------------
// Preconditions: Verify that the specified assembly document
// to open exists.
//
// Postconditions:
// 1. If the Large Design Review dialog is displayed, click OK
//    to close it.
// 2. Opens the specified assembly document and loads
//    and displays the specified component.
// 3. Examine the graphics area.
//
// NOTE: Because the model is used elsewhere, do not save changes.
//------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            DocumentSpecification swDocSpecification = default(DocumentSpecification);
            string[] componentsArray = new string[1];
            object[] components = null;
            string name = null;
            int errors = 0;
            int warnings = 0;

            //Set the specifications
            swDocSpecification = (DocumentSpecification)swApp.GetOpenDocSpec("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\advdrawings\\bowl and chute.sldasm");
            componentsArray[0] = "food bowl-1@bowl and chute";
            components = (object[])componentsArray;
            swDocSpecification.ComponentList = components;
            swDocSpecification.Selective = true;
            name = swDocSpecification.FileName;
            swDocSpecification.DocumentType = (int)swDocumentTypes_e.swDocASSEMBLY;
            swDocSpecification.DisplayState = "Default_Display State-1";
            swDocSpecification.UseLightWeightDefault = false;
            swDocSpecification.LightWeight = true;
            swDocSpecification.Silent = true;
            swDocSpecification.IgnoreHiddenComponents = true;

            //Open the assembly document as per the specifications
            swModel = (ModelDoc2)swApp.OpenDoc7(swDocSpecification);
            errors = swDocSpecification.Error;
            warnings = swDocSpecification.Warning;

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
