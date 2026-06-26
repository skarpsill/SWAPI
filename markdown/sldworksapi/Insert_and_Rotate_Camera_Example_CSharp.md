---
title: "Insert and Rotate Camera Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Rotate_Camera_Example_CSharp.htm"
---

# Insert and Rotate Camera Example (C#)

This example shows how to insert and rotate a camera.

```vb
//------------------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified model document exists.
 // 2. Open the Immediate window.
 //
 // Postconditions:
 // 1. Inserts a camera in the model, changes its type to floating,
 //    and rotates it (i.e., modifies its pitch and yaw).
 // 2. Examine the Immediate window.
 //
 // NOTE: Because the model is used elsewhere, do not save changes.
 //------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
namespace PitchYawCameraCSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDoc2 swModel = default(ModelDoc2);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}ModelDocExtension swModelDocExt = default(ModelDocExtension);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Camera swCamera = default(Camera);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int fileerror = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}int filewarning = 0;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}bool boolstatus = false;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Open part document
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swApp.OpenDoc6("C:\\Users\\Public\\Documents\\SOLIDWORKS\\SOLIDWORKS 2018\\samples\\tutorial\\api\\coffeecup.sldprt", (int)swDocumentTypes_e.swDocPART, (int)swOpenDocOptions_e.swOpenDocOptions_Silent, "", ref fileerror, ref filewarning);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel = (ModelDoc2)swApp.ActiveDoc;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModelDocExt = (ModelDocExtension)swModel.Extension;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Insert a camera
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swCamera = (Camera)swModelDocExt.InsertCamera();

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Set camera type to floating
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swCamera.Type = (int)swCameraType_e.swCameraType_Floating;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Show camera
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Camera1", "CAMERAS", 0, 0, 0, false, 0, null, 0);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}boolstatus = swModel.SetUserPreferenceToggle((int)swUserPreferenceToggle_e.swDisplayCameras, true);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.GraphicsRedraw2();

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Get camera's pitch and yaw settings
            // 1 radian = 180º/p = 57.295779513º or approximately 57.3º
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Original pitch (up or down angle) = " + swCamera.Pitch * 57.3 + " deg");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Original yaw (side-to-side angle) = " + swCamera.Yaw * 57.3 + " deg");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print(" ");

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// Rotate camera
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swCamera.Pitch = -25;
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swCamera.Yaw = 150;

kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}// New pitch and yaw settings
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("New pitch (up or down angle) = " + swCamera.Pitch * 57.3 + " deg");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("New yaw (side-to-side angle) = " + swCamera.Yaw * 57.3 + " deg");
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}swModel.GraphicsRedraw2();
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
