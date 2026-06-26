---
title: "Insert and Rotate Camera Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_and_Rotate_Camera_Example_VBNET.htm"
---

# Insert and Rotate Camera Example (VB.NET)

This example shows how to insert and rotate a camera.

'------------------------------------------------------------------------ ' Preconditions: ' 1. Verify that the specified model document exists. ' 2. Open the Immediate window. ' ' Postconditions: ' 1. Inserts a camera in the model, changes its type to floating, ' and rotates it (i.e., modifies its pitch and yaw). ' 2. Examine the Immediate window. ' ' NOTE: Because the model is used elsewhere, do not save changes. '------------------------------------------------------------------------

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public Sub main()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModel As ModelDoc2
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swModelDocExt As ModelDocExtension
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim swCamera As Camera
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim fileerror As Long, filewarning As Long
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim boolstatus As Boolean

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Open part document
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\coffeecup.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", fileerror, filewarning)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel = swApp.ActiveDoc
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModelDocExt = swModel.Extension

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Insert a camera
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swCamera = swModelDocExt.InsertCamera

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Set camera type to floating
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swCamera.Type = swCameraType_e.swCameraType_Floating

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Show camera
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModelDocExt.SelectByID2("Camera1", "CAMERAS", 0, 0, 0, False, 0, Nothing, 0)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}boolstatus = swModel.SetUserPreferenceToggle(swUserPreferenceToggle_e.swDisplayCameras, True)
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.GraphicsRedraw2()

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Get camera's pitch and yaw settings
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Original pitch (up or down angle) kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}= " & swCamera.Pitch * 57.3 & " deg")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("Original yaw (side-to-side angle) kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}= " & swCamera.Yaw * 57.3 & " deg")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print(" ")

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' Rotate camera
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swCamera.Pitch = -25
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swCamera.Yaw = 150

kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}' New pitch and yaw settings
        ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("New pitch (up or down angle) kadov_tag{{<spaces>}}         kadov_tag{{</spaces>}}= " & swCamera.Pitch * 57.3 & " deg")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Debug.Print("New yaw (side-to-side angle) kadov_tag{{<spaces>}}         kadov_tag{{</spaces>}}= " & swCamera.Yaw * 57.3 & " deg")
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}swModel.GraphicsRedraw2()

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End Sub

kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' <summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}''' </summary>
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Public swApp As SldWorks

End Class
```
