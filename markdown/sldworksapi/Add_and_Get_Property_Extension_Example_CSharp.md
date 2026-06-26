---
title: "Add and Get Property Extensions Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Get_Property_Extension_Example_CSharp.htm"
---

# Add and Get Property Extensions Example (C#)

This example shows how to add and get a property extension on a part.

```
//---------------------------------------------
// Preconditions:
// 1. Open a part.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Adds three property extensions to the part.
// 2. Gets the three property extensions added to the part.
// 3. Examine the Immediate window.
//----------------------------------------------
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
            PartDoc swPart = default(PartDoc);
            int retVal = 0;
            string[] objAdded = new string[3];
            string objRetrieved = null;

            swPart = (PartDoc)swApp.ActiveDoc;

            Debug.Print("Property extensions added:");

            objAdded[0] = "12345PID";
            retVal = swPart.AddPropertyExtension(objAdded[0]);
            Debug.Print(" First property extension: " + objAdded[0]);

            objAdded[1] = "6789PID";
            retVal = swPart.AddPropertyExtension(objAdded[1]);
            Debug.Print(" Second property extension: " + objAdded[1]);

            objAdded[2] = "00000PID";
            retVal = swPart.AddPropertyExtension(objAdded[2]);
            Debug.Print(" Third property extension: " + objAdded[2]);

            Debug.Print("Property extensions retrieved:");

            objRetrieved = (string)swPart.GetPropertyExtension(retVal - 3);
            Debug.Print(" First property extension: " + objRetrieved);

            objRetrieved = (string)swPart.GetPropertyExtension(retVal - 2);
            Debug.Print(" Second property extension: " + objRetrieved);

            objRetrieved = (string)swPart.GetPropertyExtension(retVal - 1);
            Debug.Print(" Third property extension: " + objRetrieved);

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
