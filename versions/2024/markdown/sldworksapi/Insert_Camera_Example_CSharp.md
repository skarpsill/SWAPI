---
title: "Insert Camera Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Camera_Example_CSharp.htm"
---

# Insert Camera Example (C#)

This example shows how to insert a camera and print out its settings.

```
//---------------------------------------------------------------
// Preconditions:
// 1. Open a model document that does not have any cameras inserted.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Inserts a camera in the model document.
// 2. Click View > Lights and Cameras > Properties > Camera1.
// 3. Click Zoom to Fit.
// 4. Examine the Immediate window, the graphics area, and the
//    Camera1 PropertyManager page.
//-------------------------------------------------------------
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
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Camera swCamera = default(Camera);

            swModel = (ModelDoc2)swApp.ActiveDoc;
            swModelDocExt = (ModelDocExtension)swModel.Extension;

            // Insert a camera
            swCamera = (Camera)swModelDocExt.InsertCamera();

            // Print out camera settings
            Debug.Print("ID                                               = " + swCamera.ID);
            Debug.Print("Focal distance                                   = " + swCamera.GetFocalDistance() * 1000.0 + " mm");
            Debug.Print("Perspective mode                                 = " + swCamera.Perspective);
            Debug.Print("Depth of field effects enabled                   = " + swCamera.DepthOfFieldEnabled);
            Debug.Print("Distance from focal plane to where focus is lost = " + swCamera.DepthOfFieldOffset * 1000.0 + " mm");
            Debug.Print("Horizontal angle of the field of view            = " + swCamera.FieldOfViewAngle * 1000.0 + " mm");
            Debug.Print("Depth of the field of view                       = " + swCamera.FieldOfViewDepth * 1000.0 + " mm");
            Debug.Print("Height of the field of view                      = " + swCamera.FieldOfViewHeight * 1000.0 + " mm");

        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
